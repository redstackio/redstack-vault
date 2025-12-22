---
id: b460552a-e5d3-4a9a-b139-f935db3dba59
name: 2FA-Failed-JSON-Response
type: code
language: json
verified: true
created_at: '2023-04-06T03:55:53.922460+00:00'
updated_at: '2023-04-06T03:55:53.932012+00:00'
platforms:
  - Web
tags:
  - 2fa
  - response
  - json
validated: true
---

# 2FA-Failed-JSON-Response

## Code

```json
{"success": false}
```

## Description

This JSON snippet represents a typical server response indicating failure during 2FA verification. It is the original response intercepted during the bypass procedure, which the attacker modifies to simulate success.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| success | Boolean flag for authentication status | false |

## Usage

Intercept this response using a proxy like Burp Suite during a 2FA submission with an invalid code. Use it as the baseline for modification in response tampering attacks to bypass authentication.

## Detection

- Log all 2FA responses and alert on discrepancies between request codes and response success flags.
- Monitor proxy traffic for modifications to authentication endpoints.
- Implement client-side validation of response integrity (e.g., HMAC signatures on JSON).

## Related

- [[procedures/2FA-Bypass-via-Response-Manipulation]]
- [[tools/Burp-Suite]]
