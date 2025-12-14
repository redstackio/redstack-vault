---
data: 'curl -I https://www.sfl-tap.army.mil/'
tags:
  - reconnaissance
  - web
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 2cef03e9-fe44-4f05-a14a-536de347cdac
created_at: '2025-12-14T03:16:20.574Z'
updated_at: '2025-12-14T03:16:20.574Z'
verified: false
validated: true
submitted: true
---
# curl-check-headers

## Command

```bash
curl -I https://www.sfl-tap.army.mil/
```

## Description

This command uses curl to perform a HEAD request to the target URL, retrieving only the HTTP response headers without downloading the body. It is useful for quickly inspecting security headers like X-XSS-Protection during web reconnaissance to detect misconfigurations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I, --head` | Fetch headers only (HEAD request) | Yes |
| `URL` | The target website URL (e.g., https://example.com) | Yes |

## Examples

### Basic Usage

```bash
curl -I https://www.sfl-tap.army.mil/
```

### Advanced Usage

```bash
curl -I -v https://www.sfl-tap.army.mil/  # Verbose mode for full request/response details
```

## Expected Output

HTTP/2 200 
date: Mon, 01 Oct 2023 12:00:00 GMT
server: Apache
x-xss-protection: DENY
content-type: text/html

The output lists headers; success is indicated by a 200 OK status and presence of misconfigured headers like X-XSS-Protection: DENY.

## Related

- [[Related Procedure|procedures/Inspect-HTTP-Response-Headers-Manually]]
