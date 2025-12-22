---
id: proc-uuid-005
tags:
  - query-probing
  - data-inference
type: procedure
tools:
  - '[[tools/Browser-Console]]'
  - '[[tools/PHP]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/calculate-load-times-js]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Automated Collection]]'
updated_at: '2025-12-14T17:27:50.097Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Automated Collection]]'
---
# Measure-Target-Query-Load-Times

## Summary

This procedure probes variable queries on HackerOne endpoints to capture load times, comparing against baselines to estimate response sizes and infer private data like report counts.

## Description

Modify the webpage's `<img>` sources to target user-specific queries (e.g., by report ID or status filters). Use JS to measure timings, then derive record counts by (timing delta / baseline per-byte rate) and divide by ~185 bytes per record (gzip-adjusted).

## Requirements

1. Baselines from prior step
2. Dynamic PHP or JS for query variation
3. Victim session active

## Defense

Defensive measures and detection strategies:

- Randomize response sizes with padding
- Implement timing normalization (constant delays)
- Log query patterns for anomaly detection

## Objectives

1. Detect presence of data via timing spikes
2. Guess incremental report IDs
3. Profile user activity (e.g., new reports)

## Instructions

### Step 1: Update Img Sources for Targets

**Context**: Replace src with variable params.

**Command** (PHP Dynamic):
Echo `<img src="https://hackerone.com/bugs.json?text_query=3480&subject=&sort_type=pg_search_rank&substates%5B%5D=new&rnd=[rand]">`

> Iterate IDs to probe.

### Step 2: Capture Timings

**Context**: Measure and compare.

**Command** ([[commands/calculate-load-times-js]]):
Run in console.

> Log ts; estimate size = (t - baseline_small) * bytes_per_ms.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Automated Collection]] Automated Collection

### Sub-Techniques


## Commands Used

- [[commands/calculate-load-times-js]]

## Tools Used

- [[tools/Browser-Console]]
- [[tools/PHP]]

## Tags

- [[side-channel]]
- [[inference]]
