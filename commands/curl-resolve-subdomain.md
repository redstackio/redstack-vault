---
id: cmd-curl-resolve-subdomain
data: 'curl -I http://service.kiwi.ki/'
tags:
  - recon
  - web-probe
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.269Z'
verified: false
validated: true
submitted: true
---
# curl-resolve-subdomain

## Command

```bash
curl -I http://service.kiwi.ki/
```

## Description

This command performs a HEAD request to a subdomain to check resolution, headers, and service status, useful for identifying dangling records pointing to expired services like FreshDesk.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Fetch headers only (HEAD request) | Yes |
| `http://subdomain/` | Target URL to probe | Yes |

## Examples

### Basic Usage

```bash
curl -I http://service.kiwi.ki/
```

### Advanced Usage

```bash
curl -I -v http://service.kiwi.ki/  # Verbose mode for full details
```

## Expected Output

HTTP/1.1 200 OK
Server: nginx/1.14.0
Content-Type: text/html
... (indicating FreshDesk but expired status in body if followed)

## Related

- [[commands/dig-dns-lookup]]
- [[procedures/Identify-and-Verify-Dangling-Subdomain]]
