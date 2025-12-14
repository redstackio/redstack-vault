---
id: cmd-minikube-start-vuln-001
data: minikube start --vm-driver=none --kubernetes-version='v1.18.6'
tags:
  - setup
  - kubernetes
type: command
output: |-
  Starting cluster...
  Minikube has been configured to use the none driver
  ...
  Done! kubectl is now configured to use "minikube" cluster
executor: bash
platforms:
  - Linux
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.692Z'
verified: false
validated: true
submitted: true
---
# start-minikube-vulnerable

## Command

```bash
minikube start --vm-driver=none --kubernetes-version='v1.18.6'
```

## Description

Starts a local Kubernetes cluster using minikube at the vulnerable v1.18.6 version with no VM isolation for direct host simulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--vm-driver` | Driver type (none for host-direct) | Yes |
| `--kubernetes-version` | Cluster version to use | Yes |

## Examples

### Basic Usage

```bash
minikube start --vm-driver=none --kubernetes-version='v1.18.6'
```

### Advanced Usage

```bash
minikube start --vm-driver=none --kubernetes-version='v1.18.6' --cpus=2 --memory=4096
```

## Expected Output

Cluster initialization progress, ending with kubeconfig update and API server ready.

## Related

- [[commands/verify-kubectl]]
- [[procedures/Setup-Vulnerable-Kubernetes-Cluster]]
