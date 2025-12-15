---
id: tool-createsymlink
url: null
tags:
  - symlink
  - lpe
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.728Z'
validated: true
submitted: true
---
# CreateSymlink

**Status**: Unverified

## Overview

CreateSymlink is a utility tool for creating symbolic links (symlinks) on Windows systems, commonly used in security testing for symlink attack scenarios like privilege escalation by redirecting file operations.

## Description

This tool facilitates the creation of reparse points (symlinks or junctions) between files or directories, bypassing some native limitations of mklink which requires admin rights for certain operations. In offensive security, it's used to set up attacks where privileged processes write to user-controlled paths, such as temp directories, allowing overwrite of sensitive files. No official source provided; assumed custom or third-party binary for this context.

## Features

- Feature 1: Create file/directory symlinks without elevation in user-writable paths
- Feature 2: Support for absolute and relative paths
- Feature 3: Minimal logging for stealthy operations

## Installation

### Requirements

- Windows OS (Vista+ for symlink support)
- Run as local user (no admin needed for temp paths)

### Install Commands

```cmd
# Download or copy the executable to a working directory
# No formal installation; place in PATH or current dir
```

## Basic Usage

```cmd
CreateSymlink <source> <target>
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show usage help |
| -v, --verbose | Enable verbose output for debugging |

## Examples

### Example 1: Basic Usage

```cmd
CreateSymlink %temp%\log.txt C:\protected\file.sys
```

### Example 2: Advanced Usage

```cmd
CreateSymlink --verbose %temp%\Acronis\inst.log C:\Windows\System32\drivers\pci.sys
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Tactics

- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for mklink.exe or unknown binaries creating reparse points in temp dirs
- EDR alerts on symlink creation events (Event ID 4656)
- File system audits for unexpected links to system32

## Related Procedures

- [[procedures/Create-Symlink-to-Target-System-File]]

## Related Tools

- [[mklink]] (native Windows command)
- [[junction]] (Sysinternals tool)

## References

- Windows Symlink Documentation: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/mklink
