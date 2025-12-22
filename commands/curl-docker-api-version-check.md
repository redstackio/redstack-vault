---
type: command
executor: bash
data: curl -i -k $_REGISTRY_URL/v2/
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - discovery
  - api
verified: true
validated: true
---

# curl-docker-api-version-check

## Command

```bash
curl -i -k $_REGISTRY_URL/v2/
```

## Description

Sends a HEAD request to the /v2/ endpoint to detect if the service is a Docker registry API v2.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_REGISTRY_URL | Full URL (e.g., http://registry.example.com) | Yes |
| -i | Includes HTTP headers in output | No |
| -k | Ignores SSL certificate validation | No |

## Examples

### Basic Usage

```bash
curl -i -k http://localhost:5000/v2/
```

## Expected Output

```
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Bearer ...
Content-Type: application/json; charset=utf-8
```

Or 200 OK for anonymous access, confirming Docker API.

## Related

- [[procedures/Insecure-Docker-Registry-Pentest]]
