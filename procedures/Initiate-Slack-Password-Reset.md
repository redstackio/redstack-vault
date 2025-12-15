---
id: proc-slack-reset-init-001
tags:
  - password-reset
  - slack
  - initial-access
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
updated_at: '2025-12-14T17:31:42.683Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Initiate-Slack-Password-Reset

## Summary

This procedure initiates the Slack password reset process by submitting the target's email address, triggering an email with a reset link that enables access to the vulnerable 2FA entry point.

## Description

In the context of exploiting Slack's lack of 2FA rate limiting, this step starts the password reset flow. An attacker with access to the victim's email can request a reset from the Slack login page, receiving a time-limited link. This link leads to a reset interface where 2FA is required but unprotected against brute-force. Prerequisites include email compromise; the procedure is manual and browser-based, succeeding if the email is registered with Slack.

## Requirements

1. Access to the victim's email account credentials.
2. Web browser with internet access to slack.com.
3. Target's Slack username or email known.

## Defense

Defensive measures and detection strategies:

- Implement email alerts for password reset attempts.
- Use device fingerprinting to detect unusual reset requests.
- Enforce short expiration times (e.g., 5 minutes) on reset links.

## Objectives

1. Obtain a valid password reset link via email.
2. Position for subsequent 2FA exploitation.
3. Enable account takeover without original credentials.

## Instructions

### Step 1: Navigate to Slack Login

**Context**: Access the public login page to begin the reset process.

Open a web browser and go to https://slack.com/signin. Click the "Trouble signing in?" or "Forgot password?" link.

> This loads the password recovery form without requiring authentication.

### Step 2: Submit Target Email

**Context**: Request the reset for the specific victim.

Enter the victim's email address in the recovery form and submit. Monitor the compromised email inbox for the incoming reset message.

> The email arrives containing a unique URL like https://slack.com/reset?token=abc123, valid for a short period.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-reset]]
- [[slack]]
- [[initial-access]]
