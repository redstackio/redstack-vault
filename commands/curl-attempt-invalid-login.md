---
data: >-
  curl -X POST -d "username=$USERNAME&password=$WRONGPASS" $TARGET_URL/login -c
  cookies.txt -v
tags:
  - enumeration
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:47.415Z'
id: 25f2899c-7838-4283-9313-a8a35aa1beee
verified: false
validated: true
submitted: true
---
# curl-attempt-invalid-login

## Command

```bash
curl -X POST -d "username=$USERNAME&password=$WRONGPASS" $TARGET_URL/login -c cookies.txt -v
```

## Description

This command sends an HTTP POST request to a login endpoint with a known username and intentionally incorrect password to test for 2FA prompts, enabling enumeration of 2FA status based on response differences.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method for form submission | Yes |
| `-d "username=$USERNAME&password=$WRONGPASS"` | Form data with username and wrong password (use env vars for flexibility) | Yes |
| `$TARGET_URL/login` | Target login endpoint URL | Yes |
| `-c cookies.txt` | Save session cookies to file | No |
| `-v` | Verbose output for headers and response details | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d "username=test@example.com&password=wrong" https://legalrobot.com/login -v
```

### Advanced Usage

```bash
USERNAME="targetuser" WRONGPASS="invalid123" TARGET_URL="https://target.com" curl -X POST -d "username=$USERNAME&password=$WRONGPASS" $TARGET_URL/login -c session_cookies.txt -v > response.html
```

## Expected Output

Verbose curl output showing request/response. For 2FA-enabled: Possible 302 redirect to 2FA page or HTML/JSON with 2FA fields (e.g., <form id="2fa-form">). For non-2FA: 401/403 status with error like "Invalid username or password". Inspect body for prompts.

## Related

- [[Related Procedure: Enumerate-2FA-Enabled-Users-via-Login]]
