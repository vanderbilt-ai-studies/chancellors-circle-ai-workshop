# Alternative access if Claude Code is unavailable

The workshop uses Claude Code. These are fallback instructions only; ask Jesse for help before changing tools.

Give the session access to this extracted folder using the folder controls available in your environment. Then paste:

```text
Read README.md, CLAUDE.md, docs/facilitation.md, and .claude/skills/workshop-role-play/SKILL.md in this folder. Follow that skill to guide us through a 20-minute exercise using the prepared case. Ask one short question, then wait for us. Tell us immediately if you cannot read a named file.
```

Replace `workshop-role-play` with your chosen skill's folder name. This is an explicit file-reading workflow; it does not depend on automatic skill installation. If hidden files cannot be selected, have the student open the chosen `SKILL.md` in a text editor and paste its text, followed by `docs/facilitation.md`, `materials/advisory-firm-case.md`, `materials/source-cards.md`, and `templates/scenario-brief.md` into the chat. Add `materials/role-cards.md` for role playing, `materials/constraint-cards.md` for problem solving, or `materials/simulation-worked-example.md` for simulation. The full kit ZIP is a distribution archive, not an individually installable Claude.ai skill ZIP.

