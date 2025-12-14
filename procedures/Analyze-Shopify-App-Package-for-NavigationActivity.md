---
id: proc-uuid-001
tags:
  - android
  - reverse-engineering
  - app-analysis
type: procedure
tools:
  - '[[tools/ADB-Android-Debug-Bridge]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Process Discovery]]'
updated_at: '2025-12-14T17:24:45.153Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Process Discovery]]'
---
# Analyze-Shopify-App-Package-for-NavigationActivity

## Summary

This procedure involves reverse-engineering the Shopify Android app package to identify the NavigationActivity component, which lacks URL scheme validation, enabling subsequent exploitation.

## Description

In the attack scenario, attackers analyze the app's APK or manifest to locate com.shopify.mobile.navigation.NavigationActivity. This component accepts a 'url' extra parameter without validating schemes like 'javascript:' or 'data:', allowing arbitrary content loading in the WebView. The target environment is an Android device with the Shopify app installed. Prerequisites include ADB access and basic reverse-engineering tools. Expected outcomes include confirmation of the vulnerability for crafting exploits.

## Requirements

1. Android device or emulator with Shopify app (com.shopify.mobile) installed
2. ADB enabled for package inspection
3. APK decompilation tools like APKTool (optional for deeper analysis)

## Defense

Defensive measures and detection strategies:

- Implement URL scheme whitelisting in app components
- Use runtime validation for intent extras in WebView loaders
- Monitor ADB usage and app launches via device logs

## Objectives

1. Identify vulnerable components in the app manifest
2. Confirm lack of scheme validation in NavigationActivity
3. Prepare for payload crafting based on parameter details

## Instructions

### Step 1: Pull and Examine App Package

**Context**: Use ADB to dump the app's package info and manifest to locate the NavigationActivity.

**Command** (no specific command; use ADB shell):
```bash
adb shell dumpsys package com.shopify.mobile | grep NavigationActivity
```

> This command retrieves package details, revealing com.shopify.mobile.navigation.NavigationActivity and its intent filters. Expected output includes component name and exported status. Success indicates the component accepts extras like 'url'.

### Step 2: Decompile Manifest for Details

**Context**: If needed, decompile the APK to inspect the full manifest and code for validation logic.

**Command** (using APKTool, assuming APK is pulled):
```bash
apktool d shopify.apk
```

> Decompile the APK file. Look in AndroidManifest.xml for the activity declaration. Expected output: XML showing no scheme restrictions on 'url' extra. No direct command link, but confirms vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Process Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ADB-Android-Debug-Bridge]]

## Tags

- [[android]]
- [[reverse-engineering]]
