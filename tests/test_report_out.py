"""Exercise report validation and real Git publication without touching GitHub."""
from pathlib import Path
from unittest.mock import patch
import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from report_out import filename, read_report, render_index
from publish_report import git, publish


def report(table, industry, summary='Our table sees a possible service change, conditional on reliable review. We would test whole-workflow quality and time.'):
    return f'''# {table}: {industry} analysis

**Table:** {table}
**Industry:** {industry}
**Approach(es):** Simulation
**Date:** 2026-10-16
**Horizon:** Three to five years

## Summary

{summary}

## 1. The change we investigated
A fictional test report, used only in a temporary repository.
'''


class ReportOutTests(unittest.TestCase):
    def test_names_and_summary(self):
        self.assertEqual(filename('Future Builders!', 'Healthcare Operations'), 'future-builders-healthcare-operations-analysis.md')
        self.assertEqual(filename('../Café Team', 'Retail / Service'), 'cafe-team-retail-service-analysis.md')
        with self.assertRaises(ValueError):
            filename('!!!', 'Retail')
        with self.assertRaises(ValueError):
            read_report(report('Table A', 'Retail', 'First paragraph.\n\nSecond paragraph.'))
        with self.assertRaises(ValueError):
            read_report(report('Table A', 'Retail').replace('**Industry:** Retail', ''))

    def test_index_sections_and_order(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            for table in ['Zebra Team', 'Alpha Team']:
                (root / filename(table, 'Retail')).write_text(report(table, 'Retail'))
            text = render_index(root)
            self.assertEqual(text.count('\n## '), 2)
            self.assertLess(text.index('Alpha Team'), text.index('Zebra Team'))
            self.assertIn('](alpha-team-retail-analysis.md)', text)
            self.assertIn('Our table sees', text)

    def test_publication_retry_concurrency_and_collision(self):
        env = {'GIT_AUTHOR_NAME': 'Workshop Test', 'GIT_AUTHOR_EMAIL': 'test@example.invalid',
               'GIT_COMMITTER_NAME': 'Workshop Test', 'GIT_COMMITTER_EMAIL': 'test@example.invalid',
               'GIT_TERMINAL_PROMPT': '0'}
        with patch.dict(os.environ, env), tempfile.TemporaryDirectory(prefix='workshop-git-test-') as t:
            base = Path(t)
            remote = base / 'remote.git'
            git('init', '--bare', '--initial-branch=main', str(remote))
            seed = base / 'seed'
            git('clone', str(remote), str(seed))
            (seed / 'README.md').write_text('# Test repository\n')
            git('add', 'README.md', cwd=seed)
            git('commit', '-m', 'Seed test', cwd=seed)
            git('push', 'origin', 'main', cwd=seed)
            alpha = base / 'alpha.md'
            alpha.write_text(report('Alpha Table', 'Retail'))
            beta = base / 'beta.md'
            beta.write_text(report('Beta Table', 'Energy'))
            pushes = []

            def concurrent_push(attempt, checkout):
                pushes.append(attempt)
                if attempt == 0:
                    publish(beta, 'Beta Table', 'Energy', remote=str(remote))

            url = publish(alpha, 'Alpha Table', 'Retail', remote=str(remote), before_push=concurrent_push)
            self.assertTrue(url.endswith('/report-out/alpha-table-retail-analysis.md'))
            self.assertEqual(pushes, [0, 1])
            index = git('--git-dir', str(remote), 'show', 'main:report-out/README.md').stdout
            self.assertEqual(index.count('\n## '), 2)
            self.assertIn('Alpha Table', index)
            self.assertIn('Beta Table', index)
            before = git('--git-dir', str(remote), 'rev-parse', 'main').stdout
            publish(alpha, 'Alpha Table', 'Retail', remote=str(remote))
            after = git('--git-dir', str(remote), 'rev-parse', 'main').stdout
            self.assertEqual(before, after, 'An identical retry must not create another commit.')
            alpha.write_text(report('Alpha Table', 'Retail', 'Different content that must not overwrite the existing table.'))
            with self.assertRaises(ValueError):
                publish(alpha, 'Alpha Table', 'Retail', remote=str(remote))
            self.assertEqual(after, git('--git-dir', str(remote), 'rev-parse', 'main').stdout)
            self.assertEqual(git('status', '--porcelain', cwd=seed).stdout, '')


if __name__ == '__main__':
    unittest.main()
