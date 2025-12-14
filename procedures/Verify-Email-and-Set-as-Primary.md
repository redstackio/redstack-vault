---
id: proc-gratipay-email-verify
tags:
  - verification
  - email
  - gratipay
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Device Registration]]'
updated_at: '2025-12-14T17:32:57.823Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Device Registration]]'
---
# Verify-Email-and-Set-as-Primary

## Summary

This procedure verifies the bypassed email addition and sets it as primary, allowing the attacker to receive sensitive notifications if email access is obtained.

## Description

Post-exploitation, the verification link is sent to the normalized email (line 131). Clicking it confirms ownership, and setting as primary (line 314) updates without re-check, enabling persistence via email control.

## Requirements

1. Access to victim's email inbox
2. Authenticated attacker session
3. Verification link from email

## Defense

Defensive measures and detection strategies:

- Re-verify uniqueness on primary set
- Require MFA for email changes
- Audit logs for duplicate email associations

## Objectives

1. Confirm email ownership via link
2. Set as primary for notification routing
3. Establish persistence mechanism

## Instructions

### Step 1: Access Victim's Email

**Context**: Retrieve the verification message.

Log into the victim's email account and open the verification email from Gratipay.

### Step 2: Click Verification Link

**Context**: Activate the added email.

Follow the link in the email to verify; this binds it to the attacker's account.

### Step 3: Set as Primary

**Context**: Elevate email privileges.

Return to attacker dashboard, select the verified email, and set it as primary.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Device Registration]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- verify
- primary-email
