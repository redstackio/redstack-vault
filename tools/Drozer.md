---
url: 'https://labs.mwrinfosecurity.com/tools/drozer/'
tags:
  - assessment
  - android
  - intent
type: tool
verified: false
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:39.852Z'
id: c2275e49-66fd-4977-bebd-8342bc64a064
validated: true
submitted: true
---
# Drozer

**Status**: Unverified

## Overview

Drozer is an Android application security assessment framework designed for dynamic analysis, allowing interaction with app components such as activities, services, and content providers via intents and agents.

## Description

Drozer enables security testers to explore Android apps for vulnerabilities like exported components, permission issues, and insecure data storage. It includes a console for running modules that simulate attacks, such as starting activities without authentication, making it ideal for mobile pentesting without root access.

## Features

- Feature 1: Intent-based component invocation for auth bypass testing
- Feature 2: Agent APK for on-device execution and embedded server
- Feature 3: Modules for app scanning, permission analysis, and exploitation

## Installation

### Requirements

- Python 2.7 or 3.x
- Android device/emulator with ADB

### Install Commands

```bash
# Install via pip
pip install drozer
# Or download console and agent from official site
```

## Basic Usage

```bash
drozer --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--debug` | Enable debug output |

## Examples

### Example 1: Basic Usage

```bash
drozer console connect
```

### Example 2: Advanced Usage

```bash
run app.activity.info --package com.nextcloud.client
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[T1417]] Access via Unauthorized Intent

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of drozer-agent.apk on device
- Network connections to port 31415
- Logs of unusual intent broadcasts

## Related Procedures

- [[procedures/Connect-to-Drozer-Console]]
- [[procedures/Exploit-Exported-FileDisplayActivity]]

## Related Tools

- [[tools/Drozer-Agent]]
- [[tools/Android-Studio-AVD]]

## References

- Official documentation: https://labs.mwrinfosecurity.com/tools/drozer/
- Related resources: Android security testing guides
