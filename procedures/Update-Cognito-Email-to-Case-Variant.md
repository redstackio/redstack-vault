---
id: proc-003
tags:
  - cognito
  - email-update
  - account-manipulation
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/aws-cognito-update-user-attributes]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:33:34.445Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Update-Cognito-Email-to-Case-Variant

## Summary

This procedure updates the user's email in Cognito to a case-sensitive variant of the victim's email, exploiting lack of verification to set up a collision.

## Description

Using the update-user-attributes endpoint, set the email to a variant like 'flickr-Benign@lauritz-holtmann.de' (capitalized differently from victim's 'flickr-benign@lauritz-holtmann.de'). Flickr normalizes emails case-insensitively on login but stores case-sensitively in Cognito, allowing takeover. No UI prevents this API call.

## Requirements

1. Valid access token with update permissions
2. Knowledge of victim's email for variant creation
3. AWS CLI ready

## Defense

Defensive measures and detection strategies:

- Restrict update-user-attributes to verified sessions only
- Require email verification before changes take effect
- Audit logs for email attribute modifications

## Objectives

1. Link attacker's account to victim's email variant
2. Trigger optional verification without enforcement
3. Enable collision on login

## Instructions

### Step 1: Prepare Variant Email

**Context**: Create a case-variant of the victim's email, e.g., change lowercase to title case.

Identify victim's email from recon, then variant it.

> Example: Victim 'user@example.com' -> 'User@Example.com'

### Step 2: Execute Update Command

**Context**: Update the attribute via API.

**Command** ([[commands/aws-cognito-update-user-attributes]]):
```bash
aws cognito-idp update-user-attributes --region us-east-1 --access-token eyJraWQ[...] (redacted token) --user-attributes Name=email,Value=flickr-Benign@lauritz-holtmann.de
```

> Response includes CodeDeliveryDetailsList with email delivery info, but login proceeds without verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used

- [[commands/aws-cognito-update-user-attributes]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[cognito]]
- [[email-update]]
- [[account-manipulation]]
