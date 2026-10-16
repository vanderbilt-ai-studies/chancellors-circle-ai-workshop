#!/usr/bin/env python3
"""Build the report-out page from one reviewed Markdown report per table."""
from pathlib import Path
import argparse
import re
import unicodedata

INTRO = '''# Report out

Each table names itself and contributes one reviewed analysis. Each section below links to that table's full report and shows its one-paragraph summary.

Reports are named `[table-name]-[industry]-analysis.md`. See [how to submit](../docs/report-out.md).
'''


def slug(value):
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode().lower()
    value = re.sub(r'[^a-z0-9]+', '-', value).strip('-')
    if not value or len(value) > 80:
        raise ValueError('Choose a table name and industry that each make a nonempty filename label of at most 80 characters.')
    return value


def filename(table, industry):
    return f'{slug(table)}-{slug(industry)}-analysis.md'


def read_report(text):
    metadata = {}
    for field in ('Table', 'Industry', 'Approach(es)', 'Date'):
        pattern = r'^\*\*' + re.escape(field) + r':\*\*[ \t]*(.+)$'
        match = re.search(pattern, text, re.M)
        if not match or not match.group(1).strip():
            raise ValueError(f'Report needs a **{field}:** metadata line; use templates/scenario-brief.md.')
        metadata[field] = match.group(1).strip()
    match = re.search(r'^## Summary\s*\n(.*?)(?=^## |\Z)', text, re.M | re.S)
    if not match:
        raise ValueError('Report needs a ## Summary section with one paragraph.')
    paragraphs = re.split(r'\n\s*\n', match.group(1).strip())
    if len(paragraphs) != 1 or not paragraphs[0] or re.match(r'^[#>*-]|^\d+\.', paragraphs[0]):
        raise ValueError('The summary must be one prose paragraph, not bullets or several paragraphs.')
    metadata['summary'] = ' '.join(paragraphs[0].split())
    return metadata


def render_index(directory):
    entries = []
    for path in Path(directory).glob('*-analysis.md'):
        meta = read_report(path.read_text())
        if path.name != filename(meta['Table'], meta['Industry']):
            raise ValueError(f'Filename does not match table and industry: {path.name}')
        entries.append((meta['Table'].casefold(), meta['Industry'].casefold(), path.name, meta))
    sections = [INTRO.rstrip()]
    if not entries:
        sections.append('No table reports have been submitted yet. Your table will get its own section here when its report is pushed.')
    for _, _, name, meta in sorted(entries):
        table = meta['Table'].replace('[', '').replace(']', '')
        industry = meta['Industry'].replace('[', '').replace(']', '')
        sections.append(f"## {table} — {industry}\n\n**Approach(es):** {meta['Approach(es)']} · **Date:** {meta['Date']}\n\n{meta['summary']}\n\n[Read the full analysis]({name})")
    return '\n\n'.join(sections) + '\n'


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--directory', type=Path, default=Path(__file__).resolve().parents[1] / 'report-out')
    args = p.parse_args()
    args.directory.mkdir(parents=True, exist_ok=True)
    (args.directory / 'README.md').write_text(render_index(args.directory))
    print(args.directory / 'README.md')


if __name__ == '__main__':
    main()
