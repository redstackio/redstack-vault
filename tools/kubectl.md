---
id: tool-kubectl-001
url: 'https://kubernetes.io/docs/reference/kubectl/'
tags:
  - kubernetes
  - cli
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.669Z'
validated: true
submitted: true
---
# kubectl

**Status**: Unverified

## Overview

Kubectl is the Kubernetes command-line tool for interacting with clusters, used to create resources, proxy, and manage webhooks in this SSRF attack.

## Description

Essential for deploying malicious configurations and triggering exploits. Supports YAML applies, proxy for debug, and resource creation.

## Features

- Feature 1: Declarative resource management
- Feature 2: Proxy and port-forwarding
- Feature 3: Logging and debugging commands

## Installation

### Requirements

- Go 1.16+ or binary download

### Install Commands

```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install kubectl /usr/local/bin/
```

## Basic Usage

```bash
kubectl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-f, --filename` | YAML/JSON file |
| `--dry-run` | Simulate apply |

## Examples

### Example 1: Basic Usage

```bash
kubectl get pods
```

### Example 2: Advanced Usage

```bash
kubectl create -f webhook.yaml
kubectl proxy &
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Windows Command Shell]] Windows Command Shell (analogous for k8s)

### Tactics

- [[Execution]] Execution

## Detection

- Audit kubectl commands in cluster logs
- RBAC restrictions on sensitive operations

## Related Procedures

- [[procedures/Create-Malicious-Admission-Webhook]]

## Related Tools

- [[tools/minikube]]
- [[tools/helm]]

## References

- Official documentation: https://kubernetes.io/docs/reference/kubectl/
