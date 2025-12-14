---
id: tool-pry-001
url: 'https://pry.github.io/'
tags:
  - repl
  - debugging
type: tool
verified: false
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.258Z'
validated: true
submitted: true
---
---

# pry

**Status**: Unverified

## Overview

Pry is an interactive Ruby REPL for runtime inspection, debugging, and testing code like the Shopify API SDK in a live environment.

## Description

Pry provides powerful features for stepping through code, setting breakpoints, and executing commands interactively, ideal for testing SDK methods like Session.setup without a full script.

## Features

- Feature 1: Interactive shell with syntax highlighting
- Feature 2: Runtime code evaluation and inspection
- Feature 3: Gem loading and object exploration

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
| -r | Require file on startup |
| --simple-prompt | Simplified prompt |

## Examples

### Example 1: Basic Usage

```bash
pry -r 'shopify_api'
```

### Example 2: Advanced Usage

```bash
pry --repl-historydir ~/.pry_history
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'pry' executable
- Ruby gem logs showing pry installation

## Related Procedures


## Related Tools

- [[tools/irb]]

## References

- Official documentation: https://pry.github.io/
- Ruby debugging resources

---
