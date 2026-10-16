# Chancellor’s Circle: student workshop instructions

Help your table explore **what AI agents could make possible in an industry over the next three to five years**. You will help operate Claude Code, explain what it is doing, contribute your perspective, and help the table judge and publish its conclusions. **You do not need to know how to code.** Ask Jesse whenever you are unsure.

**Friday, October 16, 2026:** meet at **1:45 p.m. Central** at the [Seigenthaler Center](https://maps.app.goo.gl/6peyyH6PKakXd3KA9), **Room 110C**. Bring your **laptop and charger**. The workshop runs **2:10–3:00 p.m.** Jesse will confirm on site whether you will join the following session with Vice Provost Everette Fortner and Dean Matt Johnson-Roberson.

[Print the two-page student guide](output/pdf/student-guide.pdf) · [Editable student guide](docs/student-guide.md) · [Download the whole kit](https://github.com/vanderbilt-ai-studies/chancellors-circle-ai-workshop/archive/refs/heads/main.zip) · [View table reports](report-out/README.md)

## 1. Have Claude prepare the workshop

<a id="setup-at-the-145-pm-student-check-in"></a>

At the 1:45 p.m. check-in, open Claude desktop’s **Code** tab, choose **Local**, and select a working location such as **Documents**. Paste:

```text
Clone https://github.com/vanderbilt-ai-studies/chancellors-circle-ai-workshop into its own folder here and work inside it. Read README.md and CLAUDE.md and prepare the five workshop skills.
```

Approve the setup permissions needed for this task. Claude will create the folder, clone the repository, and prepare the skills. Keep working in that workshop folder.

## 2. Check that you are ready

- Check Claude Code sign-in, your own GitHub sign-in and repository access, power, and Wi-Fi. The four student facilitators have repository admin access; each needs to be signed in on their own laptop to submit a report.
- Confirm the five commands in step 5 are available. Try one briefly with the [prepared advisory-firm case](materials/advisory-firm-case.md); check that it asks one question and waits. If a command is missing, use the fallback below.
- Have the [table guide](output/pdf/table-guide.pdf) and [scenario worksheet](output/pdf/scenario-worksheet.pdf) ready, and save the [backup pack](output/pdf/backup-pack.pdf) for offline use. The organizer needs one table guide per participant and one worksheet per table.
- Start a **fresh conversation in the same workshop project** for the actual table.

## 3. Explain an agent and a skill

Say: **“An agent can work toward a goal by using tools, checking results, and adjusting its next step. A skill gives it a reusable process and materials for a particular task.”**

You help operate Claude Code and answer questions. Members can try it too. Everyone judges the work. Keep explanations short so the table spends its time discussing. The [demonstration guide](docs/student-demo.md) has more examples of what to say and show.

## 4. Choose the industry and question

Ask: **“Which industry do we know? What could agents make possible in three to five years?”** Choose one important change to explore. Record the table’s **initial expectation before Claude analyzes it**. If the table is stuck, offer the [prepared advisory-firm case](materials/advisory-firm-case.md).

## 5. Choose one skill and start it

| If the table asks… | Choose | Type into Claude Code |
| --- | --- | --- |
| “Is this really happening?” | Research | `/workshop-research` |
| “What changes if this becomes easier?” | Simulation | `/workshop-simulation` |
| “Who would welcome or resist this?” | Role playing | `/workshop-role-play` |
| “What could make change faster or slower?” | Forecasting | `/workshop-forecasting` |
| “What is the biggest obstacle, and could we overcome it?” | Problem solving | `/workshop-problem-solving` |

Show the chosen `.claude/skills/[skill-name]/SKILL.md`: its name, description, and one timed step. Then type its command into the **Claude Code conversation**, adding the industry and question. For example:

```text
/workshop-simulation Our industry is professional services. Could a small advisory firm serve more clients with agents? Use the prepared case. Guide our table one step at a time. We have 20 minutes.
```

**Start a 20-minute timer.** Choose one approach to begin; you do not need to complete all five. If the table needs help choosing, paste:

```text
Read CLAUDE.md and docs/facilitation.md. Help our table choose research, simulation, role playing, forecasting, or problem solving. Ask one short question at a time. Do not analyze the topic until we have recorded our initial expectation. We have 20 minutes after choosing.
```

## 6. Keep the discussion moving

Read each question aloud. Let people answer, then type their views into Claude. Invite everyone to contribute, including yourself. Ask: **“Are these reasonable conclusions? What are we assuming? What would make this fail?”** Preserve disagreement and correct the agent when needed.

Name a real action as it happens: **“It opened this source”** or **“It calculated from these assumptions.”** Distinguish evidence from hypothetical numbers and imagined reactions. If Claude reads a prepared source card, say that; describe live research only when it happens.

Switch approaches if another question becomes more useful: **“Switch to role playing. Keep our notes. We have eight minutes left.”** Keep the same timer and notes.

## 7. At minute 16, ask for the draft

```text
We have four minutes left. Collect our ideas and draft our short scenario brief using templates/scenario-brief.md. Include a succinct, one-paragraph summary.
```

## 8. Review it and name your table

Read the summary aloud and correct it together. Keep the assumptions, uncertainty, and any disagreement. Ask the table to **choose its own name**.

Use the [report template](templates/scenario-brief.md): an **80–120-word summary** followed by six short sections covering the change, evidence, plausible future and assumptions, human contributions, biggest uncertainty, and changed thinking. Aim for **350–450 words total plus source links**, including the summary. Review the full report before publishing. Use public examples and omit confidential or personal information.

## 9. Ask Claude to commit and push it

Once the table has reviewed the report, replace **[TABLE NAME]** and **[INDUSTRY]** with its choices and paste:

```text
Our table is named [TABLE NAME]. Our industry is [INDUSTRY]. We have reviewed our analysis. Format it using templates/scenario-brief.md: a title; Table, Industry, Approach(es), Date, and Horizon metadata; an 80–120-word Summary paragraph; and six sections: The change we investigated; What we found happening already; A plausible future and its assumptions; What people and organizations would still contribute; Our biggest disagreement or uncertainty; What changed in our thinking. Aim for 350–450 words total plus source links. End with “We explored ___. We were surprised by ___. Our biggest uncertainty is ___.” Preserve our conclusions and mark gaps. Save as report-out/[table-name]-[industry]-analysis.md. Follow docs/report-out.md to commit and push only our report and the updated Report out page, with our summary and analysis link. Give us the verified published link.
```

Claude can form the filename for you. For example, **Future Builders** discussing **Healthcare Operations** becomes `report-out/future-builders-healthcare-operations-analysis.md`.

The [submission instructions](docs/report-out.md) tell Claude how to publish your report and update the shared [Report out page](report-out/README.md) with your summary and a link to the full analysis. You do not need to run Git commands yourself.

## 10. Verify and report back

Open the published link. Check that your table has its own section on the [Report out page](report-out/README.md), with its summary and a working link to the full analysis. **A local save alone is not a finished submission.**

Prepare this 30-second report: **“We explored ___. We were surprised by ___. Our biggest uncertainty is ___.”** Keep the report ready for the student-preparation discussion, whether or not you join the following session.

## If something goes wrong

- **Skill command missing:** ask Claude to read the selected skill file and follow it directly. For role playing, paste the example below; change the folder name for another approach.
- **Claude or Wi-Fi unavailable:** ask Jesse and use the [backup pack](output/pdf/backup-pack.pdf) on paper. It includes source cards and worked numbers. Mark evidence gaps for industries the prepared case does not cover.
- **Push fails:** keep the Markdown report and ask Jesse to push it. Tell the table that publication has not been confirmed. Do not spend discussion time troubleshooting.

```text
Read CLAUDE.md, docs/facilitation.md, and .claude/skills/workshop-role-play/SKILL.md. Follow that skill to guide our table through a 20-minute exercise. Ask one short question and wait for us. Tell us if any file is unreadable.
```

If Claude Code itself is unavailable, [alternative access instructions](docs/alternative-access.md) are also available.

## Session timing

| Time (Central) | Activity |
| --- | --- |
| 2:10–2:18 | Instructor introduction |
| 2:18–2:22 | Choose industry, change, initial expectation, and approach |
| 2:22–2:42 | One 20-minute exercise, including the first draft |
| 2:42–2:50 | Stress-test the draft: what fails, who resists, what evidence points elsewhere? |
| 2:50–2:57 | Revise, name the table, and publish the reviewed report |
| 2:57–3:00 | Share one surprise or uncertainty |

If Jesse allows only 18 minutes for the exercise, tell Claude **“18 minutes total”** and retain the final four minutes for drafting.

<details>
<summary>More workshop materials</summary>

- [Table guide](docs/table-guide.md) and [scenario worksheet](output/pdf/scenario-worksheet.pdf).
- [Facilitation rules](docs/facilitation.md) and [student demonstration guide](docs/student-demo.md).
- [Prepared case](materials/advisory-firm-case.md), [industry starters](materials/industry-starters.md), [source cards](materials/source-cards.md), [role cards](materials/role-cards.md), and [constraint cards](materials/constraint-cards.md).
- [Simulation worked example](materials/simulation-worked-example.md) and [calculator](scripts/simulate.py).
- [Report template](templates/scenario-brief.md), [worked brief](examples/scenario-brief.md), and [five sample exercise outputs](examples/approach-outputs.md).
- [Methods and sources](docs/methods-and-sources.md) and [document style](docs/visual-style.md).

The five skills are in `.claude/skills/`. Printable materials are in `output/pdf/`. Claude can keep scratch work in ignored `outputs/`; reviewed reports go in `report-out/`.

</details>

<details>
<summary>Maintainer checks</summary>

Python 3 is used by the optional calculator, validation, and report-submission helper:

```bash
python3 scripts/simulate.py
python3 scripts/validate_kit.py
python3 -m unittest discover -s tests -v
```

The PDFs can be rebuilt with `python3 scripts/build_printables.py` if ReportLab is installed. Workshop discussion needs a working Claude Code session or the printed backup. Publishing through the submission helper also requires Git, Python 3, and authenticated repository access; see [submission instructions](docs/report-out.md). See [validation notes](docs/validation.md) for what has and has not been tested.

Maintain the editable Markdown and PDF builder as the sources for revisions; rebuild the four PDFs in `output/pdf/` when their content changes. These tracked PDFs are the ready-to-print deliverables. The separate `outputs/` folder is ignored scratch space for table work; reviewed submissions belong in `report-out/`. Keep distribution ZIPs outside the repository and use the download link above for the current published kit.
</details>
