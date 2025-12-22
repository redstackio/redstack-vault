---
id: 4627e20e-1704-46d2-9994-1755adb85875
name: curl-kubernetes-list-pods-default
type: command
executor: bash
data: >-
  curl -v -H "Authorization: Bearer $_JWT_TOKEN"
  https://$_API_SERVER/api/v1/namespaces/default/pods/
output: null
created_at: '2023-04-06T03:56:01.385942+00:00'
updated_at: '2023-04-10T20:34:01.659280+00:00'
platforms:
  - Kubernetes
tags:
  - discovery
  - kubernetes
verified: true
validated: true
---

# curl-kubernetes-list-pods-default

## Command

```bash
curl -v -H "Authorization: Bearer $_JWT_TOKEN" https://$_API_SERVER/api/v1/namespaces/default/pods/
```

## Description

This command queries the Kubernetes API to list all pods in the default namespace, providing visibility into running containers and their statuses for reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_JWT_TOKEN | Bearer token for API authentication | Yes |
| $_API_SERVER | Kubernetes API server URL (e.g., https://kubernetes.default.svc:443) | Yes |
| -v | Verbose output for request/response details | No |
| -H | Header specification for Authorization | Yes |

## Examples

### Basic Usage

```bash
curl -v -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9..." https://192.168.1.100:6443/api/v1/namespaces/default/pods/
```

### Advanced Usage

Add --insecure for self-signed certs (not recommended in production):

```bash
curl -v --insecure -H "Authorization: Bearer $_JWT_TOKEN" https://$_API_SERVER/api/v1/namespaces/default/pods/
```

## Expected Output

A JSON response with pod details:

```json
{
  "kind": "PodList",
  "items": [
    {
      "metadata": {
        "name": "example-pod",
        "namespace": "default"
      },
      "status": {
        "phase": "Running"
      }
    }
  ]
}
```

Success is indicated by HTTP 200 OK and a non-empty items array; 403 errors mean permission denied.

## Related

- [[procedures/Kubernetes-Endpoint-Enumeration]]
- [[commands/curl-kubernetes-list-secrets-default]]
