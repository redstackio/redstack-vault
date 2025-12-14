---
id: tool-uuid-5
url: 'https://ruby-lang.org'
tags:
  - scripting
  - poc
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.606Z'
configuration: null
validated: true
submitted: true
---
# ruby

**Status**: Unverified

## Overview

Runs PoC scripts to demonstrate SSRF bypass in GitLab using Resolv and Socket libraries.

## Description

Core scripting language for GitLab backend; used here for local testing of vulnerability mechanics.

## Features

- Feature 1: Standard libraries like Resolv and Socket
- Feature 2: Script execution for automation
- Feature 3: Version-specific behaviors (e.g., 2.3.x)

## Installation

### Requirements

- Linux environment

### Install Commands

```bash
sudo apt install ruby-full
```

## Basic Usage

```bash
ruby script.rb
```

### Common Options

| Option | Description |
|--------|-------------|
| -e | Execute string |
| -r | Require file |

## Examples

### Example 1: Basic Usage

```bash
ruby -e 'require "resolv"; puts Resolv.getaddress("0177.1")'
```

### Example 2: Advanced Usage

```bash
ruby poc.rb  # Custom PoC script
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]] Python Interpreter (Ruby equivalent)

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Ruby process spawning with Resolv calls
- Script executions in web app contexts

## Related Procedures

- [[procedures/Import-Repository-with-Octal-Localhost-IP-for-SSRF]]

## Related Tools

- [[tools/irb]]

## References

- Ruby documentation
