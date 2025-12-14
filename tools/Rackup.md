---
url: 'https://github.com/rack/rack'
tags:
  - server-launcher
type: tool
verified: false
platforms:
  - Web
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.167Z'
id: 3ec35b64-1311-4cb0-a4c0-a34a8a1724d2
validated: true
submitted: true
---
# Rackup

**Status**: Unverified

## Overview

Rackup is a command-line tool to start Rack-based web applications, used here with Puma to launch the evil gem server.

## Description

It loads config.ru and starts the server with environment variables like RUBYGEMS_PROXY=true.

## Features

- Feature 1: Simple server startup
- Feature 2: Environment variable support
- Feature 3: Integration with various servers

## Installation

### Requirements

- Rack gem

### Install Commands

```bash
# Included with Rack
gem install rack
```

## Basic Usage

```bash
rackup
```

### Common Options

| Option | Description |
|--------|-------------|
| -p | Port |
| -E | Environment |

## Examples

### Example 1: Basic Usage

```bash
rackup
```

### Example 2: Advanced Usage

```bash
RUBYGEMS_PROXY=true rackup -p 9292
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Compromise Hardware Supply Chain]]

### Tactics

- [[Privilege Escalation]]

## Detection

Indicators and methods for detecting this tool's usage:

- rackup process invocations

## Related Procedures

- [[procedures/Set-Up-Malicious-Gem-Server-to-Serve-Deserialization-Payload]]

## Related Tools

- [[tools/Puma]]

## References

- GitHub: https://github.com/rack/rack
