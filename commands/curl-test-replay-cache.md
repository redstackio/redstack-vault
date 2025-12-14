---
id: cmd-curl-test-cache
data: >-
  curl -X POST 'https://api.gatecoin.com/api/v1/keys' -H 'Authorization: Bearer
  REUSED_SIGNATURE' -H 'Content-Type: application/json' -d
  '@initial_request.json' --output test_response.json
tags:
  - api-replay
  - cache-test
type: command
output: 'HTTP 401 duplicate error if cached, or other response.'
executor: bash
platforms:
  - Linux
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.791Z'
verified: false
validated: true
submitted: true
---
# curl-test-replay-cache

## Command

```bash
curl -X POST 'https://api.gatecoin.com/api/v1/keys' \
  -H 'Authorization: Bearer REUSED_SIGNATURE' \
  -H 'Content-Type: application/json' \
  -d '@initial_request.json' \
  --output test_response.json
```

## Description

Tests if the signature is still cached by replaying the initial request; used to monitor cache expiration in timing-based replay attacks on Gatecoin API.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H 'Authorization: Bearer REUSED_SIGNATURE'` | Reused signature header | Yes |
| `-H 'Content-Type: application/json'` | JSON type | Yes |
| `-d '@initial_request.json'` | Load payload from file | Yes |
| `--output test_response.json` | Save response | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://api.gatecoin.com/api/v1/keys' -H 'Authorization: Bearer SIG' -d '@file.json'
```

### Advanced Usage

```bash
curl -v -X POST 'https://api.gatecoin.com/api/v1/keys' -H 'Authorization: Bearer SIG' -d '@file.json' -w '%{http_code}'
```

## Expected Output

Cached: HTTP 401 'same request within millisecond'. Expired: Proceeds to validation or success.

## Related

- [[commands/curl-create-readonly-key]]
- [[procedures/Wait-for-Signature-Cache-Expiration]]
