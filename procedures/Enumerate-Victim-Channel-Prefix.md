---
tags:
  - enumeration
  - idor
  - web
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/check-quora-livedeps]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-13T23:52:44.612Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: 784fdd96-3bb7-4c26-957d-cad9785f3043
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Enumerate-Victim-Channel-Prefix

## Summary

This procedure brute-forces partial Quora channel names (window_id) using the /check_livedeps endpoint to identify valid prefixes for targeting victims via IDOR, reducing the enumeration space for channel delivery.

## Description

Quora uses channels like depXXXX-YYYYYYYYYYYYYYYYYYY for real-time updates via JSONP. The window_id parameter lacks validation, allowing arbitrary targeting. By probing /check_livedeps/index?window_id=depXXXX-, attackers validate 4-digit prefixes (0000-9999) to find live channels. This is feasible due to predictable formats and partial enumeration; full IDs (up to 19 digits) may require additional logic like simulating tchannel attachments. Prerequisites: Network access; outcomes: Valid victim channel for IDOR exploitation.

## Requirements

1. Access to Quora's check_livedeps endpoint
2. Scripting for brute-force (e.g., loop over 0000-9999)
3. Optional: Victim's approximate session timing for live channels

## Defense

Defensive measures and detection strategies:

- Validate window_id against authenticated user's sessions only
- Rate-limit check_livedeps probes
- Log and alert on repeated partial channel queries

## Objectives

1. Discover valid channel prefixes
2. Enable targeted message delivery
3. Amplify XSS impact without victim interaction

## Instructions

### Step 1: Probe Partial Channel

**Context**: Send GET requests to validate 4-digit dep prefixes.

**Command** ([[commands/check-quora-livedeps]]):
```bash
curl 'https://www.quora.com/check_livedeps/index?window_id=dep3304-'
```

> Expected output: "ok" for valid/live prefix, error otherwise. Brute-force by varying the 4 digits.

### Step 2: Construct Full Channel

**Context**: Combine prefix with guessed or known suffix for full window_id.

**Command** ([[commands/check-quora-livedeps]]):

No direct command; use results to build e.g., dep3501-3261853912009855464.

> Expected output: Valid channel name ready for use in requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

-

## Commands Used

- [[commands/check-quora-livedeps]]

## Tools Used

- [[tools/curl]]

## Tags

- enumeration
- idor
