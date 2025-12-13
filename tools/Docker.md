---
url: 'https://www.docker.com'
tags:
  - containerization
  - setup
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: >-
  Containerization platform for running and managing applications in isolated
  environments.
id: e428e90d-0029-4de6-8376-38db1445fe6d
created_at: '2025-12-13T09:01:22.391Z'
updated_at: '2025-12-13T09:01:22.391Z'
verified: false
validated: true
submitted: true
---
# Docker

**Status**: Unverified

## Overview

Docker is a platform for developing, shipping, and running applications inside containers, commonly used in security testing to create reproducible environments for vulnerabilities like the Tomcat request smuggling.

## Description

Docker enables isolation of applications, making it ideal for setting up vulnerable services without affecting the host system. In this context, it's used to deploy and manage Tomcat instances.

## Features

- Container management: Run, stop, and exec into containers
- Port mapping: Expose container ports to host
- Image pulling: From repositories like Docker Hub

## Installation

### Requirements

- Supported OS (Linux preferred)
- Internet access for pulling images

### Install Commands

```bash
# For Ubuntu: sudo apt install docker.io
```

## Basic Usage

```bash
docker --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-d` | Detached mode |

## Examples

### Example 1: Basic Usage

```bash
docker run -d tomcat:10.1.13
```

### Example 2: Advanced Usage

```bash
docker exec -it container_name /bin/sh
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor Docker daemon logs
- Check for unexpected container deployments

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Kubernetes]]

## References

- https://docs.docker.com
