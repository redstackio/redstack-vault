---
data: >-
  kubectl --client-certificate client.crt --client-key client.pem
  --certificate-authority ca.crt --server https://███ describe pods/█████ -n
  █████████
tags:
  - kubernetes
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: ea331168-1353-4dca-ba27-925efc7b46e6
created_at: '2025-12-11T06:10:23.223Z'
updated_at: '2025-12-11T06:10:23.223Z'
verified: false
validated: true
submitted: true
---
# kubectl-describe-pod

## Command

```bash
kubectl --client-certificate client.crt --client-key client.pem --certificate-authority ca.crt --server https://███ describe pods/█████ -n █████████
```

## Description

Describes a specific pod to leak details like secret names using leaked credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--client-certificate` | Client certificate file | Yes |
| `--client-key` | Client private key file | Yes |
| `--certificate-authority` | CA certificate file | Yes |
| `--server` | Kubernetes server URL | Yes |
| `describe pods/█████ -n █████████` | Describe pod in namespace | Yes |

## Examples

### Basic Usage

```bash
kubectl --client-certificate cert.crt --client-key key.pem --certificate-authority ca.crt --server https://k8s-server describe pods/my-pod -n namespace
```

## Expected Output

Detailed pod information including secrets.

## Related

- [[commands/kubectl-get-secret]]
- [[procedures/Interact-with-Kubernetes-Cluster-Using-Leaked-Credentials]]
