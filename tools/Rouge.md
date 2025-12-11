---
id: 2b6daa56-6e94-4823-8088-2623196d651c
name: Rouge
type: tool
verified: false
created_at: '2025-12-11T06:10:13.199Z'
updated_at: '2025-12-11T06:10:13.199Z'
platforms:
  - Linux
tags:
  - syntax-highlighter
url: ''
description: >-
  Syntax highlighter with formatter option used to instantiate arbitrary
  classes.
validated: true
submitted: true
---

# Rouge

**Status**: Unverified

## Overview

Rouge is a syntax highlighter integrated with Kramdown, exploitable via formatter options for class instantiation.

## Description

Allows specifying formatters like Redis or GetProcessMem, leading to code loading and injection.

## Features

- Feature 1: Code highlighting
- Feature 2: Custom formatters
- Feature 3: Integration with parsers

## Installation

### Requirements

- Ruby

### Install Commands

```bash
gem install rouge
```

## Basic Usage

```bash
rouge highlight code
```

### Common Options

| Option | Description |
|--------|-------------|
| formatter | Specify formatter class |

## Examples

### Example 1: Basic Usage

With minted alternative.

### Example 2: Advanced Usage

formatter: Redis

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Custom formatter usage in logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Kramdown]]

## References

- Related resources
