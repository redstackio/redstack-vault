---
url: ''
tags:
  - shell
type: tool
platforms:
  - Linux
description: Outputs the first part of files.
id: 2fc95427-21b6-4ff1-857b-96dd391472b6
created_at: '2025-12-13T09:01:22.294Z'
updated_at: '2025-12-13T09:01:22.294Z'
verified: false
validated: true
submitted: true
---
# Head

**Status**: Unverified

## Overview

Head is used to extract specific lines from files during payload preparation.

## Description

Core utility for slicing file contents.

## Features

- Line extraction

## Installation

Built-in.

## Basic Usage

```bash
head --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-n` | Number of lines |

## Examples

### Example 1: Basic Usage

```bash
head -11 file.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

- Shell logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/cat]]

## References

- Man page head
