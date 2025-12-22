---
id: tool-uuid-1
url: 'https://minikube.sigs.k8s.io/docs/'
tags:
  - kubernetes
  - local-cluster
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.414Z'
validated: true
submitted: true
---
# Minikube

**Status**: Unverified

## Overview

Minikube is a tool for running a local Kubernetes cluster, ideal for testing and reproducing vulnerabilities like ingress auth bypass.

## Description

Provides a single-node Kubernetes environment with addons like NGINX Ingress for simulating production setups. Used here for v1.23.2 on Windows 10 with Docker driver.

## Features

- Feature 1: Local K8s cluster provisioning
- Feature 2: Addon support (ingress, dns)
- Feature 3: Image loading from host Docker

## Installation

### Requirements

- Docker or compatible driver
- 2GB RAM minimum

### Install Commands

```bash
# Windows: choco install minikube
# macOS: brew install minikube
minikube start
```

## Basic Usage

```bash
minikube start
minikube dashboard
```

### Common Options

| Option | Description |
|--------|-------------|
| `--driver` | Specify driver (docker, virtualbox) |
| `--addons` | List available addons |

## Examples

### Example 1: Basic Usage

```bash
minikube start --driver=docker
```

### Example 2: Advanced Usage

```bash
minikube start --kubernetes-version=v1.22.2 --addons=ingress
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Process: minikube.exe or minikube binary
- Network: Local API server on 127.0.0.1:8443

## Related Procedures

- [[procedures/Setup-Minikube-and-Deploy-Vulnerable-Kubernetes-Config]]

## Related Tools

- [[tools/Docker]]
- [[tools/kubectl]]

## References

- Official documentation: https://minikube.sigs.k8s.io/docs/
