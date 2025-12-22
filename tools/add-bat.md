---
id: h8i9j0k1-l2m3-4567-hijk-890123456789
url: null
tags:
  - batch
  - registry
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:29:44.549Z'
validated: true
submitted: true
---
# add-bat

**Status**: Unverified

## Overview

A custom batch script to automate tampering of HKCU registry keys for multiple browser protocol handlers in the VeraCrypt UAC bypass attack.

## Description

add.bat contains reg add commands for protocols like HTTP, HTTPS, ChromeHTML, FirefoxURL, IE.HTTP, etc., setting their default values to invoke malstaller.bat with the URL parameter. It requires manual customization of the username (e.g., 'Temp') and paths before execution as a limited user.

## Features

- Automates multiple registry modifications
- Targets common browser protocols
- Includes %1 parameter passing for URL

## Installation

### Requirements

- Windows with reg.exe
- Write access to desktop

### Install Commands

```batch
# Create manually or via echo > add.bat
# Then edit with notepad to add reg commands
```

## Basic Usage

```batch
add.bat
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Batch has no flags; edit content |

## Examples

### Example 1: Basic Usage

```batch
# After editing, run in cmd
add.bat
```

### Example 2: Advanced Usage

Customize for more protocols by adding lines in the script.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Bypass User Account Control]]

### Tactics

- [[Privilege Escalation]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor reg add executions targeting HKCU\Software\Classes
- Scan for batch files with reg commands in user dirs
- Audit registry changes post-UAC events

## Related Procedures

- [[procedures/Tamper-HKCU-Registry-Keys-for-Protocol-Hijacking]]

## Related Tools

- [[tools/malstaller-bat]]

## References

- VeraCrypt source: WinMain.cpp
