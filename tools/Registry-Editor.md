---
id: t1b2c3d4-e5f6-7890-abcd-ef1234567898
name: Registry-Editor
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.820Z'
platforms:
  - Windows
tags:
  - registry
url: 'https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-editor'
validated: true
submitted: true
---

# Registry-Editor

**Status**: Unverified

## Overview

Registry Editor (regedit.exe) is a built-in Windows tool for viewing and editing the system registry, commonly used in security testing to tamper with keys like HKCU protocol handlers for privilege escalation attacks.

## Description

Regedit provides a graphical interface to navigate registry hives (HKCU, HKLM, etc.) and modify values, enabling attackers to redirect protocol handlers in scenarios like Malstaller. It supports export/import of .reg files for persistence and is accessible to low-priv users for HKCU.

## Features

- Feature 1: GUI navigation and search for keys/values
- Feature 2: Direct editing of string, DWORD, and binary data
- Feature 3: Backup/restore functionality via export

## Installation

### Requirements

- Windows OS (pre-installed)

### Install Commands

```cmd
# Already installed; launch via
regedit
```

## Basic Usage

```cmd
regedit
```

### Common Options

| Option | Description |
|--------|-------------|
| /e filename | Export registry to file |
| /s | Silent mode |

## Examples

### Example 1: Basic Usage

```cmd
regedit
```

> Opens GUI; navigate to HKCU\Software\Classes\https.

### Example 2: Advanced Usage

```cmd
regedit /e backup.reg HKEY_CURRENT_USER\Software\Classes
```

> Exports HKCU classes for backup before tampering.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Modify Registry]] Modify Registry

### Tactics

- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for regedit.exe executions (Sysmon Event ID 1)
- Audit registry changes via Object Access auditing

## Related Procedures

- [[procedures/Tamper-with-HKCU-Protocol-Handler-Registry-Keys]]

## Related Tools

- [[tools/PowerShell]]

## References

- Official documentation: https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-editor
