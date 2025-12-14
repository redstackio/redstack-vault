---
id: cmd-uuid-003
data: 'curl -b cookies.txt http://target.com/admin/applications'
tags:
  - auth-http
  - data-collection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.395Z'
verified: false
validated: true
submitted: true
---
# curl-access-dashboard

## Command

```bash
curl -b cookies.txt http://target.com/admin/applications
```

## Description

Fetches content from an authenticated dashboard endpoint using stored session cookies, allowing retrieval of administrative data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-b cookies.txt` | Load cookies from file | Yes |
| `http://target.com/admin/applications` | Dashboard URL | Yes |

## Examples

### Basic Usage

```bash
curl -b cookies.txt http://target.com/admin/applications
```

### Advanced Usage

```bash
curl -b cookies.txt -H "Accept: application/json" http://target.com/admin/applications
```

## Expected Output

HTML or JSON response with application lists, health metrics, and dashboard elements.

## Related

- [[Related Procedure: Access-Spring-Boot-Admin-Dashboard]]
