---
tags:
  - bitwarden
  - biometric-bypass
  - android
  - authentication-bypass
  - mobile
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Android
  - Mobile App
  - iOS
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Sign-In-to-Primary-Account-and-Enable-Biometrics]]'
  - '[[procedures/Force-Kill-Bitwarden-App]]'
  - '[[procedures/Enroll-New-Fingerprint]]'
  - '[[procedures/Observe-Biometric-Unlock-Disabled-Message]]'
  - '[[procedures/Add-Secondary-Account-and-Enable-Biometrics]]'
  - '[[procedures/Attempt-Switch-to-Primary-Account]]'
  - '[[procedures/Force-Kill-App-Again]]'
  - '[[procedures/Unlock-Secondary-Account-with-Biometrics]]'
  - '[[procedures/Switch-to-Primary-Account-and-Bypass-with-Biometrics]]'
step_count: 9
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.465Z'
description: >-
  Multi-stage attack exploiting a vulnerability in the Bitwarden Android app to
  bypass forced master password re-authentication after biometric changes,
  allowing unauthorized access to the primary vault using biometrics from a
  secondary account.
skill_level: intermediate
impact_level: high
id: db7f561a-aa92-4c6d-84c8-d3c4469ca936
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bitwarden Android Biometric Integrity Bypass via Secondary Account Switching

Multi-stage attack chain demonstrating a complete attack workflow to bypass biometric integrity checks in the Bitwarden Android app. The vulnerability allows an attacker with physical device access to access the primary vault without the master password by invalidating the biometric integrity flag through fingerprint changes and leveraging a secondary account to circumvent re-authentication.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 9 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Step 1: Sign In Primary] --> B[Step 2: Force Kill App]
    B --> C[Step 3: Enroll New Fingerprint]
    C --> D[Step 4: Observe Disabled Message]
    D --> E[Step 5: Add Secondary Account]
    E --> F[Step 6: Attempt Primary Switch]
    F --> G[Step 7: Force Kill App Again]
    G --> H[Step 8: Unlock Secondary]
    H --> I[Step 9: Bypass Primary Unlock]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#3498db
    style G fill:#f39c12
    style H fill:#3498db
    style I fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (requires physical access to Android device with Bitwarden app installed)

### Target Environment

- Android device with fingerprint sensor
- Bitwarden mobile app (vulnerable version, references GitHub bitwarden/mobile GH-1026 and GH-1093)
- No specific ports or services; local device access only

### Initial Access Requirements

- Physical access to the unlocked device
- Knowledge of primary Bitwarden account (but bypasses master password)
- Ability to enroll new biometrics
- Valid secondary Bitwarden account credentials

## Detailed Attack Procedures

### Step 1: Sign In to Primary Account and Enable Biometrics
procedure: [[procedures/Sign-In-to-Primary-Account-and-Enable-Biometrics]]

**Objective**: Log into the primary Bitwarden account and enable biometric unlock to set up the initial state for the bypass.

**Instructions**: Launch the Bitwarden app on the Android device. Enter the primary account credentials (email and master password) to sign in. Navigate to Settings > Security > Unlock with Biometrics and toggle it on to enable fingerprint unlock.

**Expected Output**: Successful login to the primary vault with biometric option active.

**Success Indicators**:
- Primary vault accessible
- Biometric unlock enabled in settings

### Step 2: Force Kill Bitwarden App
procedure: [[procedures/Force-Kill-Bitwarden-App]]

**Objective**: Ensure the app is fully locked before proceeding to biometric changes.

**Instructions**: Open the device's recent apps or settings (e.g., swipe up and swipe away the app, or go to Settings > Apps > Bitwarden > Force Stop). This locks the app state.

**Expected Output**: Bitwarden app closed and locked.

**Success Indicators**:
- App no longer running in background
- Attempting to reopen prompts for authentication

### Step 3: Enroll New Fingerprint
procedure: [[procedures/Enroll-New-Fingerprint]]

**Objective**: Invalidate the biometric integrity check by adding a new fingerprint, triggering the re-authentication requirement.

**Instructions**: Go to device Settings > Security > Biometrics > Fingerprint. Follow prompts to enroll a new fingerprint. This sets the BiometricIntegrityValid flag to false as per the vulnerability (GH-1026).

**Expected Output**: New fingerprint added successfully.

**Success Indicators**:
- New fingerprint registered in device settings
- Integrity flag invalidated (verified in next step)

### Step 4: Observe Biometric Unlock Disabled Message
procedure: [[procedures/Observe-Biometric-Unlock-Disabled-Message]]

**Objective**: Confirm the integrity check has been triggered, disabling biometric unlock for the primary account.

**Instructions**: Reopen the Bitwarden app. It should display the message 'Biometric unlock disabled pending verification of master password' due to the flag being false.

**Expected Output**: App shows the disable message; biometric unlock blocked.

**Success Indicators**:
- Message appears on app launch
- Cannot unlock primary vault with biometrics

### Step 5: Add Secondary Account and Enable Biometrics
procedure: [[procedures/Add-Secondary-Account-and-Enable-Biometrics]]

**Objective**: Introduce a secondary account with valid biometrics to facilitate the bypass.

**Instructions**: In the Bitwarden app (while primary is pending), go to Settings > Accounts > Add Account. Enter secondary account credentials to sign in, then enable biometrics for it in Security settings.

**Expected Output**: Secondary account added and biometric unlock enabled.

**Success Indicators**:
- Secondary vault accessible
- Biometrics work for secondary account

### Step 6: Attempt Switch to Primary Account
procedure: [[procedures/Attempt-Switch-to-Primary-Account]]

**Objective**: Verify that biometric unlock remains blocked for the primary account.

**Instructions**: Use the app's vault switcher (e.g., profile icon or sidebar) to select the primary account. Attempt biometric unlock; it should fail due to the pending verification.

**Expected Output**: Switch fails or prompts for master password; biometrics blocked.

**Success Indicators**:
- Cannot access primary vault biometrically
- Prompt for master password appears

### Step 7: Force Kill App Again
procedure: [[procedures/Force-Kill-App-Again]]

**Objective**: Lock both vaults to reset the app state for the bypass exploitation.

**Instructions**: Force stop the Bitwarden app via device settings or recent apps to ensure both primary and secondary vaults are locked.

**Expected Output**: App fully closed.

**Success Indicators**:
- Both accounts require re-authentication on reopen

### Step 8: Unlock Secondary Account with Biometrics
procedure: [[procedures/Unlock-Secondary-Account-with-Biometrics]]

**Objective**: Gain access to the app via the secondary account's valid biometrics.

**Instructions**: Reopen the app, select the secondary vault using the switcher, and unlock with the enrolled fingerprint.

**Expected Output**: Secondary vault unlocked successfully.

**Success Indicators**:
- App opens to secondary vault
- Biometrics authenticate without issues

### Step 9: Switch to Primary Account and Bypass with Biometrics
procedure: [[procedures/Switch-to-Primary-Account-and-Bypass-with-Biometrics]]

**Objective**: Exploit the vulnerability to unlock the primary vault biometrically from the secondary context, bypassing the integrity check.

**Instructions**: From the unlocked secondary vault, use the vault switcher to select the primary account. Attempt biometric unlock; it now succeeds due to improper enforcement when switching post-restart (GH-1093).

**Expected Output**: Primary vault unlocked with biometrics; access to view/delete passwords.

**Success Indicators**:
- Primary vault accessible without master password
- Can view and manage primary vault contents

## Attack Chain Summary

### Key Achievements

1. Invalidated biometric integrity without triggering persistent lock
2. Used secondary account to re-enable biometric context
3. Bypassed re-authentication to access primary vault

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
