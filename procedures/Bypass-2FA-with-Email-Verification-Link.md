---
tags:
  - 2fa-bypass
  - auth-bypass
  - rocket-chat
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: e87122cf-11be-4b99-827a-877913a5ee76
created_at: '2025-12-14T17:24:47.890Z'
updated_at: '2025-12-14T17:24:47.890Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass-2FA-with-Email-Verification-Link

## Summary

This procedure exploits the lack of 2FA enforcement in Rocket.Chat's email verification link, allowing direct account login without OTP entry.

## Description

After initiating an email change, the verification link provided in the email grants session access upon click, bypassing the 2FA check that should occur post-verification. This undermines 2FA entirely if the attacker controls the email. The attack assumes email interception or control and targets web sessions.

## Requirements

1. Verification link from email change process
2. Attacker access to victim's email
3. Target Rocket.Chat instance

## Defense

Defensive measures and detection strategies:

- Implement 2FA re-verification on all session-creating links
- Use short-lived tokens for verification with additional auth
- Monitor login events without 2FA for anomalies

## Objectives

1. Achieve unauthorized account access
2. Demonstrate 2FA ineffectiveness against email flaws
3. Gain full control for further exploitation

## Instructions

### Step 1: Access the Verification Link

**Context**: Use the link to attempt login.

Click the link in the received email (e.g., https://open.rocket.chat/verify-email?token=abc123).

> The link should redirect to the dashboard without prompting for 2FA.

### Step 2: Validate Access

**Context**: Confirm bypass success.

Perform account actions like viewing channels or settings.

> Expected output: Full session established; no OTP requested, confirming bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa-bypass]]
- [[auth-bypass]]
- [[rocket-chat]]
