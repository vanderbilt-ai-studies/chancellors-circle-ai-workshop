# Simulation you can do on paper

**All inputs and outputs are fictional capacity calculations, not forecasts.**

Analyst capacity = 120 analyst hours / analyst hours per brief.
Review capacity = 12 reviewer hours / review hours per brief.
Completed briefs = round DOWN the smallest of analyst capacity, review capacity, and demand.

| Case | Analyst hours / brief | Review hours / brief | Analyst capacity | Review capacity | Demand | Completed / week |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Today | 8 | 1 | 15 | 12 | 20 | 12 |
| Agent assumption | 4 | 1.5 | 30 | 8 | 20 | 8 |
| Change only review time to 1 | 4 | 1 | 30 | 12 | 20 | 12 |
| Change only review time to 0.75 | 4 | 0.75 | 30 | 16 | 20 | 16 |
| Agent assumption, demand falls to 6 | 4 | 1.5 | 30 | 8 | 6 | 6 |

Example: faster drafting doubles analyst capacity, but the assumed checking burden reduces completed briefs from 12 to 8. This illustrates a possible bottleneck; it does not demonstrate that agents cause more checking in real firms.

Ask: Is 1.5 hours realistic? What could make review easier? What is outside the model? If more briefs become feasible, would clients want them? What happens when competitors can do the same?

This is a steady weekly capacity bound. It omits arrivals, queues, variability, rework loops, quality, money, and implementation costs. It cannot establish profit, staffing needs, or actual service levels. Changing review time does not prove equal quality: test that separately.
