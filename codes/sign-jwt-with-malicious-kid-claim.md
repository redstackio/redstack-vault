---
type: code
language: js
verified: true
platforms:
  - Node.js
tags:
  - jwt
  - forgery
  - token
validated: true
---

# sign-jwt-with-malicious-kid-claim

## Code

```js
jwt.sign({
  data: 'test'
}, maliciousKey, { algorithm: 'HS256', header: { kid: 'malicious.key' } })
```

## Description

This JavaScript code snippet uses the jsonwebtoken library to sign a JWT payload with a provided key (maliciousKey) and injects a custom 'kid' value into the header to reference a malicious key file. It enables forging tokens for authentication bypass in vulnerable applications that load verification keys based on the kid without validation. Integrate into a larger Node.js script after loading the key and customizing the payload.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| maliciousKey | The RSA private key content (loaded from file, e.g., fs.readFileSync('malicious.key')) | PEM-encoded string starting with -----BEGIN PRIVATE KEY----- |
| data | Payload object to sign (customize with user claims like sub, iat) | { sub: 'admin', iat: 1516239022 } |
| kid | Key ID to inject (points to the public key file on the server) | 'malicious.key' |

## Usage

Embed in a Node.js script for offline token forging: First, install jsonwebtoken (`npm install jsonwebtoken`), load the key with fs.readFileSync, then execute this sign call. Use the resulting token in HTTP requests (e.g., Authorization: Bearer <token>). Requires prior placement of the corresponding public key at the kid path on the target server via another exploit.

## Detection

- Log all JWT verification attempts and alert on unexpected kid values or file load paths.
- Monitor for RS256/HS256 mismatches or tokens with non-standard kid formats.
- Enable application logging for key loading errors (e.g., file not found for kid).
- Network/audit logs showing forged tokens with mismatched signatures or unusual claims.

## Related

- [[procedures/JWT-kid-Claim-Misuse-Key-Injection]]
