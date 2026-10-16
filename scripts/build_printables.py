#!/usr/bin/env python3
"""Build three print-ready PDFs. Requires ReportLab, not needed during workshop."""
from pathlib import Path
from html import escape
import re
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf'
INK = colors.HexColor('#182A36')
GOLD = colors.HexColor('#9B742F')
PALE = colors.HexColor('#F1F4F5')
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleKit', fontName='Helvetica-Bold', fontSize=23, leading=27, textColor=INK, spaceAfter=15))
styles.add(ParagraphStyle(name='HeadingKit', fontName='Helvetica-Bold', fontSize=13, leading=17, textColor=INK, spaceBefore=10, spaceAfter=7))
styles.add(ParagraphStyle(name='BodyKit', fontName='Helvetica', fontSize=10.5, leading=14.5, textColor=INK, spaceAfter=7))
styles.add(ParagraphStyle(name='CellKit', fontName='Helvetica', fontSize=9, leading=12, textColor=INK))
styles.add(ParagraphStyle(name='ExerciseKit', fontName='Helvetica', fontSize=12, leading=18, textColor=INK, spaceAfter=12))
styles.add(ParagraphStyle(name='SmallKit', fontName='Helvetica', fontSize=9, leading=12, textColor=INK, spaceAfter=6))

def ascii_text(t):
    for a,b in [('–','-'),('—','-'),('‘',"'"),('’',"'"),('“','"'),('”','"'),('→','->'),('…','...')]:
        t=t.replace(a,b)
    return t

def rich(t):
    t=escape(ascii_text(t))
    t=re.sub(r'\[([^]]+)\]\((https?://[^)]+)\)', r'<link href="\2" color="#315977">\1</link>', t)
    t=re.sub(r'\[([^]]+)\]\(([^)]+)\)', r'\1', t)
    t=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',t)
    t=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',t)
    t=t.replace('`','')
    return t

def p(t,style='BodyKit'):
    return Paragraph(rich(t), styles[style])

def md(text, table_width=504):
    lines=text.strip().splitlines(); story=[]; i=0
    while i<len(lines):
        line=lines[i].strip()
        if not line:
            i+=1; continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                cells=[x.strip() for x in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?',x) for x in cells):
                    rows.append([p(x,'CellKit') for x in cells])
                i+=1
            count=len(rows[0]); widths=[table_width/count]*count
            if count==3:widths=[90,135,table_width-225]
            tab=Table(rows,colWidths=widths,repeatRows=1,hAlign='LEFT')
            tab.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),PALE),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,0),.8,GOLD),('LINEBELOW',(0,1),(-1,-1),.3,colors.HexColor('#D9E0E3')),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
            story += [tab,Spacer(1,9)];continue
        if line.startswith('# '):story.append(p(line[2:],'TitleKit'))
        elif line.startswith('## '):story.append(p(line[3:],'HeadingKit'))
        elif line.startswith('- '):story.append(p('- '+line[2:]))
        else:
            para=line
            while i+1<len(lines) and lines[i+1].strip() and not re.match(r'^(#|\||- |\d+\.)',lines[i+1].strip()):
                i+=1;para+=' '+lines[i].strip()
            story.append(p(para))
        i+=1
    return story

def footer(canvas,doc):
    canvas.saveState();w,h=letter
    canvas.setStrokeColor(GOLD);canvas.setLineWidth(.7);canvas.line(54,42,w-54,42)
    canvas.setFillColor(INK);canvas.setFont('Helvetica',8)
    canvas.drawString(54,29,"CHANCELLOR'S CIRCLE | AI 1010 TABLE WORKSHOP")
    canvas.drawRightString(w-54,29,str(doc.page))
    canvas.restoreState()

def build(name,story):
    SimpleDocTemplate(str(OUT/name),pagesize=letter,rightMargin=54,leftMargin=54,topMargin=43,bottomMargin=56,
                      title=name.replace('-',' ').replace('.pdf','').title(),author='AI Workshop').build(story,onFirstPage=footer,onLaterPages=footer)
    print(OUT/name)

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    build('table-guide.pdf',md((ROOT/'docs/table-guide.md').read_text()))
    story=[p('Our scenario brief','TitleKit'),p('Table: __________   Industry: __________________   Approach: __________________','SmallKit'),p('Future year: __________   Initial expectation: __________________________________','SmallKit')]
    fields=[('1. The change we investigated','What could agents make possible?'),('2. What is happening already?','Name evidence and sources, or mark a gap. Separate table experience.'),('3. A plausible future','What must be true? What could fail? What sign would you watch?'),('4. What people still contribute','What would people and organizations do? One implication for a new graduate?'),('5. Our biggest disagreement or uncertainty','What would help us resolve it?'),('6. What changed in our thinking?','Before ___. Now ___.')]
    for title,hint in fields:
        story += [p(title,'HeadingKit'),p(hint,'SmallKit'),Spacer(1,19)]
    story += [Spacer(1,6),p('Report: We explored ___. We were surprised by ___. Our biggest uncertainty is ___.','SmallKit')]
    build('scenario-worksheet.pdf',story)
    styles['BodyKit'].fontSize=10
    styles['BodyKit'].leading=13
    styles['BodyKit'].spaceAfter=5
    styles['HeadingKit'].spaceBefore=8
    styles['HeadingKit'].spaceAfter=5
    pages=[]
    pages.append(md('# Work without Claude\n\nChoose one exercise. Keep a 20-minute timer. Talk, test the idea, and fill in the worksheet. Use the prepared case below or an industry you know. The student keeps time and takes notes.\n\n'+(ROOT/'materials/advisory-firm-case.md').read_text().split('## Other ways into this case')[0].replace('# Prepared case: a small advisory firm','## Prepared case: a small advisory firm')))
    pages.append(md((ROOT/'materials/source-cards.md').read_text()))
    offline=(ROOT/'docs/offline-exercises.md').read_text()
    for section in offline.split('\n## ')[1:]:
        title, body=section.split('\n',1)
        exercise=[p(title,'TitleKit')]
        exercise += [p(line.strip(),'ExerciseKit') for line in body.splitlines() if line.strip()]
        exercise += [Spacer(1,15),p('Finish with the six sections: change; evidence; future and assumptions; human contribution; uncertainty; changed thinking.','SmallKit')]
        pages.append(exercise)
    pages.append(md((ROOT/'materials/simulation-worked-example.md').read_text()))
    pages.append(md((ROOT/'materials/role-cards.md').read_text()+'\n\n'+(ROOT/'materials/constraint-cards.md').read_text()))
    story=[]
    for i,page in enumerate(pages):
        if i:story.append(PageBreak())
        story+=page
    build('backup-pack.pdf',story)

if __name__=='__main__':main()
