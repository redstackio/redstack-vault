---
id: cmd-curl-inspect-headers
data: 'curl -L -I http://shop.khanacademy.org/'
tags:
  - recon
  - headers
  - web
type: command
output: |-
  HTTP/1.1 200 OK
  Server: nginx
  X-XSS-Protection: 1; mode=block
  ... (no X-Frame-Options)
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:04.959Z'
verified: false
validated: true
submitted: true
---
# curl-inspect-headers

## Command

```bash
curl -L -I http://shop.khanacademy.org/
```

## Description

This command uses curl to send an HTTP HEAD request to the specified URL, retrieving only the response headers to inspect for security configurations like frame-busting protections. Use it during reconnaissance to detect vulnerabilities such as missing X-Frame-Options for clickjacking risks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Performs a HEAD request (headers only) | Yes |
| `-L` | Follows HTTP redirects (3xx responses) | Yes (for sites with redirects) |
| `http://shop.khanacademy.org/` | The target URL to inspect | Yes |

## Examples

### Basic Usage

```bash
curl -I https://example.com
```

### Advanced Usage

```bash
curl -L -I http://shop.khanacademy.org/ | grep -i frame
```

This pipes output to grep for frame-related headers.

## Expected Output

Description of what output to expect when the command runs successfully.

HTTP/1.1 200 OK with headers like:
- Date: [timestamp]
- Server: nginx
- X-XSS-Protection: 1; mode=block
- Content-Type: text/html
But critically, no X-Frame-Options header, confirming the clickjacking vulnerability.

## Related

- [[Related Procedure: Inspect-HTTP-Headers-for-Clickjacking-Protection]]
