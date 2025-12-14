---
tags:
  - account-takeover
  - persistence
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: e1079cd0-971d-41c5-ba20-539c18ac435f
created_at: '2025-12-14T17:33:34.308Z'
updated_at: '2025-12-14T17:33:34.308Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Complete-Account-Takeover-via-Linked-Accounts

## Summary

This procedure finalizes the account takeover by leveraging the unauthorized link to access and control the victim's Rockstar Social Club account through the connected third-party service.

## Description

Post-linking, the attacker's control over the third-party account allows session propagation or credential reuse to log into Social Club. This grants access to profiles, game saves, purchases, and potentially linked payment info. The vulnerability enabled full takeover without password knowledge.

## Requirements

1. Successful linking from previous steps
2. Access to the attacker's third-party account
3. Knowledge of Social Club's linked account management

## Defense

Defensive measures and detection strategies:

- Require confirmation for account linking
- Audit linked accounts regularly
- Use multi-factor authentication for sensitive actions

## Objectives

1. Gain authenticated access to victim's account
2. Exfiltrate or modify data
3. Maintain persistence if possible

## Instructions

### Step 1: Verify Linking Success

**Context**: Confirm the victim's account is now associated with the attacker's third-party.

Log into the third-party service and check connected accounts list.

> Expected: Victim's Social Club ID appears.

### Step 2: Initiate Access

**Context**: Use the link to authenticate into Social Club.

Navigate to Social Club login and select 'Link with third-party' or use the propagated session to bypass direct login.

> This exploits the trust in linked accounts.

### Step 3: Exploit Access

**Context**: Perform actions as the victim.

Access profile, download data, or change settings.

> Expected: Full control without additional auth.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[linked-accounts]]
