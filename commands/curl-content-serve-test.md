---
id: cmd-curl-content-serve-test
data: 'curl -I https://openapi.starbucks.com/unused-url'
tags:
  - web
  - poc
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.587Z'
verified: false
validated: true
submitted: true
---
# curl-content-serve-test

## Command

```bash
curl -I https://openapi.starbucks.com/unused-url
```

## Description

Sends a HEAD request to test if custom content is served from a subdomain URL, verifying takeover PoC without full download.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Fetch headers only | Yes |
| `https://openapi.starbucks.com/unused-url` | Target URL to probe | Yes |

## Examples

### Basic Usage

```bash
curl -I https://openapi.starbucks.com/unused-url
```

### Advanced Usage

```bash
curl -v https://openapi.starbucks.com/unused-url
```

## Expected Output

HTTP headers like "HTTP/1.1 200 OK Content-Type: text/html", confirming custom content accessibility.

## Related

- [[Related Procedure: Demonstrate-Non-Destructive-PoC-for-Takeover]]
