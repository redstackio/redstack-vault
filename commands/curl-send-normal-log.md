---
id: cmd-normal-log-001
data: >-
  curl -X POST 'https://log.quora.com/ajax/batched_log_POST' -d
  'json=%5B%7B%22event%22%3A%22page_view%22%2C%22data%22%3A%22small%22%7D%5D'
tags:
  - http
  - post
  - recon
type: command
output: |-
  HTTP/1.1 200 OK
  Content-Type: application/json
  {"status":"ok"}
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.774Z'
verified: false
validated: true
submitted: true
---
# curl-send-normal-log

## Command

```bash
curl -X POST 'https://log.quora.com/ajax/batched_log_POST' -d 'json=%5B%7B%22event%22%3A%22page_view%22%2C%22data%22%3A%22small%22%7D%5D'
```

## Description

Sends a normal small JSON log payload to Quora's endpoint to observe structure and server response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-d` | Data payload as URL-encoded string | Yes |
| `json=...` | The parameter with encoded JSON array | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://log.quora.com/ajax/batched_log_POST' -d 'json=%5B%7B%22event%22%3A%22page_view%22%2C%22data%22%3A%22small%22%7D%5D'
```

### Advanced Usage

```bash
curl -X POST 'https://log.quora.com/ajax/batched_log_POST' -d 'json=...' -v
```

## Expected Output

HTTP 200 OK response with success status, indicating payload stored.

## Related

- [[commands/curl-send-oversized-log]]
