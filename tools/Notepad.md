---
id: tool-notepad
url: 'https://en.wikipedia.org/wiki/Notepad_(text_editor)'
tags:
  - text-editor
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:49.696Z'
validated: true
submitted: true
---
# Notepad

**Status**: Unverified

## Overview

Notepad is a basic text editor included with Windows, used here to craft and verify the content of malicious SVG files containing XSS payloads.

## Description

Notepad allows simple editing of plain text files, ideal for creating SVG XML with embedded JavaScript without advanced features. In offensive security, it's used for quick payload authoring before uploading to web applications.

## Features

- Feature 1: Plain text editing for XML/SVG payloads
- Feature 2: Save with custom extensions (e.g., .png for disguise)
- Feature 3: View file contents to verify onload attributes

## Installation

### Requirements

- Windows OS

### Install Commands

Pre-installed on Windows; no installation needed.

## Basic Usage

Open via Start menu or run `notepad.exe`.

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Basic editor; no CLI flags |

## Examples

### Example 1: Basic Usage

Open Notepad, paste SVG payload, save as Payload.png.

### Example 2: Advanced Usage

Edit and compare multiple payload variants for testing.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- File creation events for .svg or disguised images
- Process monitoring for notepad.exe during payload crafting

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: Windows built-in
- Related resources: SVG XSS payloads on OWASP
