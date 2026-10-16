# Why these exercises are designed this way

Research checked October 15, 2026. These are original workshop adaptations informed by established methods. **The 20-minute duration is a design target, not a duration validated by these sources.** Full methods often need hours, days, or longer. The table practices a useful reasoning move and produces a conditional brief.

## Research: focused evidence scan

**Method source:** Garritty and colleagues, [Updated recommendations for the Cochrane rapid review methods guidance](https://www.bmj.com/content/384/bmj-2023-076335), BMJ, February 6, 2024.

**Principles used:** refine the question with users, make search limits explicit, examine the evidence, and disclose uncertainty. **Our adaptation:** two targeted searches, up to three opened original sources, and a challenge round. This is a preliminary evidence scan, not a Cochrane review or a comprehensive literature search. We omit formal screening, duplicate extraction, and certainty assessment; do not use the output as decision-grade evidence.

## Simulation: a transparent what-if model

**Method sources:** AHRQ, [Simulation, Workflow Assessment for Health IT Toolkit](https://digital.ahrq.gov/health-it-tools-and-resources/evaluation-resources/workflow-assessment-health-it-toolkit/all-workflow-tools/simulation), undated; NIST/SEMATECH, [Uncertainty budgets and sensitivity coefficients](https://www.itl.nist.gov/div898/handbook/mpc/section5/mpc56.htm), undated.

**Principles used:** define what the exercise tests; use an explicit case; debrief; examine how results depend on inputs. **Our adaptation:** a deterministic weekly capacity bound with a one-input-at-a-time comparison. NIST's page concerns measurement uncertainty; we borrow only the general idea that inputs affect outputs. We do not implement its uncertainty budget or claim statistical validation. The case is invented, has no stochastic arrivals or rework, and is not a validated business model.

## Role playing: test competing perspectives

**Method sources:** IDEO.org, [Design Kit: Role Play](https://www.designkit.org/methods/36.html), undated; AHRQ PSNet, [Debriefing for Clinical Learning](https://psnet.ahrq.gov/primer/debriefing-clinical-learning), undated on this reference card.

**Principles used:** make a specific interaction tangible, assign roles relevant to what is being tested, then reflect on what happened and what needs checking. **Our adaptation:** three or four role cards, a changed condition, and an out-of-character debrief. IDEO.org suggests 30–45 minutes; prepared cards shorten setup here. AHRQ addresses clinical learning, not validation of simulated consumer opinion. Our use of Claude for one missing role is an added convenience. It does not replace interviews, predict behavior, or establish market demand.

## Forecasting: two conditional futures

**Method source:** UK Government Office for Science, [The Futures Toolkit, second edition](https://www.gov.uk/government/publications/futures-toolkit-for-policy-makers-and-analysts/the-futures-toolkit-html), 2024, especially Scenarios and Horizon Scanning.

**Principles used:** explore different plausible futures, expose critical uncertainty, and notice developments that may change the picture. **Our adaptation:** two paths over the draft's three-to-five-year horizon, one separating uncertainty, and two observable signposts. We omit a full scan, driver workshop, and four-quadrant matrix. The toolkit typically uses longer horizons; this is a near-term introductory exercise. It yields scenarios, not calibrated event probabilities.

## Problem solving: compare, constrain, and design a test

**Method sources:** ASQ, [Plan-Do-Check-Act Cycle](https://asq.org/quality-resources/pdca-cycle), undated; UK Government Office for Science, [Policy Stress-testing template](https://www.gov.uk/government/publications/policy-stress-testing-windtunnelling-template/policy-stress-testing-windtunnelling-template), August 29, 2024.

**Principles used:** define the opportunity, plan a small test, learn from results, and revisit the response; examine whether options survive changed conditions. **Our adaptation:** three responses, one added constraint, and a measurable pilot plan. The workshop does not complete the real PDCA cycle. It cannot establish a root cause or demonstrate success without observations.

## Skill implementation

Anthropic, [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills), October 16, 2025, updated December 18, 2025; [Claude Code skills documentation](https://code.claude.com/docs/en/skills), checked October 15, 2026.

We use named `SKILL.md` files in project skill folders with descriptions for discovery. Shared facilitation guidance and prepared resources stay in separate files. The explicit-file fallback avoids depending on skill discovery across Claude products. All five skills are repository-scoped and need the shared kit; do not install the folders alone as if they were independent packages.

## Empirical starter evidence

The [source cards](../materials/source-cards.md) summarize the original 2023 NBER working-paper version of *Generative AI at Work*, METR's July 2025 developer experiment, and Anthropic's skills architecture. They support questions about task differences, measurement, and reusable expertise. They do not establish present adoption in every industry or autonomous-agent productivity.

## Research access and search summary

Primary publisher sources above were located through web search and inspected through the web tool. NBER's landing page and PDF returned access errors in the web reader; the indexed original-version paper abstract supplies the historical starter summary. METR's February 24, 2026 follow-up was also inspected and is noted on its card. Searches covered Cochrane rapid-review guidance; AHRQ simulation and debriefing; NIST sensitivity; IDEO.org role play; GOV.UK futures and stress-testing; ASQ PDCA; and Anthropic skills documentation. A preliminary OpenCLI Gemini query for original methods sources failed with `BROWSER_CONNECT` and produced no research evidence (one attempt). No private planning document was sent to it. No source is treated as endorsing this kit.
