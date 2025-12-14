---
id: tool-uuid-1
url: 'https://developer.android.com/studio'
tags:
  - development
  - mobile
type: tool
verified: false
platforms:
  - Android
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.300Z'
validated: true
submitted: true
---
# Android-SDK

**Status**: Unverified

## Overview

The Android Software Development Kit (SDK) is a collection of tools for building Android apps, used here to create malicious APKs for intent interception and device feature access like email.

## Description

Includes compilers, emulators, and APIs for app development. In offensive security, it's used to craft APKs that exploit mobile vulnerabilities, such as registering intent-filters for deeplink hijacking without verification.

## Features

- Feature 1: APK building and signing
- Feature 2: ADB for device installation and debugging
- Feature 3: Access to Android APIs for intents and email

## Installation

### Requirements

- Java JDK 8 or higher
- Sufficient disk space (~2GB)

### Install Commands

```bash
# Download from official site or use sdkmanager
sdkmanager --list
sdkmanager "platform-tools" "platforms;android-30"
```

## Basic Usage

```bash
# Build APK
gradlew assembleDebug
# Install
adb install app-debug.apk
```

### Common Options

| Option | Description |
|--------|-------------|
| adb devices | List connected devices |
| gradlew clean | Clean build |

## Examples

### Example 1: Basic Usage

```bash
adb install malicious.apk
```

### Example 2: Advanced Usage

```bash
adb shell am start -a android.intent.action.VIEW -d "https://qvay.app.link/test"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hijack Execution Flow]] Hijack Execution Flow
- [[T1407]] Structure Consumption

### Tactics

- [[Execution]] Execution
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of unsigned or sideloaded APKs
- ADB processes on device
- Anomalous app permissions

## Related Procedures

- [[procedures/Configure-Malicious-App-for-Deeplink-Interception]]

## Related Tools

- [[tools/Branch-io]]

## References

- Official documentation: https://developer.android.com/studio
