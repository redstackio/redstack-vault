---
id: d43f107f-64cf-4891-b49b-d0c882c33ab5
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:15.745Z'
updated_at: '2025-12-11T06:10:15.745Z'
tactics:
  - '[[Persistence]]'
techniques:
  - '[[Modify Authentication Process]]'
sub_techniques: []
tags:
  - persistence
  - authentication-manipulation
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
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1556]]'
---

# Update User Email Attribute

## Summary

This procedure updates the email attribute in AWS Cognito to a case-varied version of the victim's email, exploiting unverified changes for account takeover.

## Description

Using the update-user-attributes API, the attacker modifies their account's email to collide with the victim's due to case-insensitivity issues. This targets Flickr's improper handling of Cognito attributes. The environment is AWS Cognito User Pools. Expected outcome is an unverified email change triggering potential collision.

## Requirements

1. Valid Cognito access token.
2. Victim's email address.
3. AWS CLI access.

## Defense

Defensive measures and detection strategies:

- Require verification for all attribute changes.
- Monitor for email attribute updates via logs.

## Objectives

1. Manipulate email to create collision.
2. Bypass verification checks.
3. Set stage for login takeover.

## Instructions

### Step 1: Execute Update Command

**Context**: Call update-user-attributes API with the new email value.

**Command** ([[commands/aws-cognito-update-user-attributes]]):
```bash
aws cognito-idp update-user-attributes --region us-east-1 --access-token eyJraWQ[...]] --user-attributes Name=email,Value=flickr-Benign@lauritz-holtmann.de
```

> Updates the user's email attribute, returning JSON with delivery details.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Modify Authentication Process]]

### Sub-Techniques



## Commands Used

- [[commands/aws-cognito-update-user-attributes]]

## Tools Used

- [[tools/AWS-Command-Line-Interface]]

## Tags

- persistence
- authentication-manipulation
