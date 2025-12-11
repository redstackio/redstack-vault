---
url: 'https://kubernetes.io/docs/reference/kubectl/'
tags:
  - kubernetes
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: Command-line interface for Kubernetes cluster management.
id: 6db231c3-1956-4dc9-8e5c-e398338fbed6
created_at: '2025-12-11T06:10:22.945Z'
updated_at: '2025-12-11T06:10:22.945Z'
verified: false
validated: true
submitted: true
---
# kubectl

**Status**: Unverified

## Overview

kubectl is the official CLI for interacting with Kubernetes APIs, used for deploying, inspecting, and managing cluster resources in security contexts.

## Description

Enables authentication via certs or tokens to perform operations like pod exec, secret retrieval, and resource enumeration.

## Features

- Feature 1: Resource management
- Feature 2: Authentication options
- Feature 3: Exec into containers

## Installation

### Requirements

- Kubernetes cluster access

### Install Commands

```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
```

## Basic Usage

```bash
kubectl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--server` | API server URL |
| `--token` | Bearer token |

## Examples

### Example 1: Basic Usage

```bash
kubectl get pods
```

### Example 2: Advanced Usage

```bash
kubectl --token token exec -it pod -- bash
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Deploy Container]]
- [[Command-Line Interface]]

### Tactics

- [[Execution]]
- [[Privilege Escalation]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor Kubernetes API logs
- Audit trail for exec commands

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[helm]]
- [[k9s]]

## References

- https://kubernetes.io/docs/tasks/tools/
