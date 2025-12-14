---
id: d4e5f6g7-h8i9-0123-defg-456789012345
data: >-
  curl -X POST http://<device-ip>/login.cgi -d
  "username=readonly_user&password=readonly_pass" -c cookies.txt -v
tags:
  - authentication
type: command
output: |-
  HTTP/1.1 302 Found
  Set-Cookie: session=abc123; Path=/
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:29:44.513Z'
verified: false
validated: true
submitted: true
---
# curl-login

## Command

```bash
curl -X POST http://<device-ip>/login.cgi -d "username=readonly_user&password=readonly_pass" -c cookies.txt -v
```

## Description

Authenticates to the Ubiquiti EdgeSwitch HTTP interface using provided read-only credentials, saving the session cookie for subsequent requests. Use this to establish initial access before exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `http://<device-ip>/login.cgi` | Target login endpoint | Yes |
| `-d "username=...&password=..."` | Form data with credentials | Yes |
| `-c cookies.txt` | Save cookies to file | Yes |
| `-v` | Verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl -X POST http://192.168.1.1/login.cgi -d "username=readonly&password=pass" -c cookies.txt
```

### Advanced Usage

```bash
curl -X POST https://192.168.1.1/login.cgi --data-urlencode "username=readonly_user" --data-urlencode "password=readonly_pass" -c cookies.txt -k
```

## Expected Output

Successful response includes a 302 redirect and Set-Cookie header with session token; verbose mode shows full headers confirming authentication.

## Related

- [[Related Procedure]]
