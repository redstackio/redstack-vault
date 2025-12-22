---
id: cmd-uuid-001
data: 'curl -I http://target.com/admin'
tags:
  - recon
  - http-probe
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.401Z'
verified: false
validated: true
submitted: true
---
# curl-check-path

## Command

```bash
curl -I http://target.com/admin
```

## Description

Probes an HTTP endpoint to check for existence and status without downloading the full body, useful for reconnaissance of admin paths in web applications like Spring Boot Admin.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | HEAD request only (headers) | Yes |
| `http://target.com/admin` | Target URL to probe | Yes |

## Examples

### Basic Usage

```bash
curl -I http://target.com/admin
```

### Advanced Usage

```bash
curl -I -H "User-Agent: Mozilla/5.0" http://target.com/admin
```

## Expected Output

HTTP/1.1 200 OK or 302 Found if exposed; 404 Not Found if absent. Look for Server headers indicating Spring Boot.

## Related

- [[Related Procedure: Discover-Exposed-Spring-Boot-Admin-Instance]]
