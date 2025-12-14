---
id: proc-nextcloud-new-device-001
tags:
  - nextcloud
  - nonce-recovery
  - multi-device
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
updated_at: '2025-12-14T17:24:42.225Z'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Use Alternate Authentication Material]]'
---
# New-Device-Setup-with-Nonce-Recovery

## Summary

This procedure sets up an additional device using the recovery nonce to restore the private key, inadvertently downloading the tampered public key without verification.

## Description

On a new Desktop or Android client, the user logs in and initiates E2E setup. The client downloads the public key from the server (now substituted). Entering the nonce restores the original private key, but since no verification occurs, the device proceeds, leading to encryption using the private key but targeted to the wrong public key.

## Requirements

1. Recovery nonce from initial setup
2. New Nextcloud client installation
3. Access to the same server account

## Defense

Defensive measures and detection strategies:

- Implement public-private key matching verification in clients
- Warn users during nonce entry about key changes
- Audit multi-device setups for anomalies

## Objectives

1. Connect new device to account
2. Restore private key via nonce
3. Download and accept tampered public key

## Instructions

### Step 1: Install Client and Log In

**Context**: Sync the new device.

Install client, enter server details and credentials.

**Expected Output**: Basic sync complete.

### Step 2: Initiate E2E Setup

**Context**: Download public key.

Toggle E2E on; client fetches public key from server automatically.

**Expected Output**: Setup prompt for recovery.

### Step 3: Enter Recovery Nonce

**Context**: Restore private key without verification.

Input the 12-word nonce; client derives private key.

**Expected Output**: E2E enabled; no mismatch errors.

**Success Indicators**:
- Device shows encrypted folders
- Sync proceeds normally

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
- [[nonce-recovery]]
- [[multi-device]]
