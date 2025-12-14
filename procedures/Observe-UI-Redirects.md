---
tags:
  - ui-restriction
  - bypass-observation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Command and Control]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.409Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 3ec415a7-32d5-4f13-841e-49d984ad4202
validated: true
mitre_tactics:
  - '[[Command and Control]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe-UI-Redirects

## Summary

This procedure involves interacting with the UI of a disabled account to confirm frontend restrictions while noting backend API calls that succeed, highlighting access control discrepancies.

## Description

After authentication, UI elements redirect to disabled pages, but GraphQL requests proceed. This step identifies the gap between frontend and backend enforcement, setting up for bypass via direct API calls.

## Requirements

1. Active session from disabled account login
2. Access to settings or menu pages
3. Burp Suite for request logging

## Defense

Defensive measures and detection strategies:

- Synchronize frontend and backend access checks
- Block API calls for disabled sessions via token validation
- Monitor for UI-API mismatch in logs

## Objectives

1. Verify UI blocks are enforced
2. Capture initial GraphQL requests in proxy history
3. Identify exploitable endpoints

## Instructions

### Step 1: Interact with Menus

**Context**: Trigger UI actions to observe redirects.

No command; Click on settings or dashboard menus.

> Expected: Redirect to https://hackerone.com/settings/disabled/edit with warning message.

### Step 2: Check Proxy History

**Context**: Review captured requests.

No command; In Burp HTTP History, filter for /graphql POSTs.

> Look for successful requests despite UI failure.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control]] Defense Evasion

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- ui-testing
- redirect-analysis
