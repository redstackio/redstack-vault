---
url: 'https://developer.android.com/studio/command-line/adb'
tags:
  - android
  - debug
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:05.897Z'
id: d4c6faa6-ac06-463c-b319-90ca534dacb2
validated: true
submitted: true
---
# adb

**Status**: Unverified

## Overview

Android Debug Bridge for device interaction, APK install, and activity triggering.

## Description

Used to install APK and trigger deep links for reverse engineering in the mobile component.

## Features

- Feature 1: Shell access
- Feature 2: App management
- Feature 3: Logcat monitoring

## Installation

### Requirements

- Android SDK

### Install Commands

Part of Android Studio or platform-tools download.

## Basic Usage

```bash
adb devices
```

### Common Options

| Option | Description |
|--------|-------------|
| shell | Run shell command |
| install | Install APK |

## Examples

### Example 1: Basic Usage

```bash
adb install app.apk
```

### Example 2: Advanced Usage

```bash
adb shell am start -d deep://link package
```

## MITRE ATT&CK Mapping

### Techniques

- [[Unsecured Credentials]]

### Tactics

- [[Collection]]

## Detection

- USB debugging enabled
- adb process running

## Related Procedures

- [[procedures/Reverse-Engineer-Android-APK-for-API-Token]]

## Related Tools

- [[tools/scrcpy]]

## References

- Android developer docs
