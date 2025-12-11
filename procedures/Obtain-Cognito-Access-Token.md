---
id: f9fec5be-d491-4af7-84f8-70d02df7f5e8
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:15.752Z'
updated_at: '2025-12-11T06:10:15.752Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - authentication
  - token-capture
commands:
  - '[[commands/aws-cognito-get-user]]'
  - '[[commands/aws-cognito-update-user-attributes]]'
  - '[[commands/aws-cognito-get-user-post-update]]'
  - '[[commands/aws-cognito-get-user-failure]]'
platforms:
  - Web
  - AWS
tools:
  - '[[tools/AWS-Command-Line-Interface]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---

# Obtain Cognito Access Token

## Summary

This procedure involves logging into an attacker-controlled Flickr account and intercepting the AWS Cognito access token from the login request for use in subsequent API manipulations.

## Description

The procedure targets the Flickr authentication flow integrated with AWS Cognito. By intercepting the POST request during login, the attacker obtains an access token that allows direct interaction with Cognito APIs, bypassing UI restrictions. This is a foundational step for email manipulation attacks. The target environment is the Flickr web platform using AWS Cognito for authentication. Expected outcome is a valid access token.

## Requirements

1. Attacker-controlled Flickr account credentials.
2. Network interception tool (e.g., browser developer tools or proxy).
3. Access to Flickr login endpoint.

## Defense

Defensive measures and detection strategies:

- Monitor for unusual API calls to Cognito endpoints.
- Enforce email verification on all changes.

## Objectives

1. Capture a valid Cognito access token.
2. Enable authenticated API access.
3. Prepare for user attribute manipulation.

## Instructions

### Step 1: Login and Intercept Request

**Context**: Log in to Flickr with attacker credentials and intercept the authentication request to extract the access token.

Intercept the POST request to AWS Cognito during login from https://identity.flickr.com/, providing username, password, and device key in the AuthParameters.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- authentication
- token-capture
