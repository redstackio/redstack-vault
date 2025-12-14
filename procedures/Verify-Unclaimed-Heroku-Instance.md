---
tags:
  - heroku
  - cloud
  - verification
type: procedure
tools:
  - '[[tools/heroku-cli]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/heroku-apps-list]]'
  - '[[commands/heroku-app-info]]'
verified: false
platforms:
  - Cloud (Heroku)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Org Information]]'
updated_at: '2025-12-14T04:38:39.933Z'
sub_techniques: []
id: a822c6f5-6b6f-40f6-bfed-32185729cb39
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Org Information]]'
---
# Verify-Unclaimed-Heroku-Instance

## Summary

This procedure checks if a Heroku app referenced in a dangling DNS record is unclaimed, confirming vulnerability to takeover by attempting to access or list the app via the Heroku API.

## Description

After identifying a CNAME pointing to a Heroku app, this step verifies ownership status. Using the Heroku CLI, query the app's existence without authentication initially, then with login if needed. Target environment is Heroku's cloud platform; outcomes include confirmation of unclaimed status, allowing progression to takeover. Prerequisites: Heroku CLI installed.

## Requirements

1. Heroku CLI installed and accessible
2. Optional: Heroku account for deeper queries
3. Knowledge of the target app name from DNS

## Defense

Defensive measures and detection strategies:

- Monitor Heroku app creation logs for unauthorized claims
- Use Heroku's organization features to lock app names
- Integrate with DNS providers to auto-delete dangling records

## Objectives

1. Confirm the Heroku app is not owned by the target organization
2. Assess if the app can be claimed
3. Document evidence for reporting or exploitation

## Instructions

### Step 1: List All Apps (Optional Initial Check)

**Context**: Get a broad view of accessible apps to see if the target appears.

**Command** ([[commands/heroku-apps-list]]):
```bash
heroku apps
```

> Lists apps under the current account or public ones; if unauthenticated, it may show limited info. Expected output: No entry for the target app, indicating unclaimed.

### Step 2: Query Specific App Info

**Context**: Directly probe the target app for status.

**Command** ([[commands/heroku-app-info]]):
```bash
heroku info --app tim-exclusive
```

> Attempts to fetch app details. Expected output: Error like "App tim-exclusive not found" if unclaimed.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Org Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- [[commands/heroku-apps-list]]
- [[commands/heroku-app-info]]

## Tools Used

- [[tools/heroku-cli]]

## Tags

- [[heroku]]
- [[cloud]]
