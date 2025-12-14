---
tags:
  - dos-verification
  - 2fa
  - account-lockout
  - shopify
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-05T12:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:30:27.374Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: a0de6a99-e5b5-4c5d-ae09-29c9172a62a5
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Verify Victim Account Lockout

## Summary

This procedure simulates or observes the victim's login attempt to confirm the DoS effect, where rate limit exhaustion prevents OTP delivery and access.

## Description

Post-spam, the victim's Shopify login redirects to 2FA but fails to deliver codes due to exhausted limits. If no recovery codes are saved, access is denied for 24 hours. This validates the attack's impact on SMS-reliant users.

## Requirements

1. Prior steps completed (tamper and spam)
2. Victim's cooperation or monitoring access
3. Knowledge of victim's credentials (for simulation)

## Defense

Defensive measures and detection strategies:

- Encourage backup 2FA methods (app-based, recovery codes)
- Notify users of rate limit hits via email
- Monitor login failures correlated with SMS volumes

## Objectives

1. Attempt victim login to trigger 2FA
2. Observe OTP and resend failures
3. Confirm 24-hour lockout

## Instructions

### Step 1: Initiate Victim Login

**Context**: Start the login process to reach 2FA.

No command; UI:

- Victim enters email and password on shopify.com/login
- Submits to authenticate

> Expected: Redirect to 2FA verification page.

### Step 2: Request OTP and Observe Failure

**Context**: Check for code delivery.

On 2FA page:

- Wait for OTP (none arrives due to limits)
- Page may show old codes if any pending

> Expected: No new SMS received.

### Step 3: Attempt Resend and Confirm Block

**Context**: Verify throttling on resend.

Click 'Resend Code':

- Multiple clicks result in errors or no response
- System indicates temporary block

> Expected: Resend denied; access locked until quota resets (24 hours).

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dos-verification
- account-lockout
