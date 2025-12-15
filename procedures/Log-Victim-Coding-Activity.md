---
tags:
  - activity-logging
  - parallel-session
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:44.438Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 4722b064-47bb-479e-b6fa-90e622e8a086
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Log-Victim-Coding-Activity

## Summary

This procedure covers the victim's normal use of their API key to log coding activity, which aggregates with the attacker's submissions on the shared dashboard.

## Description

The victim integrates their new API key into their coding platform and proceeds with development work. API calls submit data without distinguishing sessions, leading to mixed logs. This highlights the vulnerability's impact on data integrity.

## Requirements

1. Victim's API key configured in platform
2. Active coding environment
3. WakaTime extension enabled

## Defense

Defensive measures and detection strategies:

- Implement session-based API key scoping
- Detect concurrent key usage from disparate IPs
- Provide user controls for activity filtering

## Objectives

1. Submit legitimate activity via new key
2. Demonstrate coexistence with attacker's logs
3. Reveal aggregation flaws in dashboard

## Instructions

### Step 1: Configure Victim's Platform

**Context**: Set up the extension with the new key.

Paste the victim's API key into the WakaTime settings in their IDE.

> Authentication succeeds, enabling tracking.

### Step 2: Perform Coding and Log

**Context**: Generate real activity for submission.

Edit files or run code in the platform.

> Heartbeats sent to API, appearing in dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[activity-logging]]
- [[parallel-session]]
