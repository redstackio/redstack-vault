---
tags:
  - data-access
  - discovery
type: procedure
tools:
  - '[[tools/cURL]]'
  - '[[tools/Browser-Console]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-with-session-cookie]]'
platforms:
  - Web
techniques:
  - '[[Account Discovery]]'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: f477ee64-a437-4960-b3a9-363f4cabdd22
created_at: '2025-12-11T06:10:40.565Z'
updated_at: '2025-12-11T06:10:40.565Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1087]]'
---
# Access Sensitive Inboxes and Reports

## Summary

This procedure involves navigating impersonated accounts to access and view sensitive inboxes and reports, discovering confidential data.

## Description

Using the stolen session, explore inboxes like HAS, Triage, and Main to load report metadata and contents, including vulnerabilities from multiple programs on platforms like HackerOne.

## Requirements

1. Impersonated session access
2. Knowledge of platform navigation
3. No additional tools beyond browser

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls and logging
- Alert on unusual inbox access patterns

## Objectives

1. Retrieve sensitive report data
2. Assess exposure scope
3. Gather evidence

## Instructions

### Step 1: Navigate to Inboxes

**Context**: Access various inboxes using the impersonated session.

Browse to /has-inbox, /triage-inbox, and /main-inbox endpoints.

> Load up to 150 reports across inboxes.

### Step 2: View Report Details

**Context**: Open individual reports to view full contents.

Click into reports to access titles, states, comments, and vulnerability info.

> Document findings with redaction.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Browser-Console]]

## Tags

- [[data-access]]
- [[Discovery]]
