---
id: bb257670-3227-43af-b948-d4c4c71eef47
name: curl-kubernetes-api-get-pods
type: command
executor: bash
data: >-
  curl -k -H "Authorization: Bearer $_TOKEN"
  https://$_API_SERVER/api/v1/namespaces/$_NAMESPACE/pods
output: null
created_at: '2023-04-06T03:56:01.090420+00:00'
updated_at: '2023-10-10T20:34:03.470502+00:00'
platforms:
  - Kubernetes
  - Linux
tags:
  - kubernetes
  - api
  - enumeration
verified: true
validated: true
---

# curl-kubernetes-api-get-pods

## Command

```bash
curl -k -H "Authorization: Bearer $_TOKEN" https://$_API_SERVER/api/v1/namespaces/$_NAMESPACE/pods
```

## Description

This command sends a GET request to the Kubernetes API server to retrieve a list of pods in a specified namespace, simulating the `kubectl get pods` command. It uses bearer token authentication and skips SSL verification, useful for internal cluster access where certificates are self-signed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TOKEN | Bearer token for API authentication (e.g., service account JWT) | Yes |
| $_API_SERVER | Kubernetes API server URL (e.g., kubernetes.default.svc:443 or external IP) | Yes |
| $_NAMESPACE | Target namespace (e.g., default, kube-system) | Yes |
| -k | Insecure mode: skip SSL certificate verification | No (but recommended for self-signed certs) |
| -H "Authorization: Bearer ..." | Header for token-based auth | Yes |

## Examples

### Basic Usage

```bash
curl -k -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..." https://kubernetes.default.svc/api/v1/namespaces/default/pods
```

### Advanced Usage

```bash
curl -k -H "Authorization: Bearer $_TOKEN" -H "Accept: application/json" https://$_API_SERVER/api/v1/namespaces/$_NAMESPACE/pods?limit=10
```

## Expected Output

Successful execution returns a JSON object with pod details:

```json
{
  "kind": "PodList",
  "apiVersion": "v1",
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

A 401 Unauthorized indicates invalid token; 403 Forbidden suggests RBAC restrictions.

## Related

- [[procedures/Simulate-Kubectl-API-Requests-with-Curl-and-Python]]
- [[codes/Python-Requests-Kubernetes-API-Get-Pods]]
