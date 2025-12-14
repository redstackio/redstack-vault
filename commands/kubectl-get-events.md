---
id: cmd-kubectl-get-events
data: kubectl get event
tags:
  - kubernetes
  - events
type: command
output: List of events with provisioning details
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:54.821Z'
verified: false
validated: true
submitted: true
---
---

# kubectl-get-events

## Command

```bash
kubectl get event
```

## Description

Retrieves recent cluster events, useful for extracting leaked SSRF responses from provisioning activities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--namespace` | Filter to specific namespace (default: all) | No |

## Examples

### Basic Usage

```bash
kubectl get event
```

### Advanced Usage

```bash
kubectl get events --sort-by='.lastTimestamp' --namespace=default
```

## Expected Output

Table of events including provisioning failures with embedded JSON from internal APIs.

## Related

- [[commands/kubectl-describe-pvc]]
- [[procedures/Retrieve-Internal-Responses-via-Redirects-and-Events]]

---
