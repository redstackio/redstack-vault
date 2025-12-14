---
data: 'curl -I https://sub.mozaws.net'
tags:
  - web
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.445Z'
id: ac9b6f31-fb4b-4999-8b4c-0721d3f99e21
verified: false
validated: true
submitted: true
---
# curl Upload Test

## Command

```bash
curl -I https://sub.mozaws.net
```

## Description

Sends a HEAD request to verify if custom content is hosted on the subdomain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -I | HEAD request only | Yes |
| https://sub.mozaws.net | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -I https://sub.mozaws.net
```

### Advanced Usage

```bash
curl -I -H "User-Agent: Mozilla" https://sub.mozaws.net
```

## Expected Output

HTTP/1.1 200 OK with custom server headers.

## Related

- [[commands/dig-dns-lookup]]
