---
url: 'https://podman.io/'
tags:
  - container
  - rce
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:53.975Z'
id: f0928742-a989-4c9f-bb03-c1c5cf6c67f5
validated: true
submitted: true
---
# podman

**Status**: Unverified

## Overview

Podman is a daemonless container engine for running OCI containers, used by Taskcluster workers to execute tasks. In this context, it's vulnerable to command injection via unsanitized environment variable names in 'podman run' commands.

## Description

Podman provides Docker-compatible CLI for managing containers without a central daemon. In Taskcluster, workers construct podman commands from task definitions, applying shell.escape to most fields but not env names, enabling RCE. Common in cloud environments like GCP for isolated task execution.

## Features

- Feature 1: Daemonless operation for security
- Feature 2: Rootless containers by default
- Feature 3: Pod and Kubernetes YAML support

## Installation

### Requirements

- Linux kernel with user namespaces
- OCI runtime (default: runc)

### Install Commands

```bash
# On Fedora/RHEL
sudo dnf install podman

# On Ubuntu
sudo apt install podman
```

## Basic Usage

```bash
podman --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--rootful` | Run as root |
| `-e, --env` | Set environment variables |

## Examples

### Example 1: Basic Usage

```bash
podman run ubuntu:latest echo hello
```

### Example 2: Advanced Usage

```bash
podman run -e "VAR=value" --rm ubuntu:latest env
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unix Shell]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor podman run logs for unsanitized env vars
- Detect anomalous command chains in process arguments
- Alert on container escapes via injected payloads

## Related Procedures


## Related Tools

- [[docker]]
- [[runc]]

## References

- Official documentation: https://docs.podman.io/
- Taskcluster integration: https://docs.taskcluster.net/docs/reference/integrations/generic-worker/podman
