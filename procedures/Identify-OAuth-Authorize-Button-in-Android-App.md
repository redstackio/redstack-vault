---
tags:
  - reconnaissance
  - android
  - ui-analysis
  - oauth
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Mobile
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:24:35.173Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: e43df9c7-5552-4f49-be14-0f4d331d350b
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify-OAuth-Authorize-Button-in-Android-App

## Summary

This procedure involves inspecting the UI of an Android app, such as the Coinbase app, to locate the OAuth authorization button and evaluate its vulnerability to clickjacking attacks.

## Description

In the context of mobile app security testing, this procedure examines the app's OAuth flow to identify the authorize button. By decompiling the APK or using runtime inspection tools, attackers or testers can pinpoint UI elements susceptible to overlay-based attacks. The target environment is Android devices running the vulnerable app version. Expected outcomes include confirmation of the button's position and attributes, enabling further exploitation planning. Prerequisites include an Android device or emulator with the app installed and basic reverse engineering knowledge.

## Requirements

1. Android app APK file (e.g., downloaded from device or official source)
2. Tools for APK decompilation (e.g., APKTool, Jadx)
3. Access to an Android emulator or physical device for runtime testing

## Defense

Defensive measures and detection strategies:

- Implement android:filterTouchesWhenObscured="true" on sensitive UI buttons
- Use app-level overlay detection libraries to alert users of suspicious overlays
- Monitor for unusual OAuth authorization logs in app analytics

## Objectives

1. Locate the OAuth authorize button in the app's UI
2. Assess attribute configuration for clickjacking risks
3. Gather details for potential exploitation

## Instructions

### Step 1: Decompile the App APK

**Context**: Extract and analyze the app's layout files to find the OAuth UI components.

Use APKTool to decompile the APK:

```bash
apktool d coinbase.apk -o decompiled_app
```

> This command decodes the APK into smali code and resources, allowing inspection of XML layout files in res/layout for the authorize button (e.g., search for 'authorize' or 'oauth' keywords).

### Step 2: Inspect Button Attributes

**Context**: Review the button's XML definition to check for protective attributes.

Navigate to the decompiled layout files and examine the button element:

```xml
<Button android:id="@+id/authorize_button" android:filterTouchesWhenObscured="false" ... />
```

> Look for absence of android:filterTouchesWhenObscured='true'; if missing or false, the button is vulnerable to obscured touches from overlays.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[android]]
- [[ui-analysis]]
- [[oauth]]
