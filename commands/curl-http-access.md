---
data: 'curl -i http://genghis-cdn.shopify.io/'
tags:
  - http
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.599Z'
id: c58511c9-1579-42a2-b558-0a6b95fdb0d7
verified: false
validated: true
submitted: true
---
# curl-http-access

## Command

```bash
curl -i http://genghis-cdn.shopify.io/
```

## Description

This command uses curl to send an HTTP request to a target subdomain and inspect the response headers and body for error indicators, such as provider-specific messages signaling a potential subdomain takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers in output | Yes |
| `http://genghis-cdn.shopify.io/` | The target URL to access | Yes |

## Examples

### Basic Usage

```bash
curl -i http://genghis-cdn.shopify.io/
```

### Advanced Usage

```bash
curl -i -H "User-Agent: Mozilla/5.0" http://genghis-cdn.shopify.io/
```

## Expected Output

HTTP/1.1 404 Not Found or similar, with body containing 'Fastly error: unknown domain: genghis-cdn.shopify.io. Please check that this domain has been added to a service.'

## Related

- [[commands/host-dns-lookup]]
- [[procedures/Detect-Subdomain-Takeover-via-HTTP-Access]]
