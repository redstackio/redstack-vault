---
id: b7e36369-fc1f-4abf-acd2-6507f2332ea3
type: tool
verified: true
description: >-
  A utility package for converting line endings in text files between UNIX (LF),
  DOS (CRLF), and Mac (CR) formats, useful for cross-platform compatibility in
  security testing.
url: 'https://waterlan.home.xs4all.nl/dos2unix.html'
created_at: '2019-08-28T21:17:36.969184+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
  - Windows (with WSL)
tags:
  - file-conversion
  - line-endings
  - utility
  - cross-platform
commands:
  - '[[commands/dos2unix-convert-file]]'
  - '[[commands/mac2unix-convert-file]]'
  - '[[commands/unix2dos-convert-file]]'
validated: true
---

# mac2unix

**Status**: Unverified

## Overview

mac2unix is part of a classic utility package that includes dos2unix, unix2dos, mac2unix, and unix2mac. These tools convert line endings in text files between different operating system formats: UNIX/Linux (LF), DOS/Windows (CRLF), and classic Mac (CR). In security contexts, it's commonly used to ensure scripts, payloads, or configuration files are compatible across platforms during red team operations, avoiding execution errors due to mismatched line endings.

## Description

Text files originated with varying line ending conventions: DOS and Windows use carriage return (CR) followed by line feed (LF), older Macs used only CR, and UNIX/Linux use only LF. While modern editors handle these transparently, command-line tools and scripts can fail if line endings are incompatible. This package, originally developed in 1989, provides reliable conversion without altering file content otherwise. It's lightweight, dependency-free, and ideal for preparing files in penetration testing environments, such as converting Windows batch files for Linux execution or vice versa.

## Features

- **dos2unix**: Converts DOS (CRLF) to UNIX (LF).
- **unix2dos**: Converts UNIX (LF) to DOS (CRLF).
- **mac2unix**: Converts Mac (CR) to UNIX (LF).
- **unix2mac**: Converts UNIX (LF) to Mac (CR).
- Supports in-place conversion or new file creation.
- Preserves original timestamps and handles binary detection to avoid corrupting non-text files.
- Quiet mode for scripting and batch operations.

## Installation

### Requirements

- Standard build tools (gcc, make) for compilation from source.
- No special dependencies.

### Install Commands

```bash
# On Kali Linux (pre-installed in many distros, but to ensure latest):
sudo apt update && sudo apt install dos2unix

# On Ubuntu:
sudo apt update && sudo apt install dos2unix

# On macOS (via Homebrew):
brew install dos2unix

# From source (all platforms):
wget https://waterlan.home.xs4all.nl/dos2unix/dos2unix-7.5.2.tar.gz
tar -xzf dos2unix-7.5.2.tar.gz
cd dos2unix-7.5.2
./configure
make
sudo make install
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
| -V, --version | Display version information |
| -q, --quiet | Suppress conversion messages |
| -n, --newfile | Write to new file instead of overwriting |
| -k, --keepdate | Preserve modification date |

## Examples

### Example 1: Basic Usage

```bash
dos2unix payload.txt
```

Converts 'payload.txt' from DOS to UNIX format.

### Example 2: Advanced Usage

```bash
find . -name "*.bat" -exec dos2unix {} \;
```

Batch converts all .bat files in the current directory to UNIX format.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Windows Command Shell]] Windows Command Shell (for preparing Windows-compatible payloads)
- [[Unix Shell]] Unix Shell (for UNIX script adaptation)

### Tactics

- [[Execution]] Execution (enabling cross-platform command execution)

## Detection

- File modification timestamps changing without content updates.
- Process monitoring for dos2unix/unix2dos executions in security tools.
- Log analysis for batch file conversions in staging directories.

## Related Procedures

No direct procedures linked yet; useful in file transfer or payload preparation procedures.

## Related Tools

- [[tools/sed]] (for text manipulation)
- [[tools/awk]] (for advanced file processing)

## References

- Official documentation: https://waterlan.home.xs4all.nl/dos2unix.html
- Kali Tools: https://www.kali.org/tools/dos2unix
