---
data: 'curl -i http://www.grouplogic.com/ADMIN/store/index.cfm'
tags:
  - recon
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.493Z'
id: 9bca9fb8-4bfd-4988-a4a4-72c4ecf35c85
verified: false
validated: true
submitted: true
---
# curl-admin-access-test

## Command

```bash
curl -i http://www.grouplogic.com/ADMIN/store/index.cfm
```

## Description

This command uses curl to send an HTTP request to the target admin endpoint and inspect the response, verifying if the page is accessible without authentication. It is useful for initial reconnaissance of access control vulnerabilities in web applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers in output | Yes |
| `http://www.grouplogic.com/ADMIN/store/index.cfm` | The target admin URL to test | Yes |

## Examples

### Basic Usage

```bash
curl -i http://www.grouplogic.com/ADMIN/store/index.cfm
```

### Advanced Usage

```bash
curl -i -H "User-Agent: Mozilla/5.0" http://www.grouplogic.com/ADMIN/store/index.cfm
```

## Expected Output

A 200 OK status code with HTML content indicating the admin interface loads, rather than a 401/403 error or login redirect. Headers may show server details like ColdFusion version.

## Related

- [[Related Procedure|procedures/Access-Store-Admin-Without-Authentication]]
