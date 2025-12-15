---
id: cmd-5
data: 'k cp shell-5d64dd647c-8l8s6:/default.token default.token'
tags:
  - file-transfer
  - pod
type: command
output: File copied
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.543Z'
verified: false
validated: true
submitted: true
---
# kubectl-cp-token

## Command

```bash
k cp shell-5d64dd647c-8l8s6:/default.token default.token
```

## Description

Copies a file from inside a pod to the local host using kubectl.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `pod:/path` | Source in pod | Yes |
| `local.path` | Destination | Yes |

## Examples

### Basic Usage

```bash
k cp pod:/file.txt file.txt
```

### Advanced Usage

```bash
k cp pod:/dir/ local/dir/ --container=app
```

## Expected Output

File transferred silently or with progress.

## Related

- [[commands/kubectl-exec-ash]]
