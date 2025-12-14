---
id: proc-004
tags:
  - cognito
  - verification
  - recon
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/aws-cognito-get-user]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:33:34.442Z'
skill_level: beginner
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify-Cognito-Email-Update

## Summary

This procedure re-queries Cognito to confirm the email update and verify that email_verified is false, highlighting the lack of enforcement.

## Description

Post-update, use get-user again to ensure the email is set to the variant and note email_verified: false. This confirms the vulnerability, as Flickr allows login with unverified emails.

## Requirements

1. Access token still valid
2. AWS CLI
3. Updated email value known

## Defense

Defensive measures and detection strategies:

- Force verification on attribute changes
- Log repeated get-user calls post-update
- Alert on unverified email usage in auth flows

## Objectives

1. Confirm email change
2. Observe unverified status
3. Validate setup for takeover

## Instructions

### Step 1: Re-Execute Get User

**Context**: Fetch updated attributes to verify.

**Command** ([[commands/aws-cognito-get-user]]):
```bash
aws cognito-idp get-user --region us-east-1 --access-token eyJraWQi[...] (redacted token)
```

> JSON shows updated email and email_verified: false, with other attributes intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/aws-cognito-get-user]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[cognito]]
- [[verification]]
- [[recon]]
