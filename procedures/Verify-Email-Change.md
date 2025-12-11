---
id: 1a4b7026-e762-451b-80a3-f2c632222ed4
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:15.741Z'
updated_at: '2025-12-11T06:10:15.741Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
sub_techniques: []
tags:
  - discovery
  - verification
commands:
  - '[[commands/aws-cognito-get-user]]'
  - '[[commands/aws-cognito-update-user-attributes]]'
  - '[[commands/aws-cognito-get-user-post-update]]'
  - '[[commands/aws-cognito-get-user-failure]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-Command-Line-Interface]]'
skill_level: intermediate
impact_level: low
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1087]]'
---

# Verify Email Change

## Summary

This procedure verifies the email attribute change in AWS Cognito, confirming it is unverified and matches the intended value.

## Description

After updating the email, the attacker calls get-user again to check the new attributes and verification status. This ensures the manipulation was successful before attempting login. Targets AWS Cognito environments. Expected outcome is JSON confirming email_verified=false.

## Requirements

1. Valid Cognito access token post-update.
2. AWS CLI.
3. Recent email update.

## Defense

Defensive measures and detection strategies:

- Alert on repeated get-user calls.
- Enforce attribute verification.

## Objectives

1. Confirm email update.
2. Check verification status.
3. Validate manipulation success.

## Instructions

### Step 1: Execute Verification Command

**Context**: Call get-user API to confirm changes.

**Command** ([[commands/aws-cognito-get-user-post-update]]):
```bash
aws cognito-idp get-user --region us-east-1 --access-token eyJraWQi[...]]
```

> Retrieves updated user attributes, showing new email and email_verified=false.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques



## Commands Used

- [[commands/aws-cognito-get-user-post-update]]

## Tools Used

- [[tools/AWS-Command-Line-Interface]]

## Tags

- discovery
- verification
