---
tags:
  - activity-logging
  - sabotage
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
updated_at: '2025-12-14T17:28:44.448Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 3e68db3d-9a6a-450b-bffc-17aa2a3e7fe6
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Log-Attacker-Coding-Activity

## Summary

This procedure involves using the attacker's API key to submit coding activity to the victim's WakaTime account, enabling sabotage of statistics.

## Description

With the API key integrated, the attacker performs or simulates coding in their environment. The WakaTime API endpoints (e.g., /api/v1/users/current/heartbeats) receive heartbeat data without session isolation, logging it to the shared account. This can include fake projects or excessive time to inflate/deflate metrics, targeting the dashboard's aggregation logic.

## Requirements

1. Configured coding platform with attacker's API key
2. Sample code files or scripts to generate activity
3. Access to WakaTime API (implicit via extension)

## Defense

Defensive measures and detection strategies:

- Enforce single active API key per account
- Validate activity patterns against user history
- Alert on sudden spikes in logged time from unknown sources

## Objectives

1. Inject unauthorized activity into victim's records
2. Alter coding statistics and rankings
3. Maintain persistence through ongoing submissions

## Instructions

### Step 1: Initiate Coding Session

**Context**: Open and edit files to trigger WakaTime logging.

In VS Code, create or open a file (e.g., test.py) and begin typing or running code.

> The extension sends periodic heartbeats to the API, logging project, language, and time data.

### Step 2: Verify Logged Activity

**Context**: Check the dashboard for submission confirmation.

Refresh the WakaTime dashboard at https://waketime.com/dashboard.

> New activity entries appear, confirming successful sabotage injection.

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
- [[sabotage]]
