---
id: cmd-curl-admin-access
data: 'curl -i ''https://plus-website.shopifycloud.com/admin.php?_page=1'''
tags:
  - web
  - access
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.053Z'
verified: false
validated: true
submitted: true
---
# curl-access-admin

## Command

```bash
curl -i 'https://plus-website.shopifycloud.com/admin.php?_page=1'
```

## Description

This command uses curl to perform an HTTP GET request to an exposed admin panel URL, retrieving the response to check for unauthenticated access. It includes headers (-i) to show status and response details, useful for verifying if the admin interface loads without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers in output | Yes |
| URL | Target admin endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -i 'https://plus-website.shopifycloud.com/admin.php?_page=1'
```

### Advanced Usage

```bash
curl -i -X POST -d 'test=param' 'https://plus-website.shopifycloud.com/admin.php?_page=1'
```

## Expected Output

A successful response shows HTTP/1.1 200 OK followed by HTML content rendering the admin panel, including partner profile data. If redirected, expect 302 status to a login page.

## Related

- [[Related Procedure|procedures/Access-Exposed-Admin-Panel-Without-Authentication]]
