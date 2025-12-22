---
url: 'https://developer.android.com/tools/adb'
tags:
  - android
  - debug
  - mobile
type: tool
verified: false
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:42.031Z'
id: 07236199-5659-4a46-8805-643d514fb54e
validated: true
submitted: true
---
# Android Debug Bridge (ADB)

**Status**: Unverified

## Overview

ADB is a versatile command-line tool for communicating with Android devices, enabling shell access, file transfer, and app manipulation. Commonly used in security testing for intent sending, logcat monitoring, and APK analysis.

## Description

Part of the Android SDK, ADB facilitates debugging and automation on connected devices or emulators. In offensive security, it's key for exploiting Android components like intents and pulling sensitive files.

## Features

- Feature 1: Shell access for running commands on device
- Feature 2: File push/pull between host and device
- Feature 3: Activity manager (am) for intent simulation
- Feature 4: Package manager (pm) for app inspection

## Installation

### Requirements

- Java JDK
- Android SDK Platform-Tools

### Install Commands

```bash
# Download from https://developer.android.com/studio/releases/platform-tools
# Extract and add to PATH
mkdir -p ~/android-sdk/platform-tools
# Add to ~/.bashrc: export PATH=$PATH:~/android-sdk/platform-tools
```

## Basic Usage

```bash
adb devices
adb shell
```

### Common Options

| Option | Description |
|--------|-------------|
| `-s DEVICE_ID` | Target specific device |
| `--help` | Show help |
| `-d` | Use USB device |

## Examples

### Example 1: Basic Usage

```bash
adb shell ls /sdcard/
```

### Example 2: Advanced Usage

```bash
adb shell am start -n com.example/.Activity
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Command-Line Interface]] Command and Scripting Interpreter

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- USB debugging enabled in developer options
- adb processes on host or device logs
- Anomalous shell commands in logcat

## Related Procedures

- [[Identify Exported Activity in Android App]]
- [[Trigger File Copy via Exported Activity]]

## Related Tools

- [[Android Studio]]
- [[Frida]]

## References

- Official documentation: https://developer.android.com/tools/adb
- Related resources: Android Security Testing Guide
