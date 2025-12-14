---
id: tool-fiddler
url: 'https://www.telerik.com/fiddler'
tags:
  - proxy
  - intercept
type: tool
verified: false
platforms:
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:09:00.645Z'
validated: true
submitted: true
---
---

# Fiddler

**Status**: Unverified

## Overview

Fiddler is a free web debugging proxy for capturing and inspecting HTTP traffic, serving as an alternative to Burp for modifying requests in vulnerability exploitation like SSRF.

## Description

Fiddler allows inspecting and editing POST requests in real-time, useful for injecting CRLF payloads into GitLab's mirror URL parameter during testing.

## Features

- Feature 1: Traffic capture and decryption
- Feature 2: Request composer for modifications
- Feature 3: Auto-responder for custom responses

## Installation

### Requirements

- .NET Framework (Windows)
- Mono (Linux/macOS alternatives)

### Install Commands

```bash
# Windows: Download MSI
# For cross-platform: Use Fiddler Everywhere
wget https://fiddler-everywhere.s3.amazonaws.com/latest/FiddlerEverywhere_linux_x64.tar.gz
tar -xzf FiddlerEverywhere_linux_x64.tar.gz
./FiddlerEverywhere
```

## Basic Usage

```bash
# Launch
./FiddlerEverywhere
```

### Common Options

| Option | Description |
|--------|-------------|
| --help | Show help |
| --port 8888 | Custom port |

## Examples

### Example 1: Basic Usage

Set browser proxy to 127.0.0.1:8888, capture GitLab traffic.

### Example 2: Advanced Usage

Inspect session > Edit request > Inject payload > Replay.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Proxy artifacts in traffic logs
- Modified request signatures

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]

## References

- Official documentation: https://docs.telerik.com/fiddler-everywhere
- Related resources: Web proxy guides

