---
url: 'https://github.com/tus/tusd'
tags:
  - upload
  - server
type: tool
platforms:
  - Node.js
description: TUS protocol server for resumable file uploads in Uppy.
id: fc0ee274-e241-46fc-ae27-b7a28f612579
created_at: '2025-12-14T03:16:14.015Z'
updated_at: '2025-12-14T03:16:14.015Z'
verified: false
validated: true
submitted: true
---
# tusd

**Status**: Unverified

## Overview

TUSD is the reference server for the TUS resumable upload protocol, used by Uppy for handling SVG uploads; the vulnerability arises from its direct serving of files without script sanitization.

## Description

TUSD enables chunked uploads but in Uppy, it serves SVGs to browsers, allowing embedded JS execution and stored XSS when files are viewed.

## Features

- Feature 1: Resumable uploads
- Feature 2: HTTP-based protocol
- Feature 3: File storage backend support

## Installation

### Requirements

- Go runtime for standalone, or via Uppy

### Install Commands

```bash
# Via Uppy npm integration
go install github.com/tus/tusd/...
```

## Basic Usage

```bash
tusd --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help |
| --port | Specify port |

## Examples

### Example 1: Basic Usage

```bash
tusd -port=1080
```

### Example 2: Advanced Usage

```bash
tusd --upload-dir=/tmp/uploads
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- TUS endpoints in web traffic
- Upload logs with SVG files

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool: npm]]

## References

- Official documentation: https://tus.io/
