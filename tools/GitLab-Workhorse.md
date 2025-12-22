---
url: ''
tags:
  - file-upload
  - gitlab
type: tool
platforms:
  - Linux
  - Web
description: >-
  A component of GitLab that handles file uploads and proxies them to tools like
  ExifTool for processing.
id: 24ab0e1f-a3a6-4ffa-809f-cb789d6f43ea
created_at: '2025-12-11T06:10:22.414Z'
updated_at: '2025-12-11T06:10:22.414Z'
verified: false
validated: true
submitted: true
---
# GitLab Workhorse

**Status**: Unverified

## Overview

GitLab Workhorse manages file uploads, passing specific extensions like JPG to ExifTool without content validation, enabling exploitation via disguised malicious files.

## Description

It's configured to process jpg|jpeg|tiff files, but relies on extensions, allowing content-based attacks when forwarded to ExifTool.

## Features

- File upload handling
- Integration with GitLab Rails
- Performance optimization for large files

## Installation

### Requirements

- GitLab installation
- Linux server

### Install Commands

```bash
# Installed as part of GitLab
```

## Basic Usage

```bash
# Runs as service in GitLab
```

### Common Options

| Option | Description |
|--------|-------------|
| (service) | N/A |

## Examples

### Example 1: Basic Usage

Integrated in GitLab uploads.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor upload endpoints for suspicious files
- Log file processing anomalies

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/ExifTool]]

## References

- GitLab documentation
