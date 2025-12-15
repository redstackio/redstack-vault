---
id: cmd-uuid-11
data: >-
  curl -v http://app.test/protected-service/protected -H "X-Api-Key:
  secret-api-key"
tags:
  - http
  - auth
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.420Z'
verified: false
validated: true
submitted: true
---
# curl-protected-service-valid

## Command

```bash
curl -v http://app.test/protected-service/protected -H "X-Api-Key: secret-api-key"
```

## Description

Tests protected endpoint with valid API key.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Custom header | Yes |

## Examples

### Basic Usage

```bash
curl -H "X-Api-Key: secret-api-key" http://app.test/protected-service/protected
```

## Expected Output

HTTP/1.1 200 OK
Protected content.
