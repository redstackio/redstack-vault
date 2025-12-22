---
url: ''
tags:
  - registry
  - windows
type: tool
platforms:
  - Windows
description: >-
  Built-in Windows Registry Editor for viewing and modifying registry keys and
  values, including binary data edits.
id: 8c5988b8-e48c-480c-918b-a386b0359df7
created_at: '2025-12-14T17:26:48.990Z'
updated_at: '2025-12-14T17:26:48.990Z'
verified: false
validated: true
submitted: true
---
# regedit

**Status**: Verified

## Overview

Regedit is the graphical Windows Registry Editor, used for inspecting, creating, and modifying registry entries. In security testing, it is essential for manipulating application configurations like the Steam InstallPath to test for traversal and injection vulnerabilities.

## Description

Regedit allows navigation through the registry hive, editing string, DWORD, and binary values. For this attack, its binary data modification feature enables inserting non-ASCII characters like CRLF into values without triggering string validation. It runs as the current user, leveraging permissions on modifiable keys.

## Features

- Feature 1: Hierarchical tree view of registry keys
- Feature 2: Edit binary data with hex viewer
- Feature 3: Export/import registry branches

## Installation

### Requirements

- Windows OS (built-in)

### Install Commands

```cmd
# No installation needed; launch via Run dialog or Start menu
regedit
```

## Basic Usage

```cmd
regedit
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Graphical tool; use context menu for Modify Binary Data |

## Examples

### Example 1: Basic Usage

```cmd
# Launch and navigate to key
regedit > HKLM\Software\wow6432node\valve\steam
```

### Example 2: Advanced Usage

```cmd
# Edit binary: Right-click value > Modify Binary Data > Insert 0D 0A for CRLF
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Modify Registry]] Modify Registry

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Process creation of regedit.exe with registry write events (Event ID 4657)
- Unauthorized changes to application keys

## Related Procedures

- [[procedures/setup-test-environment-for-steam-registry-path-traversal]]
- [[procedures/inject-crlf-sequences-into-installpath-registry-value]]

## Related Tools

- [[tools/create-symlink]]

## References

- Microsoft Docs: Registry Editor
