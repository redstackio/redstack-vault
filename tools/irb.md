---
url: 'https://ruby-doc.org/stdlib-2.7.0/libdoc/irb/rdoc/IRB.html'
tags:
  - ruby
  - interactive
  - testing
type: tool
platforms:
  - Ruby
  - Linux
  - macOS
  - Windows
description: Interactive Ruby shell for executing and testing Ruby code snippets.
id: bb9d1743-2442-48d5-95ea-3b8c8b57347c
created_at: '2025-12-14T04:08:48.861Z'
updated_at: '2025-12-14T04:08:48.861Z'
verified: false
validated: true
submitted: true
---
# IRB

**Status**: Unverified

## Overview

IRB (Interactive Ruby) is the standard REPL for Ruby, used here to test gems like private_address_check by executing code interactively, ideal for quick vulnerability verification in security research.

## Description

IRB provides an interactive environment to load Ruby libraries, run methods, and inspect outputs without writing full scripts. In offensive security, it's commonly used for prototyping exploits, testing library behaviors, and debugging Ruby-based applications.

## Features

- Feature 1: Interactive code execution with immediate feedback
- Feature 2: Support for requiring gems and running class methods
- Feature 3: History and auto-completion for efficient testing

## Installation

### Requirements

- Ruby 2.0+ installed

### Install Commands

```bash
# IRB comes with Ruby; install Ruby if needed
# On Ubuntu: sudo apt install ruby
# On macOS: brew install ruby
```

## Basic Usage

```bash
irb
```

### Common Options

| Option | Description |
|--------|-------------|
| `-r` | Require a library on startup, e.g., `irb -r private_address_check` |
| `--repl` | Use a specific REPL mode |

## Examples

### Example 1: Basic Usage

```bash
irb
> require 'private_address_check'
> PrivateAddressCheck.private_address?("0.0.0.0")
false
```

### Example 2: Advanced Usage

```bash
irb -r private_address_check
> PrivateAddressCheck.private_address?("127.0.0.1")
true
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for `irb` executions in non-development contexts
- Log analysis for Ruby gem loads in security-sensitive environments

## Related Procedures

- [[procedures/Test-Private-Address-Check-Gem-Bypass]]

## Related Tools

- [[Ruby]]

## References

- Official Ruby IRB documentation
