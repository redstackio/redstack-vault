---
id: h8i9j0k1-l2m3-4567-hijk-890123456789
url: 'https://www.bignox.com/'
tags:
  - emulator
type: tool
verified: false
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:42.905Z'
validated: true
submitted: true
---
# Nox-App-Player

**Status**: Unverified

## Overview

Android emulator for running mobile apps in a virtual environment, ideal for security testing without physical devices.

## Description

NoxPlayer emulates Android OS, allowing installation of apps like Grab for traffic analysis. Used here to proxy app requests through tools like Charles for session extraction.

## Features

- Feature 1: Full Android OS emulation (up to Android 9)
- Feature 2: Root access and custom configurations
- Feature 3: Multi-instance support for parallel testing

## Installation

### Requirements

- Windows 7+ or macOS
- 2GB RAM minimum

### Install Commands

```bash
# Download from official site and run installer
# No CLI install; GUI-based
```

## Basic Usage

```bash
# Launch via GUI, install APK
nox -clone:instance1  # For multi-instance
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help |
| --root | Enable root mode |

## Examples

### Example 1: Basic Usage

Launch emulator and install Grab APK.

### Example 2: Advanced Usage

Configure proxy: In Nox settings, set WiFi proxy to host:8888.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Windows Command Shell]] Windows Command Shell (for setup)

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Emulator fingerprints in app logs
- Virtual device indicators in traffic

## Related Procedures


## Related Tools

- [[tools/Genymotion]]
- [[tools/Android-Studio-Emulator]]

## References

- Official documentation: https://www.bignox.com/support/
