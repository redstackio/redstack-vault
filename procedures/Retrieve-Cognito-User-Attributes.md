---
id: proc-002
tags:
  - cognito
  - user-attributes
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
updated_at: '2025-12-14T17:33:34.447Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Retrieve-Cognito-User-Attributes

## Summary

This procedure uses the AWS CLI to fetch the current user's attributes from Cognito, revealing email and verification status for manipulation planning.

## Description

After obtaining an access token, query the Cognito User Pool to retrieve details like email, email_verified, and other attributes. This is essential to confirm the attacker's current state before updating. The endpoint is get-user in us-east-1 region. Expected outcomes include JSON with UserAttributes array.

## Requirements

1. Valid access token from Flickr login
2. AWS CLI installed and accessible
3. Region set to us-east-1

## Defense

Defensive measures and detection strategies:

- Enable Cognito advanced security to log API calls
- Monitor for get-user API invocations from unusual IPs
- Implement rate limiting on authentication endpoints

## Objectives

1. Inspect current email and verification
2. Gather user sub and other identifiers
3. Validate token permissions

## Instructions

### Step 1: Execute Get User Command

**Context**: Call the Cognito API to retrieve attributes using the access token.

**Command** ([[commands/aws-cognito-get-user]]):
```bash
aws cognito-idp get-user --region us-east-1 --access-token eyJraWQiOiJPVj[...] (redacted token)
```

> This returns JSON with Username and UserAttributes, including sub, email_verified (true), email, etc. Use this to note the current email for variant creation.

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
- [[user-attributes]]
- [[recon]]
