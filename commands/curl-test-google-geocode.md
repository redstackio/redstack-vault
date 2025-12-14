---
id: cmd-001-curl-geocode
data: >-
  curl
  "https://maps.googleapis.com/maps/api/geocode/json?latlng=40,30&key=AIza████████DM"
tags:
  - api-test
  - recon
type: command
output: |-
  {
    "results": [
      {
        "address_components": [...],
        "formatted_address": "...",
        "geometry": {...},
        "place_id": "...",
        "types": [...]
      }
    ],
    "status": "OK"
  }
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T12:00:00Z'
updated_at: '2025-12-14T17:32:48.552Z'
verified: false
validated: true
submitted: true
---
# curl-test-google-geocode

## Command

```bash
curl "https://maps.googleapis.com/maps/api/geocode/json?latlng=40,30&key=AIza████████DM"
```

## Description

This command tests a Google Geocode API key by requesting reverse geocoding for coordinates 40,30, revealing if the key is valid and unrestricted for unauthorized use.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `latlng` | Comma-separated latitude and longitude | Yes |
| `key` | Google API key | Yes |

## Examples

### Basic Usage

```bash
curl "https://maps.googleapis.com/maps/api/geocode/json?latlng=40,30&key=AIza████████DM"
```

### Advanced Usage

```bash
curl "https://maps.googleapis.com/maps/api/geocode/json?address=New+York&key=AIza████████DM"
```

## Expected Output

JSON object with 'status': 'OK' and geocode results if successful; 'REQUEST_DENIED' if restricted.

## Related

- [[curl]]
- [[procedures/Test-Leaked-API-Key-for-Unauthorized-Usage]]
