---
url: null
tags:
  - containerization
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: Containerization platform for running isolated environments.
id: 81c6af11-a6cb-4d93-a75d-46058bb85ed6
created_at: '2025-12-11T03:47:47.765Z'
updated_at: '2025-12-11T03:47:47.765Z'
verified: false
validated: true
submitted: true
---
# Docker

**Status**: Unverified

## Overview

Docker is used to run and manage containerized Kibana environments for testing and exploitation of vulnerabilities like the Kibana reporting RCE.

## Description

It allows pulling and running specific images, such as Kibana 7.12.0, in interactive mode to access internal binaries like headless_shell.

## Features

- Container isolation: Run applications in sandboxed environments
- Image management: Pull from repositories like docker.elastic.co
- Interactive shells: For direct access to container filesystems

## Installation

### Requirements

- Supported OS
- Internet access

### Install Commands

```bash
# Follow official Docker installation guide for your platform
```

## Basic Usage

```bash
docker --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--rm` | Remove container after exit |

## Examples

### Example 1: Basic Usage

```bash
docker run --rm -it docker.elastic.co/kibana/kibana:7.12.0 bash
```

### Example 2: Advanced Usage

```bash
docker pull docker.elastic.co/kibana/kibana:7.12.0
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor Docker daemon logs for unauthorized pulls
- Network monitoring for repository access

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/headless_shell]]

## References

- Official Docker documentation
