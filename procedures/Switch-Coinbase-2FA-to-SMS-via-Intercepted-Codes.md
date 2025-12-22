---
id: proc-coinbase-2fa-switch-16696-3
tags:
  - 2fa-bypass
  - authentication-modification
type: procedure
tools:
  - '[[tools/Authy]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Reversible Encryption]]'
updated_at: '2025-12-14T17:24:45.408Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Reversible Encryption]]'
---
# Switch-Coinbase-2FA-to-SMS-via-Intercepted-Codes

## Summary

This procedure exploits the ability to change 2FA methods on Coinbase from app-based (Authy) to SMS using intercepted codes, without any delays or freezes, enabling full account control.

## Description

Following email and SMS compromises, attackers reset the Coinbase password and re-sync the Authy app to invalidate legitimate tokens. They then use captured SMS codes to switch 2FA to SMS, targeting the exchange's web settings. This highlights design flaws in authentication flows. Outcomes include seamless takeover, allowing immediate actions without user intervention.

## Requirements

1. Compromised email and intercepted SMS access
2. Installed Authy app on attacker's device for re-sync
3. Access to Coinbase web interface

## Defense

Defensive measures and detection strategies:

- Implement mandatory delays or email confirmations for 2FA changes
- Use biometric or hardware 2FA to prevent method switches
- Monitor account for rapid 2FA modifications via platform alerts

## Objectives

1. Invalidate existing 2FA and establish attacker-controlled method
2. Gain authenticated access to account features
3. Avoid triggering protective freezes on funds

## Instructions

### Step 1: Reset Coinbase Password

**Context**: Use email access to initiate account recovery.

Go to Coinbase login, select 'Forgot Password,' and use the compromised email to set a new password.

> Verify login with the new credentials.

### Step 2: Re-sync and Invalidate Authy

**Context**: Transfer Authy control to the attacker.

Install and re-sync Authy using the account details from email, generating new tokens that override the target's.

> Confirm old codes no longer work.

### Step 3: Switch to SMS 2FA

**Context**: Use intercepted SMS to complete the change without delays.

In Coinbase settings, select to change 2FA to SMS; enter the intercepted verification code.

> Expected output: 2FA updated to SMS, with no fund freeze activated.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Reversible Encryption]] Multi-Factor Authentication Instrument

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Authy]]

## Tags

- [[2fa-bypass]]
- [[authentication-modification]]
