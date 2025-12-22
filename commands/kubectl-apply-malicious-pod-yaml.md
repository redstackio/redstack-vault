---
id: 89286012-5f56-43fe-b44a-5377092c451d
name: kubectl-apply-malicious-pod-yaml
type: command
executor: bash
data: kubectl apply -f malicious-pod.yaml
output: null
created_at: '2023-04-06T03:56:01.251182+00:00'
updated_at: '2023-04-10T20:34:03.127967+00:00'
platforms:
  - Kubernetes
tags:
  - pod-creation
  - kubernetes
verified: true
validated: true
---

# kubectl-apply-malicious-pod-yaml

## Command

```bash
kubectl apply -f malicious-pod.yaml
```

## Description

This command applies a Kubernetes Pod manifest from a YAML file to the cluster, creating or updating the pod as defined. It is used in this context to deploy a malicious pod that abuses RBAC for data exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-f malicious-pod.yaml` | Path to the YAML file containing the Pod specification | Yes |
| `apply` | Declarative mode to create or update resources based on the file | Built-in |

## Examples

### Basic Usage

```bash
kubectl apply -f malicious-pod.yaml
```

### Advanced Usage

To apply and then watch the pod status:

```bash
kubectl apply -f malicious-pod.yaml && kubectl get pods -n kube-system -w
```

## Expected Output

Success confirmation:

```
pod/alpine created
```

Errors may include "Error from server (Forbidden): pods \"alpine\" is forbidden" if RBAC permissions are insufficient.

## Related

- [[procedures/Abuse-Kubernetes-Bootstrap-Signer-RBAC-to-Deploy-Malicious-Pod]]
