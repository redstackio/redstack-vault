---
id: d981e694-6c3e-41c0-ad96-6773b98908f8
type: tool
verified: false
created_at: '2025-12-11T03:48:05.881Z'
updated_at: '2025-12-11T03:48:05.881Z'
platforms:
  - Linux
tags:
  - archive
url: ''
description: Archiving utility for creating tarballs
validated: true
submitted: true
---

# tar

**Status**: Unverified

## Overview

tar is a standard utility for creating and extracting tape archives, often used in exploits to package malicious payloads including symlinks.

## Description

In security testing, tar is used to create gzipped archives containing symlinks for exploitation of extraction vulnerabilities, as in GitLab import flaws.

## Features

- Feature 1: Create archives with c
- Feature 2: Gzip compression with z
- Feature 3: Verbose output with v

## Installation

### Requirements

- Linux or Unix-like system

### Install Commands

```bash
# Built-in on most systems
```

## Basic Usage

```bash
tar --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `c` | Create archive |
| `z` | Gzip |
| `v` | Verbose |
| `f` | File |

## Examples

### Example 1: Basic Usage

```bash
tar cvf archive.tar dir
```

### Example 2: Advanced Usage

```bash
tar cvzf archive.tar.gz dir
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Scan archives for symlinks
- Monitor tar operations in pipelines

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #mkdir
- #ln

## References

- man tar
