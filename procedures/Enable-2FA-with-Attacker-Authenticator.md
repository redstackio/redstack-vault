---
id: proc-004
tags:
  - 2fa-enable
  - lockout
  - totp
type: procedure
tools:
  - '[[tools/Google-Authenticator]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:48.239Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enable 2FA with Attacker's Authenticator

## Summary

This procedure enables two-step verification on the unauthorized account using the attacker's Google Authenticator, resulting in permanent DoS for the victim.

## Description

By scanning the site's QR code or entering the secret key into their app, the attacker binds 2FA to their device. Any future login or reset attempt by the victim requires the attacker's TOTP codes, effectively locking them out.

## Requirements

1. Access to Google Authenticator app
2. Active session in security settings
3. Mobile device for app

## Defense

Defensive measures and detection strategies:

- Mandate email or phone verification before 2FA changes
- Alert on 2FA enablement for new/unverified accounts
- Allow 2FA recovery via verified channels

## Objectives

1. Bind 2FA to attacker's app
2. Prevent victim access to account functions
3. Achieve DoS on email-associated actions

## Instructions

### Step 1: Initiate 2FA Setup

**Context**: In security settings, select two-step verification to generate the setup key.

No command; click 'Enable' and scan QR code with [[tools/Google-Authenticator]] or manually enter secret key.

> App generates TOTP codes; enter one to confirm. 2FA activates, shown as enabled.

### Step 2: Verify Enablement

**Context**: Test by logging out and back in, requiring the app code.

No command; logout, login with password + TOTP from app.

> Successful login confirms control; victim attempts will fail without code.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Authenticator]]

## Tags

- [[2fa]]
- [[dos]]
