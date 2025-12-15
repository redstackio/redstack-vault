---
id: tool-poc-apk-001
url: >-
  https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/000/034/535/7c98cb6ae4b03f29e9badfd1b0ae8b1ecd287f69/shopifyhack.apk
tags:
  - poc
  - android-exploit
type: tool
verified: false
platforms:
  - Android
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:10.977Z'
validated: true
submitted: true
---
# Custom-POC-APK-shopifyhack

**Status**: Unverified

## Overview

This custom proof-of-concept Android APK demonstrates interception of unprotected broadcasts from the Shopify app, logging sensitive API data for vulnerability validation.

## Description

The APK includes a HackBroadcastReceiver that registers for the 'com.shopify.service.requestComplete' action via manifest intent-filter, processing Intents to extract and log extras like headers and body without permissions, simulating a malicious sideloaded app.

## Features

- Feature 1: Background broadcast reception
- Feature 2: Automatic data extraction and logging
- Feature 3: No UI for stealth

## Installation

### Requirements

- Android device with sideloading enabled

### Install Commands

```bash
adb install shopifyhack.apk
```

## Basic Usage

Install and run in background; triggers on Shopify broadcasts.

### Common Options

N/A (APK-based, no CLI options)

## Examples

### Example 1: Basic Usage

Install via ADB as above; login to Shopify to trigger.

### Example 2: Advanced Usage

Modify source to exfiltrate data via network instead of logging.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1475]] Install Malicious Application
- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Unknown APK with broadcast receivers for Shopify actions
- Logs with 'SHOPIFYHACK' tag
- App analysis showing intent-filters

## Related Procedures

- [[procedures/Install-Malicious-POC-APK-for-Broadcast-Interception]]

## Related Tools

- [[tools/ADB-Android-Debug-Bridge]]

## References

- HackerOne Report: https://hackerone.com/reports/56002
