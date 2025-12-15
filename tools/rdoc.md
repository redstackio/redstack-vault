---
url: 'https://ruby.github.io/rdoc/'
tags:
  - ruby
  - documentation
  - rce
type: tool
platforms:
  - Ruby
description: >-
  Ruby Documentation generator vulnerable to deserialization RCE via
  .rdoc_options and cache files
id: b6f460f1-20e3-4741-b5a2-4ba3b061c8ce
created_at: '2025-12-14T17:23:42.403Z'
updated_at: '2025-12-14T17:23:42.403Z'
verified: false
validated: true
submitted: true
---
# rdoc

**Status**: Unverified

## Overview

RDoc is Ruby's standard tool for generating documentation from source code, but vulnerable versions expose deserialization flaws leading to RCE when processing untrusted inputs.

## Description

RDoc parses `.rdoc_options` with unsafe YAML and loads caches with Marshal, allowing gadget chain exploits for arbitrary code execution. Used in development workflows for repo documentation.

## Features

- Feature 1: YAML-based option loading
- Feature 2: Marshal cache serialization
- Feature 3: Integration with Ruby gems

## Installation

### Requirements

- Ruby 2.x or 3.x

### Install Commands

```bash
# Via RubyGems
gem install rdoc
```

## Basic Usage

```bash
rdoc --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-v, --version` | Show version |
| `--op DIR` | Output directory |

## Examples

### Example 1: Basic Usage

```bash
rdoc
```

### Example 2: Advanced Usage

```bash
rdoc --op docs/
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]]
- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor rdoc process spawns with untrusted inputs
- Log deserialization errors in Ruby traces

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/psych]]

## References

- Official documentation: https://ruby.github.io/rdoc/
- HackerOne Report: https://hackerone.com/reports/1187477
