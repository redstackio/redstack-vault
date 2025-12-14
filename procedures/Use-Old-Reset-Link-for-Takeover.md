---
tags:
  - account-takeover
  - authentication-bypass
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
updated_at: '2025-12-14T17:33:24.564Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: f7838a7e-ca59-46af-bb52-9b648488b9a7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Use-Old-Reset-Link-for-Takeover

## Summary

This procedure exploits the Imgur vulnerability by using a previously obtained password reset link after an email change to reset the password and achieve account takeover.

## Description

After changing the account email, the attacker pastes the original reset link into a browser. Due to improper token management, the link remains valid, allowing password reset without access to the new email. This bypasses security measures intended by the email change. Targets Imgur's reset endpoint. Prerequisites: Copied reset link and post-email change timing. Outcome: Full control via new password.

## Requirements

1. Previously copied valid reset link URL
2. Web browser to access the link
3. Desired new password for the account

## Defense

Defensive measures and detection strategies:

- Enforce expiration and invalidation of reset tokens on profile changes
- Use one-time-use tokens tied to current email
- Detect anomalous reset usage post-email update

## Objectives

1. Activate stale reset link for password change
2. Bypass email verification in recovery
3. Secure persistent access to the account

## Instructions

### Step 1: Access Reset Link

**Context**: Load the old link to initiate the reset form.

Paste the copied reset URL (e.g., https://imgur.com/reset?token=exampletoken123) into the browser address bar and press enter.

> Expected output: Password reset form loads, accepting input despite email change.

### Step 2: Set New Password

**Context**: Complete the reset to update credentials.

Enter a strong new password twice, then submit the form.

> Expected output: Confirmation of password changed. Log in with new credentials to verify takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[authentication-bypass]]
