---
id: 3be4bf31-4912-4f95-bdc5-307f21160eed
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:15.748Z'
updated_at: '2025-12-11T06:10:15.748Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
sub_techniques: []
tags:
  - discovery
  - aws-cognito
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

# Retrieve User Details via AWS CLI

## Summary

This procedure uses the AWS CLI to retrieve user attributes from Cognito, allowing the attacker to view current details like email before manipulation.

## Description

Leveraging an obtained access token, the attacker calls the Cognito get-user API to fetch user information. This step is crucial for confirming the current state and planning attribute updates in authentication bypass attacks. The procedure operates in an AWS environment with Cognito User Pools. Expected outcome is a JSON response with user attributes.

## Requirements

1. Valid Cognito access token.
2. AWS CLI installed and configured.
3. Access to us-east-1 region.

## Defense

Defensive measures and detection strategies:

- Log and alert on Cognito API calls from unexpected sources.
- Implement rate limiting on user attribute queries.

## Objectives

1. Discover current user attributes.
2. Confirm email for targeting.
3. Validate token functionality.

## Instructions

### Step 1: Execute Get User Command

**Context**: Call the get-user API to view current user attributes.

**Command** ([[commands/aws-cognito-get-user]]):
```bash
aws cognito-idp get-user --region us-east-1 --access-token eyJraWQiOiJPVj[...]]
```

> Retrieves the user attributes for the authenticated user, returning JSON with Username and UserAttributes.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques



## Commands Used

- [[commands/aws-cognito-get-user]]

## Tools Used

- [[tools/AWS-Command-Line-Interface]]

## Tags

- discovery
- aws-cognito
