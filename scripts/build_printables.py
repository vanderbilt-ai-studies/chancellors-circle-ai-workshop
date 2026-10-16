#!/usr/bin/env python3
"""Build the workshop PDFs in the instructor's Chancellor's Circle handout style."""
from pathlib import Path
from html import escape
import re
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, NextPageTemplate,
                               Paragraph, Spacer, Table, TableStyle, PageBreak, Flowable)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf'
FONTS = ROOT / 'assets/fonts'
WIDTH = 546
INK = colors.HexColor('#1C1C1C')
GOLD = colors.HexColor('#7A5E1F')
RULE = colors.HexColor('#B49248')
LIGHT_GOLD = colors.HexColor('#CFAE70')
CREAM = colors.HexColor('#F6F0E1')
BORDER = colors.HexColor('#E0D5BB')
GRAY = colors.HexColor('#5A5A5A')

for name in ('Carlito-Regular', 'Carlito-Bold', 'Carlito-Italic', 'Carlito-BoldItalic',
             'Caladea-Regular', 'Caladea-Bold'):
    pdfmetrics.registerFont(TTFont(name, str(FONTS / f'{name}.ttf')))
pdfmetrics.registerFontFamily('Carlito-Regular', normal='Carlito-Regular', bold='Carlito-Bold',
                              italic='Carlito-Italic', boldItalic='Carlito-BoldItalic')
S = {
 'body': ParagraphStyle('Body', fontName='Carlito-Regular', fontSize=11.2, leading=14,
                        textColor=INK, spaceAfter=6),
 'compact': ParagraphStyle('Compact', fontName='Carlito-Regular', fontSize=10.5, leading=13,
                           textColor=INK, spaceAfter=5),
 'small': ParagraphStyle('Small', fontName='Carlito-Regular', fontSize=9.5, leading=12,
                         textColor=GRAY, spaceAfter=5),
 'cell': ParagraphStyle('Cell', fontName='Carlito-Regular', fontSize=10, leading=12,
                        textColor=INK),
 'heading': ParagraphStyle('Heading', fontName='Caladea-Bold', fontSize=14.2, leading=17,
                           textColor=INK, spaceBefore=8, spaceAfter=6, keepWithNext=True),
 'number': ParagraphStyle('Number', fontName='Caladea-Bold', fontSize=11.5, leading=14,
                          textColor=GOLD),
 'question': ParagraphStyle('Question', fontName='Caladea-Regular', fontSize=14.8,
                            leading=18.4, textColor=colors.white, spaceAfter=0),
 'delivery': ParagraphStyle('Delivery', fontName='Carlito-Regular', fontSize=11.2,
                            leading=14, textColor=INK, spaceAfter=0),
}


def ascii_text(text):
    for old, new in [('–','-'), ('—','-'), ('‘',"'"), ('’',"'"), ('“','"'),
                     ('”','"'), ('→','->'), ('…','...')]:
        text = text.replace(old, new)
    return text


def rich(text):
    text = escape(ascii_text(text))
    text = re.sub(r'\[([^]]+)\]\((https?://[^)]+)\)',
                  r'<link href="\2" color="#7A5E1F">\1</link>', text)
    text = re.sub(r'\[([^]]+)\]\(([^)]+)\)', r'\1', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<i>\1</i>', text)
    return text.replace('`', '')


def p(text, style='body'):
    return Paragraph(rich(text), S[style])


class Label(Flowable):
    def __init__(self, text, color=GOLD):
        super().__init__()
        self.text, self.color, self.height = text.upper(), color, 15
        self.keepWithNext = True

    def draw(self):
        obj = self.canv.beginText(0, 4)
        obj.setFont('Carlito-Bold', 9)
        obj.setFillColor(self.color)
        obj.setCharSpace(1.15)
        obj.textOut(self.text)
        obj.setCharSpace(0)
        self.canv.drawText(obj)


def callout(label, text, dark=False):
    content = [Label(label, LIGHT_GOLD if dark else GOLD),
               p(text, 'question' if dark else 'delivery')]
    table = Table([[content]], colWidths=[WIDTH], hAlign='LEFT')
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), INK if dark else CREAM),
        ('BOX', (0,0), (-1,-1), 0 if dark else .7, INK if dark else BORDER),
        ('LEFTPADDING',(0,0),(-1,-1),12), ('RIGHTPADDING',(0,0),(-1,-1),12),
        ('TOPPADDING',(0,0),(-1,-1),9), ('BOTTOMPADDING',(0,0),(-1,-1),10)]))
    return table


def numbered(number, text, compact=False):
    table = Table([[p(str(number), 'number'), p(text, 'compact' if compact else 'body')]],
                  colWidths=[18, WIDTH-18], hAlign='LEFT')
    table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                              ('LEFTPADDING',(0,0),(-1,-1),0),
                              ('RIGHTPADDING',(0,0),(-1,-1),0),
                              ('TOPPADDING',(0,0),(-1,-1),0),
                              ('BOTTOMPADDING',(0,0),(-1,-1),2)]))
    return table


def grid(rows):
    count = len(rows[0])
    widths = {3:[94,163,289], 4:[76,131,168,171],
              7:[111,71,71,73,73,55,92]}.get(count, [WIDTH/count]*count)
    content = [[p(f'**{cell}**' if i == 0 else cell, 'cell')
                for cell in row] for i, row in enumerate(rows)]
    table = Table(content, colWidths=widths, repeatRows=1, hAlign='LEFT')
    table.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),CREAM), ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LINEBELOW',(0,0),(-1,0),.7,RULE),
        ('LINEBELOW',(0,1),(-1,-1),.35,BORDER),
        ('LEFTPADDING',(0,0),(-1,-1),6), ('RIGHTPADDING',(0,0),(-1,-1),6),
        ('TOPPADDING',(0,0),(-1,-1),6), ('BOTTOMPADDING',(0,0),(-1,-1),6)]))
    return table


def md(text):
    lines = text.strip().splitlines()
    story, i = [], 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                row = [cell.strip() for cell in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?', cell) for cell in row):
                    rows.append(row)
                i += 1
            story += [grid(rows), Spacer(1,8)]
            continue
        if line.startswith('# '):
            # The page header carries the first H1. Later H1s become section headings.
            if story:
                story.append(p(line[2:], 'heading'))
        elif line.startswith('## '):
            story.append(p(line[3:], 'heading'))
        elif re.match(r'^\d+\. ', line):
            number, body = line.split('. ', 1)
            story.append(numbered(number, body, compact=True))
        elif line.startswith('- '):
            story.append(p('- ' + line[2:], 'compact'))
        else:
            paragraph = line
            while i+1 < len(lines) and lines[i+1].strip() and not re.match(r'^(#|\||- |\d+\.)', lines[i+1].strip()):
                i += 1
                paragraph += ' ' + lines[i].strip()
            story.append(p(paragraph, 'compact'))
        i += 1
    return story


def build(name, story, title, role, section_titles=None):
    def page(canvas, doc, page_title):
        canvas.saveState()
        label = canvas.beginText(33, 754)
        label.setFont('Carlito-Bold', 9)
        label.setCharSpace(1.15)
        label.setFillColor(GOLD)
        label.textOut("VANDERBILT CHANCELLOR'S CIRCLE · " + role.upper())
        label.setCharSpace(0)
        canvas.drawText(label)
        canvas.setFont('Caladea-Bold', 20.2)
        canvas.setFillColor(INK)
        canvas.drawString(33, 729, ascii_text(page_title))
        canvas.setStrokeColor(RULE)
        canvas.setLineWidth(1.5)
        canvas.line(33, 717, 579, 717)
        canvas.setStrokeColor(BORDER)
        canvas.setLineWidth(.7)
        canvas.line(33, 43, 579, 43)
        canvas.setFont('Carlito-Regular', 9)
        canvas.setFillColor(GRAY)
        canvas.drawString(33, 30, 'AI 1010 student-facilitated workshop')
        canvas.drawRightString(579, 30, f"Vanderbilt Chancellor's Circle | {doc.page}")
        canvas.restoreState()
    doc = BaseDocTemplate(str(OUT/name), pagesize=letter, leftMargin=27, rightMargin=27,
                          topMargin=82, bottomMargin=49, title=title,
                          author="Vanderbilt Chancellor's Circle")
    for i, page_title in enumerate(section_titles or [title]):
        frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height,
                      leftPadding=6, rightPadding=6, topPadding=6, bottomPadding=6)
        def paint(canvas, current_doc, heading=page_title):
            page(canvas, current_doc, heading)
        doc.addPageTemplates(PageTemplate(id=f'section-{i}', frames=[frame], onPage=paint))
    doc.build(story)
    print(OUT/name)


def table_guide():
    text = (ROOT/'docs/table-guide.md').read_text()
    steps = re.findall(r'^(\d+)\. (.*)$', text, re.M)
    rows = [[cell.strip() for cell in line.strip('|').split('|')]
            for line in text.splitlines() if line.startswith('|') and '---' not in line]
    story = [callout('Our question', 'Choose an industry you know. What could AI agents make possible in the next three to five years?', dark=True),
             Spacer(1,8), p('**In this 20 minute exercise, your student AI guide will run Claude Code (you can as well if you like), and answer questions. Together, you run and evaluate an analysis of the industry you choose for your table.**'),
             Label('Discussion steps')]
    story += [numbered(number, body) for number, body in steps[:6]]
    story += [Spacer(1,4), Label('Choose your approach'), grid(rows), Spacer(1,10),
              callout('7 · Name your table and submit', steps[6][1].split('** ',1)[-1]), Spacer(1,8)]
    for line in text.splitlines():
        if line.startswith(('**Stuck?', '**Keep asking:', 'Use public examples.', 'Your brief', '**Report back:')):
            story.append(p(line, 'small'))
    return story


def worksheet():
    story = [callout('Table deliverable', 'One succinct paragraph, supported by a short analysis of the future your table explored.', dark=True), Spacer(1,10),
             p('**Table name:** ____________________   **Industry:** ____________________   **Approach:** ____________________', 'compact'),
             p('**Future year:** __________   **Initial expectation:** __________________________________________________', 'compact')]
    fields = [('The change we investigated','What could agents make possible?'),
              ('What is happening already?','Name evidence and sources, or mark a gap. Separate table experience.'),
              ('A plausible future','Are our conclusions reasonable? What are we assuming? What could fail?'),
              ('What people still contribute','What would people and organizations do? One implication for a new graduate?'),
              ('Our biggest disagreement or uncertainty','What would help us resolve it?'),
              ('What changed in our thinking?','Before ___. Now ___.')]
    for number, (heading, hint) in enumerate(fields, 1):
        story += [Spacer(1,5), numbered(number, f'**{heading}**'), p(hint, 'small'), Spacer(1,22)]
    story += [callout('Name your table and submit', 'Collect your ideas. Ask Claude for one succinct paragraph and review it together. Choose a table name, then ask the student to push your reviewed analysis to **Report out**.')]
    return story


def exercise(section):
    title, body = section.split('\n',1)
    match = re.search(r'- \*\*0[^:]*:\*\* (.*)', body)
    question = match.group(1) if match else 'Choose one change to explore and test it together.'
    story = [callout('Start here', question, dark=True), Spacer(1,12), Label('20-minute discussion')]
    for line in body.splitlines():
        if not line.strip():
            continue
        match = re.match(r'- \*\*([^*]+):\*\* (.*)', line)
        if match:
            timed = Table([[p(match.group(1), 'number'), p(match.group(2))]], colWidths=[54, WIDTH-54])
            timed.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),12)]))
            story.append(timed)
        else:
            story.append(p(line, 'compact'))
    story += [Spacer(1,12), callout('Table deliverable', 'Finish with the six sections and a succinct one-paragraph summary. Name your table, then ask the student to save and push its reviewed report using **docs/report-out.md**.')]
    return title, story


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    build('table-guide.pdf', table_guide(), 'What Could Change in an Industry You Know?', 'Table discussion guide')
    build('scenario-worksheet.pdf', worksheet(), 'Our Scenario Brief', 'Table worksheet')
    # Each backup section shares the header and callout system; no forced columns.
    pages = []
    case = (ROOT/'materials/advisory-firm-case.md').read_text().split('## Other ways into this case')[0]
    pages.append(('A Small Advisory Firm', [callout('Prepared case', 'Could a small firm use agents to serve more clients without reducing quality?', dark=True), Spacer(1,8)] + md(case)))
    pages.append(('Evidence Cards', md((ROOT/'materials/source-cards.md').read_text())))
    for section in (ROOT/'docs/offline-exercises.md').read_text().split('\n## ')[1:]:
        pages.append(exercise(section))
    pages.append(('Simulation You Can Do on Paper', md((ROOT/'materials/simulation-worked-example.md').read_text())))
    pages.append(('Role Cards and Constraints', md((ROOT/'materials/role-cards.md').read_text()+'\n\n'+(ROOT/'materials/constraint-cards.md').read_text())))
    # Build one multi-page file; change only the header title between sections.
    story = []
    for i, (title, items) in enumerate(pages):
        if i:
            story += [NextPageTemplate(f'section-{i}'), PageBreak()]
        story.extend(items)
    build('backup-pack.pdf', story, 'Workshop Backup Pack', 'Prepared materials',
          section_titles=[title for title, _ in pages])


if __name__ == '__main__':
    main()
