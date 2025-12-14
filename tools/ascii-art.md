---
id: tool-ascii-art-001
url: 'https://www.npmjs.com/package/ascii-art'
name: ascii-art
tags:
  - image-processing
  - npm
  - exploitation
type: tool
verified: false
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.051Z'
validated: true
submitted: true
---
# ascii-art

**Status**: Unverified

## Overview

ascii-art is an NPM package for converting images to ASCII art, utilizing the Node.js canvas module for image loading and manipulation. In security testing, it's used to reproduce vulnerabilities in canvas by processing crafted images, leading to crashes in parsing routines.

## Description

The package wraps canvas to handle image input, resize, and pixel-to-character mapping. Due to dependencies on vulnerable canvas versions (e.g., 1.6.9), supplying malformed PNG/JPG/GIF files triggers buffer overflows and memory errors, causing DoS. It's a practical vector for testing services with image uploads.

## Features

- Feature 1: Image-to-ASCII conversion with customizable fonts
- Feature 2: Support for various image formats via canvas
- Feature 3: Command-line interface for quick testing

## Installation

### Requirements

- Node.js 0.10+ and NPM
- Cairo and Pango libraries for canvas backend

### Install Commands

```bash
npm install ascii-art
```

## Basic Usage

```bash
ascii-art image input.png
```

### Common Options

| Option | Description |
|--------|-------------|
| `--width` | Set output width |
| `--color` | Enable colored output |

## Examples

### Example 1: Basic Usage

```bash
ascii-art image /path/to/valid/image.png
```

Outputs ASCII art to console.

### Example 2: Advanced Usage

```bash
ascii-art image /full/path/to/test/image --width 120
```

Processes with specified width; crashes on malformed input.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- NPM logs showing ascii-art installation
- Node.js crashes during image processing
- Package.json dependencies on canvas

## Related Procedures

- [[procedures/Reproduce-Canvas-DoS-with-Crafted-Images-via-Ascii-Art]]

## Related Tools

- [[tools/AFL]]

## References

- Official documentation: https://www.npmjs.com/package/ascii-art
- Related resources: Canvas module docs
