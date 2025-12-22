---
id: 14716789-62e2-4a59-8ef0-c9efdf087680
name: Redis-rb
type: tool
verified: false
created_at: '2025-12-11T06:10:13.259Z'
updated_at: '2025-12-11T06:10:13.259Z'
platforms:
  - Linux
tags:
  - redis
  - ruby
url: 'https://github.com/redis/redis-rb'
description: >-
  Redis client library with driver option allowing directory traversal and code
  loading.
validated: true
submitted: true
---

# Redis-rb

**Status**: Unverified

## Overview

Ruby client for Redis, exploitable via driver options for loading arbitrary files.

## Description

Driver option permits path traversal to load malicious Ruby code.

## Features

- Feature 1: Redis connections
- Feature 2: Custom drivers

## Installation

### Requirements

- Ruby

### Install Commands

```bash
gem install redis
```

## Basic Usage

```ruby
require 'redis'
```

### Common Options

| Option | Description |
|--------|-------------|
| driver | Specify driver path |

## Examples

### Example 1: Basic Usage

driver: ../../../../path/to/file.rb

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual driver paths

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Rouge]]

## References

- https://github.com/redis/redis-rb
