---
id: cmd-curl-get-modern
data: >-
  curl -X GET
  "https://api.mapbox.com/styles/v1/{username}/{style_id}?access_token={your_token}"
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
tags:
  - http
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.304Z'
verified: false
validated: true
submitted: true
---
# curl-get-styles-modern

## Command

```bash
curl -X GET "https://api.mapbox.com/styles/v1/{username}/{style_id}?access_token={your_token}" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

## Description

This command retrieves the style with a modern browser user agent to confirm no execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP GET | Yes |
| `URL` | Endpoint | Yes |
| `-H User-Agent` | Modern browser simulation | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.mapbox.com/styles/v1/user/style1?access_token=pk.ey..." -H "User-Agent: Chrome"
```

## Expected Output

Plain JSON response without execution.

## Related

- [[Related Procedure]]
