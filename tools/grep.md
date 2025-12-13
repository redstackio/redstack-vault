---
url: 'https://www.gnu.org/software/grep/'
tags:
  - text-processing
  - verification
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: >-
  Command-line utility for searching plain-text data sets for lines matching a
  regular expression, used for filtering command outputs.
id: b6b33874-4c46-459d-bc62-9e5df8dc7f21
created_at: '2025-12-13T09:00:34.685Z'
updated_at: '2025-12-13T09:00:34.685Z'
verified: false
validated: true
submitted: true
---
# grep

**Status**: Unverified

## Overview

grep is a standard Unix tool for pattern matching in text, commonly used in security workflows to filter and verify specific strings in command outputs, such as checking for poisoned ports in responses.

## Description

grep searches input for matches to a pattern and prints matching lines, making it essential for automating verification in exploit chains like cache poisoning.

## Features

- Feature 1: Regular expression matching
- Feature 2: Output filtering
- Feature 3: Piping integration

## Installation

### Requirements

- Included in most Unix distributions
- For Windows: Available via Git Bash or Cygwin

### Install Commands

```bash
# On Debian/Ubuntu
sudo apt install grep
```

## Basic Usage

```bash
grep --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i, --ignore-case` | Ignore case distinctions |
| `-r, --recursive` | Read all files under each directory |

## Examples

### Example 1: Basic Usage

```bash
echo "test:1337" | grep ":1337"
```

### Example 2: Advanced Usage

```bash
curl example.com | grep "poisoned"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]]

### Tactics

- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor shell command history
- Detection method 2: Look for piped outputs in processes

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/awk]]
- [[tools/sed]]

## References

- Official documentation: https://www.gnu.org/software/grep/manual/
- Related resources: Man pages
