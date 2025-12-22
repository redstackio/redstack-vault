---
id: cmd-curl-fetch
type: command
executor: bash
data: curl fr1.vpn.zomans.com
output: <!-- hackerone.com/ian -->
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.582Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - http
  - verification
verified: false
validated: true
submitted: true
---

# curl-fetch-subdomain

## Command

```bash
curl fr1.vpn.zomans.com
```

## Description

Sends an HTTP GET request to the subdomain to retrieve and display the served content, verifying control after a takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `fr1.vpn.zomans.com` | The URL/subdomain to fetch | Yes |

## Examples

### Basic Usage

```bash
curl fr1.vpn.zomans.com
```

### Advanced Usage

```bash
curl -v fr1.vpn.zomans.com
```

## Expected Output

The raw HTML or content from the server, e.g., a comment like <!-- hackerone.com/ian -->, confirming custom content is served.

## Related

- [[Related Procedure: Serve-and-Verify-Custom-Content-on-Taken-Over-Subdomain]]
