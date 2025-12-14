---
tags:
  - account-creation
  - testing-setup
  - coinbase
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T17:24:42.012Z'
skill_level: novice
impact_level: low
detection_risk: low
sub_techniques: []
id: 84b789cc-3d9e-4110-91ff-0f68ef9211a7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Create-Multiple-Coinbase-Test-Accounts

## Summary

This procedure sets up multiple test accounts in the Coinbase Android app using unique email addresses, enabling simulation of user interactions for vulnerability testing without risking real funds or data.

## Description

In the context of testing the Coinbase app's privacy features, creating isolated test accounts is essential to replicate real-world transaction scenarios. Each account must be registered via the app with a distinct email to ensure traceability of disclosures. This step assumes access to an Android device and does not involve any exploits, focusing on legitimate onboarding. Expected outcomes include fully verified accounts capable of basic bitcoin transfers.

## Requirements

1. Android device or emulator running the Coinbase app (latest version at time of discovery)
2. Multiple unique, disposable email addresses (e.g., from services like Gmail or ProtonMail)
3. Stable internet connection for registration and verification

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on account creations to prevent abuse
- Monitor for unusual patterns of multi-account setups from the same IP/device
- Use CAPTCHA or additional verification for suspicious registrations

## Objectives

1. Establish sender and recipient personas for transaction testing
2. Ensure accounts are functional for bitcoin sends/receives
3. Avoid any premature data exposure during setup

## Instructions

### Step 1: Install and Launch App

**Context**: Begin the setup by accessing the official Coinbase Android app to start registration.

Download and install the Coinbase app from the Google Play Store. Open the app and select 'Sign up' to initiate account creation.

### Step 2: Register First Account

**Context**: Create the sender account with a specific email to later verify exposure.

Enter a unique email address, create a strong password, and provide necessary personal details (use fictional data for testing). Complete email verification by checking the inbox and confirming the link.

### Step 3: Register Additional Accounts

**Context**: Repeat for the recipient account to simulate peer-to-peer transfer.

Log out and repeat the registration process with a second unique email. Ensure both accounts undergo any required identity verification for transaction capabilities, though minimal for small tests.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-creation
- testing-setup
- coinbase
