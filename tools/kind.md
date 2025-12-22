---
id: tool-kind-001
url: 'https://kind.sigs.k8s.io/'
tags:
  - kubernetes
  - local-cluster
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.372Z'
validated: true
submitted: true
---
# kind

**Status**: Unverified

## Overview

Kubernetes IN Docker (kind) runs local clusters for testing, used to reproduce the DoS vulnerability outside GKE by monitoring API Server memory.

## Description

Kind creates a single-node cluster in Docker, allowing observation of memory growth during concurrent webhook calls without cloud costs.

## Features

- Feature 1: Local K8s clusters
- Feature 2: Multi-node support
- Feature 3: Configurable API Server

## Installation

### Requirements

- Docker
- Go 1.16+

### Install Commands

```bash
go install sigs.k8s.io/kind@v0.20.0
kind version
```

## Basic Usage

```bash
kind --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `create cluster` | Create cluster |
| `delete cluster` | Delete cluster |

## Examples

### Example 1: Basic Usage

```bash
kind create cluster
```

### Example 2: Advanced Usage

```bash
kind create cluster --config config.yaml
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Docker containers named kind*
- Local port 6443 usage

## Related Procedures

- Reproduction in attack chain

## Related Tools

- [[tools/kubectl]]

## References

- Official documentation: https://kind.sigs.k8s.io/docs/
