---
id: cmd-curl-trigger-001
data: >-
  curl -X POST https://target.com/api/login -H "Content-Type: application/json"
  -d '{"username": "target@example.com", "password": "knownpassword"}' -c
  cookies.txt -o initial_response.json
tags:
  - web
  - auth
type: command
output: '{"status": "otp_sent"}'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:42.604Z'
verified: false
validated: true
submitted: true
---
# curl-trigger-otp

## Command

```bash
curl -X POST https://target.com/api/login -H "Content-Type: application/json" -d '{"username": "target@example.com", "password": "knownpassword"}' -c cookies.txt -o initial_response.json
```

## Description

This command initiates a login request to a web application's authentication endpoint, triggering the generation and delivery of a 2FA OTP while capturing session cookies for subsequent requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON payload header | Yes |
| `-d '{...}'` | JSON data with username and password | Yes |
| `-c cookies.txt` | Saves cookies to file | Yes |
| `-o initial_response.json` | Outputs response to file | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/api/login -H "Content-Type: application/json" -d '{"username": "user@test.com", "password": "pass123"}' -c cookies.txt
```

### Advanced Usage

```bash
curl -X POST https://target.com/api/login -H "Content-Type: application/json" -H "User-Agent: Mozilla/5.0" -d '{"username": "user@test.com", "password": "pass123"}' -c cookies.txt -v
```

## Expected Output

JSON response indicating OTP sent, e.g., {"status": "otp_sent", "message": "Check your email for the code"}. Cookies file contains session ID for verification steps.

## Related

- [[commands/curl-2fa-brute]]
- [[procedures/Brute-Force-2FA-OTP-to-Bypass-Authentication]]
