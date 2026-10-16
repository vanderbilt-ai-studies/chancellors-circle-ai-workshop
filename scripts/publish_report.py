#!/usr/bin/env python3
"""Commit and push one explicitly approved report; leave the student's checkout alone."""
from pathlib import Path
import argparse
import subprocess
import sys
import tempfile
from report_out import filename, read_report, render_index

REPOSITORY = 'https://github.com/vanderbilt-ai-studies/chancellors-circle-ai-workshop.git'
WEB = 'https://github.com/vanderbilt-ai-studies/chancellors-circle-ai-workshop'


def git(*args, cwd=None, check=True):
    result = subprocess.run(['git', *args], cwd=cwd, capture_output=True, text=True,
                            timeout=90)
    if check and result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or 'Git command failed.')
    return result


def publish(source, table, industry, remote=REPOSITORY, before_push=None):
    source = Path(source)
    if source.is_symlink() or not source.is_file():
        raise ValueError('Choose a regular local Markdown report file.')
    source = source.resolve()
    text = source.read_text()
    meta = read_report(text)
    if meta['Table'] != table or meta['Industry'] != industry:
        raise ValueError('Table and industry arguments must match the reviewed report metadata.')
    name = filename(table, industry)
    relative = f'report-out/{name}'
    # Fresh checkouts avoid modifying the student's branch, staged files, or settings.
    # If another table wins a push race, clone the latest state and rebuild the index.
    for attempt in range(3):
        with tempfile.TemporaryDirectory(prefix='workshop-report-') as folder:
            checkout = Path(folder) / 'repo'
            git('clone', '--quiet', '--single-branch', '--branch', 'main', remote, str(checkout))
            target = checkout / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists() and target.read_text() != text:
                raise ValueError('This table/industry filename already has different content. Keep that report; choose a distinct table name or ask Jesse to review an update.')
            target.write_text(text)
            index = target.parent / 'README.md'
            index.write_text(render_index(target.parent))
            git('add', '--', relative, 'report-out/README.md', cwd=checkout)
            changed = git('diff', '--cached', '--quiet', cwd=checkout, check=False)
            if changed.returncode == 0:
                return f'{WEB}/blob/main/{relative}'
            if changed.returncode != 1:
                raise RuntimeError(changed.stderr.strip() or 'Could not inspect report changes.')
            git('commit', '--quiet', '-m', f'Add {table} report on {industry}', cwd=checkout)
            if before_push is not None:
                before_push(attempt, checkout)
            result = git('push', 'origin', 'HEAD:main', cwd=checkout, check=False)
            if result.returncode == 0:
                git('fetch', '--quiet', 'origin', 'main', cwd=checkout)
                actual = git('show', f'origin/main:{relative}', cwd=checkout).stdout
                actual_index = git('show', 'origin/main:report-out/README.md', cwd=checkout).stdout
                if actual != text or f']({name})' not in actual_index:
                    raise RuntimeError('Push returned success but report verification failed; ask Jesse to check before retrying.')
                return f'{WEB}/blob/main/{relative}'
            error = result.stderr + result.stdout
            # Reconcile ambiguous outcomes before considering another push.
            fetched = git('fetch', '--quiet', 'origin', 'main', cwd=checkout, check=False)
            if fetched.returncode == 0:
                actual = git('show', f'origin/main:{relative}', cwd=checkout, check=False)
                actual_index = git('show', 'origin/main:report-out/README.md', cwd=checkout, check=False)
                if actual.returncode == 0 and actual.stdout == text and f']({name})' in actual_index.stdout:
                    return f'{WEB}/blob/main/{relative}'
            if not any(marker in error.lower() for marker in ('fetch first', 'non-fast-forward', 'remote contains work')):
                raise RuntimeError(error.strip() or 'Push failed. Keep your local report and ask Jesse for help.')
    raise RuntimeError('Other tables updated the repository during three attempts. Your local report is intact; ask Jesse to push it.')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('report', type=Path)
    p.add_argument('--table', required=True)
    p.add_argument('--industry', required=True)
    p.add_argument('--publish', action='store_true', help='use only after the table reviewed the report and the student explicitly asked to push it')
    a = p.parse_args()
    try:
        meta = read_report(a.report.read_text())
        if meta['Table'] != a.table or meta['Industry'] != a.industry:
            raise ValueError('Table and industry must match the report metadata.')
        if not a.publish:
            print(f'Checked: report-out/{filename(a.table, a.industry)}. Not published; add --publish after the student asks to push.')
            return
        print('Published and verified: ' + publish(a.report, a.table, a.industry))
    except (ValueError, RuntimeError, OSError, subprocess.TimeoutExpired) as e:
        print(f'Not confirmed published: {e}\nKeep the local report and ask Jesse for help.', file=sys.stderr)
        raise SystemExit(1)


if __name__ == '__main__':
    main()
