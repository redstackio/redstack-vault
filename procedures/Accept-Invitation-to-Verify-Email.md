---
tags:
  - wordpress
  - verification-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0fc562eb-f398-4c2e-a732-6cf1bd50f79d
created_at: '2025-12-13T09:01:26.548Z'
updated_at: '2025-12-13T09:01:26.548Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Accept Invitation to Verify Email

## Summary

This procedure accepts an invitation from an unverified WordPress.com account to bypass standard email verification.

## Description

Accepting the invitation via notifications verifies the email address without ownership, exploiting the invitation system's flaw.

## Requirements

1. Access to unverified account
2. Received invitation
3. Web browser

## Defense

Defensive measures and detection strategies:

- Patch the invitation verification logic
- Monitor for unauthorized verifications

## Objectives

1. Verify the target email
2. Enable use of the account for SSO
3. Confirm verification status

## Instructions

### Step 1: Access Notifications

**Context**: Check for the invitation.

Go to notifications at the top right.

> Notifications panel opens.

### Step 2: Accept Invitation

**Context**: Accept to trigger verification.

See the invitation and accept it.

> Email is verified upon acceptance.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[wordpress]]
- [[verification-bypass]]
