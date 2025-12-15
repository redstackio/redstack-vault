---
data: 'curl -X GET "https://app.smule.com/redirect?url=$URL" -v'
tags:
  - web
  - test
  - redirect
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.397Z'
id: 633bdf06-2c62-45b5-8cae-13c0bd0dc054
verified: false
validated: true
submitted: true
---
# curl-redirect-test

## Command

```bash
curl -X GET "https://app.smule.com/redirect?url=$URL" -v
```

## Description

This command tests open redirect vulnerabilities by sending a GET request to the Smule redirect endpoint with a variable URL payload, using verbose output to inspect headers and redirects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP method | Yes |
| `url=$URL` | Payload URL to test for bypass | Yes |
| `-v` | Verbose mode for headers | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://app.smule.com/redirect?url=https://example.com" -v
```

### Advanced Usage

```bash
curl -X GET "https://app.smule.com/redirect?url=ja%vascript:alert(1)" -v
```

## Expected Output

HTTP/1.1 302 Found with Location header pointing to the payload URL if bypass succeeds; otherwise, 403 or validation error.

## Related

- [[Related Procedure]]
