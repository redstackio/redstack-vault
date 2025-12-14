---
url: 'https://www.ashampoo.com/en-us/snap'
tags:
  - screenshot
  - capture
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.943Z'
id: d58de27d-8089-4575-82b4-aa10ae3c9180
validated: true
submitted: true
---
# Ashampoo-Snap

**Status**: Unverified

## Overview

Ashampoo Snap is a screen capture and annotation tool used in security testing to document proof-of-concept exploits, such as capturing XSS alert dialogs or vulnerability demonstrations.

## Description

It allows users to take screenshots, record videos, and add annotations, making it ideal for creating visual evidence in bug reports or PoCs. In this context, it's used to capture the JavaScript alert triggered by the XSS in IE11.

## Features

- Feature 1: Full-screen or selective area captures
- Feature 2: Video recording for dynamic demos
- Feature 3: Built-in editor for annotations and highlights

## Installation

### Requirements

- Windows OS
- .NET Framework

### Install Commands

Download and install via GUI; no CLI.

```bash
# Run the installer executable
# ashampoo_snap_setup.exe
```

## Basic Usage

```bash
# Launch the application
"C:\Program Files\Ashampoo\Ashampoo Snap 12\Snap.exe"
```

### Common Options

| Option | Description |
|--------|-------------|
| Capture mode | Select area, window, or full screen |
| Annotate | Add text, arrows, or highlights |

## Examples

### Example 1: Basic Usage

Launch and press Print Screen to capture the current window, then save as PNG.

### Example 2: Advanced Usage

Record a video of the XSS trigger: Select video mode, start recording during field edit, stop after alert appears.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process name 'Snap.exe' running during testing
- Temporary capture files in user directories

## Related Procedures


## Related Tools

- [[tools/Internet-Explorer-11]]

## References

- Official documentation: ashampoo.com
- Related resources: Screen capture best practices in pentesting
