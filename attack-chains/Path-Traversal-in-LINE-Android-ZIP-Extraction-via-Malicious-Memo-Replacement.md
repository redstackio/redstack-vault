---
id: 663b6a7f-3632-4737-a5f7-e37d453d8084
name: Path Traversal in LINE Android ZIP Extraction via Malicious Memo Replacement
type: attack_chain
description: >-
  Multi-stage attack exploiting path traversal in the LINE Android app's ZIP
  extraction to overwrite private files using a malicious ZIP memo synced from
  LINE Chrome.
verified: false
submitted: true
step_count: 5
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:21.776Z'
procedures:
  - '[[procedures/Create-Memo-in-LINE-Chrome-for-Sync]]'
  - '[[procedures/Install-PoC-Android-App-for-Interception]]'
  - '[[procedures/Intercept-and-Replace-ZIP-with-Malicious-Version]]'
  - '[[procedures/Open-Malicious-ZIP-in-LINE-Android]]'
  - '[[procedures/Observe-App-Crash-and-File-Overwrite]]'
techniques:
  - '[[Exploitation for Client Execution]]'
tactics:
  - '[[Execution]]'
tags:
  - path-traversal
  - android
  - zip-extraction
  - file-overwrite
  - line-app
platforms:
  - Android
  - Web
tools:
  - '[[tools/PoC-Android-Application]]'
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---

# Path Traversal in LINE Android ZIP Extraction via Malicious Memo Replacement

Multi-stage attack chain demonstrating a complete attack workflow exploiting a path traversal vulnerability in the LINE Android app's Keep service ZIP extraction routine.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Memo in LINE Chrome] --> B[Install PoC App]
    B --> C[Intercept and Replace ZIP]
    C --> D[Open ZIP in LINE Android]
    D --> E[Observe Crash and Overwrite]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/PoC-Android-Application]]

### Target Environment

- Android OS (LINE app installed)
- Web (LINE for Chrome extension)
- LINE Keep service for file syncing
- No specific ports; requires app installation and web access

### Initial Access Requirements

- Access to victim's Android device for PoC app installation
- LINE account synced across Chrome and Android
- No prior credentials needed beyond app access

## Detailed Attack Procedures

### Step 1: Create Memo in LINE Chrome
procedure: [[procedures/Create-Memo-in-LINE-Chrome-for-Sync]]

**Objective**: Initiate a syncable ZIP file via a new memo in LINE for Chrome to set up the target file for replacement.

**Instructions**: Open LINE for Chrome, create a new memo with some text content, and save it. This triggers syncing as a ZIP file to the LINE Keep service.

**Expected Output**: A new memo appears in the LINE Keep on the Android device after refresh.

**Success Indicators**:
- Memo created and synced
- ZIP file visible in Android LINE Keep

### Step 2: Install PoC Android App
procedure: [[procedures/Install-PoC-Android-App-for-Interception]]

**Objective**: Deploy the interception tool on the target Android device to monitor and modify incoming ZIP files.

**Instructions**: Install the pre-built PoC Android application on the victim's device and grant the required STORAGE permission when prompted.

**Expected Output**: App installed successfully with permissions enabled.

**Success Indicators**:
- PoC app runs without errors
- STORAGE permission granted

### Step 3: Intercept and Replace ZIP
procedure: [[procedures/Intercept-and-Replace-ZIP-with-Malicious-Version]]

**Objective**: Replace the legitimate synced ZIP with a malicious one containing path traversal entries to exploit the extraction vulnerability.

**Instructions**: Open LINE for Android, navigate to Keep, and pull to refresh to trigger sync. The PoC app automatically intercepts the incoming ZIP and replaces it with a crafted malicious version using paths like '../../../../../../../data/data/jp.naver.line.android/files/something'.

**Expected Output**: Malicious ZIP in place, ready for extraction.

**Success Indicators**:
- Original ZIP intercepted
- Malicious ZIP substituted without detection

### Step 4: Open Malicious ZIP in LINE Android
procedure: [[procedures/Open-Malicious-ZIP-in-LINE-Android]]

**Objective**: Trigger the vulnerable ZIP extraction routine in the LINE app to process the malicious file.

**Instructions**: In the LINE Android app, tap on the malicious ZIP note to open its contents.

**Expected Output**: App begins extraction process.

**Success Indicators**:
- ZIP file opens
- Extraction initiates

### Step 5: Observe App Crash and File Overwrite
procedure: [[procedures/Observe-App-Crash-and-File-Overwrite]]

**Objective**: Confirm exploitation by observing the crash and verifying file overwrites in private directories.

**Instructions**: Monitor the app during extraction; it will crash with a SecurityException, but check private folders like /data/data/jp.naver.line.android/files/ for overwritten content from the malicious ZIP.

**Expected Output**: App crashes; files overwritten prior to crash.

**Success Indicators**:
- SecurityException crash logged
- Sensitive files modified or replaced

## Attack Chain Summary

### Key Achievements

1. Successful creation and syncing of a target ZIP memo
2. Interception and replacement with path traversal payload
3. Exploitation leading to private file overwrite
4. App crash confirming vulnerability trigger
5. Potential compromise of app data despite pre-fix on related insecure storage issue

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### MITRE ATT&CK Tactics

- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
