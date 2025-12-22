---
id: a81cb7ab-7f72-47d2-935e-e82d1a36eb1a
name: JWT-Signature-Disclosure-via-Invalid-Token-Submission
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:00.574439+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Cloud Instance Metadata API]]'
sub_techniques: []
tags:
  - JWT
  - Signature-Disclosure
  - CVE-2019-7644
  - Credential-Access
commands:
  - '[[commands/curl-post-invalid-jwt]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/jwt_tool]]'
validated: true
---

# JWT-Signature-Disclosure-via-Invalid-Token-Submission

## Summary

This procedure exploits a JWT signature disclosure vulnerability (CVE-2019-7644) by submitting a JSON Web Token with an intentionally incorrect signature to a protected endpoint. If vulnerable, the server responds with an error message that reveals the correct signature, allowing an attacker to forge valid tokens for unauthorized access. This technique targets symmetric key-based JWT implementations where error handling leaks sensitive information.

## Description

JWTs are commonly used for authentication and authorization in web applications. In vulnerable implementations, particularly those using libraries like certain Node.js JWT packages, submitting a token with a tampered signature can trigger an error response that includes the expected (correct) signature for comparison. This disclosure enables attackers to recover the signing key or directly forge tokens, bypassing authentication. The attack requires interaction with a JWT-protected API endpoint and assumes the use of symmetric signing (e.g., HS256). It is effective against applications that do not sanitize error messages. Expected outcomes include obtaining the valid signature, which can then be used to sign arbitrary payloads for privilege escalation or session hijacking.

## Requirements

1. Network access to a JWT-protected API endpoint (e.g., /api/user via HTTP/HTTPS).
2. Ability to craft or modify JWT tokens (manual via jwt.io or automated with tools like jwt_tool).
3. Intercepting proxy or HTTP client (e.g., Burp Suite or curl) to send requests and capture responses.
4. Knowledge of the token structure, including header, payload, and a base invalid signature.

## Defense

Defensive measures and detection strategies:

- Use asymmetric signing algorithms (e.g., RS256) for JWTs to prevent signature reuse attacks.
- Protect symmetric secrets by storing them securely (e.g., in environment variables or key vaults) and avoiding exposure in errors.
- Implement robust error handling to return generic messages without disclosing signatures or keys (e.g., "Invalid token" instead of detailed comparisons).
- Enable web application firewall (WAF) rules to detect anomalous JWT submissions and log them for review.
- Regularly audit JWT libraries for known vulnerabilities like CVE-2019-7644 and apply patches.
- Monitor for unusual error rates on authentication endpoints, which may indicate probing attempts.

## Objectives

1. Submit an invalid JWT to elicit a server response disclosing the correct signature.
2. Extract the valid signature from the error message to enable token forging.
3. Use the disclosed information to craft and validate a new JWT for unauthorized access.

## Instructions

### Step 1: Craft an Invalid JWT Token

**Context**: Create a JWT with a known payload but tamper with the signature to make it invalid. This can be done manually using an online tool like jwt.io or via a CLI tool. Ensure the header and payload are unmodified, but replace the signature with random bytes.

Use [[commands/curl-post-invalid-jwt]] to prepare and send, but first generate the token. For example, base a valid token structure on eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ (standard example) and append a fake signature like SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c.

### Step 2: Submit the Invalid JWT to the Endpoint

**Context**: Send the malformed token in an Authorization header to a protected endpoint. This triggers the server's validation, and if vulnerable, it will compare the submitted signature against the correct one in the error response.

**Command** ([[commands/curl-post-invalid-jwt]]):
```bash
curl -X POST -H "Authorization: Bearer $_INVALID_JWT" -H "Content-Type: application/json" -d '{"test":"data"}' $_ENDPOINT_URL
```

> This command sends a POST request with the invalid JWT in the Bearer token. Replace $_INVALID_JWT with your crafted token (e.g., eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.invalid_signature_here) and $_ENDPOINT_URL with the target (e.g., https://target.com/api/protected). The request body can be minimal JSON to invoke the endpoint.

### Step 3: Analyze the Error Response for Signature Disclosure

**Context**: Inspect the server's HTTP response for error details. Look for messages indicating signature mismatch that include the expected valid signature. If disclosed, copy it for use in forging new tokens.

No specific command needed here; use the response from Step 2 or proxy logs.

**Expected Output**: A 401/403 error with a message like "Invalid signature. Expected [CORRECT_SIGNATURE] got [SUBMITTED_SIGNATURE]".

Example response body:
```http
{
  "error": "Invalid signature. Expected SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c got 9twuPVu9Wj3PBneGw1ctrf3knr7RX12v-UwocfLhXIs"
}
{
  "error": "Invalid signature. Expected 8Qh5lJ5gSaQylkSdaCIDBoOqKzhoJ0Nutkkap8RgB1Y= got 8Qh5lJ5gSaQylkSdaCIDBoOqKzhoJ0Nutkkap8RgBOo="
}
```

> Success is indicated by the presence of the correct signature in the error text. If no disclosure occurs, the endpoint is not vulnerable—try different payloads or endpoints.

### Step 4: Verify Exploitation by Forging a Valid Token

**Context**: Using the disclosed signature, reconstruct a valid JWT by signing a new payload with the leaked signature (or derive the key if possible). Submit the forged token to confirm access.

Repeat Step 2 with the new $_VALID_JWT to test.

**Expected Output**: Successful 200 OK response with protected data, confirming token acceptance.
