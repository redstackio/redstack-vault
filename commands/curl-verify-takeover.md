---
data: 'curl -I https://sales.mixmax.com'
tags:
  - http
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:23.871Z'
id: f4c2d5f2-06aa-4c99-b0c0-14643e4858ff
verified: false
validated: true
submitted: true
---
# curl-verify-takeover

## Command

```bash
curl -I https://sales.mixmax.com
```

## Description

This command sends an HTTP HEAD request to the subdomain to check response status and headers, verifying if the site is unused (404) or taken over (200 with custom content).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Use HEAD method for headers only | Yes |
| `https://sales.mixmax.com` | The URL to probe | Yes |

## Examples

### Basic Usage

```bash
curl -I https://sales.mixmax.com
```

### Advanced Usage

```bash
curl -v https://sales.mixmax.com
```
(For verbose output including body)

## Expected Output

HTTP headers with status code, e.g., 'HTTP/2 404' for unused, or 'HTTP/2 200' post-takeover with custom server headers.

## Related

- [[curl-full-request]]
- [[procedures/Claim-Unused-Webflow-Site-for-Takeover]]
