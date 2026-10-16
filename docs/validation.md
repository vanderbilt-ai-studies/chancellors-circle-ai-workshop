# Validation and rehearsal notes

Checked October 15, 2026.

## Checks completed

- All five skills passed the skill-creator `quick_validate.py` checks for names and YAML frontmatter.
- `python3 scripts/validate_kit.py` checks local Markdown links and skill-resource paths. It also executes the calculator CLI and checks baseline, agent, sensitivity, demand-limited, zero-capacity, fractional-capacity, and tied-bottleneck cases. Invalid zero task time, negative demand, and non-finite demand are rejected.
- The fictional worked example and calculator agree: 12 briefs today; eight under the prepared agent assumptions; 16 if only agent review time changes to 0.75 hours; six if demand falls to six.
- The three PDFs were rendered to images and inspected. The table guide and worksheet are one page each. The backup pack has nine pages. Source references remain clickable in the digital PDF.
- Original-publisher methods sources and Anthropic's project-skill documentation informed the design. See `methods-and-sources.md` for links and access limits.

## Behavioral review

An independent agent conducted compressed offline walkthroughs of all five skills using the prepared advisory-firm case, plausible participant replies, a disagreement, and a four-minute wrap-up interruption. It also checked a switch with eight minutes remaining. This was a model-generated facilitation simulation, **not execution inside Claude**, a live group test, or a measured 20-minute rehearsal. The six-section briefs contained 405–450 words including headings and links. The calculator was also executed with a table replacement of 0.9 review hours, producing 13 completed briefs; changing only review to 0.75 produced 16. No blocking issue was identified. Review artifacts were kept outside the repository.

## Rehearse on the actual laptop

1. Open the whole extracted kit in the intended Claude environment.
2. Start one chosen skill with the prepared case. Confirm it asks and waits rather than producing the whole exercise at once.
3. Confirm the source cards and other resources are readable. If using simulation, run the calculator or open the paper example.
4. Say “four minutes left.” Confirm a brief appears and can be saved or copied.
5. Open all backup PDFs offline. Confirm the student knows how to keep time and collect the brief.

Claude discovery, institutional settings, web tools, and file-writing permissions have not been tested on the loaner configuration. Twenty minutes is the facilitation target; actual time depends on the group and tool response times. The student should shorten exploration and protect the final four minutes.
