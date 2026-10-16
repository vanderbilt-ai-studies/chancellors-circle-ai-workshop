# Student AI Guide

**Friday, October 16:** meet at **1:45 p.m. Central**, Seigenthaler Center. Bring your laptop and charger. The workshop runs **2:10-3:00 p.m.** Ask Jesse whenever you are unsure.

**Your job:** help the table choose a question, use a skill, judge the analysis, and publish its reviewed report. Contribute your own perspective too.

Repository: https://github.com/vanderbilt-ai-studies/chancellors-circle-ai-workshop

## 1. Open the kit in Claude Code

Clone the repo or download and unzip it. Open the folder containing `README.md` and `CLAUDE.md`. Ask Claude:

```text
Read README.md and CLAUDE.md. Check that all five workshop skills and their prepared materials are readable. Do not start an exercise yet.
```

## 2. Check that you are ready

Check Claude Code and GitHub sign-in, repository access, power, and Wi-Fi. Keep `output/pdf/backup-pack.pdf` available offline. Start a fresh conversation for the table.

## 3. Explain an agent and a skill

**Say:** “An agent can work toward a goal by using tools, checking results, and adjusting its next step. A skill gives it a reusable process and materials for a particular task.”

You help operate Claude Code and answer questions. Members can try it too. Everyone judges the work.

## 4. Choose the industry and question

**Ask:** “Which industry do we know? What could agents make possible in three to five years?” Write down the table's initial expectation before Claude analyzes it.

## 5. Choose one skill and start it

| Approach | Ask this | Type into Claude Code |
| --- | --- | --- |
| Research | Is it happening? | `/workshop-research` |
| Simulation | What would change? | `/workshop-simulation` |
| Role playing | Who sees it differently? | `/workshop-role-play` |
| Forecasting | Faster or slower change? | `/workshop-forecasting` |
| Problem solving | What could stop it? | `/workshop-problem-solving` |

Show the chosen `.claude/skills/[skill-name]/SKILL.md`: its name, description, and one timed step. Type the command in the **Claude Code conversation**. Add the industry's question, for example:

```text
/workshop-research Our industry is retail. Could agents help a small retailer compare product ideas? Guide us one step at a time. We have 20 minutes.
```

**Start a 20-minute timer.** Choose one approach to begin; switch if another question becomes more useful. If the table is stuck, offer the prepared advisory-firm case.

<!-- page-break -->

# Guide, Summarize, and Submit

## 6. Keep the discussion moving

Read each question aloud. Let people answer, then type their views into Claude. Invite disagreement and corrections. Name a real action as it happens: “It opened this source” or “It calculated from these assumptions.”

**Ask:** “Are these reasonable conclusions? What are we assuming? What would make this fail?” Keep evidence separate from invented numbers and imagined reactions.

To change approaches, say: “Switch to role playing. Keep our notes. We have eight minutes left.” Keep the same timer.

## 7. At minute 16, ask for the draft

```text
We have four minutes left. Collect our ideas and draft our short scenario brief using templates/scenario-brief.md. Include a succinct, one-paragraph summary.
```

## 8. Review it and name your table

Read the summary aloud. Correct it together. Keep the assumptions, uncertainty, and any disagreement. Ask the table to **choose its own name**.

The report should capture the change, evidence, plausible future, human contributions, biggest uncertainty, and changed thinking. The paragraph summary goes at the top.

## 9. Ask Claude to commit and push it

Replace [TABLE NAME] and [INDUSTRY] below with the table's actual choices. Use this after the table has reviewed the report:

```text
Our table is named [TABLE NAME]. Our industry is [INDUSTRY]. We have reviewed our analysis and its one-paragraph summary. Follow docs/report-out.md to save our well-formatted report under report-out/ as [table-name]-[industry]-analysis.md. Commit and push it to the workshop repository, include our table in the Report out page, and give us the published link when verified.
```

Use lowercase words with hyphens in the filename. Example: **Future Builders** + **Healthcare Operations** becomes `future-builders-healthcare-operations-analysis.md`. Claude can form the filename for you.

## 10. Verify and report back

Open the published link. Check that your table has its own section in **Report out**, with its summary and a link to the full analysis. Prepare this 30-second report:

**“We explored ___. We were surprised by ___. Our biggest uncertainty is ___.”**

Keep the report ready for the student-preparation discussion. Jesse will confirm whether you join that following session.

## If something goes wrong

**Skill missing:** ask Claude to read the chosen `SKILL.md` and follow it directly. **Claude or Wi-Fi unavailable:** use the backup pack on paper. **Push fails:** keep the Markdown file and ask Jesse to push it. A local save alone is not a finished submission.
