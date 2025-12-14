---
id: tool-docker-001
url: 'https://www.docker.com/'
tags:
  - containerization
  - setup
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T05:32:10.464Z'
validated: true
submitted: true
---
# Docker

**Status**: Unverified

## Overview

Docker is a platform for developing, shipping, and running applications in containers. In security testing, it is used to deploy vulnerable services with resource limits to reproduce exploits like OOM DoS.

## Description

Docker allows isolation of applications in containers, enabling easy setup of environments like Mattermost with memory caps (e.g., 4GB) to observe crashes from resource exhaustion attacks.

## Features

- Feature 1: Containerization for reproducible environments
- Feature 2: Resource limiting (CPU, memory) via flags like -m
- Feature 3: Port publishing for network access

## Installation

### Requirements

- Supported OS (Linux, Windows, macOS)
- Sufficient host resources

### Install Commands

```bash
# On Ubuntu
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

## Basic Usage

```bash
docker --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--version` | Display version info |

## Examples

### Example 1: Basic Usage

```bash
docker run hello-world
```

### Example 2: Advanced Usage

```bash
docker run --name test -d --memory=4g nginx
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Windows Command Shell]] Unix Shell (for container management)

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for docker processes and container creations
- Detection method 2: Log network binds on non-standard ports like 8065

## Related Procedures

- [[procedures/Setup-Mattermost-Docker-Environment]]

## Related Tools

- [[tools/Go]]

## References

- Official documentation: https://docs.docker.com/
