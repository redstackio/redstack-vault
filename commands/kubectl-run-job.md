---
data: kubectl run <job-name> --image=<image> --command -- <command>
tags:
  - kubernetes
  - execution
type: command
executor: bash
platforms:
  - Kubernetes
  - Linux
id: 76c4b871-48ab-4734-8d29-9139d7095f28
created_at: '2025-12-10T05:44:16.334Z'
updated_at: '2025-12-10T05:44:16.334Z'
verified: false
validated: true
submitted: true
---
# kubectl-run-job

## Command

```bash
kubectl run <job-name> --image=<image> --command -- <command>
```

## Description

This command creates and runs a job in Kubernetes, allowing execution of arbitrary commands in a pod for RCE purposes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--image` | Container image to use | Yes |
| `--command` | Command to run | Yes |

## Examples

### Basic Usage

```bash
kubectl run test-job --image=busybox --command -- echo hello
```

### Advanced Usage

```bash
kubectl run malicious --image=busybox --command -- sh -c 'curl http://internal'
```

## Expected Output

Confirmation of job creation and ability to check logs for output.

## Related

- #kubectl-get-pods
- [[procedures/Execute-Arbitrary-Code-as-Cluster-Admin]]
