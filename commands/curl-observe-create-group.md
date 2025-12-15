---
data: >-
  curl -X POST 'https://localize.example.com/pages/create_project/3F' -H
  'Content-Type: application/x-www-form-urlencoded' -H 'Cookie:
  session=your_session_cookie' -d
  'CSRFToken=your_csrf_token&group_name=test_group'
tags:
  - web-testing
  - endpoint-probe
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.743Z'
id: 6e703ff1-ed73-4fd6-bad7-902d36db04ea
verified: false
validated: true
submitted: true
---
# curl-observe-create-group

## Command

```bash
curl -X POST 'https://localize.example.com/pages/create_project/3F' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: session=your_session_cookie' \
  -d 'CSRFToken=your_csrf_token&group_name=test_group'
```

## Description

This curl command observes the group creation endpoint by sending a legitimate creation request, helping to analyze response structure for abuse potential.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP method | Yes |
| URL path | Endpoint with owned project ID (e.g., 3F) | Yes |
| `-H 'Content-Type: ...'` | Sets form data encoding | Yes |
| `-H 'Cookie: ...'` | Authenticates the session | Yes |
| `-d 'CSRFToken=...'` | Includes anti-CSRF protection | Yes |
| `-d 'group_name=...'` | Payload for creation | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://localize.example.com/pages/create_project/3F' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: session=abc123' -d 'CSRFToken=token123&group_name=test'
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST 'https://localize.example.com/pages/create_project/3F' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: session=abc123' -d 'CSRFToken=token123&group_name=test'
```

## Expected Output

HTTP 200 OK with JSON response like {"status": "success", "group_id": 100}, confirming endpoint functionality.

## Related

- [[commands/curl-modify-project-id]]
- [[procedures/Observe-Group-Creation-Endpoint-for-Abuse]]
