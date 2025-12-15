---
tags:
  - csrf
  - verification
  - hijacking
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:27:03.674Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 1550af8f-2b64-4196-a477-5365b87120d1
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify Account Replacement

## Summary

Confirms the CSRF success by checking the victim's Shopify integrations for the attacker's Pinterest account.

## Description

Post-exploitation, the OAuth callback processes the code in the victim's context, overriding the connection. Manual check via admin UI validates the hijack.

## Requirements

1. Access to victim's admin post-attack
2. Knowledge of original vs. new account
3. Recent callback load

## Defense

Defensive measures and detection strategies:

- Alert on integration changes
- Require confirmation for OAuth completions

## Objectives

1. Confirm override
2. Assess impact
3. Plan further exploitation

## Instructions

### Step 1: Access Victim Admin

**Context**: Check integrations.

Log in to victim's Shopify admin.

> Expected: Access granted.

### Step 2: Inspect Pinterest App

**Context**: Verify change.

Go to Apps > Pinterest; check connected account.

> Expected: Shows attacker's Pinterest details, e.g., different email or ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[verification]]
- [[hijacking]]
