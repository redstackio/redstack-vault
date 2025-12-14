---
url: ''
tags:
  - agent
  - android
type: tool
verified: false
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:39.839Z'
id: 7b3e71ab-6dab-4122-a7d6-fdf5b98b1317
validated: true
submitted: true
---
# Drozer-Agent

**Status**: Unverified

## Overview

Drozer Agent is the on-device APK component of the Drozer framework, facilitating console interactions and running an embedded server to proxy commands for Android app security assessments.

## Description

Installed on the target Android device, the agent enables the Drozer console to send intents and execute modules remotely. It supports embedded mode for direct device communication, essential for testing without external proxies, and is used in scenarios like invoking exported activities for vulnerability exploitation.

## Features

- Feature 1: Embedded server for local console connections
- Feature 2: Proxying of assessment commands to app components
- Feature 3: Stealth mode to minimize detection during testing

## Installation

### Requirements

- Android device/emulator (API 9+)
- ADB for APK deployment

### Install Commands

```bash
# Install via ADB
adb install drozer-agent.apk
# Start embedded server in app settings
```

## Basic Usage

Launch the agent app and enable embedded server mode.

### Common Options

| Option | Description |
|--------|-------------|
| Embedded Server | Start server on port 31415 |
| Proxy Mode | Forward traffic for remote testing |

## Examples

### Example 1: Basic Usage

Install APK, open app, start embedded server.

### Example 2: Advanced Usage

Use with console: Connect after server start for intent testing.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]] Valid Accounts

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- APK signature matching Drozer
- Running service on port 31415
- Anomalous app permissions

## Related Procedures

- [[procedures/Configure-Passcode-and-Install-Drozer]]

## Related Tools

- [[tools/Drozer]]

## References

- Included with Drozer distribution
