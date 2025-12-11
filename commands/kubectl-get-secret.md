---
data: >-
  kubectl --client-certificate client.crt --client-key client.pem
  --certificate-authority ca.crt --server https://██████ get secret███████ -n
  ███████ -o yaml
tags:
  - kubernetes
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 01e2675d-3e4f-4d1d-9cf7-9d116a114688
created_at: '2025-12-11T06:10:23.213Z'
updated_at: '2025-12-11T06:10:23.213Z'
verified: false
validated: true
submitted: true
---
# kubectl-get-secret

## Command

```bash
kubectl --client-certificate client.crt --client-key client.pem --certificate-authority ca.crt --server https://██████ get secret███████ -n ███████ -o yaml
```

## Description

Retrieves secret details including token in YAML format using leaked credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--client-certificate` | Client certificate file | Yes |
| `--client-key` | Client private key file | Yes |
| `--certificate-authority` | CA certificate file | Yes |
| `--server` | Kubernetes server URL | Yes |
| `get secret███████ -n ███████ -o yaml` | Get secret as YAML | Yes |

## Examples

### Basic Usage

```bash
kubectl --client-certificate cert.crt --client-key key.pem --certificate-authority ca.crt --server https://k8s-server get secret my-secret -n namespace -o yaml
```

## Expected Output

YAML with secret data including token.

## Related

- [[commands/kubectl-describe-pod]]
- [[procedures/Interact-with-Kubernetes-Cluster-Using-Leaked-Credentials]]
