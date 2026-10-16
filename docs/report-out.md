# Name your table and push its report

Each table chooses its own name. Its reviewed result goes in [Report out](../report-out/README.md), with one section linking to its Markdown analysis and showing its one-paragraph summary.

## Student: the final step

1. Ask the table to choose a name. Use its industry and approaches from the discussion.
2. Ask Claude to collect the ideas and write a succinct paragraph. Review and correct it together. Keep the rest of the one-page analysis beneath it, using [the template](../templates/scenario-brief.md).
3. When the table agrees the report is ready to share in this public repository, tell Claude the table name and ask it to **save, commit, and push the results**. For example:

```text
Our table is named Future Builders. Our industry is Healthcare Operations. We have reviewed the report and its one-paragraph summary. Save it as report-out/future-builders-healthcare-operations-analysis.md using the report template. Commit and push it to the workshop repository and include our table in the Report out page. Use docs/report-out.md, and give us the published link when verified.
```

Replace the name and industry with the table's own choices. You do not need to know Git commands; Claude Code can run the helper below after your request.

## Agent: prepare the report

- If the table has not named itself, ask for its name and wait. Do not invent one or use a table number as its chosen name. Use the known industry; ask only if missing.
- Use `templates/scenario-brief.md`. Put the **Table**, **Industry**, **Approach(es)**, and **Date** metadata on separate lines exactly as in that template. Include `## Summary` with one prose paragraph of roughly 80–120 words. Aim for 350–450 words total plus source links; do not make the summary a second long assignment.
- Keep evidence, assumptions, and imagined reactions clearly labeled. Do not invent table conclusions or publish confidential or personal information.
- Name the file `[table-name]-[industry]-analysis.md`: lowercase ASCII words joined with hyphens. Example: `Future Builders` + `Healthcare Operations` -> `future-builders-healthcare-operations-analysis.md`. The helper uses the same rule and removes accents and punctuation. If a name cannot make a usable label, ask for a short alternative.
- Save the reviewed file in `report-out/`. Drafts and scratch work may stay in ignored `outputs/`. Never overwrite a different table's report. If the filename is already taken with different content, ask the table to choose a distinct name or ask Jesse to review an update.
- Prepare and display the draft before publication. A student saying the report is ready and asking to push it authorizes publication; do not ask for a second confirmation. Merely finishing an exercise does not trigger a push.

## Agent: commit and push after the student's request

Run from the kit folder, using the actual file, table name, and industry:

```bash
python3 scripts/publish_report.py report-out/future-builders-healthcare-operations-analysis.md --table "Future Builders" --industry "Healthcare Operations" --publish
```

Without `--publish`, this command only checks the report. With `--publish`, it uses Git to clone the current shared repository into a temporary folder, copies only the reviewed report, rebuilds `report-out/README.md` with a section per submitted table, commits those two files, and pushes to `main`. This works from a downloaded ZIP too; it does not require changing the student's own checkout or pushing unrelated local changes.

The helper never force-pushes or overwrites a different report. If another table pushes first, it tries again from the latest repository state, up to three attempts. It verifies the report and index on the remote before reporting success. A retry of an identical report is safe.

**Access:** Git, Python 3, an authenticated GitHub account with repository push access, and Git author name/email must already work. The four student facilitators have been granted repository admin access. Use the student's own GitHub sign-in; do not share Jesse's credentials. If a sign-in, permission, branch rule, or network error blocks publication, keep the local file, say it was not confirmed published, and ask Jesse to push it. Never claim that a local save is a completed submission.

**If Python is unavailable:** Claude may use Git directly in a separate fresh clone, copy only this report, and regenerate the same index. If that is impractical, hand the Markdown file to Jesse. Do not install tools during table discussion or spend the reporting period troubleshooting.

At the end, give the table its published file link and the [Report out page](https://github.com/vanderbilt-ai-studies/chancellors-circle-ai-workshop/tree/main/report-out).

## Maintainer

The index is generated from actual `report-out/*-analysis.md` files; do not prefill fictional table results. To rebuild it locally:

```bash
python3 scripts/report_out.py
```

GitHub documents the account roles needed for pushing in [repository roles](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization). Concurrent pushes follow Git's [fast-forward update rules](https://git-scm.com/docs/git-push).
