---
tags:
  - privilege-escalation
  - shopify
  - session-escalation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:10.041Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: cbfe472a-4977-43ac-bc39-89196b51e547
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Lock and Re-login to POS with New PIN

## Summary

This procedure locks the current POS session and re-authenticates using the modified PIN of the full-permissions staff, elevating the effective privileges within the app.

## Description

POS session management allows PIN-based re-entry that inherits the associated role's permissions, bypassing checks on the initial login context. This step exploits that flaw after PIN setup, requiring device access but no new credentials.

## Requirements

1. Active POS session on terminal
2. Modified PIN '1234' set on full staff account
3. Physical access to lock/unlock screen

## Defense

Defensive measures and detection strategies:

- Enforce role validation on every re-authentication
- Log PIN usage and associated role changes
- Disable PIN inheritance from limited sessions

## Objectives

1. Trigger privilege inheritance via re-login
2. Expand UI access in POS
3. Confirm escalation without admin creds

## Instructions

### Step 1: Lock Session

**Context**: Initiate re-authentication flow.

In POS, use the lock screen feature (e.g., menu > Lock) to secure the app.

> Screen locks, prompting for PIN entry.

### Step 2: Enter Elevated PIN

**Context**: Authenticate as full staff.

Enter '1234' at the PIN prompt and unlock.

> POS reloads with full permissions reflected in menus.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[privilege-escalation]]
- [[shopify]]
- [[session-escalation]]
