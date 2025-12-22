---
id: 3e51f799-0ebb-43c8-acae-1a182e046e5a
name: cat-kubernetes-service-account-token
type: command
executor: bash
data: cat /run/secrets/kubernetes.io/serviceaccount/token
output: null
created_at: '2023-04-06T03:56:17.375578+00:00'
updated_at: '2023-04-06T03:56:17.385351+00:00'
platforms:
  - Kubernetes
tags:
  - credential-access
  - kubernetes
verified: true
validated: true
---

# cat-kubernetes-service-account-token

## Command

```bash
cat /run/secrets/kubernetes.io/serviceaccount/token
```

## Description

This command reads the Kubernetes service account token file mounted in the pod's filesystem. The token is a JWT used for authenticating pod requests to the API server. Use this inside a compromised pod to extract credentials for privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/run/secrets/kubernetes.io/serviceaccount/token` | Fixed path to the mounted token file in the pod | Yes |

## Examples

### Basic Usage

```bash
cat /run/secrets/kubernetes.io/serviceaccount/token
```

### Advanced Usage

Pipe the output to a variable for immediate use:

```bash
JWT_TOKEN=$(cat /run/secrets/kubernetes.io/serviceaccount/token)
echo $JWT_TOKEN
```

## Expected Output

A single line containing the JWT token string, e.g.:

`eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9 eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtc2VjcmV0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImRlZmF1bHQiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2VhY2NvdW50LnVpZCI6IjAwMDgwMDAtMTAwMC0xMDAwLTEwMDAtMTAwMDAwMDAwMDAwIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OmRlZmF1bHQ6ZGVmYXVsdCJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtc2VjcmV0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImRlZmF1bHQiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2VhY2NvdW50LnVpZCI6IjAwMDgwMDAtMTAwMC0xMDAwLTEwMDAtMTAwMDAwMDAwMDAwIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OmRlZmF1bHQ6ZGVmYXVsdCIsIm5iZiI6MTY4MDcyOTYwMCwiZXhwIjoxNjgwNzMzMjAwfQ.signature`

## Related

- [[procedures/Kubernetes-Privileged-Service-Account-Token-Retrieval]]
