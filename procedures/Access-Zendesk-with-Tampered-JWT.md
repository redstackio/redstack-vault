---
tags:
  - impersonation
  - access
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
id: 08c75b2f-3e8f-47bc-b30d-d01bc38f1300
created_at: '2025-12-13T09:01:26.683Z'
updated_at: '2025-12-13T09:01:26.683Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access Zendesk with Tampered JWT

## Summary

This procedure uses the forged JWT to authenticate to Zendesk as the target user.

## Description

By navigating to the Zendesk JWT endpoint with the tampered token, the attacker gains access to the victim's support tickets. This completes the impersonation in a web SSO context.

## Requirements

1. Tampered JWT token
2. Browser access to Zendesk domain

## Defense

Defensive measures and detection strategies:

- Implement nonce or additional validation in JWT claims
- Monitor for anomalous logins

## Objectives

1. Achieve unauthorized access
2. Access sensitive support data
3. Validate exploit success

## Instructions

### Step 1: Navigate with Token

**Context**: Initiate login with forged token.

Navigate to https://trintsupport.zendesk.com/access/jwt?jwt=[TAMPERED_JWT_TOKEN] to log in as the victim.

> Confirm access to victim's tickets and history.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[impersonation]]
- [[access]]
