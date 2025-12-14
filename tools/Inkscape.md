---
id: tool-inkscape
url: 'https://inkscape.org/'
tags:
  - graphics
  - svg
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:10.485Z'
validated: true
submitted: true
---
# Inkscape

**Status**: Unverified

## Overview

Inkscape is an open-source vector graphics editor for creating and editing SVG files, ideal for crafting malicious SVGs in security testing, such as embedding external references for SSRF exploitation.

## Description

Used in offensive ops to generate precise XML-based payloads for file upload vulnerabilities. It supports SVG standards and XML editing, making it suitable for inserting xlink:href attributes without syntax errors. Version 0.48.4 was noted in the original report.

## Features

- Feature 1: Full SVG support with XML source editing
- Feature 2: GUI for visual design and export
- Feature 3: Extensions for automation

## Installation

### Requirements

- GTK+ libraries on Linux

### Install Commands

```bash
# On Ubuntu
apt install inkscape

# On macOS
brew install --cask inkscape
```

## Basic Usage

```bash
inkscape --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help |
| `--export-plain-svg` | Export as plain SVG |
| `--file` | Open specific file |

## Examples

### Example 1: Basic Usage

```bash
inkscape new.svg
```
(Create and edit new.svg.)

### Example 2: Advanced Usage

```bash
inkscape --export-plain-svg=input.svg output.svg
```
(Export without Inkscape-specific elements.)

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Unsecured Credentials]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: File metadata showing Inkscape version
- Detection method 2: Unusual SVG files in upload logs

## Related Procedures

- [[procedures/Craft-Malicious-SVG-with-External-Reference]]

## Related Tools

- [[Related Tool 1|Adobe Illustrator]]
- [[Related Tool 2|LibreOffice Draw]]

## References

- Official documentation: https://inkscape.org/doc/
- Related resources: SVG specification
