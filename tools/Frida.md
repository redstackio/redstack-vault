---
url: 'https://frida.re/'
tags:
  - instrumentation
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:57.864Z'
id: b2186ecf-495c-4225-b681-d4869ebecaad
validated: true
submitted: true
---
# Frida

**Status**: Unverified

## Overview

Dynamic toolkit for app hooking and tracing.

## Description

Hooks methods like DataSnapshot.getValue() to log secrets in Android apps.

## Features

- Feature 1: JS scripting
- Feature 2: USB/ remote attach
- Feature 3: Native and Java support

## Installation

### Requirements

- Python/pip

### Install Commands

```bash
pip install frida-tools
```

## Basic Usage

```bash
frida --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -U | USB |
| -l | Load script |

## Examples

### Example 1: Basic Usage

Attach to app.

### Example 2: Advanced Usage

Hook specific class.

## MITRE ATT&CK Mapping

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Tactics

- [[Discovery]] Discovery

## Detection

Frida server processes.

## Related Procedures

- [[procedures/Extract-API-Token-from-APK-Using-ADB-and-Frida]]

## Related Tools

- [[tools/ADB]]

## References

- frida.re docs
