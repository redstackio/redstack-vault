---
url: 'https://notepad-plus-plus.org/'
tags:
  - editor
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.560Z'
id: ae8fd5f0-da65-4abd-ad76-9e6ae12d1f15
validated: true
submitted: true
---
# Notepad++

**Status**: Unverified

## Overview

Notepad++ is a free, open-source text editor for Windows, commonly used in security testing for crafting PoC files like malicious HTML for XSS/CSRF demos.

## Description

It supports syntax highlighting for HTML/JS, URL encoding, and easy saving of test files. In offensive ops, it's ideal for quick edits without complex IDE overhead.

## Features

- Syntax highlighting for web languages.
- Plugins for encoding/decoding (e.g., URL encode payloads).
- Multi-tab editing for iterative PoC development.

## Installation

### Requirements

- Windows OS.

### Install Commands

```bash
# Download from official site; no CLI install needed
# Run installer as admin
```

## Basic Usage

```bash
# Launch via GUI; open file > edit > save
notepad++.exe poc.html
```

### Common Options

| Option | Description |
|--------|-------------|
| Plugins > MIME Tools > URL Encode | Encode payloads for arg2 |
| View > Show Symbol > Show All Characters | Verify encoding |

## Examples

### Example 1: Basic Usage

Open Notepad++, paste HTML form, encode arg2 payload, save as poc.html.

### Example 2: Advanced Usage

Use Plugins > HashTools to generate obfuscated JS if needed.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- File modifications with timestamps matching PoC creation.
- Presence of notepad++.exe in process lists during testing.

## Related Procedures


## Related Tools

- [[tools/VS-Code]]
- [[tools/Vim]]

## References

- Official documentation: https://notepad-plus-plus.org/doc/
- Related resources: Security PoC guides on GitHub
