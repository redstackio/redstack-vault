---
data: >-
  curl -H "Authorization: Bearer overly_permissive_key"
  https://api.stripo.com/v1/endpoints
tags:
  - api-enumeration
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.777Z'
id: f38ad08f-2b08-46c2-84f1-2f0a818b5f00
verified: false
validated: true
submitted: true
---
# curl-api-enumerate

## Command

```bash
curl -H "Authorization: Bearer overly_permissive_key" https://api.stripo.com/v1/endpoints
```

## Description

Enumerates available API endpoints using an authenticated request, helping map misconfigured access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | HTTP header for auth | Yes |
| `Bearer overly_permissive_key` | API token | Yes |
| `https://api.stripo.com/v1/endpoints` | Enumeration endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: Bearer key" https://api.example.com/endpoints
```

### Advanced Usage

```bash
curl -H "Authorization: Bearer key" https://api.example.com/endpoints -v
```

## Expected Output

JSON list of endpoints, e.g., {"endpoints": ["/v1/storage", "/v1/users"]}.

## Related

- [[Related Procedure: Exploit Overly Permissive API Keys]]
