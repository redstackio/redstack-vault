---
url: ''
tags:
  - inspection
  - clipboard
type: tool
platforms:
  - macOS
description: Utility to inspect clipboard contents including custom UTIs on macOS
id: 6890f656-49a8-4dbb-9524-1772e8e9c6bb
created_at: '2025-12-13T23:55:38.168Z'
updated_at: '2025-12-13T23:55:38.168Z'
verified: false
validated: true
submitted: true
---
# Clipboard-Viewer

**Status**: Unverified

## Overview

Clipboard Viewer is a macOS tool for viewing and debugging clipboard data, useful for verifying custom UTI injections in security testing like XSS payloads.

## Description

It displays all clipboard types, including org.chromium.web-custom-data, allowing inspection of injected JSON for Slack exploits.

## Features

- Feature 1: View all clipboard formats and contents
- Feature 2: Decode custom UTIs like Chromium's
- Feature 3: Real-time monitoring during pastes

## Installation

### Requirements

- macOS

### Install Commands

```bash
# Built-in or via App Store; no install needed for basic use
```

## Basic Usage

```bash
open /Applications/Clipboard\ Viewer.app
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | GUI-based, no CLI options |

## Examples

### Example 1: Basic Usage

```bash
# Launch and select custom data type
```

### Example 2: Advanced Usage

Inspect after running Python script to confirm payload.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for clipboard apps
- Log clipboard access events

## Related Procedures


## Related Tools

- [[Related Tool: Python]]

## References

- Apple Developer Docs on NSPasteboard
