---
id: tool-race-script-001
url: 'https://github.com/PortSwigger/turbo-intruder/tree/master/scripts'
tags:
  - race-condition
  - script
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:57.213Z'
validated: true
submitted: true
---
# race-single-packet-attack.py

**Status**: Unverified

## Overview

A Python script for Turbo Intruder that performs single-packet race condition attacks by sending HTTP requests in extremely rapid succession to exploit timing vulnerabilities.

## Description

Designed for Burp integration, it uses minimal delays to race requests, useful for bypassing rate limits in APIs like HackerOne's GraphQL by overwhelming sequential checks.

## Features

- Feature 1: Configurable loop iterations
- Feature 2: Single-packet timing for races
- Feature 3: Logging of responses

## Installation

### Requirements

- Turbo Intruder in Burp

### Install Commands

```bash
# Download from Turbo Intruder repo and load in Burp
# No separate install; paste into script pane
```

## Basic Usage

```python
# In Turbo Intruder: Paste script, set loop=100, Attack
for i in range(100):
    http.request(method='POST', path='/graphql', ...)
```

### Common Options

| Option | Description |
|--------|-------------|
| loop range | Number of iterations (default 1) |
| delay | Microsecond delays between sends |

## Examples

### Example 1: Basic Usage

Default race on loaded request.

### Example 2: Advanced Usage

Modify for 100 iterations on GraphQL POST.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Ultra-low inter-request times (<1ms)
- Identical payloads in bursts

## Related Procedures

- [[procedures/Configure-and-Execute-Turbo-Intruder-Race-Attack]]

## Related Tools

- [[tools/Turbo-Intruder]]

## References

- Turbo Intruder scripts: https://github.com/PortSwigger/turbo-intruder
