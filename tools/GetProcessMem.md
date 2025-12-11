---
id: c1ffb335-7527-4989-a841-f5098cea92ad
name: GetProcessMem
type: tool
verified: false
created_at: '2025-12-11T06:10:13.225Z'
updated_at: '2025-12-11T06:10:13.225Z'
platforms:
  - Linux
tags:
  - ruby
  - memory
url: 'https://github.com/schneems/get_process_mem'
description: 'Gem to get process memory, exploited for command injection via ps_memory.'
validated: true
submitted: true
---

# GetProcessMem

**Status**: Unverified

## Overview

Ruby gem for retrieving process memory usage, vulnerable to command injection in ps_memory method.

## Description

When passing a hash as pid, it allows backtick execution of user-controlled input.

## Features

- Feature 1: Memory querying
- Feature 2: Process inspection

## Installation

### Requirements

- Ruby

### Install Commands

```bash
gem install get_process_mem
```

## Basic Usage

```ruby
require 'get_process_mem'
```

### Common Options

| Option | Description |
|--------|-------------|
| a | Injection parameter |

## Examples

### Example 1: Basic Usage

formatter: GetProcessMem, a: '`command`'

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Injection in ps commands

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Redis-rb]]

## References

- https://github.com/schneems/get_process_mem
