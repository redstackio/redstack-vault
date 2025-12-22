---
data: >-
  POST /users/session HTTP/1.1

  Host: uber.readme.io

  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:42.0)
  Gecko/20100101 Firefox/42.0

  Accept: application/json, text/plain, */*

  Accept-Language: en-GB,en;q=0.5

  Accept-Encoding: gzip, deflate

  Content-Type: application/json;charset=utf-8

  Content-Length: 84

  Cookie: YOUR CONNECT.SID COOKIE HERE

  Connection: close

  Pragma: no-cache

  Cache-Control: no-cache


  {"email":"readme2@thursday.eml.cc","password":"pjJnBODjkLFv!!11","action":"session"}
tags:
  - authentication
  - http-post
type: command
executor: bash
platforms:
  - Web
id: 21160d2e-e859-4ba3-99cc-7dd0cffac157
created_at: '2025-12-13T23:56:20.318Z'
updated_at: '2025-12-13T23:56:20.318Z'
verified: false
validated: true
submitted: true
---
# Authenticate Session POST

## Command

```bash
POST /users/session HTTP/1.1
Host: uber.readme.io
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:42.0) Gecko/20100101 Firefox/42.0
Accept: application/json, text/plain, */*
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
Content-Length: 84
Cookie: YOUR CONNECT.SID COOKIE HERE
Connection: close
Pragma: no-cache
Cache-Control: no-cache

{"email":"readme2@thursday.eml.cc","password":"pjJnBODjkLFv!!11","action":"session"}
```

## Description

This command sends a POST request to authenticate a session on uber.readme.io using JSON credentials, used to gain authenticated access after obtaining an initial cookie.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `email` | Specifies the email address for authentication (readme2@thursday.eml.cc) | Yes |
| `password` | Specifies the password for authentication (pjJnBODjkLFv!!11) | Yes |
| `action` | Indicates the action as 'session' for login | Yes |
| `Cookie` | Initial connect.sid cookie | Yes |

## Examples

### Basic Usage

```bash
POST /users/session HTTP/1.1
Host: uber.readme.io
... (full headers and body as above)
```

### Advanced Usage

Use with curl: curl -X POST -H "Content-Type: application/json" -d '{"email":"readme2@thursday.eml.cc","password":"pjJnBODjkLFv!!11","action":"session"}' -b "connect.sid=YOURCOOKIE" https://uber.readme.io/users/session

## Expected Output

JSON response containing user details like id, name, email, and accessToken, along with a new connect.sid cookie.

## Related

- [[procedures/Authenticate-Session-via-POST-Request]]
