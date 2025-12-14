---
tags:
  - data-access
  - decryption
  - e2e-encryption
  - nextcloud
  - android
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1533]]'
updated_at: '2025-12-14T17:24:42.191Z'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
id: 454123e2-8439-48e7-b3a6-354f9141a941
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[T1533]]'
---
# Access-Persistent-Encrypted-Files

## Summary

This procedure allows an attacker to decrypt and view E2E encrypted files in the Nextcloud Android app using persistent local keys after re-authentication.

## Description

Once re-logged in, the app uses the uncleared E2E keys from local storage to automatically decrypt files during sync and display. This compromises the encryption's confidentiality, exposing all previously protected data to anyone with device access.

## Requirements

1. Active session in Nextcloud app post-re-authentication
2. Encrypted files present on the server
3. Local keys intact from prior steps

## Defense

Defensive measures and detection strategies:

- Verify app patches clear keys properly
- Encrypt device storage and use secure deletion tools
- Audit file access logs on Nextcloud server

## Objectives

1. Retrieve and decrypt sensitive files
2. Exfiltrate or view data without additional barriers
3. Demonstrate full compromise of E2E protections

## Instructions

### Step 1: Navigate to Files

**Context**: Access the file list in the app.

**Action**:
Open the file browser in the Nextcloud app and select the folder containing E2E encrypted files.

> Files sync and appear as decryptable.

### Step 2: Decrypt and View

**Context**: Trigger decryption using stored keys.

**Action**:
Tap on an encrypted file to open it; the app decrypts inline without prompts.

> Content displays in cleartext, confirming key persistence.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[T1533]] Data from Local System

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[data-access]]
- [[e2e-encryption]]
- [[nextcloud]]
