---
id: tool-ios-dataprotection
url: 'https://github.com/ciso/ios-dataprotection/'
tags:
  - ios
  - data-protection
  - forensic
type: tool
verified: false
platforms:
  - iOS
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:39.891Z'
validated: true
submitted: true
---
# iOS-Data-Protection-Tool

**Status**: Unverified

## Overview

The iOS Data Protection tool verifies the protection status of files on iOS devices, helping identify if app data is accessible when the device is locked.

## Description

This open-source tool analyzes iOS file system protection classes, such as NSFileProtectionComplete, to detect insecure storage. It's used in mobile security testing to probe app sandboxes without jailbreaking, focusing on vulnerabilities like exposed credentials.

## Features

- Feature 1: Query file protection attributes via USB
- Feature 2: Report accessibility in locked/unlocked states
- Feature 3: Support for app-specific sandbox inspection

## Installation

### Requirements

- macOS or Linux
- Xcode command-line tools
- USB connection to iOS device

### Install Commands

```bash
# Clone repository
git clone https://github.com/ciso/ios-dataprotection/
cd ios-dataprotection
make
```

## Basic Usage

```bash
./ios-dataprotection --device locked --path /path/to/file
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--device` | Specify device state (locked/unlocked) |
| `--path` | Target file or directory path |

## Examples

### Example 1: Basic Usage

```bash
./ios-dataprotection --device locked --path /var/mobile/Containers/Data/Application/[ID]/Library/Preferences/com.irccloud.IRCCloud.plist
```

### Example 2: Advanced Usage

```bash
./ios-dataprotection --verbose --app IRCCloud --check-protection
```

## Expected Output

Protection status report, e.g., 'File accessible: Yes (No protection class applied)'.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials In Files]] Credentials In Files

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- USB connection logs on device
- Anomalous file queries in system logs

## Related Procedures


## Related Tools

- [[tools/iExplorer]]

## References

- Official GitHub: https://github.com/ciso/ios-dataprotection/
