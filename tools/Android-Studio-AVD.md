---
url: ''
tags:
  - emulator
  - android
type: tool
verified: false
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:39.836Z'
id: e4f9055d-c588-41dc-a7ed-14aca27b623c
validated: true
submitted: true
---
# Android-Studio-AVD

**Status**: Unverified

## Overview

Android Studio AVD (Android Virtual Device) is an emulator tool within Android Studio for simulating Android devices, used to test apps and vulnerabilities in a controlled, non-physical environment.

## Description

AVD allows creation of virtual devices with specific OS versions and configurations, such as non-rooted Android 9, ideal for reproducing mobile vulnerabilities like app component exposures without hardware. It integrates with ADB for app installation and debugging, supporting security assessments on emulated targets.

## Features

- Feature 1: Customizable OS versions and hardware profiles
- Feature 2: Non-rooted emulation for realistic testing
- Feature 3: Integration with ADB and Studio tools for deployment

## Installation

### Requirements

- Android Studio installed
- SDK components downloaded

### Install Commands

```bash
# AVD managed via Android Studio GUI
# Or via command line: avdmanager create avd -n test -k "system-images;android-28;google_apis;x86"
```

## Basic Usage

```bash
emulator -avd <avd_name>
```

### Common Options

| Option | Description |
|--------|-------------|
| `-avd` | Specify AVD name |
| `-no-snapshot` | Boot without snapshot |

## Examples

### Example 1: Basic Usage

Create and start AVD for Android 9: Use AVD Manager in Studio.

### Example 2: Advanced Usage

```bash
emulator -avd android9_nonroot @ -writable-system
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]] Valid Accounts

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Running emulator processes (qemu-system)
- Virtual device artifacts in host filesystem
- ADB connections to localhost ports

## Related Procedures

- [[procedures/Set-Up-Android-Emulation-and-Install-Nextcloud]]

## Related Tools

- [[tools/Drozer]]

## References

- Android Studio documentation
