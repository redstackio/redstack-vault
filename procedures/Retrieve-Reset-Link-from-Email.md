---
tags:
  - email-access
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
updated_at: '2025-12-14T17:32:58.262Z'
sub_techniques: []
id: 0b46ce08-0974-483b-8dd1-271da0c8fffb
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Retrieve Reset Link from Email

## Summary

This procedure accesses the victim's email to obtain the password reset link sent by Weblate.

## Description

After submission, Weblate emails a reset link. The attacker must access this email (e.g., via compromised credentials or open session) to proceed. This step highlights the risk of email access in shared environments like cafes.

## Requirements

1. Access to victim's email inbox
2. Email client or webmail interface
3. Recent submission to ensure link timeliness

## Defense

Defensive measures and detection strategies:

- Use short-lived reset links (e.g., 5 minutes)
- Require additional verification in email (e.g., OTP)
- Monitor email access logs for anomalies

## Objectives

1. Locate the reset email
2. Extract the link URL
3. Ensure link validity

## Instructions

### Step 1: Check Inbox

**Context**: Search for the incoming reset email.

Log into the victim's email (e.g., via Gmail at mail.google.com) and check the inbox or spam for an email from Weblate with subject like 'Password reset requested.' Open it and copy the link.

> Expected output: Email body contains a URL like https://hosted.weblate.org/accounts/password_reset/key/...

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[email-access]]
- [[web]]
