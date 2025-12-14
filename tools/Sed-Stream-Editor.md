---
url: 'https://www.gnu.org/software/sed/'
tags:
  - text-processing
  - payload-generation
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:55.967Z'
id: 88e9e96c-0cce-45d0-bf14-a1b670930ca0
validated: true
submitted: true
---
# Sed-Stream-Editor

**Status**: Unverified

## Overview

Sed is a stream editor for filtering and transforming text, used in security for payload manipulation, such as substituting characters to build large strings for exploits.

## Description

Sed excels at non-interactive text replacement, piping input for real-time processing. In attacks, it's chained with other tools to craft repetitive payloads for DoS or fuzzing.

## Features

- Feature 1: Global substitutions (s///g)
- Feature 2: Piping integration
- Feature 3: Regex-based editing

## Installation

### Requirements

- Core Unix tool

### Install Commands

```bash
# Usually pre-installed; on minimal systems
apt install sed
```

## Basic Usage

```bash
sed --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-e` | Execute script |
| `-n` | Suppress auto-print |
| `s/pattern/repl/g` | Substitute globally |

## Examples

### Example 1: Basic Usage

```bash
echo 'abc' | sed 's/b/x/'
```

### Example 2: Advanced Usage

```bash
head -c 10 /dev/zero | sed 's/\x00/a/g'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unix Shell]] Unix Shell
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Process chains involving sed with /dev/zero
- High I/O from text transformations

## Related Procedures


## Related Tools

- [[tools/Awk]]
- [[tools/Grep]]

## References

- Official documentation: https://www.gnu.org/software/sed/manual/sed.html
