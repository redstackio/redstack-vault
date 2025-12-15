---
tags:
  - android-reverse
  - apk-analysis
  - intent-bypass
type: procedure
tools:
  - '[[tools/MobSF]]'
  - '[[tools/Genymotion]]'
  - '[[tools/ADB]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/adb-bypass-part1]]'
  - '[[commands/adb-bypass-part2]]'
  - '[[commands/adb-bypass-part3]]'
  - '[[commands/adb-extract-prefs]]'
verified: false
platforms:
  - Android
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Cloud Storage]]'
updated_at: '2025-12-14T17:32:58.235Z'
skill_level: advanced
impact_level: medium
detection_risk: low
sub_techniques: []
id: 9fde533c-d472-45c3-9c1e-e45f19e46606
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Cloud Storage]]'
---
# Android-APK-Reverse-Engineering

## Summary

This procedure downloads the BountyPay APK, analyzes it with MobSF, emulates on Genymotion, and bypasses activity checks with ADB to extract the API token from shared preferences.

## Description

The APK from /uploads is statically analyzed for vulnerabilities. Dynamic analysis bypasses intent checks in PartOneActivity, PartTwoActivity, and PartThreeActivity to reach CongratsActivity, revealing the token in user_created.xml.

## Requirements

1. Downloaded APK file
2. Genymotion emulator setup
3. ADB and MobSF installed

## Defense

- Obfuscate APK code and use secure intent filters
- Encrypt sensitive data in shared preferences
- Implement runtime checks for activity bypasses

## Objectives

1. Analyze APK for secrets
2. Bypass protections to access hidden data
3. Extract API token

## Instructions

### Step 1: Download and Static Analysis

**Context**: Download APK and run MobSF.

Download from https://software.bountypay.h1ctf.com/uploads/BountyPay.apk; upload to MobSF for analysis.

> Identifies insecure storage.

### Step 2: Emulate and Bypass Activities

**Context**: Use ADB to start activities with crafted intents.

**Command** ([[commands/adb-bypass-part1]]):
```bash
adb shell am start -a android.intent.action.VIEW -d "one://part?start=PartTwoActivity" -n bounty.pay/.PartOneActivity
```

> Advances to PartTwo.

**Command** ([[commands/adb-bypass-part2]]):
```bash
adb shell am start -a android.intent.action.VIEW -d "two://part?two=light&switch=on" -n bounty.pay/.PartTwoActivity
```

> Shows form.

**Command** ([[commands/adb-bypass-part3]]):
```bash
adb shell am start -a android.intent.action.VIEW -d "three://part?three=UGFydFRocmVlQWN0aXZpdHk=&switch=b24=&header=X-Token" -n bounty.pay/.PartThreeActivity
```

> Reaches hash input.

### Step 3: Extract Preferences

**Context**: Dump shared prefs for token.

**Command** ([[commands/adb-extract-prefs]]):
```bash
adb shell cat ./data/data/bounty.pay/shared_prefs/user_created.xml
```

> XML with token 8e9998ee3137ca9ade8f372739f062c1.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Cloud Storage]] Data from Cloud Storage (adapted for local)

### Sub-Techniques

- None

## Commands Used

- [[commands/adb-bypass-part1]]
- [[commands/adb-bypass-part2]]
- [[commands/adb-bypass-part3]]
- [[commands/adb-extract-prefs]]

## Tools Used

- [[tools/MobSF]]
- [[tools/Genymotion]]
- [[tools/ADB]]

## Tags

- [[android-reverse]]
- [[apk-analysis]]
- [[intent-bypass]]
