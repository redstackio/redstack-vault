---
data: 'curl -I https://nexus.imgur.com/'
tags:
  - recon
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.501Z'
id: df2d0f20-7820-4849-9260-825799c83b4e
verified: false
validated: true
submitted: true
---
# curl-access-nexus-url

## Command

```bash
curl -I https://nexus.imgur.com/
```

## Description

This command performs a HEAD request to check the accessibility of the Nexus Repository Manager URL, useful for confirming public exposure in initial reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Fetch headers only | Yes |
| `https://nexus.imgur.com/` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -I https://nexus.imgur.com/
```

### Advanced Usage

```bash
curl -I -u anonymous:anonymous https://nexus.imgur.com/service/rest/v1/status
```

## Expected Output

HTTP/1.1 200 OK
Server: Nexus/3.x
Content-Type: text/html

Indicates the service is reachable.

## Related

- [[Related Procedure]]
