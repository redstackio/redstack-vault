---
url: 'https://developer.android.com/tools/adb'
tags:
  - android
  - debug
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: >-
  Android Debug Bridge for device interaction, including shell access and
  activity launches.
id: b97d0f2c-c4d6-43a1-8e24-03af60b63047
created_at: '2025-12-13T23:52:44.004Z'
updated_at: '2025-12-13T23:52:44.004Z'
verified: false
validated: true
submitted: true
---
# ADB

**Status**: Unverified

## Overview

ADB (Android Debug Bridge) is a versatile command-line tool for communicating with Android devices, essential for debugging, installing apps, and simulating attacks like intent-based exploits.

## Description

ADB enables shell access, file pushes, and activity starts via 'am' commands. In security testing, it's used to reproduce mobile vulnerabilities without root, such as launching exported activities with malicious intents.

## Features

- Feature 1: Interactive shell for running device commands
- Feature 2: Intent manipulation for app exploitation
- Feature 3: Logcat for monitoring app behavior

## Installation

### Requirements

- Java JDK
- Android SDK Platform-Tools

### Install Commands

```bash
# Download from Android SDK
sdkmanager "platform-tools"
# Or direct: wget https://dl.google.com/android/repository/platform-tools-latest-linux.zip
unzip platform-tools-latest-linux.zip
export PATH=$PATH:$PWD/platform-tools
```

## Basic Usage

```bash
adb --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help |
| -d | Device-specific |

## Examples

### Example 1: Basic Usage

```bash
adb devices
```

### Example 2: Advanced Usage

```bash
adb shell am start -n com.example/.Activity
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- USB debugging enabled in developer options
- adb processes on host or logcat entries on device

## Related Procedures

- [[procedures/Launch-ActionBarContentActivity-with-Malicious-HTML-via-ADB]]

## Related Tools

- [[Android Studio]]

## References

- Official documentation: https://developer.android.com/tools/adb
