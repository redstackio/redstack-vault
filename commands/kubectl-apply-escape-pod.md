---
data: kubectl --kubeconfig sa.kubeconfig apply -f escape_pod.yaml
tags:
  - escape
  - pod
type: command
output: Pod creation confirmation
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.861Z'
id: 3945e7d1-6b60-413b-87c9-a4057ddc412b
verified: false
validated: true
submitted: true
---
# kubectl-apply-escape-pod

## Command

```bash
kubectl --kubeconfig sa.kubeconfig apply -f escape_pod.yaml
```

## Description

Deploys a privileged pod YAML for host escape using escalated kubeconfig.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--kubeconfig` | Path to SA kubeconfig | Yes |
| `-f` | Path to escape pod YAML | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

"pod/escape-pod created".

## Related

- [[procedures/Escape-to-Host-via-Privileged-Pod]]
