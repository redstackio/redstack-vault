---
id: cmd-14
data: >-
  k config set-credentials pwn --client-certificate=user.pem
  --client-key=user-key.pem
tags:
  - config
  - auth
type: command
output: Credentials updated
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.516Z'
verified: false
validated: true
submitted: true
---
# kubectl-config-set-credentials

## Command

```bash
k config set-credentials pwn --client-certificate=user.pem --client-key=user-key.pem
```

## Description

Sets client certificate and key credentials in kubeconfig.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `pwn` | Credential name | Yes |
| `--client-certificate` | Cert file | Yes |
| `--client-key` | Key file | Yes |

## Examples

### Basic Usage

```bash
k config set-credentials user --client-certificate=cert.pem --client-key=key.pem
```

### Advanced Usage

```bash
k config set-credentials user --token=eyJ...
```

## Expected Output

'Credential "pwn" set'.

## Related

- [[commands/export-kubeconfig]]
