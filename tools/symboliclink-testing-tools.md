---
url: 'https://github.com/googleprojectzero/symboliclink-testing-tools'
tags:
  - symlink
  - testing
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:51.570Z'
id: 61451661-c6e2-48d8-a382-aebbd9beba54
validated: true
submitted: true
---
# symboliclink-testing-tools

**Status**: Unverified

## Overview

A set of tools for testing and creating symbolic links and hardlinks on Windows, useful for exploiting symlink vulnerabilities in privilege escalation scenarios.

## Description

Developed by James Forshaw of Google Project Zero, this repository provides executables like CreateSymlink.exe to create symlinks, aiding in attacks where services follow links without validation, such as in file copy operations by privileged processes.

## Features

- Feature 1: Create symbolic links between paths
- Feature 2: Test hardlink and symlink behaviors on NTFS
- Feature 3: Support for various Windows versions

## Installation

### Requirements

- Git
- Windows with NTFS filesystem

### Install Commands

```cmd
git clone https://github.com/googleprojectzero/symboliclink-testing-tools.git
cd symboliclink-testing-tools
# Compile if needed, or use pre-built executables
```

## Basic Usage

```cmd
CreateSymlink.exe <source> <target>
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help |

## Examples

### Example 1: Basic Usage

```cmd
CreateSymlink.exe "link_path" "target_path"
```

### Example 2: Advanced Usage

Use in scripts for automated testing.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Tactics

- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor executions of unknown exes in temp dirs
- Sysmon logs for process creation with symlink args

## Related Procedures

- [[procedures/Create-Symlink-in-Quarantine-for-Overwrite]]

## Related Tools

- [[tools/requests-python-library]]

## References

- https://github.com/googleprojectzero/symboliclink-testing-tools
