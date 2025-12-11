---
data: >-
  kubectl --client-certificate client.crt --client-key client.pem
  --certificate-authority ca.crt --server https://██████ get pods
  --all-namespaces
tags:
  - kubernetes
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: a791cf46-7c52-4cee-b3d1-b5952e0f3fce
created_at: '2025-12-11T06:10:23.340Z'
updated_at: '2025-12-11T06:10:23.340Z'
verified: false
validated: true
submitted: true
---
# kubectl-get-pods

## Command

```bash
kubectl --client-certificate client.crt --client-key client.pem --certificate-authority ca.crt --server https://██████ get pods --all-namespaces
```

## Description

Lists all pods in the Kubernetes cluster using leaked certificates for authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--client-certificate` | Client certificate file | Yes |
| `--client-key` | Client private key file | Yes |
| `--certificate-authority` | CA certificate file | Yes |
| `--server` | Kubernetes server URL | Yes |
| `get pods --all-namespaces` | List pods across namespaces | Yes |

## Examples

### Basic Usage

```bash
kubectl --client-certificate cert.crt --client-key key.pem --certificate-authority ca.crt --server https://k8s-server get pods --all-namespaces
```

## Expected Output

List of namespaces, pod names, status, etc.

## Related

- [[commands/kubectl-create-pod]]
- [[procedures/Interact-with-Kubernetes-Cluster-Using-Leaked-Credentials]]
