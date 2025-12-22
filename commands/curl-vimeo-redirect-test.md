---
data: 'curl -L "https://vimeo.com/tools/edit?image=$URL" -I'
tags:
  - web-testing
  - redirect
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:23.325Z'
id: d02b4aca-4819-49e7-93b0-8b892e391a1a
verified: false
validated: true
submitted: true
---
# curl-vimeo-redirect-test

## Command

```bash
curl -L "https://vimeo.com/tools/edit?image=$URL" -I
```

## Description

This command tests open redirection in Vimeo's /tools/edit endpoint by sending a GET request with a crafted image parameter and following redirects to inspect the Location header. Use it to verify if a URL bypasses filters and redirects to an external domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | Follow HTTP redirects | Yes |
| `-I` | Show response headers only | Yes |
| `$URL` | The image parameter value (e.g., http://evil.com?filter/.png) | Yes |

## Examples

### Basic Usage

```bash
curl -L "https://vimeo.com/tools/edit?image=https://vimeocdn.com/image.png" -I
```

### Advanced Usage

```bash
curl -L "https://vimeo.com/tools/edit?image=http://securityidiots.com?vimeocdn.com/.png" -v
```

(Adds -v for verbose output to see full request/response.)

## Expected Output

Successful redirect shows:
```
HTTP/2 302
location: http://securityidiots.com
```

No redirect for invalid URLs shows a 200 or error without Location header.

## Related

- [[Related Procedure]]
