---
id: fc2518d9-52e1-4ca3-a637-447509d55a88
name: dos2unix
type: tool
verified: true
created_at: '2019-08-28T21:17:23.753961+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
  - Windows (via WSL/Cygwin)
tags:
  - file-conversion
  - utilities
  - post-exploitation
url: 'https://waterlan.home.xs4all.nl/dos2unix.html'
validated: true
---

# dos2unix

**Status**: Unverified

## Overview

Dos2unix is a command-line utility package for converting line endings in text files between different operating system formats: Unix/Linux (LF), DOS/Windows (CRLF), and old Mac (CR). It includes binaries like dos2unix, unix2dos, mac2unix, and unix2mac. In security contexts, it's useful for ensuring script and payload compatibility across mixed environments, such as converting Windows-generated batch files for Linux targets during red team engagements or post-exploitation file manipulation.

## Description

The tool addresses line ending inconsistencies that can break scripts, configs, or logs when transferred between systems. For example, CRLF endings in Unix shells can cause "bad interpreter" errors. Developed in 1989, it's lightweight, fast, and handles binary detection to avoid corrupting non-text files. Common use cases in offensive security include preparing cross-platform payloads, normalizing exfiltrated data, or obfuscating file artifacts to evade detection.

## Features

- Convert DOS (CRLF) to Unix (LF) with dos2unix
- Convert Unix (LF) to DOS (CRLF) with unix2dos
- Convert Mac (CR) to Unix (LF) with mac2unix
- Convert Unix to Mac (CR) with unix2mac
- In-place conversion or new file output
- Preserve original timestamps and permissions
- ISO encoding support for international characters
- Quiet mode and verbose reporting
- Automatic binary file skipping

## Installation

### Requirements

- Standard Unix-like environment (no special dependencies)
- For Windows: Use WSL, Cygwin, or Git Bash

### Install Commands

```bash
# Kali Linux (pre-installed in many distros)
sudo apt update && sudo apt install dos2unix

# Ubuntu/Debian
sudo apt install dos2unix

# macOS (via Homebrew)
brew install dos2unix

# From source (optional)
wget https://waterlan.home.xs4all.nl/dos2unix/dos2unix-7.5.2.tar.gz
tar -xzf dos2unix-7.5.2.tar.gz
cd dos2unix-7.5.2
./configure && make && sudo make install
```

## Basic Usage

```bash
dos2unix --help
```

Displays help for all utilities in the package.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --version | Display version information |
| -q | Quiet mode: suppress conversion messages |
| -k, --keepdate | Keep file modification time |
| -n IN OUT | Convert to new file instead of in-place |
| -c, --convmode | Set conversion mode (e.g., cr, mac) |

## Examples

### Example 1: Basic Usage

```bash
dos2unix payload.sh
```

Converts `payload.sh` from DOS to Unix format in place.

### Example 2: Advanced Usage

```bash
find . -name "*.txt" -exec unix2dos {} \;
```

Batch converts all .txt files in the current directory to DOS format (combine with [[commands/dos2unix-basic-conversion]] or [[commands/unix2dos-basic-conversion]] for targeted use).

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]] Obfuscated Files or Information (for normalizing file formats to evade script execution detection)
- [[NTFS File Attributes]] Hidden Files and Directories (indirectly, via file manipulation in post-exploitation)

### Tactics

- [[Execution]] Execution (preparing cross-platform executables/scripts)
- [[Defense Evasion]] Defense Evasion (file format adjustments to blend in)

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for `dos2unix` or `unix2dos` executions in unusual contexts (e.g., during payload deployment)
- File integrity checks showing sudden line ending changes in scripts/configs
- Audit logs of file modifications in staging directories
- YARA rules for the binary signatures if custom-compiled

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[sed]] (alternative for simple line ending replacements)
- [[awk]] (scripting-based conversions)

## References

- Official documentation: https://waterlan.home.xs4all.nl/dos2unix.html
- Man page: `man dos2unix`
- Kali Tools: https://www.kali.org/tools/dos2unix/
