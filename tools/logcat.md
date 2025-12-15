---
id: tool-uuid-001
url: 'https://developer.android.com/tools/logcat'
tags:
  - android
  - debugging
  - logging
type: tool
verified: false
platforms:
  - Android
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:35.235Z'
validated: true
submitted: true
---
# logcat

**Status**: Unverified

## Overview

Logcat is a command-line tool included in the Android SDK for capturing, viewing, and filtering system and application logs from Android devices. It is commonly used in security testing to monitor app behavior, detect errors, and identify leaked sensitive information like OAuth tokens in verbose outputs.

## Description

Logcat reads from the Android device's log buffer, displaying messages from the kernel, system services, and apps. In offensive security, it helps extract credentials or tokens logged insecurely by vulnerable apps, such as during OAuth flows. It supports filtering by tags, priorities, and processes, making it essential for debugging and exploitation on rooted or ADB-enabled devices.

## Features

- Feature 1: Real-time log streaming with ADB integration
- Feature 2: Filtering by log level (verbose, debug, info, warn, error) and tags
- Feature 3: Output redirection to files for analysis

## Installation

### Requirements

- Android SDK Platform-Tools installed
- ADB enabled on the device

### Install Commands

```bash
# Download via Android Studio SDK Manager or standalone
sdkmanager "platform-tools"
```

## Basic Usage

```bash
adb logcat
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output with timestamps |
| `-d` | Dump logs and exit |
| `-f file` | Write to file instead of stdout |

## Examples

### Example 1: Basic Usage

```bash
adb logcat
```

Streams all logs from the connected device.

### Example 2: Advanced Usage

```bash
adb logcat *:V Twitter:D | grep oauth
```

Filters verbose logs from Twitter tag for OAuth mentions.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- ADB connections from unknown hosts
- Unusual logcat queries in device forensics
- Elevated USB debugging activity

## Related Procedures

- [[procedures/Extract-Leaked-OAuth-Token-from-Logcat]]

## Related Tools

- [[ADB]]

## References

- Official documentation: https://developer.android.com/tools/logcat
