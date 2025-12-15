---
id: proc-slack-reset-access-001
tags:
  - password-reset
  - slack
  - web-access
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
updated_at: '2025-12-14T17:31:42.679Z'
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
# Access-Slack-Password-Reset-Page

## Summary

This procedure uses the emailed reset link to load Slack's password reset interface, which includes the vulnerable 2FA code input field without rate limiting.

## Description

Following email compromise and reset initiation, this step accesses the reset page via the provided URL. The page requires a new password and 2FA code but imposes no limits on failed attempts, setting up brute-force. It's a manual browser step; success depends on the link not expiring and no additional verifications.

## Requirements

1. Valid reset email with clickable link received.
2. Web browser capable of handling Slack's interface.
3. No VPN or proxy restrictions blocking slack.com.

## Defense

Defensive measures and detection strategies:

- Monitor for multiple reset link accesses from suspicious IPs.
- Require additional email confirmation before link activation.
- Log all reset page loads for anomaly detection.

## Objectives

1. Load the reset form with 2FA prompt.
2. Prepare for unprotected code entry.
3. Maintain session for brute-force attempts.

## Instructions

### Step 1: Open Reset Email

**Context**: Retrieve the link from the inbox.

Log into the victim's email and locate the Slack reset notification email.

> The email body contains a button or URL for the reset page.

### Step 2: Navigate to Reset Page

**Context**: Activate the link to reach the form.

Click the link in the email to open https://slack.com/reset?token=... in the browser. The page should display fields for new password and 2FA code.

> If the link expires, repeat the initiation procedure.

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
- [[web-access]]
