---
id: tool-adb-001
url: 'https://developer.android.com/tools/adb'
tags:
  - debugging
  - android
type: tool
verified: false
platforms:
  - Android
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:10.979Z'
validated: true
submitted: true
---
# ADB-Android-Debug-Bridge

**Status**: Unverified

## Overview

ADB is a versatile command-line tool for communicating with Android devices, used here to view logs and verify data leakage from app broadcasts.

## Description

ADB enables interaction with Android devices over USB or TCP, including installing APKs, running shell commands, and capturing logs via logcat. In this context, it's essential for inspecting the output of the POC APK without rooting the device.

## Features

- Feature 1: Log capture with filtering (logcat)
- Feature 2: Package management and app installation
- Feature 3: Shell access for debugging

## Installation

### Requirements

- Java JDK
- Android SDK Platform-Tools

### Install Commands

```bash
# On Linux/macOS
sudo apt install android-tools-adb  # Ubuntu
# Or download from official site
```

## Basic Usage

```bash
adb --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-s` | Device serial selector |
| `-d` | Direct to USB device |

## Examples

### Example 1: Basic Usage

```bash
adb logcat
```

### Example 2: Advanced Usage

```bash
adb logcat -s TAG:V
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1475]] Install Malicious Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- USB debugging enabled on device
- ADB processes running on host machine
- Logcat commands in shell history

## Related Procedures

- [[procedures/View-Leaked-Data-in-Android-Logs]]

## Related Tools

- [[tools/Custom-POC-APK-shopifyhack]]

## References

- Official documentation: https://developer.android.com/tools/adb
