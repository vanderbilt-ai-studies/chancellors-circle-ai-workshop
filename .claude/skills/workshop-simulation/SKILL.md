---
name: workshop-simulation
description: Lead a 20-minute workshop what-if calculation about how agents could change capacity and surrounding work. Use when a table wants to change assumptions and compare outcomes; not for estimating real business performance without data.
---

# Simulation: what changes when work gets easier?

Read `docs/facilitation.md` first. It sets the one-question-at-a-time interaction, evidence labels, switching behavior, and four-minute wrap-up. All paths below are relative to the repository root. Use the supplied topic and time; ask only for what is missing. Ask for the table's initial expectation before doing analysis. If no topic is chosen, offer `materials/advisory-firm-case.md` and wait for agreement.

The student keeps time. The schedule below totals 20 minutes including a first brief. At four minutes remaining, skip unfinished exploration and draft. Do not run all the steps in one answer.

## 0–2 minutes: choose the outcome

Ask what the table wants to compare: completed work, waiting, quality, or another outcome. Default to the prepared case's completed briefs per week if accepted. Read `materials/simulation-worked-example.md`. Its tiny capacity model supports throughput only; treat other outcomes qualitatively or state a separate model.

## 2–6 minutes: expose the assumptions

Show the case's analyst hours, reviewer hours, time per brief, and demand. Label every input fictional. Ask which assumption seems least believable. Accept the table's replacement as a hypothesis, recording units. For another industry, ask the table to accept or replace hypothetical inputs; do not imply these are industry estimates.

If using the calculator, run `python3 scripts/simulate.py` from the repository root. It needs only Python 3. If execution fails, use the worked example on paper immediately. Do not install packages during the exercise. For custom assumptions, use its `--help`; do not silently use defaults after the table changes them.

## 6–11 minutes: compare and change one thing

Show today's baseline and the agent-assisted case, including the limiting step. Explain the equation in words: completed work cannot exceed the slowest capacity or customer demand. Ask which one input to change. Hold all other inputs fixed, recalculate, and show the before/after. Keep distinct the table's chosen assumptions and the prepared assumptions.

A narrative about “what happens next” is a hypothesis. Numbers from this model are conditional calculations, not empirical evidence or an agent-based economic simulation.

## 11–16 minutes: test what the model leaves out

Ask: “What important cost, quality check, or handoff is missing?” Then offer one implication for services, customers, or competition and invite correction. Do not translate spare capacity directly into revenue or fewer jobs. Ask what people still contribute and what changed in the table's thinking, in separate short turns.

## 16–20 minutes: write the brief

Use `templates/scenario-brief.md`. Include assumptions, baseline and changed output, bottleneck, one sensitivity comparison, one model limitation, and a real measurement that would test it. “Already happening” uses a relevant source card if appropriate or states that no direct industry evidence was collected. Keep invented arithmetic out of the evidence section.

## Basis

Use explicit case design and a debrief (AHRQ), with sensitivity to assumptions informed by NIST. This is our workshop capacity model, not a validated model from either source. Details and boundaries are in `docs/methods-and-sources.md`.
