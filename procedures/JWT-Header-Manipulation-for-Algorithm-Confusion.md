---
type: procedure
description: >-
  Modify the header of a JSON Web Token to change the signing algorithm,
  potentially bypassing signature verification.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Use Alternate Authentication Material]]'
sub_techniques:
  - '[[Credentials in Files]]'
tags:
  - jwt
  - header-manipulation
  - algorithm-confusion
  - authentication-bypass
commands:
  - '[[commands/jwt-tool-modify-header]]'
platforms:
  - Web
tools:
  - '[[tools/jwt-tool]]'
validated: true
---

# JWT-Header-Manipulation-for-Algorithm-Confusion

## Summary

JWT Header Manipulation involves altering the header section of a JSON Web Token (JWT) to change critical parameters like the signing algorithm (alg). This technique exploits implementations that do not strictly validate the algorithm, allowing an attacker to switch from an asymmetric algorithm like RS256 to a symmetric one like HS256, where the attacker can forge a valid signature using a known public key as the secret. It is commonly used in web applications for authentication bypass or privilege escalation.

## Description

JSON Web Tokens (JWTs) consist of a header, payload, and signature, base64-encoded and separated by dots. The header specifies the token type (typ: JWT) and signing algorithm (alg). Vulnerable applications may parse the alg claim without enforcing it, enabling attackers to manipulate the header to use a weaker or known algorithm. For example, changing alg to "none" disables signature checks, or switching to HS256 allows resigning with the public key. This procedure uses the jwt_tool.py script to inspect and modify JWT headers. It applies to scenarios where an attacker has intercepted a valid JWT via network traffic, proxy, or client-side access. Success depends on the server's validation logic; outcomes include unauthorized access to protected resources or admin privileges.

## Requirements

1. A valid JWT token obtained from the target application (e.g., via browser dev tools or proxy interception).
2. jwt_tool.py installed and accessible (Python 3 environment).
3. Basic understanding of JWT structure and base64 encoding.
4. Network access to submit the modified token to the target endpoint.

## Defense

Defensive measures and detection strategies:

- Always use strong, asymmetric algorithms like RS256 or ES256 and never accept 'none' or symmetric algorithms unless explicitly required.
- Implement strict algorithm whitelisting in the JWT parser to reject unexpected alg values.
- Verify the signature using the corresponding private key and log any signature validation failures.
- Use content security policies (CSP) and input validation to prevent client-side token tampering.
- Monitor for anomalous token usage, such as unexpected alg changes or high failure rates in authentication logs.

## Objectives

1. Modify the JWT header to alter the signing algorithm and bypass authentication checks.
2. Resubmit the manipulated token to gain unauthorized access or elevate privileges in the target system.
3. Demonstrate the vulnerability to validate weak JWT implementations.

## Instructions

### Step 1: Inspect the Original JWT Header

**Context**: Before manipulation, decode and examine the JWT header to understand its current structure, including the typ and alg fields. This helps identify the target algorithm for confusion (e.g., RS256 to HS256).

Use jwt_tool.py to inspect the token:

**Command** ([[commands/jwt-tool-inspect]]):
```bash
python3 jwt_tool.py $_JWT_TOKEN -I -p
```

> This command decodes the JWT without modifying it, displaying the header, payload, and signature in human-readable format. Look for the "alg" field in the header output.

**Expected Output**: A breakdown like:

Header: {"typ": "JWT", "alg": "RS256"}
Payload: {"sub": "user123", "role": "user"}

If the alg is asymmetric, proceed to manipulation.

### Step 2: Modify the JWT Header

**Context**: Alter specific header claims, such as changing the alg to "HS256" or adding custom fields. This step forges a new signature if needed, exploiting the server's potential reuse of the public key as a symmetric secret.

**Command** ([[commands/jwt-tool-modify-header]]):
```bash
python3 jwt_tool.py $_JWT_TOKEN -I -hc alg -hv HS256
```

> Replace $_JWT_TOKEN with the base64-encoded JWT string. The -hc flag specifies the header claim (e.g., alg), and -hv sets its value (e.g., HS256). For multiple changes, chain -hc/-hv pairs. The tool will output the modified JWT.

**Expected Output**: The new JWT string with updated header, e.g., eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9... (modified token ready for use).

### Step 3: Resign and Test the Modified Token

**Context**: If the server requires a valid signature, use the tool to tamper and resign the token. Test by submitting it to the application's authentication endpoint to verify bypass.

**Command** ([[commands/jwt-tool-tamper-and-resign]]):
```bash
python3 jwt_tool.py $_MODIFIED_JWT -T -M hs256
```

> The -T flag enables tampering mode, and -M specifies the method (hs256). Provide the server's public key if needed for symmetric signing simulation.

**Expected Output**: A fully signed modified JWT. Upon submission (e.g., via curl or browser), expect successful authentication without errors.

**Success Indicators**:
- Modified header reflects changes (verify with base64 decode).
- Token accepted by server, granting access to restricted areas.
- No signature validation errors in application logs.
