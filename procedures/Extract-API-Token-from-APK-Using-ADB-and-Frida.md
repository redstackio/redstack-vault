---
tags:
  - frida-hooking
  - token-extraction
  - deep-links
type: procedure
tools:
  - '[[tools/ADB]]'
  - '[[tools/Frida]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/adb-shell-am-start-one]]'
  - '[[commands/adb-shell-am-start-two]]'
  - '[[commands/adb-shell-am-start-three]]'
  - '[[commands/frida-attach-script]]'
  - '[[commands/adb-shell-input-text]]'
  - '[[commands/adb-logcat]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:32:57.977Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 9f312d35-444a-41ec-a34a-0b5efe10b423
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Extract API Token from APK Using ADB and Frida

## Summary

Use deep links to navigate APK activities and hook Firebase calls with Frida to extract API token.

## Description

Launch activities with ADB deep links (one://, two://, three:// with base64 params), hook DataSnapshot.getValue() in bounty_app.js to log 'Token', input extracted token, monitor logs for http://api.bountypay.h1ctf.com and 8e9998ee3137ca9ade8f372739f062c1.

## Requirements

1. Installed APK on rooted device
2. Frida server on device
3. Custom JS script for hooking

## Defense

Defensive measures: Use secure storage for tokens (e.g., Keystore), avoid Firebase leaks; Detection: Monitor ADB/Frida connections on devices.

## Objectives

1. Navigate app stages
2. Hook and extract token
3. Expected outcome: API details

## Instructions

### Step 1: Launch First Activity

**Context**: Start progression.

**Command** ([[commands/adb-shell-am-start-one]]):
```bash
adb shell am start -a "android.intent.action.VIEW" -d "one://part/?start=PartTwoActivity"
```

> Expected output: PartTwoActivity launched.

### Step 2: Launch Second Activity

**Context**: Reveal inputs.

**Command** ([[commands/adb-shell-am-start-two]]):
```bash
adb shell am start -a "android.intent.action.VIEW" -d "two://part/?two=light\\&switch=on"
```

> Expected output: Interface updated.

### Step 3: Launch Third and Hook

**Context**: Access final stage and extract.

**Command** ([[commands/adb-shell-am-start-three]]):
```bash
adb shell am start -a "android.intent.action.VIEW" -d "three://part/?three=UGFydFRocmVlQWN0aXZpdHk=\\&switch=b24=\\&header=X-Token"
```
**Command** ([[commands/frida-attach-script]]):
```bash
frida -U -l bounty_app.js --no-pause -f bounty.pay
```
**Command** ([[commands/adb-shell-input-text]]):
```bash
adb shell input text 8e9998ee3137ca9ade8f372739f062c1
```
**Command** ([[commands/adb-logcat]]):
```bash
adb logcat
```

> Expected output: Logs with token and host.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Credentials In Files]] Credentials In Files

### Sub-Techniques

- None

## Commands Used

- [[commands/adb-shell-am-start-one]]
- [[commands/adb-shell-am-start-two]]
- [[commands/adb-shell-am-start-three]]
- [[commands/frida-attach-script]]
- [[commands/adb-shell-input-text]]
- [[commands/adb-logcat]]

## Tools Used

- [[tools/ADB]]
- [[tools/Frida]]

## Tags

- frida-hooking
- token-extraction
- deep-links
