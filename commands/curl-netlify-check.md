---
id: uuid-for-cmd3
data: 'curl -I https://$NETLIFY_DOMAIN'
tags:
  - http
  - probe
type: command
output: |-
  HTTP/1.1 200 OK
  Server: Netlify
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.416Z'
verified: false
validated: true
submitted: true
---
# curl-netlify-check

## Command

```bash
curl -I https://$NETLIFY_DOMAIN
```

## Description

Sends a HEAD request to probe a Netlify domain's status, checking for unclaimed indicators.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | HEAD request only | Yes |
| `$NETLIFY_DOMAIN` | Target Netlify URL | Yes |

## Examples

### Basic Usage

```bash
curl -I https://unclaimed-site.netlify.app
```

### Advanced Usage

```bash
curl -I -H "User-Agent: Mozilla/5.0" https://unclaimed-site.netlify.app
```

## Expected Output

Headers showing Netlify server with default or 404 status for unclaimed sites.

## Related

- [[Related Procedure: Verify-Unclaimed-Netlify-Domain]]
