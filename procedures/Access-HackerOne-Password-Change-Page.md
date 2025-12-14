---
tags:
  - web
  - auth
type: procedure
tools:
  - '[[tools/Charles-Proxy]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:52.993Z'
sub_techniques: []
id: 15b95860-2ea4-4e15-bd87-7efa91539c71
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-HackerOne-Password-Change-Page

## Summary

This procedure logs into a HackerOne account and navigates to the password change page, setting up for capturing authentication-sensitive requests during a password update.

## Description

In the context of testing GraphQL session invalidation, this step authenticates to the HackerOne platform and accesses the password edit interface at https://hackerone.com/settings/pass/edit. It requires valid credentials and prepares the environment for proxy interception. The outcome positions the attacker to observe and capture the GraphQL mutation used for password changes, exploiting the platform's delay in token invalidation.

## Requirements

1. Valid HackerOne account credentials (username/email and current password)
2. Web browser with proxy support (e.g., configured for Charles Proxy)
3. Network access to https://hackerone.com

## Defense

Defensive measures and detection strategies:

- Implement immediate token revocation on password changes
- Monitor for anomalous password update requests post-sign-out
- Use short-lived session tokens and enforce re-authentication for sensitive actions

## Objectives

1. Gain authenticated access to the password change interface
2. Prepare for request capture without triggering premature sign-out
3. Validate initial access to the target account

## Instructions

### Step 1: Log In to HackerOne

**Context**: Authenticate to the platform to access user settings.

Navigate to https://hackerone.com/users/sign_in in a web browser and enter credentials to log in.

> Successful login redirects to the dashboard, confirming access.

### Step 2: Navigate to Password Edit Page

**Context**: Access the specific endpoint for password modification.

From the dashboard, go to https://hackerone.com/settings/pass/edit. The page displays a form with fields for current password, new password, and confirmation.

> Form loads successfully, ready for input; no submission yet to avoid early sign-out.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Charles-Proxy]]

## Tags

- web
- auth
