---
id: tool-gcloud-001
url: 'https://cloud.google.com/sdk/gcloud'
tags:
  - gcp
  - cli
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.381Z'
validated: true
submitted: true
---
# gcloud

**Status**: Unverified

## Overview

Google Cloud CLI for managing GCP resources, used here for provisioning GKE clusters in DoS testing.

## Description

gcloud provides commands for Compute Engine, Kubernetes Engine, and more. In this attack, the beta container subcommand creates private clusters with custom scopes and network settings.

## Features

- Feature 1: Cluster management (create, describe, delete)
- Feature 2: Authentication and project configuration
- Feature 3: Integration with kubectl for kubeconfig

## Installation

### Requirements

- Python 3.5+
- Supported OS

### Install Commands

```bash
# On Linux/macOS
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init
```

## Basic Usage

```bash
gcloud --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help |
| `--project` | Specify project |
| `--zone` | Specify zone |

## Examples

### Example 1: Basic Usage

```bash
gcloud container clusters list
```

### Example 2: Advanced Usage

```bash
gcloud beta container clusters create my-cluster --num-nodes=1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- gcloud auth logs in GCP
- API calls from CLI IP

## Related Procedures

- [[procedures/Create-Private-GKE-Cluster]]

## Related Tools

- [[tools/kubectl]]

## References

- Official documentation: https://cloud.google.com/sdk/docs
