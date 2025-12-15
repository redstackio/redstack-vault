---
tags:
  - android
  - recon
  - exported-components
type: procedure
tools:
  - '[[tools/adb]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '[TIMESTAMP]'
techniques:
  - '[[T1417]]'
updated_at: '2025-12-14T17:24:39.656Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 69d93a43-2d44-4f1a-b1fb-aa4a33dedd55
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1417]]'
---
# Identify-Exported-Android-Activities

## Summary

This procedure involves inspecting an Android app's manifest to identify improperly exported activities that can be accessed externally, enabling potential authentication bypass or data exposure in apps like Whisper.

## Description

In Android applications, activities declared in AndroidManifest.xml with android:exported="true" (or default true pre-API 12) without proper intent filters or permissions can be launched by external apps or tools like ADB. This procedure targets sensitive activities such as notifications or inbox handlers in the Whisper app (package sh.whisper), allowing attackers to discover components vulnerable to unauthorized invocation. The attack scenario assumes physical or ADB access to a device with the app installed, common in lost device scenarios or malware contexts. Expected outcomes include listing of exported components, confirming root causes like missing android:exported="false" per CWE-926.

## Requirements

1. Android device with USB debugging enabled and Whisper app installed
2. ADB (Android Debug Bridge) installed on the attacking machine
3. USB cable or network ADB setup for device connection

## Defense

Defensive measures and detection strategies:

- Set android:exported="false" for sensitive activities in app manifests
- Use custom permissions or intent filters to restrict external access
- Monitor ADB logs for suspicious activity launches; implement app-level logging for unauthorized invocations

## Objectives

1. Discover exported Android components in the target app
2. Confirm lack of protections on sensitive activities
3. Prepare for exploitation by identifying launchable components

## Instructions

### Step 1: Connect Device and Dump Package Info

**Context**: Establish connection and retrieve package details to inspect components.

Connect the device:

```bash
adb devices
```

> Lists connected devices; ensure the target is authorized.

Dump the package manifest:

```bash
adb shell pm dump sh.whisper > manifest_dump.txt
```

> Pulls detailed package info including activities; grep for 'activity' to filter.

### Step 2: Analyze for Exported Activities

**Context**: Search the dump for exported sensitive activities.

Filter activities:

```bash
grep -A 20 "activity" manifest_dump.txt | grep exported
```

> Identifies activities like sh.whisper.WNotificationsActivity and sh.whisper.WInboxActivity marked as exported without restrictions.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[T1417]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/adb]]

## Tags

- [[android]]
- [[recon]]
- [[exported-components]]
