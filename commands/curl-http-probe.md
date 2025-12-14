---
id: cmd-uuid-002
data: 'curl -I http://production.s3.rubygems.org/'
tags:
  - http
  - validation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.684Z'
verified: false
validated: true
submitted: true
---
# curl-http-probe

## Command

```bash
curl -I http://production.s3.rubygems.org/
```

## Description

This command probes an HTTP endpoint on a subdomain to check for service configuration errors, such as Fastly's unconfigured response, confirming a dangling DNS record.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Performs a HEAD request only (headers) | Yes |
| `http://production.s3.rubygems.org/` | The URL to probe | Yes |

## Examples

### Basic Usage

```bash
curl -I http://production.s3.rubygems.org/
```

### Advanced Usage

```bash
curl -I -H "Host: production.s3.rubygems.org" http://fastly-ip/
```

## Expected Output

HTTP headers with status 404 or error body indicating "No service configured for this domain" from Fastly.

## Related

- [[Related Procedure|procedures/Discover-Dangling-DNS-Records-for-Subdomain-Takeover]]
