---
url: 'https://github.com/googleprojectzero/symboliclink-testing-tools/'
tags:
  - symlink
  - ntfs
  - bypass
type: tool
platforms:
  - Windows
description: >-
  Utility for creating symbolic links using NTFS reparse points and
  object-directory symlinks without administrator privileges.
id: 2a53933b-f663-451a-8afb-5c52d3673df1
created_at: '2025-12-14T17:26:48.988Z'
updated_at: '2025-12-14T17:26:48.988Z'
verified: false
validated: true
submitted: true
---
# Create Symlink

**Status**: Unverified

## Overview

CreateSymlink.exe is a testing tool from Project Zero for creating advanced symlinks on NTFS filesystems. It combines reparse points and object-directory symlinks to enable redirection of file I/O from privileged processes to arbitrary locations, useful for privilege escalation and file hijacking in local attacks.

## Description

The tool automates the creation of a reparse point on a user-writable directory (e.g., pointing to `\RPC Control\`) and an object-directory symlink within it to the target file. This allows non-admin users to trick SYSTEM processes into writing to protected files. Binaries are available in GitHub releases; no compilation needed.

## Features

- Feature 1: Bypasses SeCreateSymbolicLinkPrivilege requirement
- Feature 2: Supports file and directory redirection
- Feature 3: Works on modern Windows (10/11)

## Installation

### Requirements

- Windows with NTFS
- Download from GitHub releases

### Install Commands

```cmd
# Download and extract to a folder, e.g., C:\tools\
# No formal install; run executable directly
```

## Basic Usage

```cmd
CreateSymlink.exe <source> <target>
```

### Common Options

| Option | Description |
|--------|-------------|
| None | Simple CLI; source and target paths only |

## Examples

### Example 1: Basic Usage

```cmd
CreateSymlink.exe C:\test\logs\service_log.txt C:\target.txt
```

### Example 2: Advanced Usage

```cmd
CreateSymlink.exe C:\logs\output.log C:\Windows\System32\drivers\etc\hosts
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Windows Service]] Create or Modify System Process (Configuration File)

### Tactics

- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- Reparse point creation events (ETW or Sysmon ID 1)
- Unexpected symlinks in object manager (`objdir` queries)

## Related Procedures

- [[procedures/create-symlinks-to-redirect-steam-log-writes-to-arbitrary-files]]

## Related Tools

- [[tools/regedit]]

## References

- GitHub: https://github.com/googleprojectzero/symboliclink-testing-tools/
