---
tags:
  - nextcloud
  - android
  - e2e-encryption
  - key-persistence
  - cryptographic-failure
  - physical-access
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Android
  - Mobile
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-E2E-Encryption-in-Nextcloud-Android]]'
  - '[[procedures/Remove-Account-Without-Clearing-Keys]]'
  - '[[procedures/Obtain-Physical-Access-and-Re-Authenticate]]'
  - '[[procedures/Access-Persistent-Encrypted-Files]]'
step_count: 6
techniques:
  - '[[Valid Accounts]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:24:42.214Z'
description: >-
  An attack chain exploiting the failure of the Nextcloud Android app to clear
  end-to-end encryption keys upon account removal, allowing physical access
  attackers to decrypt and access sensitive files after re-authenticating.
skill_level: low
impact_level: high
id: 75e21459-d47b-41e2-8851-81ccb3cdc08d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Unsecured Credentials]]'
---
# Access E2E Encrypted Files via Persistent Keys After Account Removal in Nextcloud Android App

Multi-stage attack chain demonstrating a complete attack workflow exploiting a cryptographic failure in the Nextcloud Android app.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~5 minutes |
| Skill Level | Low |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup E2E Encryption] --> B[Create Encrypted Data]
    B --> C[Remove Account]
    C --> D[Obtain Physical Access]
    D --> E[Re-Authenticate]
    E --> F[Access Decrypted Files]

    style A fill:#e74c3c
    style B fill:#e74c3c
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Physical access to the Android device
- Knowledge of the target's Nextcloud account credentials or ability to reset password

### Target Environment

- Android device with Nextcloud app installed
- Nextcloud server with E2E encryption enabled
- No specific ports or network access beyond standard app connectivity

### Initial Access Requirements

- Physical possession of the device post-account removal
- Valid account credentials (via reset if needed)
- No prior network position required; local device access suffices

## Detailed Attack Procedures

### Step 1: Setup E2E Encryption
procedure: [[procedures/Setup-E2E-Encryption-in-Nextcloud-Android]]

**Objective**: Enable end-to-end encryption for the target account on the Android device to protect data that will later be compromised.

**Instructions**: Open the Nextcloud Android app, navigate to settings, and enable the E2E encryption feature for the account on the specified server. Generate or note the mnemonic phrase for key management.

**Expected Output**: E2E encryption activated, with keys stored locally in the app.

**Success Indicators**:
- Encryption toggle enabled in app settings
- Mnemonic phrase displayed and stored

### Step 2: Create Encrypted Data
procedure: [[procedures/Setup-E2E-Encryption-in-Nextcloud-Android]]

**Objective**: Generate or upload files that are encrypted using the E2E keys, simulating sensitive data storage.

**Instructions**: Within the app, upload files or create content that triggers E2E encryption. Verify that files are marked as encrypted in the app interface.

**Expected Output**: Encrypted files visible in the app, accessible only with local keys.

**Success Indicators**:
- Files listed as E2E encrypted
- Attempt to view file requires local decryption

### Step 3: Remove Account Without Clearing Keys
procedure: [[procedures/Remove-Account-Without-Clearing-Keys]]

**Objective**: Remove the account from the device, exploiting the vulnerability where keys and mnemonics persist in local storage.

**Instructions**: In the Nextcloud app, go to account settings and select to remove the account from the device. Confirm removal without additional key clearance prompts.

**Expected Output**: Account removed from app list, but underlying storage retains E2E keys.

**Success Indicators**:
- Account no longer visible in app
- No prompt to clear mnemonic or keys

### Step 4: Obtain Physical Access
procedure: [[procedures/Obtain-Physical-Access-and-Re-Authenticate]]

**Objective**: Gain physical possession of the device after account removal to enable local exploitation.

**Instructions**: Secure the Android device through physical means (e.g., theft or temporary access). Unlock the device if screen lock is bypassed.

**Expected Output**: Full control over the device hardware and software.

**Success Indicators**:
- Device powered on and accessible
- App drawer or home screen reachable

### Step 5: Re-Authenticate to Account
procedure: [[procedures/Obtain-Physical-Access-and-Re-Authenticate]]

**Objective**: Log back into the Nextcloud account using the app, leveraging persistent keys without needing the mnemonic.

**Instructions**: Open the Nextcloud app, add the account by entering server details, and authenticate via password reset or known credentials. Complete the login process.

**Expected Output**: Account re-added and session established.

**Success Indicators**:
- Successful login confirmation
- Syncing of files initiates

### Step 6: Access Persistent Encrypted Files
procedure: [[procedures/Access-Persistent-Encrypted-Files]]

**Objective**: Decrypt and view previously encrypted files using the uncleared local keys, compromising data confidentiality.

**Instructions**: Navigate to the encrypted files in the app. The app automatically decrypts them using stored keys, displaying content without additional authentication.

**Expected Output**: Cleartext view of all E2E encrypted files.

**Success Indicators**:
- Files decrypt seamlessly
- Sensitive data visible without mnemonic entry

## Attack Chain Summary

### Key Achievements

1. Bypassed E2E encryption protections through key persistence
2. Enabled post-removal data access with minimal effort
3. Compromised confidentiality of cloud-synced sensitive files via local device exploit

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Unsecured Credentials]] Unsecured Credentials

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
