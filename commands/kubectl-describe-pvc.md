---
id: cmd-kubectl-describe-pvc
data: kubectl describe pvc xxx
tags:
  - kubernetes
  - debugging
type: command
output: PVC details with events containing leaked JSON
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:54.830Z'
verified: false
validated: true
submitted: true
---
---

# kubectl-describe-pvc

## Command

```bash
kubectl describe pvc xxx
```

## Description

Describes a PersistentVolumeClaim, revealing status, events, and leaked responses from SSRF provisioning failures.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `pvc` | Name of the PVC (e.g., xxx or poc-ssrf) | Yes |

## Examples

### Basic Usage

```bash
kubectl describe pvc poc-pvc
```

### Advanced Usage

```bash
kubectl describe pvc poc-pvc -n default
```

## Expected Output

Detailed PVC info including Events section with JSON leaks from internal services.

## Related

- [[commands/kubectl-get-events]]
- [[procedures/Retrieve-Internal-Responses-via-Redirects-and-Events]]

---
