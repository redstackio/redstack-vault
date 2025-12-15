---
data: kubectl run rate --image=busybox
tags:
  - pod-creation
type: command
output: pod/rate-c848c5c8b-5b8vm created
executor: bash
platforms:
  - Kubernetes
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.623Z'
id: 53d5ba81-212e-4570-ae92-ee1fb3e4d0eb
verified: false
validated: true
submitted: true
---
# kubectl-run-pod

## Command

```bash
kubectl run rate --image=busybox
```

## Description

Creates a new pod in the Kubernetes cluster using the specified image, useful for quick deployment in testing or attack scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| run | Subcommand to create a pod | Yes |
| rate | Pod name | Yes |
| --image=busybox | Container image to use | Yes |

## Examples

### Basic Usage

```bash
kubectl run rate --image=busybox
```

### Advanced Usage

```bash
kubectl run rate --image=busybox --restart=Never
```

## Expected Output

"pod/<pod-name> created" with a hashed pod identifier.

## Related

- [[commands/kubectl-exec-pod]]
- [[procedures/Create-Malicious-Kubernetes-Pod]]
