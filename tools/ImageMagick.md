---
url: null
tags:
  - image-processing
  - vulnerability
type: tool
platforms:
  - Linux
description: Image processing library vulnerable to exploits via improper patching.
id: 914db2ba-10cd-4658-8818-0fef36406e5d
created_at: '2025-12-11T06:10:32.956Z'
updated_at: '2025-12-11T06:10:32.956Z'
verified: false
validated: true
submitted: true
---
# ImageMagick

**Status**: Unverified

## Overview

ImageMagick is a software suite for creating, editing, and composing bitmap images, commonly used in web applications for image processing. It can be vulnerable to RCE if not properly configured.

## Description

In this context, it's exploited due to allowing Postscript files to trigger Ghostscript without disabling dangerous formats in policy.xml, leading to arbitrary command execution.

## Features

- Image format conversion
- Processing of various file types including PS/EPS
- Integration with web servers for uploads

## Installation

### Requirements

- Linux environment

### Install Commands

```bash
sudo apt install imagemagick
```

## Basic Usage

```bash
convert input.jpg output.png
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
convert test.jpg test.png
```

### Example 2: Advanced Usage

```bash
convert -resize 50% input.jpg output.jpg
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for unexpected Ghostscript invocations
- Check policy.xml configurations

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Ghostscript]]

## References

- Official ImageMagick documentation
