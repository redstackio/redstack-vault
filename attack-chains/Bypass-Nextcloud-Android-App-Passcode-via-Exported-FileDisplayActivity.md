---
tags:
  - android
  - auth-bypass
  - nextcloud
  - exported-activity
  - mobile
type: attack_chain
tools:
  - '[[tools/Drozer]]'
  - '[[tools/Drozer-Agent]]'
  - '[[tools/Android-Studio-AVD]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Android
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-Android-Emulation-and-Install-Nextcloud]]'
  - '[[procedures/Configure-Passcode-and-Install-Drozer]]'
  - '[[procedures/Connect-to-Drozer-Console]]'
  - '[[procedures/Exploit-Exported-FileDisplayActivity]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[T1417]]'
updated_at: '2025-12-14T17:24:39.886Z'
description: >-
  Multi-stage attack exploiting an exported activity in the Nextcloud Android
  app to bypass passcode protection and gain unauthorized access to user files
  and sensitive information on non-rooted Android 9 devices.
skill_level: intermediate
impact_level: high
id: 377244bd-d8f6-4f58-8d06-9984ddfe1e5e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[T1417]]'
---
# Bypass Nextcloud Android App Passcode via Exported FileDisplayActivity

Multi-stage attack chain demonstrating exploitation of an exported activity in the Nextcloud Android app to bypass passcode protection, allowing unauthorized access to the app's UI, files, and sensitive information on non-rooted Android 9 devices. This vulnerability was identified using Drozer for intent-based component invocation without authentication checks.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Environment] --> B[Install and Configure App] --> C[Connect Drozer] --> D[Exploit Activity]
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Android-Studio-AVD]]
- [[tools/Drozer]]
- [[tools/Drozer-Agent]]

### Target Environment

- Android OS version 9, non-rooted device or emulator
- Nextcloud Android app installed
- Valid Nextcloud account credentials

### Initial Access Requirements

- Local access to the Android device/emulator
- No prior root access needed
- Host machine with Android Studio and Drozer installed

## Detailed Attack Procedures

### Step 1: Set Up Android Emulation and Install Nextcloud
procedure: [[procedures/Set-Up-Android-Emulation-and-Install-Nextcloud]]

**Objective**: Prepare a non-rooted Android 9 environment and install the vulnerable Nextcloud app with authentication.

**Instructions**: Launch Android Studio AVD to create an emulated device running Android 9 without root privileges. Download and install the Nextcloud Client APK, then log in using valid user credentials to establish a connected account.

**Expected Output**: Emulated device booted, Nextcloud app installed and logged in successfully.

**Success Indicators**:
- AVD emulator running Android 9
- Nextcloud app accessible with account synced

### Step 2: Configure Passcode and Install Drozer
procedure: [[procedures/Configure-Passcode-and-Install-Drozer]]

**Objective**: Enable passcode protection in the app to simulate a secured state and set up the Drozer assessment framework.

**Instructions**: Within the Nextcloud app settings, configure a passcode for protection. On the host, install the Drozer framework, and deploy the Drozer Agent APK to the emulated device. Start the Drozer embedded server on the device.

**Expected Output**: Passcode screen active on app reopen; Drozer Agent installed and server running.

**Success Indicators**:
- Passcode prompt appears when reopening the app
- Drozer embedded server logs show it's listening

### Step 3: Connect to Drozer Console
procedure: [[procedures/Connect-to-Drozer-Console]]

**Objective**: Establish a secure console connection to the device for executing assessment commands.

**Instructions**: Open a command prompt on the host and connect to the Drozer agent using [[commands/drozer-console-connect]]:

```bash
drozer console connect
```

**Expected Output**: Successful connection message from Drozer console.

**Success Indicators**:
- Console connected without errors
- Drozer prompt available for command execution

### Step 4: Exploit Exported FileDisplayActivity
procedure: [[procedures/Exploit-Exported-FileDisplayActivity]]

**Objective**: Bypass the passcode by directly invoking the exported FileDisplayActivity via intent, gaining unauthorized UI access.

**Instructions**: With the app closed to trigger passcode on reopen, execute the exploit command in the Drozer console using [[commands/run-app-activity-start]]:

```bash
run app.activity.start --component com.nextcloud.client com.owncloud.android.ui.activity.FileDisplayActivity
```

This launches the activity directly, bypassing authentication.

**Expected Output**: FileDisplayActivity opens, displaying app UI and files without passcode entry.

**Success Indicators**:
- App UI accessible without passcode
- User files and sensitive info viewable

## Attack Chain Summary

### Key Achievements

1. Simulated a secured Nextcloud app environment on Android 9
2. Leveraged Drozer to exploit exported component without root
3. Achieved full unauthorized access to app data, demonstrating auth bypass impact

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[T1417]] Access via Unauthorized Intent

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
