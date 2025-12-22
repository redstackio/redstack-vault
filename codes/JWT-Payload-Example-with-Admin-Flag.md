---
id: 46e435d6-a5e2-4e9a-8e0b-f3880c02f482
name: JWT-Payload-Example-with-Admin-Flag
type: code
language: json
verified: true
created_at: '2023-04-06T03:56:00.492805+00:00'
updated_at: '2023-04-10T20:22:33.134822+00:00'
platforms:
  - Web
tags:
  - jwt
  - payload
  - token
validated: true
---

# JWT-Payload-Example-with-Admin-Flag

## Code

```json
{
    "sub":"1234567890",
    "name":"Amazing Haxx0r",
    "exp":"1466270722",
    "admin":true
}
```

## Description

This JSON object represents a sample JWT payload with custom claims, including a subject ID, user name, expiration timestamp, and an admin privilege flag set to true. It is used as the data portion of a JWT token in authentication testing to simulate elevated access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| sub | Subject/user ID claim | 1234567890 |
| name | User name claim | Amazing Haxx0r |
| exp | Expiration Unix timestamp | 1466270722 |
| admin | Boolean flag for admin privileges | true |

## Usage

Embed this payload in a JWT encoding script (e.g., using PyJWT in Python) to generate a token for injection into web requests. Customize claims to match the target's expected format, then use the token in Authorization: Bearer headers for privilege escalation tests.

## Detection

- Inspect JWT payloads for unexpected claims like unauthorized 'admin' flags
- Log and alert on tokens with past/future exp times or non-standard claims
- Use JWT validation libraries to reject malformed or suspicious payloads

## Related

- [[procedures/Forge-Custom-JWT-Token-for-Auth-Bypass]]
- [[commands/python-encode-jwt-payload]]
