---
tags:
  - 2fa
  - authenticator-app
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: 61ae3e1c-9fc7-4db7-9a10-0b3a1b73ae21
created_at: '2025-12-14T17:24:45.472Z'
updated_at: '2025-12-14T17:24:45.472Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enable-2FA-with-Authenticator-App

## Summary

This procedure activates 2FA using an authenticator app on the Legal Robot platform, focusing solely on app-based method to set up the vulnerability reproduction.

## Description

Legal Robot's 2FA system supports multiple methods, but this isolates the authenticator app. The process involves scanning a QR code and verifying a time-based one-time password (TOTP). Prerequisites include a logged-in account and a mobile authenticator app. Outcome: 2FA enforced for logins.

## Requirements

1. Logged-in Legal Robot account
2. Mobile device with authenticator app (e.g., Google Authenticator)
3. Camera access for QR scanning

## Defense

Defensive measures and detection strategies:

- Enforce 2FA enablement prompts for all users
- Log 2FA activation events for auditing
- Validate TOTP codes server-side to prevent bypass

## Objectives

1. Secure the account with app-based 2FA
2. Establish baseline for disablement testing
3. Confirm 2FA integration in login flow

## Instructions

### Step 1: Access 2FA Settings

**Context**: Locate and initiate 2FA setup.

Log in and go to account settings > security > 2FA. Select 'Authenticator App' option.

### Step 2: Scan and Verify

**Context**: Pair the app with the platform.

Scan the QR code displayed. Enter the 6-digit code from the app to confirm enablement.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa]]
- [[authenticator-app]]
- [[web]]
