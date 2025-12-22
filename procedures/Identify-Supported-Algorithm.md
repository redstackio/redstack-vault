---
tags:
  - fingerprinting
  - algorithm-detection
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
updated_at: '2025-12-14T17:31:30.968Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 524036b3-909e-4b46-975e-5c885faf558e
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Identify-Supported-Algorithm

## Summary

This procedure uses timing analysis results to determine the server's supported Digest Authentication algorithm, completing the reconnaissance via the curl timing vulnerability.

## Description

Based on observed timings, the algorithm with the highest deviation (e.g., MD5 at +25.9%) is identified as the matched one, as curl's strcmp() takes longer for correct comparisons. This fingerprints server config for potential targeted attacks on weak algorithms, though the curl team deems it non-security due to explicit protocol announcements.

## Requirements

1. Timing data from previous analysis
2. PoC script with detection logic

## Defense

Defensive measures and detection strategies:

- Standardize on strong algorithms (e.g., SHA-256) and announce consistently
- Monitor for timing-based probes in auth logs
- Upgrade curl to mitigate client-side leaks

## Objectives

1. Pinpoint the vulnerable/supported algorithm
2. Assess reconnaissance impact
3. Confirm attack chain success

## Instructions

### Step 1: Interpret Deviations

**Context**: The PoC auto-detects based on max time; manually verify if needed.

No command; review 'The server likely uses algorithm: MD5'.

### Step 2: Validate Fingerprint

**Context**: Cross-check with direct protocol inspection (e.g., Wireshark) to confirm.

> Expected: Matches PoC output, e.g., 'VULNERABILITY CONFIRMED'.

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

- fingerprinting
- algorithm-detection
- recon
