---
id: cmd-22
data: 'k cp shell-78d66f6f7c-ft7ch:/admin.token admin.token'
tags:
  - file-transfer
type: command
output: File copied
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.490Z'
verified: false
validated: true
submitted: true
---
# kubectl-cp-admin-token

## Command

```bash
k cp shell-78d66f6f7c-ft7ch:/admin.token admin.token
```

## Description

Copies the admin token file from master pod to local.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `pod:/path` | Source | Yes |
| `local` | Dest | Yes |

## Examples

### Basic Usage

```bash
k cp pod:/admin.token .
```

## Expected Output

File transferred.

## Related

- [[commands/export-cloudsdk-admin-token]]
