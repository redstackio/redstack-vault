---
id: tool-uuid-1
url: 'https://notepad-plus-plus.org/'
tags:
  - editor
  - text
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:42.458Z'
validated: true
submitted: true
---
# Notepad++

**Status**: Unverified

## Overview

Notepad++ is a free, open-source text editor for Windows, commonly used in security testing for editing scripts, PoCs, and configuration files due to its syntax highlighting and plugin support.

## Description

Notepad++ supports multiple languages with features like auto-completion, macros, and regex search/replace, making it ideal for crafting HTML PoCs or payloads in offensive operations. In this context, it's used to build and save the CSRF HTML file with embedded XSS.

## Features

- Feature 1: Syntax highlighting for HTML, JS, PHP.
- Feature 2: Multi-document tab interface.
- Feature 3: Plugin ecosystem for advanced editing.

## Installation

### Requirements

- Windows OS (7 or later).

### Install Commands

```bash
# Download from official site or use winget
winget install Notepad++.Notepad++
```

## Basic Usage

```bash
tool-name --help
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | GUI-based; no CLI options for basic use |

## Examples

### Example 1: Basic Usage

Open Notepad++ and create a new file for HTML PoC editing.

### Example 2: Advanced Usage

Use Find & Replace with regex to encode payloads.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for notepad++.exe in security contexts.
- File creation logs for .html PoCs.

## Related Procedures


## Related Tools

- [[tools/Vim]]
- [[tools/VS-Code]]

## References

- Official documentation: https://notepad-plus-plus.org/doc/
- Related resources: Security PoC guides.
