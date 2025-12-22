---
data: >-
  curl -X POST https://backend.singlestore.com/auth/login -H "Content-Type:
  application/json" -d '{"username": "your_username", "password":
  "your_password"}'
tags:
  - api
  - auth
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:34.565Z'
id: 9143a9f9-220e-4362-8e6b-eeaf37e7a672
verified: false
validated: true
submitted: true
---
# curl-authenticate-singlestore

## Command

```bash
curl -X POST https://backend.singlestore.com/auth/login -H "Content-Type: application/json" -d '{"username": "your_username", "password": "your_password"}'
```

## Description

This command authenticates to the SingleStore backend API using provided credentials, returning an access token for subsequent authenticated requests. Use it as the first step in API interactions requiring authorization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `-H "Content-Type: application/json"` | Sets the request header for JSON payload | Yes |
| `-d '{"username": "...", "password": "..."}'` | JSON body with login credentials | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://backend.singlestore.com/auth/login -H "Content-Type: application/json" -d '{"username": "user@example.com", "password": "pass123"}'
```

### Advanced Usage

Add `-v` for verbose output to debug connection issues:

```bash
curl -v -X POST https://backend.singlestore.com/auth/login -H "Content-Type: application/json" -d '{"username": "user@example.com", "password": "pass123"}'
```

## Expected Output

Successful execution returns JSON like: {"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...", "expires_in": 3600}. Errors return HTTP 401 with {"error": "Invalid credentials"}.

## Related

- [[Related Procedure|procedures/Exploit-IDOR-in-GetNotebookScheduledPaginatedJobs]]
