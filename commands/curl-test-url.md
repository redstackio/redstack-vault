---
id: c-curl-test-url
data: curl "%s" %s
tags:
  - web
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.482Z'
verified: false
validated: true
submitted: true
---
# curl-test-url

## Command

```bash
curl "https://example.com?param=value" -v
```

## Description

This command tests web endpoints for vulnerabilities like open redirects by sending HTTP requests and observing responses or redirects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output for headers | No |
| `-L` | Follow redirects | No |
| `URL` | Target URL with parameters | Yes |

## Examples

### Basic Usage

```bash
curl "https://example.com" -v
```

### Advanced Usage

```bash
curl -L "https://example.com?redirect=https://evil.com"
```

## Expected Output

HTTP response or redirect chain, e.g., 302 to arbitrary site.

## Related

- [[Related Procedure]]
