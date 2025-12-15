---
url: 'https://kubernetes.io/docs/reference/kubectl/'
tags:
  - kubernetes
  - cli
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:38.906Z'
id: c25cafe9-973c-481e-8289-6f1c79dfb5bf
validated: true
submitted: true
---
# kubectl

**Status**: Unverified

## Overview

kubectl is the command-line tool for interacting with Kubernetes clusters, used to deploy malicious pods and manage deployments for SSRF hijacking.

## Description

Facilitates applying YAML manifests, scaling deployments, and logging in Kubernetes, essential for exploiting aggregated API servers like metrics-server.

## Features

- Feature 1: Resource creation and management
- Feature 2: Namespace operations
- Feature 3: Log and exec access

## Installation

### Requirements

- Kubernetes cluster access
- KUBECONFIG env set

### Install Commands

```bash
# On Linux
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
```

## Basic Usage

```bash
kubectl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -n | Namespace |
| -f | Filename |

## Examples

### Example 1: Basic Usage

```bash
kubectl apply -f go-redirect.yaml
```

### Example 2: Advanced Usage

```bash
kubectl get pods -n kube-system
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- kubectl processes in audits
- Unauthorized applies in kube-system

## Related Procedures

- [[procedures/Deploy-Malicious-Pod-to-Hijack-Metrics-Server]]

## Related Tools

- [[tools/Docker]]

## References

- Official documentation: https://kubernetes.io/docs/reference/kubectl/
