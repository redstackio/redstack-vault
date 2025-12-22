---
url: ''
tags:
  - sandbox
type: tool
platforms:
  - macOS
description: Sandbox environment for mruby scripts
id: 80262b56-9a3c-4cc4-84ae-e6d0a2ad9d57
created_at: '2025-12-11T03:47:47.964Z'
updated_at: '2025-12-11T03:47:47.964Z'
verified: false
validated: true
submitted: true
---
# mruby-engine

**Status**: Unverified

## Overview

mruby-engine provides a sandbox for running mruby scripts, affected by the same time-related vulnerabilities.

## Description

Used in production environments like Shopify, requires patching for security.

## Features

- Script sandboxing
- Runtime execution

## Installation

### Requirements

- mruby

### Install Commands

```bash
# Custom build
```

## Basic Usage

```bash
./bin/sandbox script.rb
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Script path |

## Examples

### Example 1: Basic Usage

```bash
./bin/sandbox crash.rb
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Sandbox crash logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #mruby

## References

- Internal Shopify docs
