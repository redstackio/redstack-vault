---
tags:
  - physical-access
  - re-authentication
  - nextcloud
  - android
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:42.196Z'
skill_level: low
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[T1078.004]]'
id: d0fea2da-8d8e-4714-b5ba-73a1b773870d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Obtain-Physical-Access-and-Re-Authenticate

## Summary

This procedure involves gaining physical access to the Android device and re-authenticating to the Nextcloud account, leveraging persistent E2E keys to bypass full credential requirements.

## Description

With physical access post-account removal, the attacker can add the account back to the app using password reset or known credentials. The uncleared keys allow seamless session establishment without mnemonic re-entry, setting the stage for data access.

## Requirements

1. Physical possession of the unlocked Android device
2. Ability to perform password reset on the Nextcloud account (e.g., via email)
3. Network connectivity for authentication

## Defense

Defensive measures and detection strategies:

- Enable strong device PIN/biometrics and remote lock/wipe
- Monitor account login logs on Nextcloud server for unusual locations
- Use multi-factor authentication to complicate resets

## Objectives

1. Secure device control
2. Re-establish account session exploiting key persistence
3. Prepare for file decryption

## Instructions

### Step 1: Secure Device Access

**Context**: Unlock and control the device.

**Action**:
Power on the device, bypass screen lock if possible, and access the app drawer.

> Ensure no tamper-evident features alert the owner.

### Step 2: Add and Authenticate Account

**Context**: Re-add the account to trigger key usage.

**Action**:
Launch Nextcloud app, tap 'Add account', enter server URL, username, and reset password if needed. Complete login.

> App syncs without prompting for mnemonic due to stored keys.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- [[T1078.004]] Cloud Accounts

## Commands Used

- None

## Tools Used

- None

## Tags

- [[physical-access]]
- [[nextcloud]]
- [[android]]
