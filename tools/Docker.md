---
url: 'https://docker.io/weinong/go-redirect'
tags:
  - container
  - build
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:38.917Z'
id: bf0739d7-aba0-4b18-98b1-c2e314adaf96
validated: true
submitted: true
---
# Docker

**Status**: Unverified

## Overview

Docker is a platform for developing, shipping, and running applications in containers, used here to build the malicious go-redirect image for Kubernetes SSRF exploitation.

## Description

Enables containerization of the Go redirection server, allowing deployment as a pod to hijack metrics-server. Common in offensive ops for creating custom payloads.

## Features

- Feature 1: Image building from source
- Feature 2: Container runtime for testing
- Feature 3: Registry push for Kubernetes pulls

## Installation

### Requirements

- Linux kernel with cgroups
- 2GB+ RAM

### Install Commands

```bash
# On Ubuntu
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

## Basic Usage

```bash
docker --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -t | Tag image |
| -f | Dockerfile path |

## Examples

### Example 1: Basic Usage

```bash
docker build -t weinong/go-redirect .
```

### Example 2: Advanced Usage

```bash
docker run -p 8080:8080 weinong/go-redirect
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Docker daemon processes
- Image pulls from untrusted registries

## Related Procedures

- [[procedures/Build-Malicious-Redirection-Server]]

## Related Tools

- [[tools/kubectl]]

## References

- Official documentation: https://docs.docker.com
