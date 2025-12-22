---
id: cmd-kubectl-create-sa-001
data: kubectl create sa testpoc
tags:
  - service-account
  - trigger
type: command
output: serviceaccount/testpoc created
executor: bash
platforms:
  - Kubernetes
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.678Z'
verified: false
validated: true
submitted: true
---
# create-test-service-account

## Command

```bash
kubectl create sa testpoc
```

## Description

Creates a service account named testpoc, triggering the admission webhook for SSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sa` | Resource type (serviceaccount) | Yes |
| `testpoc` | Name | Yes |

## Examples

### Basic Usage

```bash
kubectl create sa testpoc
```

### Advanced Usage

```bash
kubectl create sa testpoc --dry-run=client -o yaml
```

## Expected Output

Creation confirmation.

## Related

- [[commands/verify-webhook]]
- [[procedures/Trigger-Webhook-with-Service-Account-Creation]]
