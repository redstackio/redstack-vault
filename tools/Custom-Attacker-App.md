---
id: tool-uuid-001
url: 'https://hackerone.com/reports/1455987'
tags:
  - exploit
  - android
  - intent
type: tool
verified: false
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.342Z'
validated: true
submitted: true
---
# Custom-Attacker-App

**Status**: Unverified

## Overview

A malicious Android APK crafted to exploit the exported SMFeedbackActivity in the Exness Social Trading app by injecting Intent Extras for universal XSS in WebView.

## Description

This tool automates the launch of intents targeting com.exness.investments.SMFeedbackActivity, setting extras like smSPageURL and smSPageHTML to deliver payloads. It includes delays (8s and 20s) for sequencing and uses standard Android APIs for cross-app interaction, enabling cookie theft without root access.

## Features

- Feature 1: Automated intent crafting and launching
- Feature 2: Payload injection for HTML/JS via extras
- Feature 3: Built-in delays for exploit chaining

## Installation

### Requirements

- Android development environment (Android Studio)
- Knowledge of Intent and PackageManager APIs

### Install Commands

No standard install; build from source or use provided APK:

```bash
# Via ADB
adb install malicious-attacker.apk
```

## Basic Usage

```bash
# Launch via ADB or directly on device
adb shell am start -n com.attacker/.MainActivity
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | App runs autonomously upon launch |

## Examples

### Example 1: Basic Usage

Install and launch the app on device; it auto-triggers exploits.

### Example 2: Advanced Usage

Modify source to adjust payloads/delays, rebuild, and reinstall.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript
- [[Remote File Copy]] Ingress Tool Transfer

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Logcat for intent launches to SMFeedbackActivity
- Detection method 2: Anomalous WebView loads with external extras

## Related Procedures


## Related Tools


## References

- HackerOne Report #1455987
- Android Intent Documentation
