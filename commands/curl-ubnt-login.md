---
data: >-
  curl -X POST https://www.ubnt.com/login -d
  "username=validuser&password=validpass" -c cookies.txt -v
tags:
  - auth
  - web
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 822e6309-8224-4bdf-95d3-f491254c7244
created_at: '2025-12-14T17:31:19.772Z'
updated_at: '2025-12-14T17:31:19.772Z'
verified: false
validated: true
submitted: true
---
# curl-ubnt-login

## Command

```bash
curl -X POST https://www.ubnt.com/login -d "username=validuser&password=validpass" -c cookies.txt -v
```

## Description

This command performs a POST request to Ubiquiti's login endpoint with valid credentials, saving session cookies for 2FA follow-up. Use it to initiate authentication in web-based attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-d` | Data payload with username and password | Yes |
| `-c cookies.txt` | Saves cookies to file | Yes |
| `-v` | Verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl -X POST https://www.ubnt.com/login -d "username=validuser&password=validpass" -c cookies.txt
```

### Advanced Usage

```bash
curl -X POST https://www.ubnt.com/login -d "username=validuser&password=validpass" -H "User-Agent: Mozilla/5.0" -c cookies.txt -v
```

## Expected Output

HTTP response body indicating 2FA required (e.g., JSON with {"status": "2fa_needed"}), headers with Set-Cookie for session, and verbose logs showing request/response details.

## Related

- [[Related Procedure]]
