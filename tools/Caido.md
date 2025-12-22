---
id: tool-caido
url: 'https://caido.io'
tags:
  - proxy
  - web-testing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.550Z'
validated: true
submitted: true
---
# Caido

**Status**: Unverified

## Overview

Caido is a modern web security testing platform and proxy tool, serving as an alternative to Burp Suite for intercepting and modifying HTTP traffic in vulnerability assessments like OTP response manipulation.

## Description

Caido focuses on ease of use with a clean UI, supporting request interception, editing, and replay. It's used in red teaming for web app exploits, particularly for quick response alterations in authentication flows.

## Features

- Feature 1: Intuitive traffic interception
- Feature 2: Built-in repeater for modifications
- Feature 3: Collaboration and reporting tools

## Installation

### Requirements

- Rust runtime (via cargo)
- 4GB+ RAM

### Install Commands

```bash
# Install via official binary or cargo
cargo install caido
```

## Basic Usage

```bash
caido --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

Launch Caido, set browser proxy to localhost:6113, intercept traffic.

### Example 2: Advanced Usage

Capture verification POST, modify JSON success field, replay.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### Tactics

- [[Initial Access]]
- [[Lateral Movement]]

## Detection

Indicators and methods for detecting this tool's usage:

- Proxy connections on non-standard ports (e.g., 6113)
- Log anomalies in request/response pairs

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]

## References

- Official documentation: https://caido.io/docs
- Related resources: Security testing blogs
