---
url: ''
tags:
  - shell
type: tool
platforms:
  - Linux
description: Generates sequences of numbers.
id: 32dba867-e887-42cf-b4f6-f2bce9c226b0
created_at: '2025-12-13T09:01:22.306Z'
updated_at: '2025-12-13T09:01:22.306Z'
verified: false
validated: true
submitted: true
---
# Seq

**Status**: Unverified

## Overview

Seq generates number sequences for loops, used in creating large strings for payloads.

## Description

Core utility for scripting repetitive tasks like appending characters.

## Features

- Sequence generation

## Installation

Built-in on most Linux systems.

## Basic Usage

```bash
seq --help
```

### Common Options

| Option | Description |
|--------|-------------|
| (none) | N/A |

## Examples

### Example 1: Basic Usage

```bash
seq 8179
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

- Script execution logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/echo]]

## References

- Man page seq
