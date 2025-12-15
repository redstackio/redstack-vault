---
id: ac-uuid-placeholder
tags:
  - path-traversal
  - android
  - mattermost
  - rce
  - code-execution
  - intent-injection
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Persistence]]'
verified: false
platforms:
  - Android
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-Android-App-with-EvilContentProvider]]'
  - '[[procedures/Send-Malicious-Share-Intent-to-Mattermost-ShareActivity]]'
  - '[[procedures/Process-Share-and-Save-Traversed-File-in-Mattermost]]'
  - '[[procedures/Relaunch-Mattermost-to-Execute-Malicious-Library]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Hijack Execution Flow]]'
updated_at: '2025-12-14T17:24:45.212Z'
description: >-
  Multi-stage attack exploiting a path traversal vulnerability in the Mattermost
  Android app's ShareActivity to overwrite native libraries and achieve
  persistent arbitrary code execution upon app relaunch.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Hijack Execution Flow]]'
---
# Path Traversal in Mattermost Android ShareActivity Leading to Arbitrary Code Execution

Multi-stage attack chain demonstrating exploitation of a path traversal vulnerability in the Mattermost Android app. The attack involves creating a malicious app that sends a crafted share intent to the exported ShareActivity, allowing traversal sequences to overwrite critical files like native libraries (e.g., libyoga.so). Upon relaunching Mattermost, the malicious library executes arbitrary code, enabling persistent compromise. This was discovered via analysis of RealPathUtil.java, where DISPLAY_NAME from the content provider is used unsanitized as the filename.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious App] --> B[Send Share Intent]
    B --> C[Overwrite Library via Traversal]
    C --> D[Relaunch and Execute Code]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Android Studio (for building the malicious app)
- ADB (Android Debug Bridge) for installation and intent sending

### Target Environment

- Android device or emulator with Mattermost app installed (version vulnerable to CVE or similar, pre-2021 patches)
- Android SDK for app development
- Root not required, but physical or ADB access to device

### Initial Access Requirements

- Ability to install apps on the target device (user interaction or sideload)
- Mattermost app must be installed and ShareActivity exported (default behavior)

## Detailed Attack Procedures

### Step 1: Create Malicious Android App
procedure: [[procedures/Create-Malicious-Android-App-with-EvilContentProvider]]

**Objective**: Develop and prepare a malicious Android app that provides a content provider capable of serving traversed filenames and malicious payloads.

**Instructions**: Use Android Studio to create an app with an EvilContentProvider that responds to URI queries by returning a MatrixCursor with a path traversal name (e.g., "../../lib-main/libyoga.so") and opens the malicious library file (e.g., /data/data/com.example.android.pocok/libevil-lib.so).

**Expected Output**: Compiled APK ready for installation.

**Success Indicators**:
- App builds without errors
- EvilContentProvider registers correctly in AndroidManifest.xml

### Step 2: Send Malicious Share Intent
procedure: [[procedures/Send-Malicious-Share-Intent-to-Mattermost-ShareActivity]]

**Objective**: Launch the malicious app and dispatch a crafted ACTION_SEND intent to Mattermost's ShareActivity, embedding the traversal URI.

**Instructions**: Install the APK via ADB, then use ADB shell or app code to create an Intent with ACTION_SEND, setClassName to Mattermost's ShareActivity, and putExtra for STREAM URI (content://com.example.android.pocok/?path=/data/data/com.example.android.pocok/libevil-lib.so&name=../../lib-main/libyoga.so), with type application/*.

**Expected Output**: Intent delivered, Mattermost receives and processes the share.

**Success Indicators**:
- No intent resolution errors
- Mattermost ShareActivity launches

### Step 3: Process Share and Save Traversed File
procedure: [[procedures/Process-Share-and-Save-Traversed-File-in-Mattermost]]

**Objective**: Exploit the lack of validation in RealPathUtil.getPathFromSavingTempFile to save the malicious file using the traversed filename, overwriting app directories.

**Instructions**: In Mattermost, the app queries the provider, retrieves unsanitized DISPLAY_NAME, creates a File in cacheDir with the traversal path (resolving to /lib-main/libyoga.so), and copies the malicious content.

**Expected Output**: Malicious library overwritten in Mattermost's lib directory.

**Success Indicators**:
- File saved without exceptions
- Verify via ADB pull or logcat for file operations

### Step 4: Relaunch Mattermost to Execute Malicious Library
procedure: [[procedures/Relaunch-Mattermost-to-Execute-Malicious-Library]]

**Objective**: Trigger loading of the overwritten native library on app startup, resulting in arbitrary code execution.

**Instructions**: Force close and relaunch the Mattermost app via launcher or ADB (am start -n com.mattermost.rn/.MainActivity).

**Expected Output**: Malicious code executes; in POC, app crashes due to unmodified library.

**Success Indicators**:
- App launches and loads libyoga.so
- Logcat shows execution or crash indicating load

## Attack Chain Summary

### Key Achievements

1. Successful path traversal via unsanitized DISPLAY_NAME in content provider
2. Overwrite of native library (libyoga.so) with malicious payload
3. Persistent RCE on Mattermost relaunch without further interaction

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Hijack Execution Flow]] Hijack Execution Flow

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Persistence]] Persistence

---
*Last updated: 2023-10-01T00:00:00Z*
