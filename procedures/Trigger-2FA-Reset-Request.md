---
tags:
  - 2fa-bypass
  - reset-trigger
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
  - '[[Modify Authentication Process]]'
updated_at: '2025-12-14T17:33:12.287Z'
skill_level: low
impact_level: medium
detection_risk: medium
sub_techniques: []
id: f35533b7-b1ed-4323-adf3-237d436adf9f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
---
# Trigger-2FA-Reset-Request

## Summary

This procedure initiates a 2FA reset during the HackerOne login process by skipping TOTP entry, sending a cancellation email to the victim and starting the auto-disable timer.

## Description

The core exploit leverages a flaw where the login flow allows skipping TOTP and opting for reset without strong confirmation. This sends an email to the victim's address with a cancellation link; if ignored, 2FA disables after 24 hours. The target environment is the HackerOne web login page. Prerequisites include 2FA-enabled account and known credentials. Expected outcome is the reset request queued, with email dispatched.

## Requirements

1. 2FA-enabled HackerOne account with known email/password
2. Access to a web browser
3. Victim's email must be monitored indirectly (no interaction needed)

## Defense

Defensive measures and detection strategies:

- Require explicit confirmation for reset progression, not just cancellation
- Shorten the auto-disable window or eliminate it entirely
- Alert users immediately on reset attempts and require phone/SMS verification

## Objectives

1. Bypass TOTP requirement during login
2. Trigger email-based reset process
3. Set up conditions for automatic 2FA disablement

## Instructions

### Step 1: Access Login Page

**Context**: Begin the login flow on the vulnerable endpoint.

Open https://hackerone.com/account/sign_in in a web browser.

> Page loads with email, password, and TOTP fields.

### Step 2: Enter Credentials and Skip TOTP

**Context**: Submit partial login to expose reset option.

Fill in email and password fields, leave TOTP blank, and submit the form.

> System detects missing TOTP and presents reset option.

### Step 3: Initiate Reset

**Context**: Confirm the reset to send the email.

Click 'Reset two-factor authentication' and confirm with 'OK' in the dialog.

> Reset request processed; email sent to victim with cancellation link.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Modify Authentication Process]] Modify Authentication Process

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa-bypass]]
- [[reset-trigger]]
