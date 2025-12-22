---
id: 149bcae3-53a9-4ab8-a1aa-fb49390f4c81
name: unix2dos
type: tool
verified: true
created_at: '2019-08-28T21:17:31.879182+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Unix
  - macOS
tags:
  - utility
  - file-conversion
  - line-endings
url: 'https://waterlan.home.xs4all.nl/dos2unix.html'
validated: true
---

# unix2dos

**Status**: Unverified

## Overview

unix2dos is a command-line utility for converting line endings in text files between Unix (LF), DOS/Windows (CRLF), and older Mac (CR) formats. In security testing, it's commonly used to prepare scripts, payloads, or configuration files for cross-platform compatibility, preventing execution errors due to mismatched line endings on target systems like Windows during red team operations or post-exploitation.

## Description

The dos2unix package provides four utilities: dos2unix, unix2dos, mac2unix, and unix2mac. These tools handle conversions between different text file formats. Windows and DOS use CRLF for line endings, Unix uses LF, and classic Mac used CR. While modern editors handle mixed formats, command-line tools and scripts often fail with incorrect endings. Developed in 1989, this is a lightweight, essential utility for file manipulation in penetration testing workflows, such as adapting bash scripts for PowerShell or ensuring batch files run correctly on Windows targets.

## Features

- Feature 1: In-place or new-file conversion to avoid overwriting originals
- Feature 2: Support for quiet mode and verbose output for scripting
- Feature 3: Handling of Mac CR format for legacy file compatibility
- Feature 4: Preservation of file timestamps with -k option

## Installation

### Requirements

- Standard Unix-like system with package manager (apt, yum, etc.)
- No additional dependencies

### Install Commands

```bash
# On Kali Linux (pre-installed in many distros)
sudo apt update && sudo apt install dos2unix

# On Ubuntu/Debian
sudo apt install dos2unix

# On CentOS/RHEL/Fedora
sudo yum install dos2unix  # or dnf install dos2unix

# On macOS (via Homebrew)
brew install dos2unix
```

## Basic Usage

```bash
unix2dos --help
```

Displays help for all options.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Verbose output showing conversions |
| -q, --quiet | Suppress output |
| -n, --newfile | Create new file instead of overwriting |
| -k, --keepdate | Keep original file date |
| -c, --convmode | Specify conversion mode (dos, mac, mixed)

## Examples

### Example 1: Basic Usage

```bash
unix2dos script.sh
```

Converts Unix script to DOS format in place.

### Example 2: Advanced Usage

```bash
unix2dos -n -v payload.txt payload_dos.txt
```

Creates a verbose new DOS-formatted file.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Windows Command Shell]] Windows Command Shell (for preparing payloads)
- [[Remote File Copy]] Ingress Tool Transfer (file format adaptation)

### Tactics

- [[Execution]] Execution
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: File system monitoring for sudden line ending changes in scripts (e.g., via auditd or Windows Event Logs)
- Detection method 2: Process monitoring for 'unix2dos' or 'dos2unix' executions in unusual contexts
- Detection method 3: Log analysis for file modifications in staging directories

## Related Procedures

No direct procedures linked yet. Commonly used in file preparation steps within post-exploitation procedures.

## Related Tools

- [[tools/dos2unix]] (same package)
- [[sed]] (alternative for simple conversions)

## References

- Official documentation: https://waterlan.home.xs4all.nl/dos2unix.html
- Kali Tools: https://www.kali.org/tools/dos2unix/
