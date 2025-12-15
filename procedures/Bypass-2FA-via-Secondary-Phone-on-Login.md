---
id: proc-slack-2fa-bypass
tags:
  - 2fa-bypass
  - account-takeover
  - login
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:27:29.551Z'
skill_level: basic
impact_level: critical
detection_risk: high
sub_techniques:
  - '[[T1078.004]]'
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass-2FA-via-Secondary-Phone-on-Login

## Summary

This procedure leverages the added secondary phone to intercept 2FA codes during login, achieving account takeover or causing DoS for the victim.

## Description

With the secondary number active, the attacker logs in using victim's credentials, selects the attacker's phone for code delivery, receives SMS, and completes authentication. If victim lacks primary 2FA, login becomes impossible without the code, leading to DoS.

## Requirements

1. Victim's username/password known
2. Secondary phone confirmed active
3. Attacker's phone ready for SMS

## Defense

Defensive measures and detection strategies:

- Disable secondary 2FA options or require approval
- Use app-based 2FA (TOTP) over SMS
- Monitor login attempts from unusual locations
- Alert on multiple 2FA code requests

## Objectives

1. Gain full account access
2. Divert 2FA to attacker
3. Optionally lock out victim

## Instructions

### Step 1: Initiate Login

**Context**: Go to Slack login page with victim's creds.

Enter username/password; proceed to 2FA.

> Triggers code send.

### Step 2: Select and Use Secondary Number

**Context**: Choose the added phone for code.

Receive SMS (e.g., 196206), enter it.

> Success: Logged in to victim's account.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- [[T1078.004]] Cloud Accounts

## Commands Used


## Tools Used


## Tags

- [[2fa-bypass]]
- [[account-takeover]]
