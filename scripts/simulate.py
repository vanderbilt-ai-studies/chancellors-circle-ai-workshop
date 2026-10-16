#!/usr/bin/env python3
"""Fictional weekly capacity model. Python standard library only."""
import argparse
import json
import math


def positive(value):
    n = float(value)
    if not math.isfinite(n) or n <= 0:
        raise argparse.ArgumentTypeError('must be a finite number greater than zero')
    return n


def nonnegative(value):
    n = float(value)
    if not math.isfinite(n) or n < 0:
        raise argparse.ArgumentTypeError('must be a finite nonnegative number')
    return n


def capacity(analyst_hours, reviewer_hours, analyst_time, review_time, demand):
    values = (analyst_hours, reviewer_hours, analyst_time, review_time, demand)
    if not all(math.isfinite(x) for x in values):
        raise ValueError('all inputs must be finite')
    if analyst_time <= 0 or review_time <= 0 or min(analyst_hours, reviewer_hours, demand) < 0:
        raise ValueError('time per brief must be positive; weekly hours and demand cannot be negative')
    bounds = {'analysts': analyst_hours / analyst_time,
              'review': reviewer_hours / review_time, 'demand': demand}
    limiting = min(bounds.values())
    return {'analyst_capacity': bounds['analysts'], 'review_capacity': bounds['review'],
            'demand': demand, 'completed_briefs': math.floor(limiting),
            'limiting_factors': [key for key, value in bounds.items()
                                 if math.isclose(value, limiting, rel_tol=1e-9, abs_tol=1e-9)]}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--analyst-hours', type=nonnegative, default=120)
    p.add_argument('--reviewer-hours', type=nonnegative, default=12)
    p.add_argument('--demand', type=nonnegative, default=20)
    p.add_argument('--baseline-analyst-time', type=positive, default=8)
    p.add_argument('--baseline-review-time', type=positive, default=1)
    p.add_argument('--agent-analyst-time', type=positive, default=4)
    p.add_argument('--agent-review-time', type=positive, default=1.5)
    p.add_argument('--sensitivity-review-time', type=positive, default=0.75,
                   help='change only agent review hours per brief for a third comparison')
    p.add_argument('--json', action='store_true')
    a = p.parse_args()
    cases = [('Today', a.baseline_analyst_time, a.baseline_review_time),
             ('Agent assumption', a.agent_analyst_time, a.agent_review_time),
             ('Change only agent review time', a.agent_analyst_time, a.sensitivity_review_time)]
    result = {'label': 'FICTIONAL assumptions; capacity bound, not a forecast',
              'inputs': vars(a), 'cases': []}
    for label, analyst_time, review_time in cases:
        row = {'case': label, 'analyst_hours_per_brief': analyst_time,
               'review_hours_per_brief': review_time}
        row.update(capacity(a.analyst_hours, a.reviewer_hours, analyst_time, review_time, a.demand))
        result['cases'].append(row)
    if a.json:
        print(json.dumps(result, indent=2))
        return
    print(result['label'])
    print('Weekly analyst hours: %g | reviewer hours: %g | demand: %g' %
          (a.analyst_hours, a.reviewer_hours, a.demand))
    print('| Case | Analyst h/brief | Review h/brief | Analyst capacity | Review capacity | Completed/week | Limit |')
    print('|---|---:|---:|---:|---:|---:|---|')
    for row in result['cases']:
        print('| %s | %g | %g | %.2f | %.2f | %d | %s |' %
              (row['case'], row['analyst_hours_per_brief'], row['review_hours_per_brief'],
               row['analyst_capacity'], row['review_capacity'], row['completed_briefs'],
               ', '.join(row['limiting_factors'])))
    print('Omits costs, queues, variability, rework, quality, and implementation. More capacity does not prove demand or profit.')


if __name__ == '__main__':
    main()
