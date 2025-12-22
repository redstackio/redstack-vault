---
id: 4accb392-9146-4bd4-895f-4c235f079aba-1
name: kubectl-apply-everything-allowed-exec-pod
type: command
executor: bash
data: >-
  kubectl apply -f
  https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/everything-allowed/pod/everything-allowed-exec-pod.yaml
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Kubernetes
tags:
  - kubectl
  - deployment
  - pod
verified: true
validated: true
---

# kubectl-apply-everything-allowed-exec-pod

## Command

```bash
kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/everything-allowed/pod/everything-allowed-exec-pod.yaml
```

## Description

Applies the BadPods manifest for a pod with all risky privileges enabled (privileged, host namespaces, etc.) to test cluster security policies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-f` | Path to YAML manifest (fixed URL here) | Yes |

## Examples

### Basic Usage

```bash
kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/everything-allowed/pod/everything-allowed-exec-pod.yaml
```

### With Namespace

```bash
kubectl apply -n badpods-test -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/everything-allowed/pod/everything-allowed-exec-pod.yaml
```

## Expected Output

```
pod/everything-allowed-exec-pod created
```

## Related

- [[procedures/Deploy-BadPods-for-Kubernetes-Security-Testing]]
- [[tools/kubectl]]
