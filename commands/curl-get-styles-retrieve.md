---
id: cmd-curl-get-retrieve
data: >-
  curl -X GET
  "https://api.mapbox.com/styles/v1/{username}/{style_id}?access_token={your_token}"
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
updated_at: '2025-12-13T23:52:55.308Z'
verified: false
validated: true
submitted: true
---
# curl-get-styles-retrieve

## Command

```bash
curl -X GET "https://api.mapbox.com/styles/v1/{username}/{style_id}?access_token={your_token}"
```

## Description

This command fetches a Mapbox style to verify payload storage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP GET method | Yes |
| `URL` | API endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.mapbox.com/styles/v1/user/style1?access_token=pk.ey..."
```

## Expected Output

JSON with style details, including unsanitized name.

## Related

- [[Related Procedure]]
