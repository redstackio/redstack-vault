---
url: ''
tags:
  - shell
type: tool
platforms:
  - Linux
description: Concatenates and outputs files.
id: 761e7a9b-4d46-464a-8bc6-a25d659ec4fc
created_at: '2025-12-13T09:01:22.290Z'
updated_at: '2025-12-13T09:01:22.290Z'
verified: false
validated: true
submitted: true
---
# Cat

**Status**: Unverified

## Overview

Cat is used to append files or pipe contents, common in payload assembly and delivery.

## Description

Versatile for combining files or sending data to other tools like curl.

## Features

- File concatenation
- Piping

## Installation

Built-in.

## Basic Usage

```bash
cat --help
```

### Common Options

| Option | Description |
|--------|-------------|
| (none) | N/A |

## Examples

### Example 1: Basic Usage

```bash
cat file.txt >> target.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

- Monitor file operations

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/head]]

## References

- Man page cat
