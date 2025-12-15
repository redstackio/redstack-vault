---
url: ''
tags:
  - text-editor
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.213Z'
id: 0b4c942b-aa17-4e28-b088-5b71a76a364b
validated: true
submitted: true
---
# nano

**Status**: Unverified

## Overview

Nano is a simple, user-friendly command-line text editor for Unix-like systems, commonly used in security testing to quickly edit and save files like exported HTTP requests.

## Description

It's lightweight and ideal for creating or modifying small files during pentests, such as saving Burp Suite requests for SQLMap. No advanced features, but perfect for ad-hoc edits in offensive workflows.

## Features

- Feature 1: Syntax highlighting for common formats
- Feature 2: Search and replace functionality
- Feature 3: Easy save/exit shortcuts

## Installation

### Requirements

- Standard on most Linux distros

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt install nano
```

## Basic Usage

```bash
nano filename.txt
```

### Common Options

| Option | Description |
|--------|-------------|
| `-w` | Disable word wrapping |
| `-l` | Show line numbers |

## Examples

### Example 1: Basic Usage

```bash
nano testsql.txt
```
Paste content and save with Ctrl+O.

### Example 2: Advanced Usage

```bash
nano -w testsql.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for nano executions
- File modification timestamps

## Related Procedures

- [[procedures/Save-Burp-Request-to-File-with-Nano]]

## Related Tools

- [[tools/Burp-Suite]]

## References

- Man page: man nano
