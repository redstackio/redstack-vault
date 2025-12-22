---
id: cmd-uuid-1
data: 'curl -I "https://tinyurl.com/ybk7sqrg"'
tags:
  - verification
  - http
type: command
output: 'HTTP/1.1 301 Moved Permanently\nLocation: http://0:6000/\n...'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:18.649Z'
verified: false
validated: true
submitted: true
---
# curl-verify-redirect

## Command

```bash
curl -I "https://tinyurl.com/ybk7sqrg"
```

## Description

Performs a HEAD request to a TinyURL to verify it redirects to the intended internal endpoint, useful for SSRF payload preparation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Fetch headers only | Yes |
| URL | The short URL to test | Yes |

## Examples

### Basic Usage

```bash
curl -I "https://tinyurl.com/ybk7sqrg"
```

### Advanced Usage

```bash
curl -I -L "https://tinyurl.com/ybk7sqrg"  # Follow redirect
```

## Expected Output

Headers showing 301/302 status and Location: http://0:6000/ indicating successful redirect setup.

## Related

- [[commands/curl-trigger-ssrf]]
