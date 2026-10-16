# What becomes possible when teams have AI agents?

A table workshop for the Chancellor's Circle, with an AI 1010 student helping each table use **Claude Code**. **Start here. You do not need to know how to code.**

[GitHub repository](https://github.com/vanderbilt-ai-studies/chancellors-circle-ai-workshop) · [Download the whole kit](https://github.com/vanderbilt-ai-studies/chancellors-circle-ai-workshop/archive/refs/heads/main.zip)

## The task

Choose an industry you know. Explore one important change AI agents could make possible in three to five years. Test what would have to be true. Leave with a one-page scenario brief.

An agent can use tools to research, calculate, and create files. A **skill** is a reusable folder of instructions that teaches the agent how to do a particular kind of work. Here, each skill runs one discussion exercise. People supply experience, challenge the work, and decide what to keep.

## Friday, October 16: bring your laptop

- **Meet at 1:45 p.m. Central** at the [Seigenthaler Center](https://maps.app.goo.gl/6peyyH6PKakXd3KA9), next to the Commons Campus. Allow time to get there. Download the kit at check-in and get Claude Code ready on your own laptop. Bring your charger.
- **Workshop: 2:10–3:00 p.m.** 
- You will help the table work, demonstrate Claude Code and skills, explain what the agent is doing, and contribute your own perspective. Ask Jesse whenever you are unsure.
- - We **might** join the following session led by Vice Provost Everette Fortner and Dean Matt Johnson-Roberson. Jesse will confirm on site.

## Student guide: do these six things

1. At check-in, have Claude access and prepare all the skills in this repo. Follow the setup steps below.
2. Have [the table guide](output/pdf/table-guide.pdf) and [the worksheet](output/pdf/scenario-worksheet.pdf) ready. For printing, the organizer needs one guide per participant and one worksheet per table. Save the [backup pack](output/pdf/backup-pack.pdf) on your laptop.
3. Ask: **“Which industry do we know? What is one change worth exploring?”** Record the table's first expectation before asking Claude for analysis. If the table is stuck after one minute, offer the prepared advisory-firm case.
4. Help the table pick **research, simulation, role playing, forecasting, or problem solving**. Show its `SKILL.md` file, then type its `/workshop-...` command into Claude Code. Start a 20-minute timer. Read each question aloud; let people answer before typing.
5. At minute 16, type **“We have four minutes left. Draft our brief now from what we have.”** Read the draft aloud and correct it together.
6. Save the brief, then prepare a 30-second report: **“We explored ___. We were surprised by ___. Our biggest uncertainty is ___.”** Follow the organizer's instructions for handing it over. Nothing is sent automatically.

## Choose one of the five workshop approaches

| If the table asks… | Choose | Paste into Claude Code |
| --- | --- | --- |
| “Is this really happening?” | Research | `/workshop-research` |
| “What changes if this becomes easier?” | Simulation | `/workshop-simulation` |
| “Who would welcome or resist this?” | Role playing | `/workshop-role-play` |
| “What could make change faster or slower?” | Forecasting | `/workshop-forecasting` |
| “What is the biggest obstacle, and could we overcome it?” | Problem solving | `/workshop-problem-solving` |

**Choose one approach to begin. Change approaches if another question becomes more useful. You do not need to complete all five.** Each has its own skill and a roughly 20-minute exercise, including a first brief.

Add your industry and proposed change after the command, or let Claude ask. Example:

```text
/workshop-simulation Our industry is professional services. Could a small advisory firm serve more clients with agents? Use the prepared case. Guide our table one step at a time. We have 20 minutes.
```

To begin without deciding, paste:

```text
Read CLAUDE.md and docs/facilitation.md. Help our table choose research, simulation, role playing, forecasting, or problem solving. Ask one short question at a time. Do not analyze the topic until we have recorded our initial expectation. We have 20 minutes after choosing.
```

You can change approaches. Say: **“Switch to role playing. Keep our notes. We have eight minutes left.”** Claude should run only the useful next step and protect time for the brief. Do not restart another 20-minute exercise.

## Setup at the 1:45 p.m. student check-in

### Claude Code: project skills

1. Download and unzip the kit using the link above, or clone `https://github.com/vanderbilt-ai-studies/chancellors-circle-ai-workshop.git`. Keep the folder intact; do not copy only the visible Markdown files.
2. Open Claude Code in the extracted or cloned repository folder: the folder containing `README.md` and `CLAUDE.md`. If using a terminal with Claude Code already installed, change into that folder and run `claude`.
3. Confirm all five commands are available: `/workshop-research`, `/workshop-simulation`, `/workshop-role-play`, `/workshop-forecasting`, and `/workshop-problem-solving`. If they are missing, use the explicit-file prompt below. Do not spend table time troubleshooting skill discovery.
4. Do a quick check with the prepared case: invoke a skill and confirm that it asks one question and waits. Ask it to read a source card; if possible, save a practice note in `outputs/` and run the simulation. You do not need to finish a 20-minute exercise during check-in. Use a fresh chat for the actual table.
5. Check Claude Code sign-in, approved account, power, Wi-Fi, and the backup PDFs. The exercises need no extra package installation, API key, or connector once Claude Code is working. Live research needs web access; each exercise has an offline path. If setup stalls, ask Jesse and use the paper backup.

Anthropic documents project skills in `.claude/skills/` and the `SKILL.md` format in its [Claude Code skills guide](https://code.claude.com/docs/en/skills). Product and organization settings may affect availability. Setup documentation checked October 15, 2026.

### If a command is missing

Paste this directly into Claude Code, replacing the skill folder name if needed:

```text
Read CLAUDE.md, docs/facilitation.md, and .claude/skills/workshop-role-play/SKILL.md. Follow that skill to guide our table through a 20-minute exercise. Ask one short question and wait for us. Tell us if any file is unreadable.
```

If Claude Code itself is unavailable, ask Jesse. [Alternative access instructions](docs/alternative-access.md) are available as a backup.

### If Claude or Wi-Fi fails

Open [the backup pack](output/pdf/backup-pack.pdf). Follow the chosen exercise on paper, using its source cards and worked numbers. A person keeps time and another takes notes. The table can still produce the same brief. For a different industry without web access, mark evidence gaps rather than treating the prepared case's studies as evidence about that industry.

## Explain what is happening while you work

Use the short talking points in [the student demonstration guide](docs/student-demo.md). Show the skill file and its command once, then name a real tool action as it happens. Keep each explanation to one or two sentences so the table stays involved.

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
| 0–8 (2:10–2:18) | Instructor introduction |
| 8–12 (2:18–2:22) | Choose industry, change, initial expectation, and approach |
| 12–32 (2:22–2:42) | One complete 20-minute exercise, including a first brief |
| 32–40 (2:42–2:50) | Stress-test: what fails, who resists, what evidence points elsewhere? |
| 40–47 (2:50–2:57) | Revise and agree on the one-page brief |
| 47–50 (2:57–3:00) | Report one surprise or uncertainty |

This shifts the draft's 18-minute open investigation to 20 minutes and shortens the separate stress test by two minutes. The exercise already includes a challenge round. If the instructor keeps the original 12–30 window, type **“18 minutes total”**; shorten exploration by two minutes and retain the final four minutes for the brief. Begin with one exercise. Later discussion can use any of the other approaches without restarting the clock.

## What is in this repository?

- [Table guide](docs/table-guide.md): the simple participant instructions.
- [Student demonstration guide](docs/student-demo.md): short explanations and what to show in Claude Code.
- [Facilitation rules](docs/facilitation.md): pacing and agent behavior shared by all five skills.
- [Prepared case](materials/advisory-firm-case.md): fictional firm, work, and starting assumptions.
- [Source cards](materials/source-cards.md): short attributed evidence summaries available offline.
- [Industry starters](materials/industry-starters.md): quick ways to use the table's own expertise.
- [Role cards](materials/role-cards.md) and [constraint cards](materials/constraint-cards.md).
- [Simulation worked example](materials/simulation-worked-example.md) and [calculator](scripts/simulate.py): no external dependencies.
- [Brief template](templates/scenario-brief.md), [worked brief](examples/scenario-brief.md), and [five sample exercise outputs](examples/approach-outputs.md).
- [Methods and sources](docs/methods-and-sources.md): the research behind each approach and what we shortened.
- `.claude/skills/`: five short, readable skills with equal standing as starting options. Open one to show what instructions look like.
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

This kit is published in the Vanderbilt AI Studies [GitHub repository](https://github.com/vanderbilt-ai-studies/chancellors-circle-ai-workshop). It includes no attendee profiles, emails, or internal planning attachments. Students can download the whole repository ZIP without signing in once the repository is public. Share the whole kit; the individual skills use shared materials here. Your table's local `outputs/` files are ignored by Git by default and are not included in repository downloads.

## Maintainer checks

Python 3 is needed only for the optional calculator and validation:

```bash
python3 scripts/simulate.py
python3 scripts/validate_kit.py
```

The PDFs can be rebuilt with `python3 scripts/build_printables.py` if ReportLab is installed. Runtime requirements for normal workshop use are only a working Claude Code session, or the printed backup. See [validation notes](docs/validation.md) for what has and has not been tested.
