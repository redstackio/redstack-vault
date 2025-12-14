---
tags:
  - analysis
  - timing
  - recon
type: procedure
tools:
  - '[[tools/poc-timing-attack-py]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2024-12-14T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:31:30.971Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 942cc24d-8f9d-4760-a7a7-0f6ceec6fb0e
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Analyze-Response-Timings

## Summary

This procedure involves reviewing the output from the timing attack PoC to observe differences in response times caused by curl's non-constant-time string comparison.

## Description

After executing the PoC, timings for each algorithm (e.g., MD5 at 963236.5 ns, MD5-sess at 826390.0 ns) are compared. Discrepancies arise because strcmp() exits early on mismatches, leaking information about the server's announced algorithm. This step provides reconnaissance on server config, though easily detectable otherwise. No additional tools needed beyond PoC logs; focuses on manual or scripted deviation calculation.

## Requirements

1. PoC execution complete with logged timings
2. Basic understanding of timing side-channels

## Defense

Defensive measures and detection strategies:

- Use timing-normalized implementations in clients
- Avoid relying on legacy auth protocols
- Analyze client-side logs for anomalous processing times

## Objectives

1. Identify timing variations across algorithms
2. Quantify the side-channel leak
3. Validate the vulnerability presence

## Instructions

### Step 1: Review PoC Output

**Context**: Examine console logs or saved output for per-algorithm timings.

No command; parse lines like 'SHA-1: 814495.0 ns'.

### Step 2: Calculate Deviations

**Context**: Compute percentage differences to highlight the matched algorithm's longer time.

Example manual calc: For MD5 deviation +25.9% vs. average.

> Expected: Clear outliers indicating the supported algorithm due to full strcmp() traversal.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Hardware

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/poc-timing-attack-py]]

## Tags

- analysis
- timing
- recon
