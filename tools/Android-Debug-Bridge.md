---
url: 'https://developer.android.com/tools/adb'
tags:
  - adb
  - android
  - debugging
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:18.208Z'
description: >-
  Versatile command-line tool for communicating with Android devices, used for
  app debugging and testing intents.
id: f9237bd9-c96b-4800-891c-c371534b67c0
validated: true
submitted: true
---
# Android-Debug-Bridge

**Status**: Unverified

## Overview

ADB provides shell access, file transfer, and app installation on Android devices, essential for mobile security testing like intent exploitation.

## Description

Part of Android SDK, allows running shell commands, starting activities, and pulling files remotely.

## Features

- Feature 1: Device shell access
- Feature 2: APK management
- Feature 3: Intent launching

## Installation

### Requirements

- Android SDK Platform-Tools

### Install Commands

```bash
# Download platform-tools
sdkmanager "platform-tools"
# Or direct: wget https://dl.google.com/android/repository/platform-tools-latest-linux.zip
unzip platform-tools-latest-linux.zip
export PATH=$PATH:`pwd`/platform-tools
```

## Basic Usage

```bash
adb --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `devices` | List connected devices |
| `shell` | Run shell command |
| `pull` | Transfer file from device |

## Examples

### Example 1: Basic Usage

```bash
adb devices
```

### Example 2: Advanced Usage

```bash
adb shell am start -a VIEW -d uri package
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- ADB server processes
- USB debugging enabled on device

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Android-Studio]]
- [[Scrcpy]]

## References

- Official documentation: https://developer.android.com/tools/adb
