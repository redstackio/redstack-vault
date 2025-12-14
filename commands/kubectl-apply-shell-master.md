---
id: cmd-19
data: k apply -f shell-master.yaml
tags:
  - deploy
  - master
type: command
output: Pod created on master
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.501Z'
verified: false
validated: true
submitted: true
---
# kubectl-apply-shell-master

## Command

```bash
k apply -f shell-master.yaml
```

## Description

Deploys a pod manifest targeted to the master node via nodeSelector.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-f` | Manifest file | Yes |
| `shell-master.yaml` | Pod spec with node affinity | Yes |

## Examples

### Basic Usage

```bash
k apply -f shell-master.yaml
```

### Advanced Usage

```bash
k apply -f ... --dry-run=client
```

## Expected Output

Pod scheduled on master.

## Related

- [[commands/kubectl-exec-master-ash]]
