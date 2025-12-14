---
tags:
  - account-creation
  - setup
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:24:47.537Z'
sub_techniques: []
id: 0fe7d8b5-4280-480a-bfde-224315ba0933
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Create-Bitwarden-Account

## Summary

This procedure creates a new Bitwarden account to serve as a test environment for demonstrating the 2FA brute-force vulnerability.

## Description

In the context of testing Bitwarden's email 2FA rate limiting, a fresh account is registered on vault.bitwarden.com. This allows enabling 2FA and simulating login flows without affecting real user data. The process involves standard web registration and requires an email address for verification.

## Requirements

1. Internet access to vault.bitwarden.com
2. A disposable or test email address
3. Web browser or proxy tool like Burp Suite for interception

## Defense

Defensive measures and detection strategies:

- Monitor for unusual account creation patterns from single IPs
- Implement CAPTCHA on registration to deter automation

## Objectives

1. Obtain valid credentials for 2FA testing
2. Set up environment for vulnerability exploitation
3. Ensure controlled testing without real compromise

## Instructions

### Step 1: Navigate to Registration

**Context**: Access the Bitwarden vault signup page to begin account creation.

No specific command; use browser to visit https://vault.bitwarden.com/register.

> Fill in email, master password, and complete registration. Expect a verification email.

### Step 2: Verify Email

**Context**: Confirm the account via email link to activate it.

Click the verification link in the received email.

> Successful verification allows login with email/password.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[External Remote Services]] External Remote Services

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[account-creation]]
- [[setup]]
