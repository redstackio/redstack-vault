---
id: 40e4fffa-5f64-49b5-81e2-ac47f244d096
name: Modified-Host-Header-POST-Request-for-Password-Reset
type: code
language: http
verified: true
created_at: '2023-04-06T03:55:53.787655+00:00'
updated_at: '2023-04-06T03:55:53.790787+00:00'
platforms:
  - Web
tags:
  - http
  - request-tampering
  - phishing
validated: true
---

# Modified-Host-Header-POST-Request-for-Password-Reset

## Code

```http
POST https://example.com/reset.php HTTP/1.1
Accept: */*
Content-Type: application/json
Host: attacker.com
```

## Description

This HTTP request snippet demonstrates a tampered POST for initiating a password reset, with the Host header modified to an attacker-controlled domain. When forwarded to the server, it poisons the reset process by generating tokens or links pointing to the attacker's site instead of the legitimate one. This is a core element of password reset poisoning attacks, allowing credential capture on the fake completion page.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| example.com/reset.php | The target password reset endpoint | https://target.com/api/reset |
| attacker.com | Attacker's controlled domain for Host injection | evil.com |
| */* | Accept header for any response type | text/html |
| application/json | Content-Type for request body | application/x-www-form-urlencoded |

## Usage

Intercept the victim's reset initiation request using a proxy like Burp Suite, replace the Host header with this snippet's format, add the email body (e.g., {"email":"victim@target.com"}), and forward. The server will respond with a poisoned reset flow. Used in phishing-driven account takeover scenarios where the victim is proxied through the attacker's setup.

## Detection

- Web server logs showing mismatched Host headers in password reset endpoints.
- Anomaly detection in request patterns: Unusual Host values during reset flows.
- Client-side: Proxy indicators if using tools like Burp (e.g., via browser extensions).
- Email analysis: Reset links pointing to non-whitelisted domains.

## Related

- [[procedures/Account-Takeover-Through-Password-Reset-Poisoning]]
- [[tools/Burp-Suite]]
