---
url: null
tags:
  - imagemagick
  - xxe
type: tool
platforms:
  - Web
  - Windows
description: 'Library for image processing, vulnerable to XXE in SVG conversion'
id: e0511d70-ac85-4afb-8e1a-39557473cf75
created_at: '2025-12-13T09:00:28.088Z'
updated_at: '2025-12-13T09:00:28.088Z'
verified: false
validated: true
submitted: true
---
# ImageMagick

**Status**: Unverified

## Overview

ImageMagick is a software suite for creating, editing, and composing bitmap images, commonly used for format conversions like SVG to PNG. In this context, it's exploited due to vulnerabilities in handling external entities.

## Description

The tool processes images on the server-side, but vulnerable versions allow XXE, LFI, and SSRF through improper handling of XML in SVGs. It's typically used in web applications for image manipulation.

## Features

- Image format conversion: SVG to PNG
- XML parsing for vector graphics
- Support for external references (exploitable)

## Installation

### Requirements

- Compatible OS (Windows, Linux)
- Build dependencies (libxml2, etc.)

### Install Commands

```bash
apt install imagemagick
```

## Basic Usage

```bash
convert input.svg output.png
```

### Common Options

| Option | Description |
|--------|-------------|
| `-define` | Define settings |
| `-verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
convert malicious.svg emblem.png
```

### Example 2: Advanced Usage

```bash
convert -define xml:external-entity=no input.svg output.png
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Unsecured Credentials]]

### Tactics

- [[Initial Access]]
- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for external entity requests in logs
- Check for anomalous image processing traffic

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[curl]]
- [[libxml2]]

## References

- Official documentation: https://imagemagick.org
- Vulnerability reports
