---
url: ''
tags:
  - compression
type: tool
platforms:
  - Linux
description: >-
  Command-line utility for compressing files into zip archives, inferred for
  creating .nupkg.
id: 3e24dfaf-f1fe-44bc-8c2b-972c9c6e1f2e
created_at: '2025-12-11T03:47:39.701Z'
updated_at: '2025-12-11T03:47:39.701Z'
verified: false
validated: true
submitted: true
---
# zip

**Status**: Unverified

## Overview

zip is a standard utility for creating zip archives, used here to package .nuspec into .nupkg for GitLab exploits.

## Description

Simple compression tool for preparing malicious packages.

## Features

- Archive creation
- Compression levels
- File addition

## Installation

### Requirements

- Linux system

### Install Commands

```bash
sudo apt install zip
```

## Basic Usage

```bash
zip --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-r` | Recursive |

## Examples

### Example 1: Basic Usage

```bash
zip dummy.nupkg dummy.nuspec
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor zip commands in processes

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #rubyzip

## References

- man zip
