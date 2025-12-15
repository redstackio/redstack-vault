---
tags:
  - nextcloud
  - android
  - account-removal
  - key-persistence
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:24:42.202Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
id: 7cca1ac0-bee8-44fe-9d3d-6c2ae1d87a7c
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Remove-Account-Without-Clearing-Keys

## Summary

This procedure removes a Nextcloud account from the Android app, exploiting the vulnerability where E2E encryption keys and mnemonics remain in local storage, enabling future unauthorized access.

## Description

The Nextcloud Android app's account removal process does not securely delete E2E-related data from the device's local storage. This leaves keys intact, allowing re-authentication to decrypt files without the original mnemonic. This step is performed by the legitimate user but sets up the exploit for an attacker with physical access.

## Requirements

1. Nextcloud app with E2E-enabled account active
2. Android device under control
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Patch the app to versions that clear keys on removal
- Manually delete app data post-removal via device settings
- Implement app sandboxing and storage auditing

## Objectives

1. Remove account visibility from the app
2. Preserve keys in storage for exploitation
3. Simulate user error leading to data exposure

## Instructions

### Step 1: Initiate Account Removal

**Context**: Trigger the removal process without key clearance.

**Action**:
In the app, go to Settings > Accounts, select the account, and choose 'Remove account'. Confirm the action.

> The app removes session data but retains E2E keys in local files (e.g., in app's private directory).

### Step 2: Verify Persistence

**Context**: Confirm no immediate data wipe occurred (for testing).

**Action**:
Check app storage via device file manager or ADB if advanced; keys should still exist in /data/data/com.nextcloud.client/files/ or similar.

> No visible change in account list, but underlying storage unchanged.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

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
- [[key-persistence]]
