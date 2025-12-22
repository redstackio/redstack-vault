---
data: kind create cluster --config lab.yaml
tags:
  - kubernetes
  - setup
type: command
output: Cluster creation logs and confirmation
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.892Z'
id: de6c45b4-e4dd-4ccf-915d-51d67e823aba
verified: false
validated: true
submitted: true
---
# kind-create-cluster-with-config

## Command

```bash
kind create cluster --config lab.yaml
```

## Description

Creates a local Kubernetes cluster using the Kind tool with a specified configuration file (lab.yaml), including custom node labels and port mappings for ingress testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--config` | Path to the Kind cluster configuration YAML file | Yes |

## Examples

### Basic Usage

```bash
kind create cluster --config lab.yaml
```

### Advanced Usage

```bash
kind create cluster --config lab.yaml --name mycluster --wait 300s
```

## Expected Output

Logs showing image pulls, node creation, kubeadm init, and finally "Cluster created". Verify with `kubectl get nodes`.

## Related

- [[procedures/Setup-Kind-Kubernetes-Cluster]]
