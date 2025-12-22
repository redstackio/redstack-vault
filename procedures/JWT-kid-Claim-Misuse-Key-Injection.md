---
type: procedure
verified: true
submitted: false
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Forge Web Credentials]]'
sub_techniques: []
tags:
  - '[[tags/JWT Claims]]'
  - '[[tags/JWT - JSON Web Token]]'
  - '[[tags/JWT kid Claim Misuse]]'
  - jwt
  - authentication-bypass
  - token-forgery
commands:
  - '[[commands/extract-jwt-header-and-payload]]'
  - '[[commands/generate-rsa-private-key]]'
platforms:
  - Web
tools: []
validated: true
---

# JWT-kid-Claim-Misuse-Key-Injection

## Summary

This procedure demonstrates how to exploit a misconfigured JSON Web Token (JWT) implementation by injecting a malicious key identifier (kid) into the header, allowing an attacker to forge valid-looking tokens for authentication bypass. By generating a custom RSA private key, signing a new payload with it, and setting the kid to reference a controllable key file, an attacker can impersonate users if the application loads verification keys from the specified kid path without proper validation or sanitization.

## Description

JWTs are compact, URL-safe tokens used for secure data exchange, commonly in web applications for authentication and authorization. The 'kid' (key ID) header parameter is intended to identify the cryptographic key used for signing or encryption. In vulnerable implementations, the application may load the public key for verification directly from a file path specified in the kid claim, without validating the path or ensuring it points to a trusted location. This can enable key injection attacks, especially if combined with path traversal or if the attacker can influence file placement (e.g., via upload vulnerabilities). The technique allows forging tokens to escalate privileges, access sensitive data, or perform unauthorized actions. It targets web applications using libraries like jsonwebtoken in Node.js. Success requires a valid intercepted JWT to mimic structure and an environment where the server trusts the injected kid path. Note: The algorithm is adjusted to RS256 for compatibility with the generated RSA key; vulnerable apps may accept mismatched algorithms if validation is weak.

## Requirements

1. A valid JWT token intercepted from the target application (e.g., via browser dev tools or proxy like Burp Suite).
2. Access to a Linux/Unix-like system with bash and openssl installed (standard on Kali Linux).
3. Node.js environment with the 'jsonwebtoken' npm package installed (run `npm install jsonwebtoken`).
4. Basic knowledge of JWT structure and the target application's token usage.
5. The target application must load keys from local files based on the kid claim without path sanitization.

## Defense

- Implement strict validation of the kid claim: whitelist allowed key IDs and reject unexpected values or paths.
- Use a secure key management system (e.g., AWS KMS, HashiCorp Vault) to store and retrieve keys dynamically without exposing file paths.
- Enforce algorithm matching: verify the header algorithm matches the expected one and reject 'none' or mismatches.
- Monitor for anomalous JWT usage, such as unusual kid values or high failure rates in token verification logs.
- Apply least privilege: run the application in a sandboxed environment to prevent file system access via kid paths.

## Objectives

1. Decode an existing JWT to understand its structure and claims.
2. Generate a malicious RSA private key for signing forged tokens.
3. Sign a new JWT with the malicious key and inject a custom kid to trick the verifier into using a corresponding public key.
4. Use the forged token to bypass authentication and access protected resources.

## Instructions

### Step 1: Extract JWT Header and Payload

**Context**: Decode the provided JWT to inspect the header (including current kid and algorithm) and payload (user claims like sub, iat). This helps replicate the structure for the forged token and identify the expected claims for impersonation. Use base64 decoding to reveal the JSON contents without the signature.

**Command** ([[commands/extract-jwt-header-and-payload]]):
```bash
echo "Header: $(echo $_JWT | cut -d. -f1 | base64 -d 2>/dev/null)" && echo "Payload: $(echo $_JWT | cut -d. -f2 | base64 -d 2>/dev/null)"
```

> This command splits the JWT by dots, decodes the first two parts (header and payload) separately using base64 -d, and prints them as readable JSON. The 2>/dev/null suppresses padding errors. Replace $_JWT with the actual token string. This step confirms the current kid and allows copying necessary claims.

### Step 2: Generate Malicious Private Key

**Context**: Create a new 2048-bit RSA private key that the attacker will use to sign the forged JWT. The corresponding public key must be placed at the path referenced by the kid (e.g., via another vulnerability like arbitrary file write); this step focuses on generating the private component for offline signing.

**Command** ([[commands/generate-rsa-private-key]]):
```bash
openssl genrsa -out $_KEY_FILE 2048
```

> The openssl genrsa command generates an RSA private key of the specified bit length and saves it to the output file. Use $_KEY_FILE=malicious.key for the default. Verify the file was created with ls -la malicious.key. This key will be loaded in the next step for signing; extract the public key separately if needed for server-side placement (e.g., openssl rsa -in malicious.key -pubout -out malicious.pub).

### Step 3: Sign Forged JWT with Malicious Key and Injected kid

**Context**: Load the generated private key and use it to sign a custom payload, injecting a malicious kid value into the header. This tricks the server into loading the attacker's public key from the specified file path during verification. Customize the payload to impersonate a target user (e.g., set sub to a privileged account). Run this in a Node.js environment after installing jsonwebtoken.

**Code** ([[codes/sign-jwt-with-malicious-kid-claim]]):
```js
jwt.sign({
  data: 'test'
}, maliciousKey, { algorithm: 'HS256', header: { kid: 'malicious.key' } })
```

> Before running the code, prepare a Node.js script: const jwt = require('jsonwebtoken'); const fs = require('fs'); const maliciousKey = fs.readFileSync('malicious.key', 'utf8'); const payload = { sub: 'target_user_id', iat: Math.floor(Date.now() / 1000) }; // Customize payload here const signedToken = jwt.sign(payload, maliciousKey, { algorithm: 'RS256', header: { kid: 'malicious.key' } }); console.log(signedToken); Note: Updated algorithm to RS256 for RSA compatibility; original HS256 may cause errors. The 'data: 'test'' in the code is a placeholder—replace with your payload object. Expected output: A full JWT string (header.payload.signature) that can be used in requests. Test by sending it to the application; success if accepted without signature errors.
