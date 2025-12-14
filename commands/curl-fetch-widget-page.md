---
id: cmd-uuid-001
data: 'curl -i https://www.bookfresh.com/cindex.php/widget/customize/'
tags:
  - web
  - recon
  - access-control
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.607Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-widget-page

## Command

```bash
curl -i https://www.bookfresh.com/cindex.php/widget/customize/
```

## Description

This command uses curl to perform an HTTP GET request to the Bookfresh widget customization endpoint, fetching the page content and headers to verify if it loads without authentication. It is useful for testing access control bypass in web applications by simulating direct navigation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers in output | Yes |
| `https://www.bookfresh.com/cindex.php/widget/customize/` | The target URL for the customization page | Yes |

## Examples

### Basic Usage

```bash
curl -i https://www.bookfresh.com/cindex.php/widget/customize/
```

### Advanced Usage

```bash
curl -i -H "User-Agent: Mozilla/5.0" https://www.bookfresh.com/cindex.php/widget/customize/
```

> Adds a browser-like User-Agent header to mimic legitimate traffic.

## Expected Output

A successful response includes HTTP/1.1 200 OK status, followed by headers and the HTML content of the customization page. If vulnerable, no 401/403 errors or login redirects occur. Example snippet:

```
HTTP/1.1 200 OK
Content-Type: text/html
...
<html>...</html>
```

## Related

- [[Related Procedure: Access-Bookfresh-Widget-Customization-Without-Authentication]]
