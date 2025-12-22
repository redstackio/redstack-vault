---
url: 'https://github.com/Shopify/toxiproxy#cli-example'
tags:
  - cli
  - management
type: tool
platforms:
  - macOS
  - Linux
description: Command-line client for interacting with Toxiproxy's HTTP API.
id: dbd2f36e-f6c5-49f4-aa4c-2ddc2038671e
created_at: '2025-12-14T17:27:29.676Z'
updated_at: '2025-12-14T17:27:29.676Z'
verified: false
validated: true
submitted: true
---
# toxiproxy-cli

**Status**: Unverified

## Overview

CLI tool to create, inspect, and manage proxies in Toxiproxy, useful for verifying CSRF-induced changes during attacks.

## Description

Provides a terminal interface to the API for scripting and manual inspection in exploitation workflows.

## Features

- Feature 1: Inspect and list proxies
- Feature 2: Add/remove toxics
- Feature 3: JSON output for parsing

## Installation

### Requirements

- Toxiproxy server installed

### Install Commands

```bash
brew install toxiproxy
```

## Basic Usage

```bash
toxiproxy-cli --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h | Help |

## Examples

### Example 1: Basic Usage

```bash
toxiproxy-cli list
```

### Example 2: Advanced Usage

```bash
toxiproxy-cli inspect myproxy
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[System Information Discovery]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Executions of toxiproxy-cli binary
- API calls logged

## Related Procedures

- [[procedures/Verify-Proxy-Creation-with-Toxiproxy-CLI]]

## Related Tools

- [[tools/toxiproxy]]

## References

- CLI examples in repo
