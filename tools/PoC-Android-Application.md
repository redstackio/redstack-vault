---
id: 4658cf9f-80d1-4159-8ec2-89833364ad01
name: PoC-Android-Application
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:21.721Z'
platforms:
  - Android
tags:
  - poc
  - interception
  - android
url: 'https://hackerone.com/reports/859469'
validated: true
submitted: true
---

# PoC-Android-Application

**Status**: Unverified

## Overview

Custom proof-of-concept Android app designed to intercept LINE Keep ZIP syncs and replace them with malicious files exploiting path traversal in ZIP extraction.

## Description

This tool is a pre-installed APK that runs in the background, monitoring for ZIP downloads from LINE's sync service. Upon detecting a target memo ZIP, it substitutes it with a crafted malicious archive containing traversal paths to overwrite app private files. It's used in offensive security testing for mobile app vulnerabilities, specifically targeting LINE Android's unsafe unzipping. Configuration involves granting STORAGE permission; no network access required beyond app syncs.

## Features

- Feature 1: Automatic ZIP interception during LINE sync
- Feature 2: Seamless replacement with pre-loaded malicious ZIP
- Feature 3: Logging of interception events for verification

## Installation

### Requirements

- Android device (API 21+)
- USB debugging enabled for sideloading

### Install Commands

```bash
# Transfer APK
adb install poc-app.apk

# Grant permission manually in settings
```

## Basic Usage

```bash
# Launch app
am start -n com.poc.interceptor/.MainActivity
```

### Common Options

| Option | Description |
|--------|-------------|
| STORAGE permission | Required for file access |
| Background service | Runs interception automatically |

## Examples

### Example 1: Basic Usage

Install and launch; it waits for sync triggers.

### Example 2: Advanced Usage

Configure malicious ZIP path in app settings before sync.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Unknown app with STORAGE permission
- Anomalous file modifications in LINE directories
- Background processes named 'interceptor' or similar

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- HackerOne Report #859469
- LINE Android Security Analysis
