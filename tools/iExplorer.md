---
id: tool-iexplorer
url: null
tags:
  - ios
  - file-extraction
  - forensic
type: tool
verified: false
platforms:
  - iOS
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:39.889Z'
validated: true
submitted: true
---
# iExplorer

**Status**: Unverified

## Overview

iExplorer is a GUI tool for browsing and extracting files from iOS devices, useful for accessing app data without jailbreaking, including on locked devices for unprotected files.

## Description

It provides a file manager-like interface to iOS backups and live devices via USB, allowing navigation to app sandboxes and export of plists or other files. The demo version suffices for testing single file extractions like session tokens.

## Features

- Feature 1: Live device file browsing
- Feature 2: Export/import files from app directories
- Feature 3: Plist viewing and editing

## Installation

### Requirements

- macOS or Windows
- iTunes (for device connection)
- USB cable

### Install Commands

Download from official site (macroplant.com/iexplorer) and install via installer.

```bash
# No CLI install; GUI app
```

## Basic Usage

Launch iExplorer, connect device, browse to file path, and export.

### Common Options

| Option | Description |
|--------|-------------|
| File > Export | Download selected file |
| View > Raw Data | Inspect file contents |

## Examples

### Example 1: Basic Usage

Connect locked device, navigate to IRCCloud app Preferences, select plist, export to desktop.

### Example 2: Advanced Usage

Browse sandbox, search for 'session', view plist XML inline.

## Expected Output

Exported file ready for parsing, e.g., plist XML with token.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials In Files]] Credentials In Files

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- iTunes USB trust prompts
- File access in device logs

## Related Procedures


## Related Tools

- [[tools/iOS-Data-Protection-Tool]]

## References

- Official site: macroplant.com/iexplorer
