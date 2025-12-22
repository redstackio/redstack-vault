---
id: cmd-curl-status
data: 'curl -I https://support.easycontactnow.com'
tags:
  - web
  - probe
type: command
output: HTTP/1.1 200 OK or redirect headers indicating abandonment.
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:24.048Z'
verified: false
validated: true
submitted: true
---
# curl-check-status

## Command

```bash
curl -I https://support.easycontactnow.com
```

## Description

This command performs a HEAD request to check the HTTP status of a subdomain's service endpoint, helping verify if it's abandoned (e.g., unclaimed Zendesk).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | HEAD request only | Yes |
| `URL` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -I https://example.com
```

### Advanced Usage

```bash
curl -I -L https://support.easycontactnow.com
```

## Expected Output

Headers like "HTTP/1.1 200 OK" with location redirects to signup pages.

## Related

- [[Related Procedure: Verify-Service-Abandonment-for-Takeover]]
