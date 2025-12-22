---
id: proc-static-analysis-exported-activity-001
tags:
  - android
  - manifest
  - exported-component
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:39.330Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Static Analysis of Exported Android Activity

## Summary

This procedure involves decompiling an Android APK and analyzing the manifest to identify exported components like activities that can be invoked by external apps via intents, revealing potential entry points for exploitation such as XSS.

## Description

In the context of the IRCCloud Android app, static analysis uncovers the ImageViewerActivity as exported with intent-filters for VIEW actions on custom schemes (IMAGE_SCHEME and IMAGE_SCHEME_SECURE). This allows any app on the device or Instant Apps to launch it without permissions, passing arbitrary data that may lead to vulnerabilities like unsanitized input in WebViews. Prerequisites include an APK file and a decompiler; outcomes include mapping attack surfaces for further dynamic testing.

## Requirements

1. Android APK of the target app (e.g., IRCCloud)
2. Decompiler tool like JADX or APKTool
3. Basic knowledge of Android manifest structure

## Defense

Defensive measures and detection strategies:

- Restrict exported components with android:exported="false" or permission checks
- Use static analysis tools like MobSF to scan for exported activities during app reviews
- Monitor intent logs via ADB for anomalous launches

## Objectives

1. Identify unrestricted exported activities as initial access vectors
2. Document intent-filters and schemes for exploitation planning
3. Validate browsability without installation

## Instructions

### Step 1: Decompile the APK

**Context**: Extract the AndroidManifest.xml to inspect component exports.

Use JADX to decompile:

```bash
jadx -d output_dir irccloud.apk
```

> This generates source code and manifest; navigate to AndroidManifest.xml.

### Step 2: Inspect Manifest for Exported Activities

**Context**: Search for activities with intent-filters lacking protections.

Open AndroidManifest.xml and locate:

```xml
<activity android:name="com.irccloud.android.activity.ImageViewerActivity">
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <data android:scheme="irccloud-image" />
    </intent-filter>
</activity>
```

> Confirm no android:permission or exported="false"; this makes it launchable externally.

### Step 3: Verify Custom Schemes

**Context**: Note schemes like IMAGE_SCHEME for intent crafting.

Document schemes from intent-filters.

**Expected Output**: List of exported activities and their filters.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- android-manifest
- static-analysis
