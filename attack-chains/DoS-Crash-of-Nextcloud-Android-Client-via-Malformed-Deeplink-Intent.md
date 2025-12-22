---
id: ac-nextcloud-android-dos-deeplink
tags:
  - dos
  - android
  - nextcloud
  - deeplink
  - intent
  - crash
  - exception-handling
type: attack_chain
tools:
  - '[[tools/ADB-Android-Debug-Bridge]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Android
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Examine-AndroidManifest-for-Registered-Deeplinks]]'
  - '[[procedures/Analyze-ModifiedAuthenticatorActivity-for-Exception-Issues]]'
  - '[[procedures/Exploit-DoS-by-Sending-Malformed-Intent-with-ADB]]'
step_count: 3
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:24:39.773Z'
description: >-
  Multi-stage attack demonstrating denial of service in Nextcloud Android client
  by exploiting improper exception handling in deeplink processing, leading to
  app crash.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# DoS Crash of Nextcloud Android Client via Malformed Deeplink Intent

Multi-stage attack chain demonstrating a complete denial of service workflow against the Nextcloud Android client by exploiting a vulnerability in deeplink processing. The attack leverages improper exception handling in the `parseLoginDataUrl` method, causing the app to crash when processing a malformed `nc://login` intent. This disrupts user access to the app and can be triggered by malicious apps or external intents.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Examine Manifest for Deeplinks] --> B[Analyze Code for Exceptions]
    B --> C[Send Malformed Intent to Crash App]
    C --> D[DoS Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ADB-Android-Debug-Bridge]]

### Target Environment

- Target OS/Platform: Android device with Nextcloud client installed (com.nextcloud.client package)
- Required services/ports: USB debugging enabled on device; no network ports required as this is local intent-based
- Network access requirements: Local access to device via ADB

### Initial Access Requirements

- Credential requirements: None (requires physical or ADB access to device)
- Network position: Direct USB connection or ADB over network
- Prior access needed: ADB setup and Nextcloud app installed

## Detailed Attack Procedures

### Step 1: Examine AndroidManifest for Registered Deeplinks
procedure: [[procedures/Examine-AndroidManifest-for-Registered-Deeplinks]]

**Objective**: Identify the deeplink handlers in the Nextcloud Android app to target vulnerable components.

**Instructions**: Decompile or review the AndroidManifest.xml file from the app's APK to locate registered deeplinks. Focus on activities handling custom URI schemes like `nc://login`.

**Expected Output**: Confirmation of `nc://login` deeplink registered to `com.owncloud.android.authentication.ModifiedAuthenticatorActivity`.

**Success Indicators**:
- Deeplink scheme and handler activity identified
- Target component for further analysis noted

### Step 2: Analyze ModifiedAuthenticatorActivity for Exception Issues
procedure: [[procedures/Analyze-ModifiedAuthenticatorActivity-for-Exception-Issues]]

**Objective**: Inspect the source code of the handler to uncover improper exception handling in deeplink parsing.

**Instructions**: Review the `ModifiedAuthenticatorActivity` class, particularly the `parseLoginDataUrl` method, for unhandled exceptions when processing malformed inputs like plain `nc://login` without parameters.

**Expected Output**: Identification of exception-throwing logic without try-catch blocks, confirming vulnerability to crashes.

**Success Indicators**:
- Parsing method found to lack exception handling
- Malformed input test case validated (e.g., via static analysis)

### Step 3: Exploit DoS by Sending Malformed Intent with ADB
procedure: [[procedures/Exploit-DoS-by-Sending-Malformed-Intent-with-ADB]]

**Objective**: Trigger the app crash by sending a malformed intent, achieving denial of service.

**Instructions**: Use ADB to launch the vulnerable activity with the malformed deeplink URI. Execute the following command:

using [[commands/adb-shell-am-start-malformed-nc-login-intent]]:

```bash
adb shell am start -a "android.intent.action.VIEW" -c "android.intent.category.DEFAULT" -n "com.nextcloud.client/com.owncloud.android.authentication.ModifiedAuthenticatorActivity" -d "nc://login"
```

Monitor the device for the app crash.

**Expected Output**: App process terminates with an unhandled exception in `parseLoginDataUrl`.

**Success Indicators**:
- App crashes and restarts or force-closes
- Logcat shows exception details confirming DoS

## Attack Chain Summary

### Key Achievements

1. Identified vulnerable deeplink in manifest
2. Confirmed exception handling flaw in code
3. Successfully crashed the app via intent, demonstrating DoS impact

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
