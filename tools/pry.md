---
id: tool-uuid-1
url: 'https://pry.github.io/'
tags:
  - debugging
  - interactive
type: tool
verified: false
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:18.706Z'
validated: true
submitted: true
---
# pry

**Status**: Unverified

## Overview

Pry is an interactive Ruby shell and runtime debugger, ideal for testing SDK behavior, simulating session setups, and stepping through code during security assessments like SSRF exploitation in the Shopify API.

## Description

Pry enhances irb with features like syntax highlighting, command history, and pry-remote for debugging. In offensive security, it's used to load gems, inspect methods, and execute payloads interactively without full scripts.

## Features

- Feature 1: Interactive REPL with tab completion
- Feature 2: Breakpoint debugging with pry-byebug integration
- Feature 3: Custom commands for repetitive tasks

## Installation

### Requirements

- Ruby 2.0+

### Install Commands

```bash
gem install pry
```

## Basic Usage

```bash
pry
```

### Common Options

| Option | Description |
|--------|-------------|
| -r file | Require file on startup |
| --simple-prompt | Minimal prompt |

## Examples

### Example 1: Basic Usage

```bash
pry -r 'shopify_api'
```

### Example 2: Advanced Usage

```bash
pry --gem  # List installed gems
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process: ruby/pry processes
- Network: No direct network, but used in exploits

## Related Procedures

- [[procedures/Analyze-Shopify-API-SDK-for-Input-Validation-Flaws]]
- [[procedures/Exploit-Port-Parameter-for-Arbitrary-Host-Injection]]

## Related Tools

- [[tools/irb]]

## References

- Official documentation: https://pry.github.io/
