---
id: proc-identify-widgetsettings
tags:
  - android
  - exported-activity
  - recon
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/adb-dumpsys-package]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1422]]'
updated_at: '2025-12-14T17:24:39.312Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1422]]'
---
# Identify Exported WidgetSettingsActivity

## Summary

This procedure identifies the exported WidgetSettingsActivity in the Twitter Android app, confirming it extends PreferenceActivity and is vulnerable to external intent invocation without restrictions. It is the reconnaissance step for Fragment Injection attacks.

## Description

In Android apps, exported activities can be invoked by external apps via intents. The Twitter app's WidgetSettingsActivity is exported, allowing attackers to target it for fragment injection. This procedure uses system tools to query and verify the component's exposure, referencing the app's manifest and runtime behavior. Prerequisites include ADB access to the device with the Twitter app installed. Expected outcomes: confirmation of export status, enabling subsequent exploitation.

## Requirements

1. ADB installed and device/emulator connected
2. Twitter Android app installed on target device
3. Basic Android development knowledge for manifest interpretation

## Defense

Defensive measures and detection strategies:

- Use android:exported="false" in app manifests for sensitive activities
- Implement intent validation to restrict extras like ':android:show_fragment'
- Monitor logcat for unusual activity invocations from external packages

## Objectives

1. Confirm WidgetSettingsActivity is exported and extends PreferenceActivity
2. Identify lack of intent filters or validation
3. Prepare for crafting malicious intents

## Instructions

### Step 1: Connect to Device and Query Package

**Context**: Establish ADB connection and dump package details to locate activities.

**Command** ([[commands/adb-dumpsys-package]]):
```bash
adb shell dumpsys package com.twitter.android | grep -A 10 "Activity"
```

> This command retrieves detailed package info, filtering for activities. Expected output includes lines like "Activity: com.twitter.android.WidgetSettingsActivity" with export status.

### Step 2: Verify Extension and Export Status

**Context**: Analyze output to confirm the activity extends PreferenceActivity and is exported.

**Command** ([[commands/adb-dumpsys-package]]):
```bash
adb shell dumpsys package com.twitter.android activities | grep WidgetSettingsActivity
```

> Look for "exported=true" or absence of restrictions. Cross-reference with app decompilation if needed using tools like APKTool (not covered here).

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[T1422]] Software Discovery (adapted for mobile component enumeration)

### Sub-Techniques


## Commands Used

- [[commands/adb-dumpsys-package]]

## Tools Used


## Tags

- android
- exported-activity
- recon
