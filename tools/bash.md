---
id: tool-uuid-4
url: null
tags:
  - shell
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:31.005Z'
validated: true
submitted: true
---
# bash

**Status**: Unverified

## Overview

Bash is the GNU Bourne-Again Shell, a command-line interpreter for executing scripts and commands on Unix-like systems.

## Description

Used as the execution environment for commands like touch and npm in this attack, handling shell escaping for malicious filenames.

## Features

- Feature 1: Interactive shell
- Feature 2: Script execution
- Feature 3: Variable expansion and quoting

## Installation

### Requirements

- Linux/macOS

### Install Commands

```bash
# Pre-installed
sudo apt install bash  # On Debian
```

## Basic Usage

```bash
bash --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -c | Execute command string |
| -i | Interactive mode |

## Examples

### Example 1: Basic Usage

```bash
bash -c 'touch file.txt'
```

### Example 2: Advanced Usage

```bash
bash -c "touch '\"><svg onload=alert(3);>'"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unix Shell]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for bash with suspicious args
- Command history analysis

## Related Procedures

- [[procedures/Create-Malicious-Filename-for-XSS]]

## Related Tools

- [[tools/touch]]

## References

- https://www.gnu.org/software/bash/
