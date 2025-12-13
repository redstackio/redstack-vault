---
tags:
  - saml
  - authentication-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 7e160af1-aa03-41e8-a353-785173cf8294
created_at: '2025-12-13T09:01:26.332Z'
updated_at: '2025-12-13T09:01:26.332Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Submit Faked SAML Response for Authentication

## Summary

This procedure involves submitting a forged SAML response to authenticate as an arbitrary user after validation has been disabled.

## Description

Once SAML signature verification is bypassed, an attacker can create and submit a fake SAML assertion claiming any user's identity, allowing login without valid credentials. This leads to unauthorized access, potentially including administrative privileges.

## Requirements

1. SAML validation already disabled on the target
2. Ability to intercept or submit SAML responses (e.g., via browser tools)
3. Knowledge of target user identities

## Defense

Defensive measures and detection strategies:

- Enforce strict SAML signature validation
- Monitor authentication logs for anomalous logins

## Objectives

1. Authenticate as arbitrary user
2. Gain unauthorized access
3. Escalate privileges if targeting admins

## Instructions

### Step 1: Craft and Submit Faked Response

**Context**: Use browser tools or a proxy to forge and send a SAML response claiming the desired user's identity.

> Craft a SAML assertion with the target user's details and submit it through the login endpoint. No specific command is required; this is done via HTTP POST to the SAML callback.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[saml]]
- [[authentication-bypass]]
