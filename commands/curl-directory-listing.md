---
data: 'curl -i https://try.nextcloud.com/assets/'
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
id: 13b7ae48-0f00-4094-ab5d-7d95ee9eef0e
created_at: '2025-12-14T17:26:17.407Z'
updated_at: '2025-12-14T17:26:17.407Z'
verified: false
validated: true
submitted: true
---
# curl-directory-listing

## Command

```bash
curl -i https://try.nextcloud.com/assets/
```

## Description

This command uses curl to fetch the HTTP response (including headers) for a target directory URL, checking for enabled directory listing. It is useful for reconnaissance on web servers to detect exposed file structures without a browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers in output | Yes |
| `URL` | The target directory path (e.g., https://example.com/assets/) | Yes |

## Examples

### Basic Usage

```bash
curl -i https://try.nextcloud.com/assets/
```

### Advanced Usage

```bash
curl -i -s https://try.nextcloud.com/css/ | grep -E "<a href|Server:"
```

This silent (-s) version pipes output to grep for filtering links and server headers.

## Expected Output

A successful run returns HTTP/1.1 200 OK, headers like Server: Apache/2.4.41 (Ubuntu), Content-Type: text/html, and body with directory listing HTML (e.g., file names in <pre> tags). If disabled, expect 403 Forbidden or 404 Not Found.

## Related

- [[Related Procedure|procedures/Access-Exposed-Directories-via-Listing]]
