---
url: 'https://imagemagick.org/script/command-line-options.php'
tags:
  - image-processing
  - cli
type: tool
platforms:
  - Linux
  - Web
description: Image processing library used for transformations in the exploit chain.
id: be7b6820-f294-4064-b76d-52fb90dbaa11
created_at: '2025-12-14T17:28:28.316Z'
updated_at: '2025-12-14T17:28:28.316Z'
verified: false
validated: true
submitted: true
---
# ImageMagick

**Status**: Unverified

## Overview

ImageMagick is a software suite for image manipulation, commonly used in web apps for resizing and processing. In this context, it's exploited via CLI injections in convert commands.

## Description

Provides command-line tools like convert for batch image operations. Vulnerable when arguments are user-controlled, allowing file writes and SSRF.

## Features

- Feature 1: Supports resize, rotate, and metadata setting
- Feature 2: CLI options for input/output paths
- Feature 3: Integration with wrappers like MiniMagick

## Installation

### Requirements

- Linux or compatible OS

### Install Commands

```bash
# Ubuntu/Debian
apt-get install imagemagick
```

## Basic Usage

```bash
convert --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help |
| -resize | Resize image |
| -write | Write intermediate file |

## Examples

### Example 1: Basic Usage

```bash
convert input.jpg -resize 100x100 output.png
```

### Example 2: Advanced Usage

```bash
convert input.jpg -auto-orient -write /tmp/out.jpg output.png
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

- Monitor convert command logs for unusual arguments
- Policy restrictions in /etc/ImageMagick/policy.xml

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/MiniMagick]]
- [[tools/ImageProcessing]]

## References

- Official documentation
