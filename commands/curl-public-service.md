---
id: cmd-uuid-10
data: 'curl -v http://app.test/public-service/public'
tags:
  - http
  - test
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.427Z'
verified: false
validated: true
submitted: true
---
# curl-public-service

## Command

```bash
curl -v http://app.test/public-service/public
```

## Description

Sends a verbose GET request to the public service endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output | No |
| `url` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl http://app.test/public-service/public
```

## Expected Output

HTTP/1.1 200 OK
Public content response.

## Related

- [[commands/curl-protected-service-valid]]
