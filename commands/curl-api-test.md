---
id: cmd-uuid-3
data: >-
  curl
  "https://maps.googleapis.com/maps/api/staticmap?key=YOUR_API_KEY&center=40.714%2C-74.006&zoom=12&size=400x400&format=png"
tags:
  - api-test
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:38.656Z'
verified: false
validated: true
submitted: true
---
# curl-api-test

## Command

```bash
curl "https://maps.googleapis.com/maps/api/staticmap?key=YOUR_API_KEY&center=40.714%2C-74.006&zoom=12&size=400x400&format=png"
```

## Description

Tests a Google Maps Static API key by requesting a sample map image to verify validity and restrictions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `key=YOUR_API_KEY` | API key parameter | Yes |
| `center=...` | Map center coordinates | Yes |
| `zoom=12` | Zoom level | No |
| `size=400x400` | Image dimensions | No |
| `format=png` | Output format | No |

## Examples

### Basic Usage

```bash
curl "https://maps.googleapis.com/maps/api/staticmap?key=AIza...&center=0,0&zoom=1&size=200x200"
```

### Advanced Usage

```bash
curl -s -o map.png "https://maps.googleapis.com/maps/api/staticmap?key=AIza...&center=NYC&zoom=10"
```

## Expected Output

Binary PNG data on success (HTTP 200); error JSON on failure (e.g., {"error_message":"Invalid key"}).

## Related

- [[Related Procedure: Test-and-Abuse-Unrestricted-Google-Maps-API-Key]]
