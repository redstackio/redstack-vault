---
url: null
tags:
  - poc
  - malicious-app
  - intent
type: tool
verified: false
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:42.783Z'
id: a348785c-35a8-4e61-9b09-123757557d0b
validated: true
submitted: true
---
# setresultcontactphotocrop

**Status**: Unverified

## Overview

Proof-of-concept Android app designed to exploit intent vulnerabilities in apps like Nextcloud by responding to GET_CONTENT intents with URIs to private files, enabling arbitrary file reads.

## Description

This custom tool is a malicious APK that registers an EvilActivity for android.intent.action.GET_CONTENT. When selected, it returns a hardcoded file URI to sensitive Nextcloud data, causing the target app to upload it. Used in offensive security testing for Android intent abuse.

## Features

- Intent filter for '*/*' mime types with DEFAULT and OPENABLE categories
- Automatic URI setting in onCreate without UI interaction
- Targets specific private paths like shared_prefs and databases
- Finishes activity post-response for seamless exploitation

## Installation

### Requirements

- Android Studio or build tools
- Android device/emulator for testing
- Basic Java knowledge for customization

### Install Commands

```bash
# Build APK
./gradlew assembleDebug

# Install on device
adb install app/build/outputs/apk/debug/app-debug.apk
```

## Basic Usage

```bash
# Launch via intent to test (optional)
adb shell am start -n com.example.setresultcontactphotocrop/.EvilActivity
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Customizable URI in code |
| Logcat | Monitor with `adb logcat | grep heen` for "EvilActivity started!" |

## Examples

### Example 1: Basic Installation

Install the APK on the target device to make it available in choosers.

### Example 2: Advanced Usage

Modify PRIVATE_URI in EvilActivity.java to target other files like /data/data/com.nextcloud.client/databases/files.db, rebuild, and reinstall.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Data from Local System]] Data from Local System
- [[File and Directory Discovery]] File and Directory Discovery

### Tactics

- [[Collection]] Collection
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of app with suspicious intent filters in manifest
- Log entries for EvilActivity launches
- Anomalous file uploads from private URIs in app logs

## Related Procedures


## Related Tools

- Android Debug Bridge (adb)
- APKTool for manifest analysis

## References

- HackerOne Report #1142918
- Android Developer Docs on Intents
