---
id: p2q3r4s5-t6u7-8901-cdef-gh2345678901
tags:
  - authentication
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.513Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Authenticate-HackerOne-Account

## Summary

This procedure logs into a HackerOne account as a hacker persona to gain access to user settings and preferences, required for interacting with the vulnerable Bounty Preferences feature.

## Description

HackerOne requires authentication to access personalized features like invitation preferences. This step uses standard login credentials to establish a session. The target environment is the web platform, with outcomes including a valid session cookie for subsequent requests. No special tools needed beyond a browser.

## Requirements

1. Valid HackerOne hacker account email and password
2. Network access to https://hackerone.com
3. Browser with proxy configured if intercepting

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA)
- Rate-limit login attempts
- Log and alert on suspicious login patterns

## Objectives

1. Establish authenticated session
2. Access protected endpoints
3. Prepare for preference modifications

## Instructions

### Step 1: Navigate to Login

**Context**: Reach the authentication page.

Open https://hackerone.com/users/sign_in in the browser.

> Page loads with login form.

### Step 2: Submit Credentials

**Context**: Authenticate the account.

Enter email and password, then submit the form.

> Successful redirect to dashboard; session established.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- login
- session
