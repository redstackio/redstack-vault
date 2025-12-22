---
id: proc-nextcloud-initial-setup-001
tags:
  - nextcloud
  - device-setup
  - key-generation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
  - Desktop
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Use Alternate Authentication Material]]'
updated_at: '2025-12-14T17:24:42.232Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Use Alternate Authentication Material]]'
---
# Initial-Device-Setup-and-Data-Upload

## Summary

This procedure configures the first client device with E2E encryption, generates a keypair, stores the recovery nonce, and uploads encrypted data to establish the initial encrypted state.

## Description

Using the Nextcloud Desktop or Android client, the user enables E2E encryption, which triggers keypair generation (public/private keys). The recovery nonce is displayed and must be saved securely. Sample files are then encrypted using the private key and uploaded to the server, where only the public key is stored. This step highlights the baseline where data is confidentially stored.

## Requirements

1. Installed Nextcloud client (Desktop or Android)
2. User credentials and server URL
3. E2E encryption enabled on server

## Defense

Defensive measures and detection strategies:

- Educate users on secure nonce storage
- Monitor for unusual key generation events
- Enforce client-side key verification in updates

## Objectives

1. Generate and store user keypair
2. Upload initial encrypted data
3. Obtain recovery nonce for multi-device use

## Instructions

### Step 1: Install and Log In to Client

**Context**: Connect the device to the Nextcloud account.

Download and install the Nextcloud client, enter server URL and credentials to sync.

**Expected Output**: Account synced; files accessible.

### Step 2: Enable E2E and Generate Keys

**Context**: Activate encryption and save nonce.

In client settings, toggle E2E encryption on; follow prompts to generate keys and note the displayed nonce.

**Expected Output**: Keys generated; nonce shown (e.g., 12-word phrase).

### Step 3: Upload Encrypted Data

**Context**: Test encryption by uploading files.

Create or select files, enable E2E for folders, and upload; client encrypts before transmission.

**Expected Output**: Files appear encrypted on server.

**Success Indicators**:
- No decryption errors on device
- Server shows encrypted file metadata

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Use Alternate Authentication Material]] Use Alternate Authentication Material

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[nextcloud]]
- [[device-setup]]
- [[key-generation]]
