#!/usr/bin/env python3
"""Check local links, skill metadata, and meaningful calculator invariants."""
from pathlib import Path
from urllib.parse import unquote
import json
import math
import re
import subprocess
import sys
from simulate import capacity

ROOT = Path(__file__).resolve().parents[1]

def main():
    checked = 0
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:
            continue
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
            if '://' in target or target.startswith('#'):
                continue
            target = unquote(target.split('#')[0])
            assert (path.parent / target).exists(), f'Broken link in {path}: {target}'
            checked += 1
    skills = sorted((ROOT / '.claude/skills').glob('*/SKILL.md'))
    assert len(skills) == 5
    for path in skills:
        text = path.read_text()
        header = text.split('---', 2)[1]
        assert f'name: {path.parent.name}\n' in header
        assert re.search(r'^description: .+', header, re.M)
        for ref in re.findall(r'`((?:docs|materials|templates)/[^`]+\.md)`', text):
            assert (ROOT / ref).exists(), f'Missing skill resource: {ref}'
    assert capacity(120, 12, 8, 1, 20)['completed_briefs'] == 12
    assert capacity(120, 12, 4, 1.5, 20)['completed_briefs'] == 8
    assert capacity(120, 12, 4, .75, 20)['completed_briefs'] == 16
    assert capacity(120, 12, 4, .75, 6)['completed_briefs'] == 6
    assert capacity(120, 12, 8, 1, 0)['completed_briefs'] == 0
    assert capacity(0, 12, 8, 1, 20)['completed_briefs'] == 0
    assert capacity(10, 10, 3, 3, 10)['completed_briefs'] == 3
    assert capacity(12, 12, 1, 1, 12)['limiting_factors'] == ['analysts', 'review', 'demand']
    for invalid in (0, -1, math.nan, math.inf):
        try:
            capacity(120, 12, invalid, 1, 20)
        except ValueError:
            pass
        else:
            raise AssertionError('invalid time accepted')
    calc = ROOT / 'scripts/simulate.py'
    out = subprocess.check_output([sys.executable, str(calc), '--json'], text=True)
    assert [c['completed_briefs'] for c in json.loads(out)['cases']] == [12, 8, 16]
    out = subprocess.check_output([sys.executable, str(calc), '--demand', '6', '--json'], text=True)
    assert all(c['completed_briefs'] == 6 for c in json.loads(out)['cases'])
    for args in (['--agent-review-time', '0'], ['--demand', '-1'], ['--demand', 'nan']):
        assert subprocess.run([sys.executable, str(calc)] + args, capture_output=True).returncode != 0
    print(f'PASS: {len(skills)} skills; {checked} local links; calculator scenarios, boundaries, ties and CLI rejection checks.')

if __name__ == '__main__':
    main()
