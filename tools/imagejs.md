---
id: tool-imagejs-001
url: 'http://jklmnn.de/imagejs/'
tags:
  - js-embedding
  - steganography
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:33.990Z'
validated: true
submitted: true
---
# imagejs

**Status**: Unverified

## Overview

imagejs is a tool for embedding JavaScript code directly into image files such as GIF, Bitmap, WebP, Netbpm Anymap, and Progressive Graphics, while ensuring the images remain valid and displayable. It's commonly used in security testing for XSS payloads in upload scenarios.

## Description

The tool modifies image data to hide JS scripts that can be extracted and executed when the image is misinterpreted as script content, ideal for bypassing filters in web uploads and proxies.

## Features

- Feature 1: Supports multiple image formats (GIF, BMP, WebP, etc.)
- Feature 2: Keeps images visually intact
- Feature 3: Extracts JS on demand for execution

## Installation

### Requirements

- Node.js or compatible runtime
- Git for cloning

### Install Commands

```bash
# Clone and install
git clone https://github.com/jklmn/imagejs
go build  # If Go-based, or npm install if JS
```

## Basic Usage

```bash
imagejs --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --input | Input image file |
| -o, --output | Output image file |
| -e, --embed | JS code to embed |

## Examples

### Example 1: Basic Usage

```bash
imagejs -i pikachu.gif -o malicious.gif -e "alert(document.cookie);"
```

### Example 2: Advanced Usage

```bash
imagejs -i input.png -o output.png -e "var x = 1; console.log(x);" --format webp
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Obfuscated Files or Information]]

### Tactics

- [[Execution]]
- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous image files with embedded non-image data
- JS execution from image MIME types

## Related Procedures

- [[procedures/Craft-Malicious-Image-with-ImageJS]]

## Related Tools

- [[Related Tool: Steghide]]

## References

- Official GitHub: https://github.com/jklmn/imagejs
- Usage docs: http://jklmnn.de/imagejs/
