---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - jwt
  - misconfiguration
  - debug-mode
  - otp-exposure
  - email-decryption
  - authentication-bypass
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Exploit-JWT-Merchant-ID-Misconfiguration]]'
  - '[[procedures/Leverage-Production-Debug-Mode-for-OTP-Exposure]]'
  - '[[procedures/Decrypt-Verification-Email-Content]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[Unsecured Credentials]]'
  - '[[Deobfuscate-Decode Files or Information]]'
updated_at: '2025-12-14T17:24:39.832Z'
description: >-
  A multi-stage attack exploiting JWT header misconfiguration, enabled debug
  mode in production, and weak email encryption to expose OTPs and sensitive
  verification details, enabling potential account takeover.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Unsecured Credentials]]'
  - '[[Deobfuscate-Decode Files or Information]]'
---
# JWT Merchant ID Misconfiguration and Debug Mode Enabling OTP Exposure with Email Decryption

Multi-stage attack chain demonstrating exploitation of authentication misconfigurations and weak protections in a web-based payment system to leak one-time passwords (OTPs) and sensitive verification data, leading to unauthorized access and account takeover risks.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Exploit JWT Misconfiguration] --> B[Leverage Debug Mode]
    B --> C[Decrypt Email Content]
    C --> D[Access Verification Details and OTPs]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[Burp Suite]] (for intercepting and modifying requests)
- [[curl]] (for API testing)

### Target Environment

- Web platform with JWT-based authentication
- Email service for verification
- Mobile OTP service
- Access to production endpoints

### Initial Access Requirements

- Valid merchant ID or ability to register/test accounts
- Network access to the web application
- No prior credentials needed, but basic user registration helps

## Detailed Attack Procedures

### Step 1: Exploit JWT Merchant ID Misconfiguration
procedure: [[procedures/Exploit-JWT-Merchant-ID-Misconfiguration]]

**Objective**: Identify and abuse improper handling of merchant ID in JWT headers to bypass authentication checks and access protected endpoints.

**Instructions**: Intercept authentication requests using a proxy tool like Burp Suite. Modify the JWT header to manipulate the merchant ID field, such as setting it to a null or unauthorized value. Submit the altered request to the authentication endpoint.

Use [[commands/curl-modify-jwt]] to test the misconfiguration:

```bash
curl -X POST https://api.kartpay.com/auth -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZXJjaGFudElkIjoiMDAwIn0.invalid_signature" -d '{"phone":"+1234567890"}'
```

Then validate response for unauthorized access indicators.

**Expected Output**: Response containing authentication tokens or session data without proper merchant validation.

**Success Indicators**:
- Server accepts invalid merchant ID
- Access to OTP request endpoints granted

### Step 2: Leverage Production Debug Mode for OTP Exposure
procedure: [[procedures/Leverage-Production-Debug-Mode-for-OTP-Exposure]]

**Objective**: Exploit accidentally enabled debug mode to retrieve exposed OTPs for mobile numbers, bypassing normal verification.

**Instructions**: With access from Step 1, send a request to trigger OTP generation. Append debug parameters or access debug endpoints directly, as the mode was left enabled post-testing.

Use [[commands/curl-trigger-otp-debug]] to request OTP with debug flag:

```bash
curl -X POST https://api.kartpay.com/otp/send -H "Authorization: Bearer modified_token" -d '{"phone":"+1234567890", "debug":true}'
```

Inspect the response for plaintext OTP disclosure.

**Expected Output**: Debug response including the generated OTP value.

**Success Indicators**:
- OTP visible in response body
- No additional verification required

### Step 3: Decrypt Verification Email Content
procedure: [[procedures/Decrypt-Verification-Email-Content]]

**Objective**: Intercept and decrypt the verification email to access sensitive information intended for post-verification disclosure only.

**Instructions**: Trigger email verification during registration. Capture the email content via email interception or API response. Apply basic decryption (e.g., using known weak keys or tools) since encryption is easily breakable.

Use [[commands/openssl-decrypt-email]] to attempt decryption assuming weak symmetric encryption:

```bash
echo "encrypted_email_content" | openssl enc -d -aes-128-cbc -k weak_key -in email.enc -out decrypted.txt
```

Review decrypted.txt for sensitive details.

**Expected Output**: Plaintext email revealing account verification info, links, or tokens.

**Success Indicators**:
- Successful decryption without errors
- Exposure of pre-verification sensitive data

## Attack Chain Summary

### Key Achievements

1. Bypassed merchant ID validation via JWT manipulation
2. Exposed mobile OTPs through persistent debug mode
3. Decrypted verification emails to access hidden sensitive information

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts (JWT auth bypass)
- [[Unsecured Credentials]] Unprotected Service (debug mode and weak crypto)
- [[Deobfuscate-Decode Files or Information]] Deobfuscate/Decode Files or Information (email decryption)

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access (via misconfigured auth)
- [[Credential Access]] Credential Access (OTP and verification data exposure)

---
*Last updated: 2023-10-01T12:00:00Z*
