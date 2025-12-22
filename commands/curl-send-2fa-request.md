---
id: f89077f6-68a2-4a9d-9b98-7d7b2377f975
name: curl-send-2fa-request
type: command
executor: bash
data: >-
  curl -X POST https://target-app.com/api/2fa-verify -H "Content-Type:
  application/json" -H "Cookie: session_id=$_SESSION_ID" -d '{"code":
  "$_2FA_CODE"}' -k
output: null
created_at: '2023-04-06T03:55:53.922523+00:00'
updated_at: '2023-04-06T03:55:53.932067+00:00'
platforms:
  - Web
tags:
  - 2fa
  - authentication
verified: true
validated: true
---

# curl-send-2fa-request

## Command

```bash
curl -X POST https://target-app.com/api/2fa-verify \
  -H "Content-Type: application/json" \
  -H "Cookie: session_id=$_SESSION_ID" \
  -d '{"code": "$_2FA_CODE"}' \
  -k
```

## Description

This command sends a POST request to the 2FA verification endpoint with a provided code, simulating a user's 2FA submission. It is used to trigger and observe the authentication response, which can then be intercepted and manipulated for bypass purposes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SESSION_ID | Session cookie from initial login | Yes |
| $_2FA_CODE | 2FA code to submit (use incorrect for failure test) | Yes |
| -X POST | Specifies POST method | Built-in |
| -H "Content-Type: application/json" | Sets JSON content type | Built-in |
| -H "Cookie: ..." | Includes session cookie | Built-in |
| -d '...' | JSON payload with code | Built-in |
| -k | Ignores SSL certificate validation (for testing) | No |

## Examples

### Basic Usage

```bash
curl -X POST https://target-app.com/api/2fa-verify \
  -H "Content-Type: application/json" \
  -H "Cookie: session_id=abc123" \
  -d '{"code": "123456"}' \
  -k
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST https://target-app.com/api/2fa-verify \
  -H "Content-Type: application/json" \
  -H "Cookie: session_id=abc123" \
  -d '{"code": "123456"}' \
  -k
```

## Expected Output

A JSON response indicating failure for incorrect codes:

```json
{"success": false, "message": "Invalid 2FA code"}
```

Successful response (with correct code):

```json
{"success": true, "redirect": "/dashboard"}
```

## Related

- [[procedures/2FA-Bypass-via-Response-Manipulation]]
- [[tools/Burp-Suite]]
