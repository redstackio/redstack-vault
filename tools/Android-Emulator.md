---
url: 'https://developer.android.com/studio/run/emulator'
tags:
  - android
  - emulation
  - testing
type: tool
platforms:
  - Android
description: >-
  Simulates Android devices for app testing and vulnerability demonstration
  without physical hardware.
id: 545f1378-453e-4a25-9539-4d6ed4104bd6
created_at: '2025-12-14T17:24:42.745Z'
updated_at: '2025-12-14T17:24:42.745Z'
verified: false
validated: true
submitted: true
---
# Android-Emulator

**Status**: Unverified

## Overview

The Android Emulator is a core component of Android Studio used to simulate Android devices for development, testing, and security research, including vulnerability PoCs like app interception demos.

## Description

It provides a virtual mobile device environment supporting various API levels, hardware configurations, and features like GPS simulation. In offensive security, it's used to safely demonstrate exploits, such as intercepting broadcasts, without risking real devices.

## Features

- Feature 1: GPS and sensor simulation for location-based testing
- Feature 2: ADB integration for app installation and log monitoring
- Feature 3: Snapshot and state management for repeatable tests

## Installation

### Requirements

- Java JDK 8 or higher
- Sufficient RAM (4GB+ recommended)

### Install Commands

```bash
# Install Android Studio which includes the emulator
# Download from https://developer.android.com/studio
# After installation, use SDK Manager to install emulator images
```

## Basic Usage

```bash
emulator -avd Pixel_3_API_28
```

### Common Options

| Option | Description |
|--------|-------------|
| `-avd` | Specify AVD name |
| `-writable-system` | Allow system modifications |
| `-no-snapshot` | Disable snapshots for clean runs |

## Examples

### Example 1: Basic Usage

```bash
emulator -avd Test_Device
```

Launches the specified virtual device.

### Example 2: Advanced Usage

```bash
emulator -avd Pixel_3 -gpu host -no-audio -no-window
```

Runs headless with GPU acceleration for faster performance.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1429]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Running processes like 'qemu-system' or 'emulator'
- Virtual device artifacts in /tmp or Android Studio directories
- Network traffic from emulated IPs

## Related Procedures


## Related Tools

- [[Android Studio]]
- [[ADB]]

## References

- Official documentation: https://developer.android.com/studio/run/emulator
- Related resources: Android Developer Guides
