---
url: 'http://www.graphicsmagick.org/'
tags:
  - image-processing
type: tool
platforms:
  - Linux
description: >-
  Image processing library used server-side in Shopify for handling uploads,
  vulnerable to SSRF in SVG parsing.
id: 28f7e2d5-707a-491c-afb2-1e0300157c65
created_at: '2025-12-14T03:46:14.337Z'
updated_at: '2025-12-14T03:46:14.337Z'
verified: false
validated: true
submitted: true
---
# GraphicsMagick

**Status**: Unverified

## Overview

GraphicsMagick is a robust image processing tool for formats like SVG, PNG, TIFF; exploited here for SSRF via external fetches in SVG before validation.

## Description

Used in Shopify for upload conversion; processes <image> tags, enabling HTTP/FTP requests. Version 1.4 snapshot-20160531 leaks paths in TIFF comments.

## Features

- Feature 1: Multi-format support including SVG with external resources
- Feature 2: Conversion and validation
- Feature 3: Metadata embedding

## Installation

### Requirements

- Linux environment

### Install Commands

```bash
# Ubuntu/Debian
apt-get install graphicsmagick
```

## Basic Usage

```bash
gm convert input.png output.tiff
```

### Common Options

| Option | Description |
|--------|-------------|
| `-comment` | Add comment to image |
| `-size` | Set dimensions |

## Examples

### Example 1: Basic Conversion

```bash
gm convert svgfile.svg output.png
```

### Example 2: Advanced with External Fetch

```bash
gm convert -size 100x100 svg_with_xlink.svg test.png
```

> Fetches external if not sandboxed.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor gm processes with external network activity
- Log temp file creations in /tmp/gm*

## Related Procedures


## Related Tools

- [[ImageMagick]]

## References

- Official documentation: http://www.graphicsmagick.org/
- SSRF exploits in image libs
