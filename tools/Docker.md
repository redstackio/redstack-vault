---
id: f02ce370-55ae-46d2-ae32-00d65b42809c
name: Docker
type: tool
verified: false
created_at: '2025-12-11T06:10:28.479Z'
updated_at: '2025-12-11T06:10:28.479Z'
platforms:
  - Linux
tags:
  - containerization
  - deployment
url: ''
description: >-
  Containerization platform used for installing and running GitLab Enterprise
  Edition.
validated: true
submitted: true
---

# Docker

**Status**: Unverified

## Overview

Docker is a platform for developing, shipping, and running applications inside containers, commonly used for deploying services like GitLab in isolated environments.

## Description

Enables containerization of GitLab Enterprise Edition, allowing easy setup and management of the application for testing vulnerabilities.

## Features

- Feature 1: Container isolation for security testing
- Feature 2: Easy deployment of complex applications
- Feature 3: Portability across environments

## Installation

### Requirements

- Linux host
- Docker engine installed

### Install Commands

```bash
# Follow official Docker installation guide for your OS
```

## Basic Usage

```bash
docker --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --version` | Show version |

## Examples

### Example 1: Basic Usage

```bash
docker run -d gitlab/gitlab-ee:11.9.4-ee
```

### Example 2: Advanced Usage

```bash
docker run -d -p 80:80 gitlab/gitlab-ee:11.9.4-ee
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Escape to Host]]
- [[Exploitation for Client Execution]]

### Tactics

- [[Execution]]
- [[Persistence]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor container creation logs
- Network traffic to Docker registries

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Kubernetes]]
- [[Podman]]

## References

- https://docs.docker.com
