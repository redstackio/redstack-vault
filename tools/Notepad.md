---
id: tool-notepad
url: null
name: Notepad
tags:
  - text-editor
  - basic
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:05.326Z'
validated: true
submitted: true
---
# Notepad

**Status**: Unverified

## Overview

Notepad is a basic text editor included with Windows operating systems, used here for creating simple HTML proof-of-concept files in security testing scenarios like demonstrating web vulnerabilities.

## Description

Notepad provides plain text editing capabilities without advanced features, making it suitable for quick scripting or HTML prototyping in offensive security operations, such as building clickjacking PoCs. It lacks syntax highlighting but ensures clean, unformatted output for web files.

## Features

- Feature 1: Plain text editing for HTML, scripts, and configs
- Feature 2: Simple save-as functionality with file extensions
- Feature 3: Lightweight and always available on Windows

## Installation

### Requirements

- Windows OS (pre-installed)

### Install Commands

No installation required; accessible via Start menu or Run (notepad.exe).

## Basic Usage

```bash
notepad
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Notepad has no CLI options; GUI-based |

## Examples

### Example 1: Basic Usage

Open Notepad and paste HTML code, then save as .html.

### Example 2: Advanced Usage

Use via command line to open a file:

```bash
notepad clickjacking-poc.html
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- File creation events in Windows logs for .html or .txt files with suspicious content
- Process monitoring for notepad.exe in security testing contexts

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Microsoft Documentation: Notepad
