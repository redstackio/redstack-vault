---
url: 'https://ruby-doc.org/stdlib-3.0.0/libdoc/digest/rdoc/Digest/SHA2.html'
tags:
  - ruby
  - hashing
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: Ruby library for computing SHA256 hashes.
id: a9d3ca09-c5bf-4817-b45c-8f3a2724b43d
created_at: '2025-12-11T03:47:59.470Z'
updated_at: '2025-12-11T03:47:59.470Z'
verified: false
validated: true
submitted: true
---
# Digest::SHA2

**Status**: Unverified

## Overview

Ruby's Digest::SHA2 module provides SHA256 hashing, used in security contexts for path calculations and data integrity.

## Description

Part of Ruby's standard library, it computes hexadecimal digests for strings, essential for tasks like GitLab repository path hashing.

## Features

- SHA256, SHA384, SHA512 support
- Hex and base64 output
- Simple API

## Installation

### Requirements

- Ruby installed

### Install Commands

Built-in with Ruby.

## Basic Usage

```ruby
require 'digest'; Digest::SHA2.hexdigest('input')
```

### Common Options

| Option | Description |
|--------|-------------|
| `hexdigest` | Hex output |
| `digest` | Binary output |

## Examples

### Example 1: Basic Usage

```ruby
Digest::SHA2.hexdigest("38006449")
```

### Example 2: Advanced Usage

Use in scripts for batch hashing.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Data from Information Repositories]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Ruby script execution monitoring
- Hash computation patterns in logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/fake_server.py]]

## References

- Ruby docs: https://ruby-doc.org/stdlib-3.0.0/libdoc/digest/rdoc/Digest/SHA2.html
