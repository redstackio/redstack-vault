---
tags:
  - authentication
  - valid-accounts
  - disabled-account
type: procedure
tools: []
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
updated_at: '2025-12-14T17:25:53.411Z'
skill_level: basic
impact_level: medium
detection_risk: medium
sub_techniques: []
id: a0ab7ad2-f0d0-4786-8289-682368042db2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-Disabled-Account

## Summary

This procedure demonstrates logging into a disabled user account on a platform like HackerOne, establishing an authenticated session via backend APIs despite frontend restrictions.

## Description

Disabled accounts are meant to be inaccessible, but if authentication endpoints do not enforce status checks, attackers with credentials can gain session tokens. This leads to backend API access, such as GraphQL, for data exfiltration or modification. The target environment is a web application with session-based auth using tokens and cookies.

## Requirements

1. Valid username/password for the disabled target account
2. Access to the login endpoint (e.g., https://hackerone.com/login)
3. Proxied browser setup (optional but recommended for capture)

## Defense

Defensive measures and detection strategies:

- Enforce disabled status checks in all authentication and API endpoints
- Log failed/successful logins for disabled accounts and alert admins
- Implement multi-factor authentication (MFA) to add friction for stolen creds

## Objectives

1. Obtain active session tokens for a disabled account
2. Confirm backend authentication succeeds despite UI blocks
3. Prepare for API exploitation without reactivation

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the authentication interface.

No command; Open browser to https://hackerone.com/login.

> Ensure proxy is configured if using Burp.

### Step 2: Submit Credentials

**Context**: Perform login to generate session artifacts.

No command; Enter username and password, submit form.

> Expected: Redirect to disabled page, but check network tab for auth success (200 OK on login POST).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-login
- session-hijack-potential
