---
id: cmd-uuid-7936-inspect
data: >-
  curl -X POST https://www.secret.ly/_/login -H "Content-Type: application/json"
  -d '{"Login":"test@example.com","Password":"testpass"}'
tags:
  - web
  - inspection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:27:23.467Z'
verified: false
validated: true
submitted: true
---
# curl-login-inspect

## Command

```bash
curl -X POST https://www.secret.ly/_/login -H "Content-Type: application/json" -d '{"Login":"test@example.com","Password":"testpass"}'
```

## Description

This command tests the login endpoint by sending a sample JSON POST request to inspect for CSRF protection. It helps verify if the endpoint accepts requests without tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `-H "Content-Type: application/json"` | Sets the request header for JSON | Yes |
| `-d '{...}'` | JSON payload with credentials | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.secret.ly/_/login -H "Content-Type: application/json" -d '{"Login":"test@example.com","Password":"testpass"}'
```

### Advanced Usage

```bash
curl -X POST https://www.secret.ly/_/login -H "Content-Type: application/json" -H "Referer: evil.com" -d '{"Login":"test@example.com","Password":"testpass"}'
```

## Expected Output

A JSON response from the server, such as {"success": false, "message": "Invalid credentials"}, without CSRF-related errors, indicating vulnerability.

## Related

- [[Related Procedure|procedures/Inspect-Login-Endpoint-for-CSRF-Protection]]
