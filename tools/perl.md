---
url: ''
tags:
  - scripting
type: tool
platforms:
  - Linux
description: Scripting language for text manipulation.
id: d82771b4-c9d3-48ec-9939-5dee99eacf9e
created_at: '2025-12-13T09:01:22.298Z'
updated_at: '2025-12-13T09:01:22.298Z'
verified: false
validated: true
submitted: true
---
# Perl

**Status**: Unverified

## Overview

Perl is used for one-liners to print special characters or strings in payloads.

## Description

Powerful for handling escape sequences like \r\n in HTTP payloads.

## Features

- One-liner execution
- Text processing

## Installation

```bash
sudo apt install perl
```

## Basic Usage

```bash
perl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-e` | Execute code |

## Examples

### Example 1: Basic Usage

```bash
perl -e 'print "\r\n"'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

- Monitor perl executions

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

- https://www.perl.org/
