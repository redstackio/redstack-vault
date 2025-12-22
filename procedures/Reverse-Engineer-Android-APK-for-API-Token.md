---
tags:
  - reverse-engineering
  - android-apk
  - deep-links
  - token-extraction
type: procedure
tools:
  - '[[tools/adb]]'
  - '[[tools/Apktool]]'
  - '[[tools/dex2jar]]'
  - '[[tools/jd-gui]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/adb-install-apk]]'
  - '[[commands/adb-trigger-deep-link-one]]'
  - '[[commands/adb-trigger-deep-link-two]]'
  - '[[commands/adb-trigger-deep-link-three]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:33:06.047Z'
skill_level: advanced
impact_level: high
detection_risk: low
sub_techniques: []
id: f1634367-7409-45cb-9d98-4243cf8b6504
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Reverse Engineer Android APK for API Token

## Summary

This procedure involves decompiling and dynamically analyzing an Android APK using deep links to trigger hidden activities, extracting an API token from application logs.

## Description

The BountyPay.apk manifest defines deep links (one://part, two://part?two=light&switch=on, three://part?switch=b24&three=... ). Triggering them via adb reveals progressive unlocks, with the final link logging the token '8e9998ee3137ca9ade8f372739f062c1' and API URL.

## Requirements

1. Downloaded APK file
2. Android emulator or device with adb
3. Decompilers: Apktool, dex2jar, jd-gui
4. adb logcat for monitoring

## Defense

Defensive measures and detection strategies:

- Obfuscate deep links and sensitive data in APK
- Avoid logging tokens; use secure storage like Android Keystore
- Validate deep link parameters server-side

## Objectives

1. Unpack and analyze APK manifest for deep links
2. Trigger links to unlock functionalities
3. Extract token from runtime logs

## Instructions

### Step 1: Install APK on Emulator

**Context**: Prepare the app for dynamic analysis.

**Command** ([[commands/adb-install-apk]]):
```bash
adb install BountyPay.apk
```

> Installs the app. Expected output: Success message.

### Step 2: Trigger First Deep Link

**Context**: Start the activity chain.

**Command** ([[commands/adb-trigger-deep-link-one]]):
```bash
adb shell am start -W -a android.intent.action.VIEW -d "one://part?start=PartTwoActivity" bounty.pay
```

> Launches PartOneActivity to PartTwoActivity.

### Step 3: Trigger Second Deep Link

**Context**: Proceed to next stage.

**Command** ([[commands/adb-trigger-deep-link-two]]):
```bash
adb shell am start -W -a android.intent.action.VIEW -d "two://part?two=light\&switch=on" bounty.pay
```

> Reveals text box and MD5 hash.

### Step 4: Trigger Third Deep Link and Capture Logs

**Context**: Extract the token.

**Command** ([[commands/adb-trigger-deep-link-three]]):
```bash
adb shell am start -W -a android.intent.action.VIEW -d "three://part?switch=b24\&three=UGFydFRocmVlQWN0aXZpdHk%3D\&header=X-Token" bounty.pay
```

> Run with adb logcat | grep -i token. Expected output: Logs with X-Token: 8e9998ee3137ca9ade8f372739f062c1.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

- None

## Commands Used

- [[commands/adb-install-apk]]
- [[commands/adb-trigger-deep-link-one]]
- [[commands/adb-trigger-deep-link-two]]
- [[commands/adb-trigger-deep-link-three]]

## Tools Used

- [[tools/adb]]
- [[tools/Apktool]]
- [[tools/dex2jar]]
- [[tools/jd-gui]]

## Tags

- reverse-engineering
- android-apk
- deep-links
- token-extraction
