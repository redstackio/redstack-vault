---
url: ''
tags:
  - verification
type: tool
platforms:
  - Linux
description: File reading utility
id: aafbece4-c0fe-48b0-9ccc-645f0fa45450
created_at: '2025-12-11T03:48:05.948Z'
updated_at: '2025-12-11T03:48:05.948Z'
verified: false
validated: true
submitted: true
---
# cat

**Status**: Unverified

## Overview

Standard tool for reading file contents.

## Description

Used to verify exploitation by checking created files.

## Features

- Concatenate and display

## Installation

### Requirements

- Coreutils

### Install Commands

```bash
# Built-in
```

## Basic Usage

```bash
cat file
```

### Common Options

| Option | Description |
|--------|-------------|
| (none) |  |

## Examples

### Example 1: Basic Usage

```bash
cat /tmp/file
```

## MITRE ATT&CK Mapping

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

- File access logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools



## References

- Cat man page
