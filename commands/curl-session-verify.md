---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: 'curl -b cookies.txt http://<device-ip>/status.cgi -v'
tags:
  - verification
type: command
output: <html><body>Device Status Dashboard...</body></html>
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:29:44.510Z'
verified: false
validated: true
submitted: true
---
# curl-session-verify

## Command

```bash
curl -b cookies.txt http://<device-ip>/status.cgi -v
```

## Description

Verifies an active session by fetching a protected read-only page like the status dashboard, using the stored cookie to bypass login.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-b cookies.txt` | Load cookies from file | Yes |
| `http://<device-ip>/status.cgi` | Target protected endpoint | Yes |
| `-v` | Verbose output | No |

## Examples

### Basic Usage

```bash
curl -b cookies.txt http://192.168.1.1/status.cgi
```

### Advanced Usage

```bash
curl -b cookies.txt -H "User-Agent: Mozilla/5.0" https://192.168.1.1/status.cgi -k
```

## Expected Output

HTML content of the dashboard indicating successful access; 401 error if session invalid.

## Related

- [[Related Procedure]]
