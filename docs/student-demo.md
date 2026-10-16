# Student guide: explain it as you do it

Meet Friday, October 16 at **1:45 p.m. Central** at the Seigenthaler Center. Bring your laptop and charger. The workshop runs **2:10–3:00 p.m.** Ask Jesse if you are unsure. Participation in the following session is possible; he will confirm.

You help run Claude Code, explain what is happening, and contribute your perspective. The table chooses the industry and the approach. Keep explanations short and return to the discussion.

## 1. Explain an agent in one sentence

“An AI agent can work toward a goal by taking steps, using tools, checking the results, and adjusting what it does next.”

Point to an actual action when it happens: reading a file, searching a source, running a calculation, or saving the brief. Which actions are available depends on the session's tools and permissions.

## 2. Show the skill before you call it

Open the chosen file in an editor or ask Claude Code to display it:

| The table chooses | File to show | Command to type in Claude Code |
| --- | --- | --- |
| Research | `.claude/skills/workshop-research/SKILL.md` | `/workshop-research` |
| Simulation | `.claude/skills/workshop-simulation/SKILL.md` | `/workshop-simulation` |
| Role playing | `.claude/skills/workshop-role-play/SKILL.md` | `/workshop-role-play` |
| Forecasting | `.claude/skills/workshop-forecasting/SKILL.md` | `/workshop-forecasting` |
| Problem solving | `.claude/skills/workshop-problem-solving/SKILL.md` | `/workshop-problem-solving` |

Say: “A skill is a reusable set of instructions, with any materials the agent needs. This one tells Claude how to lead our exercise.”

Point to `name` and `description`, then one timed step and a reference to a prepared file. Say: “We can read these instructions and change them. Calling the skill gives Claude this process to follow.”

## 3. Call it in front of the table

Type the command into the **Claude Code conversation**, not your laptop's shell. Add the industry and question. For example:

```text
/workshop-research Our industry is retail. Could agents help a small retailer compare new product ideas? Lead us one step at a time. We have 20 minutes.
```

Let the table supply its initial expectation before Claude starts analyzing. Say: “You choose the direction. I will help operate Claude Code.”

## 4. Explain one real action or analysis step

Use the example that matches what actually happened:

- **Research:** “It opened this source. Let's check what the source actually supports.” If using prepared cards, say it read a prepared summary; do not describe that as live research.
- **Simulation:** “It calculated the result from these assumptions. We can change an assumption and compare.” If the code did not execute, say you are using the worked example.
- **Role playing:** “It is helping us try another perspective. An imagined reaction gives us a question to test with real people.”
- **Forecasting:** “It drafted two possible futures. Let's check what would have to be true for each and what signs we could watch.” These are scenarios, not established predictions.
- **Problem solving:** “It compared responses to this obstacle. Let's add a constraint and see which response still works.” A proposed test does not establish that a solution works.
- **Saving:** “It is putting our conclusions in a file we can review and revise.” Say this only if it saved a file; otherwise copy the displayed brief.

A skill supplies instructions; tools let the agent take actions. Neither guarantees the answer is correct. Invite a correction and show Claude how to revise its work.

## 5. Keep people involved

Ask: “What did it miss?” “Who sees this differently?” “What should we change?” Do not turn the demonstration into a lecture. If you do not know an answer, say so and ask Jesse.

At minute 16, type: **“We have four minutes left. Draft our brief now.”** Read it together. Keep the table's disagreement and make sure the draft reflects what people actually said.

## 6. Name the table and publish its reviewed report

Ask Claude to collect the table's ideas into a succinct one-paragraph summary. Review it together, then ask the table to choose its own name.

Give Claude the chosen name and industry and ask it to save, commit, and push the report as `report-out/[table-name]-[industry]-analysis.md`. Use the exact final prompt in [the submission instructions](report-out.md). Confirm Claude returns a verified published link and that your table has its own section in [Report out](../report-out/README.md). If a push fails, keep the local file and ask Jesse to submit it.

The brief describes a possible industry future and what people would still need to contribute. It will inform the discussion about preparing students. One implication for a new graduate is enough here; the next session can explore preparation in depth. Keep the brief ready whether or not students join that session.

Offer all five approaches equally. The table chooses one to begin and can switch if another question becomes more useful. Keep the same notes and remaining time; no table needs to complete all five.
