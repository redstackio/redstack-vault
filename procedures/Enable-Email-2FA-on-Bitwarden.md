---
tags:
  - 2fa-setup
  - authentication
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
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:24:47.534Z'
sub_techniques: []
id: db91347f-13b0-48fd-b583-cf132e226b63
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Enable-Email-2FA-on-Bitwarden

## Summary

This procedure configures email-based two-factor authentication on a Bitwarden account, exposing the vulnerable 2FA code verification endpoint for brute-force testing.

## Description

After logging into the Bitwarden vault, users can enable 2FA via account settings, selecting email as the delivery method. This sends a 6-digit code to the registered email for verification. The endpoint handling code submission lacks strict rate limiting, allowing repeated attempts.

## Requirements

1. Active Bitwarden account with login access
2. Access to the registered email inbox
3. Web browser for settings navigation

## Defense

Defensive measures and detection strategies:

- Enforce device binding for 2FA to prevent code reuse
- Log and alert on multiple failed 2FA attempts per session

## Objectives

1. Activate email 2FA to simulate protected login
2. Generate a static 6-digit code for brute-force target
3. Prepare for login interception

## Instructions

### Step 1: Access Account Settings

**Context**: Log in and navigate to 2FA configuration.

Log in at https://vault.bitwarden.com, go to Account Settings > Security > Two-step login.

> Select 'Email' as the method and save.

### Step 2: Verify Initial Code

**Context**: Enter the emailed code to enable 2FA.

Check email for 6-digit code and input it during setup.

> 2FA enabled; future logins require code.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa-setup]]
- [[authentication]]
