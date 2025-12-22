---
id: 8510e07a-f4d7-493b-b427-721de529adb5
name: mruby
type: tool
verified: false
created_at: '2025-12-11T03:47:48.100Z'
updated_at: '2025-12-11T03:47:48.100Z'
platforms:
  - macOS
tags:
  - ruby
  - interpreter
url: 'https://github.com/mruby/mruby'
description: Lightweight Ruby interpreter for embedded systems.
validated: true
submitted: true
---

# mruby

**Status**: Unverified

## Overview

mruby is a lightweight implementation of the Ruby language, designed for embedding in other applications, used here to execute scripts and demonstrate crashes.

## Description

mruby provides a compact Ruby interpreter suitable for resource-constrained environments, but vulnerable to certain code generation bugs leading to crashes.

## Features

- Lightweight Ruby execution
- Embeddable in applications like Shopify Scripts
- Supports Ruby 2.3.0 syntax

## Installation

### Requirements

- Git
- Build tools

### Install Commands

```bash
git clone https://github.com/mruby/mruby.git
cd mruby
make
```

## Basic Usage

```bash
./bin/mruby --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
./dev/bin/mruby script.rb
```

### Example 2: Advanced Usage

```bash
./dev/bin/mruby -v script.rb
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]]
- [[Endpoint Denial of Service]]

### Tactics

- [[Execution]]
- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for mruby process crashes
- Log script executions in embedded environments

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #lldb
- #sandbox

## References

- https://github.com/mruby/mruby
