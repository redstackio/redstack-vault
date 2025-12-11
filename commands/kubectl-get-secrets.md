---
data: kubectl get secrets --all-namespaces
tags:
  - kubernetes
  - credential-access
type: command
executor: bash
platforms:
  - Kubernetes
  - Linux
id: d27909be-1981-4a82-99a1-2d65a15aa842
created_at: '2025-12-10T05:44:16.336Z'
updated_at: '2025-12-10T05:44:16.336Z'
verified: false
validated: true
submitted: true
---
# kubectl-get-secrets

## Command

```bash
kubectl get secrets --all-namespaces
```

## Description

This command retrieves a list of secrets stored in the Kubernetes cluster, which can contain credentials and sensitive data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--all-namespaces` | Include all namespaces | No |
| `-o yaml` | Output in YAML format | No |

## Examples

### Basic Usage

```bash
kubectl get secrets --all-namespaces
```

### Advanced Usage

```bash
kubectl get secret <name> -o yaml
```

## Expected Output

List of secrets or detailed YAML with base64-encoded data.

## Related

- #kubectl-run-job
- [[procedures/Retrieve-Internal-Credentials-from-Kubernetes]]
