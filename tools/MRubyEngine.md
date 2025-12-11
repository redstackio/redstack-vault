---
url: null
tags:
  - mruby
  - sandbox
type: tool
platforms:
  - Ruby
  - mruby
description: >-
  Sandboxed execution environment for mruby code, used in Shopify's ecosystem
  for script evaluation with memory and execution limits.
id: f05c6b2a-50fc-4523-8a8e-126df8245c81
created_at: '2025-12-11T03:47:48.304Z'
updated_at: '2025-12-11T03:47:48.304Z'
verified: false
validated: true
submitted: true
---
# MRubyEngine

**Status**: Unverified

## Overview

MRubyEngine is a tool for sandboxed execution of mruby code, commonly used in environments like Shopify-scripts to run user-provided scripts securely with constraints on memory and execution time.

## Description

It allows instantiation with parameters for memory allocation and limits, providing a sandbox_eval method to run code in isolated paths. In security contexts, it's exploited for vulnerabilities like null pointer dereferences in mruby classes.

## Features

- Feature 1: Sandboxed code evaluation
- Feature 2: Configurable memory and execution limits
- Feature 3: Integration with shopify-scripts and mruby-engine

## Installation

### Requirements

- Ruby/mruby runtime
- Shopify's mruby-engine library

### Install Commands

```bash
# Typically integrated in Shopify environments; no standalone install
```

## Basic Usage

```ruby
MRubyEngine.new(memory, limit1, limit2).sandbox_eval(path, code)
```

### Common Options

| Option | Description |
|--------|-------------|
| `memory` | Memory allocation in bytes |
| `limit1` | Execution limit parameter |
| `limit2` | Additional limit parameter |

## Examples

### Example 1: Basic Usage

```ruby
MRubyEngine.new(512*1024, 1000, 1000).sandbox_eval("/tmp", "puts 'Hello'")
```

### Example 2: Advanced Usage

```ruby
MRubyEngine.new(512*1024, 1000, 1000).sandbox_eval("/tmp", %{Range.remove_method(:initialize_copy)
(1..2).dup.to_s})
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

- Detection method 1: Monitor for sandbox_eval calls with suspicious code
- Detection method 2: Log segfaults in mruby processes

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools



## References

- HackerOne Report #181685
- mruby documentation
