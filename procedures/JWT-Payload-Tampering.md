---
id: 1fb3ac43-62f1-4f11-9c90-74c9402fa8e2
name: JWT-Payload-Tampering
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:00.520091+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - '[[tags/JWT Format]]'
  - '[[tags/JWT - JSON Web Token]]'
  - '[[tags/Payload]]'
  - jwt
  - token-tampering
  - authentication-bypass
commands:
  - '[[commands/jwt-tool-decode-token]]'
  - '[[commands/jwt-tool-tamper-payload]]'
platforms:
  - Web
tools:
  - '[[tools/JWT-Tool]]'
validated: true
---

# JWT-Payload-Tampering

## Summary

This procedure demonstrates how to tamper with the payload of a JSON Web Token (JWT) to modify user claims, such as roles or privileges, potentially bypassing authentication and authorization controls in web applications that use JWT for session management.

## Description

JWTs are compact, URL-safe tokens used for securely transmitting information between parties as claims between a client and a server. They consist of three Base64Url-encoded parts: header, payload, and signature, separated by dots. The payload contains claims like user ID, roles, or expiration time. If the application does not properly validate the signature or uses weak signing algorithms (e.g., none algorithm), an attacker can decode the token, modify the payload (e.g., change 'user' to 'admin'), re-encode it, and use the tampered token to gain elevated access. This is common in single-page applications (SPAs) or APIs relying on JWT without server-side verification. The procedure assumes access to a valid JWT from a low-privilege user session and uses the JWT Tool to perform the modifications.

## Requirements

1. A valid JWT token obtained from the target application (e.g., via browser developer tools or intercepted traffic).
2. Installed JWT Tool (python-based toolkit for JWT analysis and manipulation).
3. Python 3 environment on the attacker's machine.
4. Basic understanding of Base64 encoding and JWT structure.

## Defense

- Always validate JWT signatures server-side using strong algorithms (e.g., RS256) and trusted keys.
- Implement short token expiration times and refresh mechanisms.
- Use HTTPS to prevent token interception.
- Monitor for anomalous token usage, such as unexpected privilege escalations or invalid signatures.
- Avoid the 'none' algorithm and enforce claim validation (e.g., 'iss', 'aud', 'exp').

## Objectives

1. Decode and inspect the existing JWT payload to identify modifiable claims.
2. Tamper with payload claims to escalate privileges (e.g., change role from 'user' to 'admin').
3. Re-encode and test the tampered token for unauthorized access.

## Instructions

### Step 1: Decode and Inspect the JWT Token

**Context**: Begin by decoding the JWT to view its header and payload without verification. This reveals the current claims, such as user roles or permissions, to identify tampering opportunities. Use the JWT Tool in decode mode to output the token structure in JSON format.

**Command** ([[commands/jwt-tool-decode-token]]):
```bash
python3 jwt_tool.py $_JWT_TOKEN -X s
```

> This command decodes the token and displays the header, payload, and any signature details. Look for claims like 'role', 'admin', or 'permissions' in the payload output. If the signature is weak or absent, proceed to tampering.

**Expected Output**: JSON representation of the token parts, e.g., {"header": {"alg": "HS256"}, "payload": {"sub": "user123", "role": "user"}}.

### Step 2: Tamper with the Payload Claims

**Context**: Modify specific claims in the payload to escalate privileges. For example, change a 'role' claim from 'user' to 'admin'. The tool allows in-place modification without needing the signing key if the app accepts unsigned or weakly signed tokens.

**Command** ([[commands/jwt-tool-tamper-payload]]):
```bash
python3 jwt_tool.py $_JWT_TOKEN -I -pc $_CLAIM_NAME -pv $_NEW_VALUE
```

> Replace $_CLAIM_NAME with the target claim (e.g., 'role') and $_NEW_VALUE with the desired value (e.g., 'admin'). The -I flag modifies the token in place. After running, the tool outputs the tampered token string, which can be copied for use.

**Expected Output**: The modified JWT token string, e.g., eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMTIzIiwicm9sZSI6ImFkbWluIn0.signature, along with confirmation of the change.

### Step 3: Test the Tampered Token

**Context**: Inject the tampered token back into the application (e.g., via Authorization header in API requests or browser storage) to verify if the changes grant elevated access. Use tools like curl or Burp Suite to send requests with the new token.

**Instructions**: 
- Set the tampered token in the application's session (e.g., localStorage.setItem('token', 'tampered_jwt')) or HTTP header.
- Attempt actions requiring higher privileges, such as accessing admin endpoints.
- If successful, the app will treat the user as having the modified role without re-authentication.

**Expected Output**: Successful response from privileged endpoints, e.g., 200 OK with admin-only data, instead of 403 Forbidden.

**Success Indicators**:
- Payload claims modified without signature errors.
- Application accepts the tampered token and grants elevated access.
