---
id: cmd-15
data: >-
  k config set-cluster kops --certificate-authority=ca.pem
  --server=https://<kops-ip>
tags:
  - config
  - cluster
type: command
output: Cluster updated
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.513Z'
verified: false
validated: true
submitted: true
---
# kubectl-config-set-cluster

## Command

```bash
k config set-cluster kops --certificate-authority=ca.pem --server=https://<kops-ip>
```

## Description

Configures cluster details including CA and API server in kubeconfig.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `kops` | Cluster name | Yes |
| `--certificate-authority` | CA file | Yes |
| `--server` | API endpoint | Yes |

## Examples

### Basic Usage

```bash
k config set-cluster mycluster --server=https://api.example.com --certificate-authority=ca.crt
```

### Advanced Usage

```bash
k config set-cluster ... --insecure-skip-tls-verify
```

## Expected Output

'Cluster "kops" set'.

## Related

- [[commands/kubectl-config-set-credentials]]
