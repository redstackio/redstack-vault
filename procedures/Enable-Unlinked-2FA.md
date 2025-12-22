---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
name: Enable-Unlinked-2FA
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:31:42.503Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - 2fa-bypass
  - auth-bypass
platforms:
  - Web
tools:
  - '[[tools/Google-Authenticator]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Enable-Unlinked-2FA

## Summary

This procedure enables two-factor authentication (2FA) on HackerOne using the Google Authenticator app without properly linking it to the user's account, exploiting a misconfiguration that allows unverified 2FA setup and subsequent bypass of security checks.

## Description

In the context of HackerOne's platform, the 2FA enforcement fails to validate proper account linkage during setup. By generating 2FA codes in the Google Authenticator app independently (without scanning a QR code or entering a secret key tied to the account), an attacker can input these codes to enable 2FA. This creates an unverified state, allowing access to features like program invitations without full authentication rigor. The target environment is the HackerOne web dashboard, requiring an existing account. Expected outcomes include 2FA appearing active while bypassing intended verification logic.

## Requirements

1. HackerOne account with access to settings
2. Mobile device with Google Authenticator app installed
3. No existing 2FA setup on the account

## Defense

Defensive measures and detection strategies:

- Enforce strict 2FA secret key validation during setup to prevent unlinked code entry
- Log and alert on 2FA enable/disable cycles within short timeframes
- Require re-verification for sensitive actions post-2FA changes

## Objectives

1. Establish unverified 2FA to evade enforcement checks
2. Enable access to invitation acceptance without linkage validation
3. Set stage for further manipulation of authentication state

## Instructions

### Step 1: Setup Google Authenticator Without Linkage

**Context**: Generate independent 2FA codes to simulate setup without account association.

Open the Google Authenticator app and add a new account manually by entering a generic secret key or using time-based codes without scanning any QR code from HackerOne.

> This produces a stream of 6-digit codes that can be used for input.

### Step 2: Enable 2FA in HackerOne Settings

**Context**: Input the unlinked codes to activate 2FA, exploiting the lack of validation.

Navigate to HackerOne account settings > Security > Two-Factor Authentication. Select to enable 2FA, enter your password, and input sequential codes from the unlinked Google Authenticator app to verify.

> Upon success, 2FA status shows as enabled, but the system does not enforce proper linkage.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Authenticator]]

## Tags

- [[2fa-bypass]]
- [[auth-bypass]]
