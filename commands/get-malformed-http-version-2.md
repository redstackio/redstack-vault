---
data: GET /yeettest?yeettest=1 HTTP/1.123456
tags:
  - http
  - malformed
type: command
executor: bash
platforms:
  - Web
id: 9c84f6a7-5a82-47db-96eb-58dbe8393158
created_at: '2025-12-13T09:00:34.350Z'
updated_at: '2025-12-13T09:00:34.350Z'
verified: false
validated: true
submitted: true
---
# GET Malformed HTTP Version 2

## Command

```bash
GET /yeettest?yeettest=1 HTTP/1.123456
```

## Description

Sends a similar malformed HTTP GET request to verify if the poisoned 400 response is served from cache.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `path` | /yeettest?yeettest=1 - same test path | Yes |
| `version` | HTTP/1.123456 - slightly different invalid version | Yes |

## Examples

### Basic Usage

```bash
GET /yeettest?yeettest=1 HTTP/1.123456
```

## Expected Output

Cached 400 Bad Request instead of expected 404.

## Related

- [[commands/get-malformed-http-version-1]]
- [[procedures/Verify-Cached-Poisoned-Response]]
