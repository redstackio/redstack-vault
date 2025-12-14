---
tags:
  - race-condition
  - web
  - analysis
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:22.721Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 3b86e89f-a748-4f0d-a09d-e1f1885f2e73
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Analyze-Responses-for-Multiple-Votes

## Summary

This procedure examines Burp Intruder responses to confirm multiple votes were accepted due to the race condition, verifying manipulation of vote counts.

## Description

Review JSON responses for incrementing up/down counts across concurrent requests. Scenario: Post-Intruder attack on voting API. Prerequisites: Completed concurrent replay. Expected: Evidence of vote inflation, e.g., up votes increasing by more than 1.

## Requirements

1. Burp Intruder results available
2. Knowledge of baseline vote counts
3. JSON parsing capability

## Defense

Defensive measures and detection strategies:

- Audit logs for vote discrepancies
- Alert on rapid vote changes per definition
- Post-vote verification queries

## Objectives

1. Validate multiple votes processed
2. Quantify impact on popularity scores
3. Document proof for reporting

## Instructions

### Step 1: Review Response Codes

**Context**: Check for successful processing.

No command; in Burp Intruder, inspect response codes.

> All should be 200 OK; failures indicate throttling.

### Step 2: Parse JSON Payloads

**Context**: Look for vote count increments.

No command; examine bodies like {"status":"saved","up":6429,"down":1798} progressing to {"status":"saved","up":6433,"down":1795}.

> Confirm increments match thread count (e.g., +4 for 4 extra votes).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- race-condition
- web
- analysis
