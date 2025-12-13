---
url: ''
tags:
  - metadata
  - image
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: Metadata editor for images
id: 4d513a2f-bc60-4f5a-8004-fc9727e4b53e
created_at: '2025-12-13T09:00:33.644Z'
updated_at: '2025-12-13T09:00:33.644Z'
verified: false
validated: true
submitted: true
---
# EXIFTool

**Status**: Unverified

## Overview

Tool for reading and writing metadata in files, used for injecting XXE in XMP.

## Description

Supports various formats including JPEG for custom metadata.

## Features

- Metadata manipulation
- Batch processing

## Installation

### Requirements

- Perl

### Install Commands

```bash
sudo apt install exiftool
```

## Basic Usage

```bash
exiftool file.jpg
```

## Examples

### Example 1: Basic Usage

```bash
exiftool -XMP='payload' file.jpg
```

## MITRE ATT&CK Mapping

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

- Metadata scanning

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/oxml-xxe]]

## References

- Official site
