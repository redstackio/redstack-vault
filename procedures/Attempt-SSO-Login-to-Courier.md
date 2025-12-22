---
tags:
  - sso
  - login
  - cognito
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - AWS
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 093e5605-6456-44e8-ba92-d97f76310f8c
created_at: '2025-12-13T09:01:26.277Z'
updated_at: '2025-12-13T09:01:26.278Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Attempt SSO Login to Courier

## Summary

This procedure describes initiating an SSO login to the Courier application using a previously revoked provider, exploiting potential caching in AWS Cognito.

## Description

After revoking access from the SSO provider, attempt to log in to Courier via the same provider. Due to Cognito's caching, the login may succeed without revalidating the token, allowing access for up to 1 hour.

## Requirements

1. Web browser with access to Courier login page
2. Previously linked SSO account
3. Internet connectivity

## Defense

Defensive measures and detection strategies:

- Configure Cognito to check token status on each login
- Log and alert on logins with revoked tokens

## Objectives

1. Test login flow post-revocation
2. Exploit caching vulnerability
3. Gain unauthorized access temporarily

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the Courier application's SSO login endpoint.

Open a browser and go to the Courier login URL, selecting SSO with Google or GitHub.

> Ensure no active sessions exist.

### Step 2: Initiate SSO Flow

**Context**: Proceed with the SSO authentication process.

Click the SSO button and follow the provider's redirect if prompted.

> Cognito uses the cached token without API recheck.

### Step 3: Complete Login

**Context**: Verify if access is granted.

If successful, you will be redirected to the Courier dashboard.

> Note the time of successful login for cache expiration tracking.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[sso]]
- [[cognito]]
