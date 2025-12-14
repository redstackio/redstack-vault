---
id: tool-redis-cli
url: 'https://redis.io/docs/management/cli/'
tags:
  - redis
  - database
  - queue
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.452Z'
validated: true
submitted: true
---
# Redis-CLI

**Status**: Unverified

## Overview

Redis CLI is the command-line interface for Redis, an in-memory data store used for caching, queues, and more. In security testing, it's used to interact with Redis-backed systems like GitLab's Sidekiq for enqueuing jobs or data manipulation.

## Description

Redis CLI allows executing commands like RPUSH for list operations, essential for exploiting job queues. It supports connections to remote instances and is lightweight for offensive operations targeting misconfigured Redis servers.

## Features

- Feature 1: Interactive shell for real-time command execution
- Feature 2: Support for authentication and TLS connections
- Feature 3: Pipeline mode for batch operations

## Installation

### Requirements

- Redis server installed (CLI comes bundled)

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update && sudo apt install redis-tools

# On macOS with Homebrew
brew install redis
```

## Basic Usage

```bash
redis-cli --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --host` | Server hostname |
| `-p, --port` | Server port |
| `-a, --auth` | Password authentication |

## Examples

### Example 1: Basic Usage

```bash
redis-cli ping
```

### Example 2: Advanced Usage

```bash
redis-cli -h localhost rpush mylist "value"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to Redis port 6379 from unexpected sources
- Log entries for RPUSH or other queue commands in Redis logs
- Process monitoring for redis-cli executions

## Related Procedures

- [[procedures/Enqueue-Malicious-GitLab-Sidekiq-Job]]

## Related Tools

- [[Burp Suite]]
- [[Metasploit]]

## References

- Official documentation: https://redis.io/docs/management/cli/
- Related resources: Redis security hardening guides
