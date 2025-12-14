---
id: tool-docker-fetch
url: 'https://github.com/NotSoSecure/docker_fetch'
tags:
  - docker
  - registry
  - dumping
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:57.158Z'
validated: true
submitted: true
---
---
# docker_fetch

**Status**: Unverified

## Overview

docker_fetch is a tool for fetching and dumping Docker images from v2 registries, particularly useful against unauthenticated endpoints.

## Description

It interacts with the Docker Distribution API to pull manifests, configs, and layers without docker client, ideal for exploiting exposed registries in pentests.

## Features

- Feature 1: Unauth registry support
- Feature 2: Full image export (tar format)
- Feature 3: API endpoint probing

## Installation

### Requirements

- Go 1.13+ or pre-built binary

### Install Commands

```bash
# From source
go install github.com/NotSoSecure/docker_fetch@latest

# Or download binary from releases
```

## Basic Usage

```bash
docker_fetch --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `<URL>` | Registry base URL |
| `<repo>` | Repository name |
| `-o` | Output directory |

## Examples

### Example 1: Basic Usage

```bash
docker_fetch http://registry:5000 library/nginx
```

### Example 2: Advanced Usage

```bash
docker_fetch http://127.0.0.1:5555 lgtm/top -o dump_dir
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Data from Cloud Storage]] Data from Cloud Storage Object
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- API logs showing repeated GET /v2/ requests
- Unusual download volumes from registry
- Binary execution traces

## Related Procedures


## Related Tools

- [[tools/SSH]]

## References

- Official documentation: https://github.com/NotSoSecure/docker_fetch
- Related resources: Docker Registry API docs

---
