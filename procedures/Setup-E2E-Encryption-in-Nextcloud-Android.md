---
tags:
  - nextcloud
  - android
  - e2e-encryption
  - setup
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
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:24:42.205Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: eac869aa-2c65-4576-99ac-d92b1574e4e6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Setup-E2E-Encryption-in-Nextcloud-Android

## Summary

This procedure enables end-to-end encryption in the Nextcloud Android app for a user account, setting up the conditions for subsequent exploitation of key persistence issues.

## Description

In the context of testing or simulating the vulnerability, this step involves activating E2E encryption on an Android device connected to a Nextcloud server. The app generates encryption keys and a mnemonic phrase stored locally. This is a prerequisite for creating encrypted data that remains accessible post-account removal due to the app's failure to clear storage.

## Requirements

1. Android device with Nextcloud app installed (version affected by the vulnerability, e.g., pre-fix versions)
2. Active Nextcloud account on a server supporting E2E encryption
3. Internet connectivity for initial setup

## Defense

Defensive measures and detection strategies:

- Ensure app updates to patched versions that clear keys on removal
- Monitor device for unauthorized physical access
- Use device encryption and remote wipe capabilities

## Objectives

1. Activate E2E encryption to protect (temporarily) sensitive files
2. Store keys and mnemonic locally for later persistence exploitation
3. Verify encryption functionality before proceeding

## Instructions

### Step 1: Enable E2E Feature

**Context**: Access app settings to toggle encryption for the account.

**Action**:
Open the Nextcloud app, select the account, go to Settings > End-to-end encryption, and enable it. Follow prompts to generate keys.

> The app will display a mnemonic phrase; note it for verification, but in exploitation, it won't be needed later.

### Step 2: Verify Setup

**Context**: Confirm encryption is active by attempting to encrypt a test file.

**Action**:
Upload a sample file via the app and check that it is marked as E2E encrypted in the file list.

> Successful setup shows files locked with E2E icon, decryptable only locally.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[nextcloud]]
- [[android]]
- [[e2e-encryption]]
