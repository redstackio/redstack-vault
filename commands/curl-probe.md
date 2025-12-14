---
id: cmd-curl-probe
data: 'curl -I https://fddkim.freshdesk.com'
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
updated_at: '2025-12-14T04:38:39.889Z'
verified: false
validated: true
submitted: true
---
# curl-probe

## Command

```bash
curl -I https://fddkim.freshdesk.com
```

## Description

Sends a HEAD request to probe a URL for availability, confirming if a service is active or dangling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | HEAD request only | Yes |
| `URL` | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -I https://example.com
```

### Advanced Usage

```bash
curl -I -k https://fddkim.freshdesk.com
```

## Expected Output

HTTP headers, e.g., 404 Not Found indicating unclaimed.

## Related

- [[Related Procedure: Verify-Dangling-DNS-Records]]
