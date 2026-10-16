# What becomes possible when teams have AI agents?

A table workshop for the Chancellor's Circle, with an AI 1010 student helping each table use Claude. **Start here. You do not need to know how to code.**

## The task

Choose an industry you know. Explore one important change AI agents could make possible in three to five years. Test what would have to be true. Leave with a one-page scenario brief.

An agent can use tools to research, calculate, and create files. A **skill** is a reusable folder of instructions that teaches the agent how to do a particular kind of work. Here, each skill runs one discussion exercise. People supply experience, challenge the work, and decide what to keep.

## Student guide: do these six things

1. Before the session, get the **whole folder**, including the hidden `.claude` folder. Open it in Claude Code, or give a folder-capable Claude session access to it. A repository link alone does not guarantee file access. See setup below.
2. Print [the table guide](output/pdf/table-guide.pdf), one per participant, and [the worksheet](output/pdf/scenario-worksheet.pdf), one per table. Keep a copy of the [backup pack](output/pdf/backup-pack.pdf) on the laptop.
3. Ask: **“Which industry do we know? What is one change worth exploring?”** Record the table's first expectation before asking Claude for analysis. If the table is stuck after one minute, offer the prepared advisory-firm case.
4. Help the table pick **one** approach below. Paste its start prompt. Start a 20-minute timer. Read each question aloud; let people answer before typing.
5. At minute 16, type **“We have four minutes left. Draft our brief now from what we have.”** Read the draft aloud and correct it together.
6. Save the brief, then prepare a 30-second report: **“We explored ___. We were surprised by ___. Our biggest uncertainty is ___.”** Follow the organizer's instructions for handing it over. Nothing is sent automatically.

## Choose an approach

| If the table asks… | Choose | Paste into Claude Code |
| --- | --- | --- |
| “Is this really happening?” | Research | `/workshop-research` |
| “What changes if this becomes easier?” | Simulation | `/workshop-simulation` |
| “Who would welcome or resist this?” | Role playing | `/workshop-role-play` |
| “How could the future unfold differently?” | Forecasting | `/workshop-forecasting` |
| “What is stopping this from working?” | Problem solving | `/workshop-problem-solving` |

Add your industry and proposed change after the command, or let Claude ask. Example:

```text
/workshop-simulation Our industry is professional services. Could a small advisory firm serve more clients with agents? Use the prepared case. Guide our table one step at a time. We have 20 minutes.
```

To begin without deciding, paste:

```text
Read CLAUDE.md and docs/facilitation.md. Help our table choose one of the five workshop skills. Ask one short question at a time. Do not analyze the topic until we have recorded our initial expectation. We have 20 minutes after choosing.
```

You can change approaches. Say: **“Switch to role playing. Keep our notes. We have eight minutes left.”** Claude should run only the useful next step and protect time for the brief. Do not restart another 20-minute exercise.

## Setup before people arrive

### Claude Code: project skills

1. Download and unzip the kit, or clone its repository if the organizer supplies a remote URL. Keep the folder intact; do not copy only the visible Markdown files.
2. Open Claude Code in the `table-workshop` folder. If using a terminal with Claude Code already installed, change into the folder and run `claude`.
3. Confirm the five `/workshop-...` commands are available. If they are missing, use the explicit-file prompt below. Do not spend table time troubleshooting skill discovery.
4. Run one practice exercise with the prepared case. Confirm Claude can read the source cards, write an output file, and run the simulation if available. Use a fresh chat for the actual table.
5. Check sign-in, approved account, power, Wi-Fi, and the backup PDFs. No extra package installation, API key, or connector is required for the exercises. Live research needs web access; all five have an offline path.

Anthropic documents project skills in `.claude/skills/` and the `SKILL.md` format in its [Claude Code skills guide](https://code.claude.com/docs/en/skills). Product and organization settings may affect availability. Setup documentation checked October 15, 2026.

### Folder-capable Claude, including a configured Cowork session

Give the session access to this extracted folder using the folder controls available in your environment. Then paste:

```text
Read README.md, CLAUDE.md, docs/facilitation.md, and .claude/skills/workshop-role-play/SKILL.md in this folder. Follow that skill to guide us through a 20-minute exercise using the prepared case. Ask one short question, then wait for us. Tell us immediately if you cannot read a named file.
```

Replace `workshop-role-play` with your chosen skill's folder name. This is an explicit file-reading workflow; it does not depend on automatic skill installation. If hidden files cannot be selected, have the student open the chosen `SKILL.md` in a text editor and paste its text, followed by `docs/facilitation.md`, `materials/advisory-firm-case.md`, `materials/source-cards.md`, and `templates/scenario-brief.md` into the chat. Add `materials/role-cards.md` for role playing, `materials/constraint-cards.md` for problem solving, or `materials/simulation-worked-example.md` for simulation. The full kit ZIP is a distribution archive, not an individually installable Claude.ai skill ZIP.

### If Claude or Wi-Fi fails

Open [the backup pack](output/pdf/backup-pack.pdf). Follow the chosen exercise on paper, using its source cards and worked numbers. A person keeps time and another takes notes. The table can still produce the same brief. For a different industry without web access, mark evidence gaps rather than treating the prepared case's studies as evidence about that industry.

## What to say while guiding

- “What would you change in that answer?”
- “What are we assuming?”
- “What happens to the rest of the work?”
- “Who knows something the agent missed?”
- “What would convince us we are wrong?”

Invite each person to contribute, including yourself. You are a participant as well as the operator. Keep answers short enough that people spend more time talking than watching. Preserve disagreements.

## Fit within the 50-minute session

| Session minute | Activity |
| --- | --- |
| 0–8 | Instructor introduction |
| 8–12 | Choose industry, change, initial expectation, and approach |
| 12–32 | One complete 20-minute exercise, including a first brief |
| 32–40 | Stress-test: what fails, who resists, what evidence points elsewhere? |
| 40–47 | Revise and agree on the one-page brief |
| 47–50 | Report one surprise or uncertainty |

This shifts the draft's 18-minute open investigation to 20 minutes and shortens the separate stress test by two minutes. The exercise already includes a challenge round. If the instructor keeps the original 12–30 window, type **“18 minutes total”**; shorten exploration by two minutes and retain the final four minutes for the brief. Do one exercise, not all five. Later discussion can use another approach without restarting.

## What is in this repository?

- [Table guide](docs/table-guide.md): the simple participant instructions.
- [Facilitation rules](docs/facilitation.md): pacing and agent behavior shared by all five skills.
- [Prepared case](materials/advisory-firm-case.md): fictional firm, work, and starting assumptions.
- [Source cards](materials/source-cards.md): short attributed evidence summaries available offline.
- [Industry starters](materials/industry-starters.md): quick ways to use the table's own expertise.
- [Role cards](materials/role-cards.md) and [constraint cards](materials/constraint-cards.md).
- [Simulation worked example](materials/simulation-worked-example.md) and [calculator](scripts/simulate.py): no external dependencies.
- [Brief template](templates/scenario-brief.md), [worked brief](examples/scenario-brief.md), and [five sample exercise outputs](examples/approach-outputs.md).
- [Methods and sources](docs/methods-and-sources.md): the research behind each approach and what we shortened.
- `.claude/skills/`: five short, readable skills. Open one to show what instructions look like.
- `output/pdf/`: ready-to-print table guide, worksheet, and backup pack.
- `outputs/`: your table's local working files. Git ignores these by default.

## Show what a skill is: a 60-second demonstration

1. Open [.claude/skills/workshop-role-play/SKILL.md](.claude/skills/workshop-role-play/SKILL.md).
2. Point to `name` and `description`: these tell Claude what the skill is for.
3. Show the timed steps: these describe how to lead the exercise.
4. Open [the role cards](materials/role-cards.md): a skill can use prepared resources.
5. Start the skill. Show that it asks for the table's judgment before continuing.

The skill supplies a process. It does not establish that Claude's claims or imagined stakeholder reactions are true. See Anthropic's [explanation of Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).

## Save and share

Use `outputs/table-01-scenario-brief.md` (change the table number). If Claude cannot write files, copy its brief into a local document. Keep it to about 350–450 words plus source links. Review it before sharing. Use public examples and fictional numbers; omit confidential company, client, employee, or student information.

This kit is a standalone local Git repository. It includes no attendee profiles, emails, or internal planning attachments. It has no configured remote and nothing is published automatically. To distribute it, send the supplied ZIP or have the organizer publish this folder to an approved repository. Share the whole kit; the individual skills use shared materials here.

## Maintainer checks

Python 3 is needed only for the optional calculator and validation:

```bash
python3 scripts/simulate.py
python3 scripts/validate_kit.py
```

The PDFs can be rebuilt with `python3 scripts/build_printables.py` if ReportLab is installed. Runtime requirements for normal workshop use are only a working Claude session, or the printed backup. See [validation notes](docs/validation.md) for what has and has not been tested.
