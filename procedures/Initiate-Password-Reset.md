---
tags:
  - auth-bypass
  - web
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
updated_at: '2025-12-14T17:32:58.265Z'
sub_techniques: []
id: 079f2295-b118-4359-a8b3-1dbf57797a06
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Initiate Password Reset

## Summary

This procedure triggers the password reset flow on Weblate's login page, redirecting to the reset form without authentication.

## Description

By clicking the 'Reset it' link on the login page, the attacker begins the process to request a reset email. This step exploits the public nature of the reset initiation, requiring no prior access. It sets up the vulnerability exploitation in subsequent steps.

## Requirements

1. Access to the login page from previous procedure
2. Web browser
3. No email or credentials yet

## Defense

Defensive measures and detection strategies:

- Log reset initiations and alert on high volumes from single IP
- Require pre-login verification for reset starts
- Monitor for automated form submissions

## Objectives

1. Activate reset workflow
2. Redirect to email submission form
3. Avoid any early authentication checks

## Instructions

### Step 1: Click Reset Link

**Context**: From the login page, select the reset option to proceed.

Locate and click the 'Reset it' button under the password field.

> Expected output: Browser redirects to /accounts/password_reset/ or similar, showing email input and CAPTCHA.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[web]]
