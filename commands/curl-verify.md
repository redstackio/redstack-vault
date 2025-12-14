---
data: 'curl -I https://s00397nasv101-datacafe-cert.azurewebsites.net/'
tags:
  - http
  - probe
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:01.971Z'
id: c6614ffd-06a4-4d49-95e0-b86396fde8bc
verified: false
validated: true
submitted: true
---
# curl-verify

## Command

```bash
curl -I https://s00397nasv101-datacafe-cert.azurewebsites.net/
```

## Description

Sends a HEAD request to check if a cloud endpoint is live or unclaimed, useful for takeover validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | HEAD request | Yes |
| `URL` | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -I https://example.azurewebsites.net/
```

### Advanced Usage

```bash
curl -I -k --max-time 10 https://unclaimed.azurewebsites.net/
```

## Expected Output

HTTP 404 or connection refused for unclaimed.

## Related

- [[commands/curl-access]]
