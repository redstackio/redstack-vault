---
data: GET /yeettest?yeettest=1 HTTP/1.1234567
tags:
  - http
  - malformed
type: command
executor: bash
platforms:
  - Web
id: 2d5bb276-1ac3-4354-914d-39108f0b30f5
created_at: '2025-12-13T09:00:34.353Z'
updated_at: '2025-12-13T09:00:34.353Z'
verified: false
validated: true
submitted: true
---
# GET Malformed HTTP Version 1

## Command

```bash
GET /yeettest?yeettest=1 HTTP/1.1234567
```

## Description

Sends a malformed HTTP GET request with an invalid version to trigger a 400 Bad Request and poison the web cache.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `path` | /yeettest?yeettest=1 - arbitrary test path with parameter | Yes |
| `version` | HTTP/1.1234567 - invalid version to cause error | Yes |

## Examples

### Basic Usage

```bash
GET /yeettest?yeettest=1 HTTP/1.1234567
```

## Expected Output

400 Bad Request response, which gets cached.

## Related

- [[commands/get-malformed-http-version-2]]
- [[procedures/Send-Malformed-HTTP-Request-to-Poison-Cache]]
