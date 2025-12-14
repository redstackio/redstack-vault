---
id: cmd-curl-fetch-headers
data: 'curl -I https://doc.owncloud.org/'
tags:
  - reconnaissance
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:26.925Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-headers

## Command

```bash
curl -I https://doc.owncloud.org/
```

## Description

This command uses curl to perform a HEAD request, fetching only the HTTP response headers from the target URL without the body content. It is ideal for quick reconnaissance of server configurations, security headers, and potential vulnerabilities like missing X-XSS-Protection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I, --head` | Fetch headers only (HEAD method) | Yes |
| `URL` | Target endpoint (e.g., https://doc.owncloud.org/) | Yes |

## Examples

### Basic Usage

```bash
curl -I https://doc.owncloud.org/
```

### Advanced Usage

```bash
curl -s -I https://doc.owncloud.org/ | grep -i security
```

## Expected Output

HTTP/2 200 
server: nginx
content-type: text/html; charset=UTF-8
date: Mon, 01 Oct 2023 12:00:00 GMT
(No X-XSS-Protection line indicates absence.)

## Related

- [[Related Procedure|procedures/Inspect-HTTP-Response-Headers]]
