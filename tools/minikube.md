---
id: tool-minikube-001
url: 'https://minikube.sigs.k8s.io/docs/'
tags:
  - kubernetes
  - local-cluster
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.672Z'
validated: true
submitted: true
---
# minikube

**Status**: Unverified

## Overview

Minikube is a tool for running a single-node Kubernetes cluster locally, ideal for development and vulnerability reproduction like SSRF in admission webhooks.

## Description

It simulates production environments, supporting specific versions for PoCs. Used here with none driver for host-direct execution on vulnerable k8s v1.18.6.

## Features

- Feature 1: Easy single-command cluster start/stop
- Feature 2: Version pinning for reproducibility
- Feature 3: Integration with kubectl and Docker

## Installation

### Requirements

- Virtualization support (or none driver)
- 2GB RAM minimum

### Install Commands

```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

## Basic Usage

```bash
minikube --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help |
| `--vm-driver` | Specify driver (none, virtualbox) |

## Examples

### Example 1: Basic Usage

```bash
minikube start
```

### Example 2: Advanced Usage

```bash
minikube start --vm-driver=none --kubernetes-version=v1.18.6
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

- Monitor for minikube binaries or processes
- Detect unusual local cluster startups in audit logs

## Related Procedures

- [[procedures/Setup-Vulnerable-Kubernetes-Cluster]]

## Related Tools

- [[tools/kubectl]]
- [[tools/kind]]

## References

- Official documentation: https://minikube.sigs.k8s.io/docs/
