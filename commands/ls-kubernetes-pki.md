---
data: ls /etc/kubernetes/pki/
tags:
  - pki
  - escalation
type: command
output: List of cert/key files
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.857Z'
id: e56a4930-2a02-4208-8860-e146d9223760
verified: false
validated: true
submitted: true
---
# ls-kubernetes-pki

## Command

```bash
ls /etc/kubernetes/pki/
```

## Description

Lists Kubernetes PKI files on the host node for potential cert/key extraction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/etc/kubernetes/pki/` | Path to PKI directory | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

Files like "apiserver.crt  apiserver.key  ca.crt".

## Related

- [[procedures/Escape-to-Host-via-Privileged-Pod]]
