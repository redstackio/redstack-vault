---
tags:
  - otp-leak
  - auth-bypass
  - account-takeover
  - api-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Submit-Phone-Number-to-Authentication-API]]'
  - '[[procedures/Inspect-API-Response-for-Leaked-OTP]]'
  - '[[procedures/Complete-Authentication-with-Leaked-OTP]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:48.496Z'
description: >-
  An attack chain exploiting an API vulnerability where OTP codes are leaked in
  responses, allowing unauthorized authentication and account takeovers via
  arbitrary phone numbers.
skill_level: intermediate
impact_level: high
id: a79412d5-0ab3-493b-a081-881c355c9ca4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# OTP Code Leaked in API Response Enabling Account Takeover

Multi-stage attack chain demonstrating a complete attack workflow exploiting OTP leakage in an authentication API, allowing attackers to bypass SMS-based verification for account takeovers and unauthorized sign-ups.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Submit Phone Number] --> B[Inspect Leaked OTP] --> C[Authenticate with OTP]
    C --> D[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP clients like curl or browser dev tools)

### Target Environment

- Web application with phone-based OTP authentication API
- Accessible public-facing API endpoint for OTP requests
- No specific ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Network access to the target web application
- Knowledge of the authentication API endpoint (e.g., via documentation or inspection)
- Arbitrary 10-digit phone number (can be fabricated)

## Detailed Attack Procedures

### Step 1: Submit Phone Number
procedure: [[procedures/Submit-Phone-Number-to-Authentication-API]]

**Objective**: Trigger OTP generation by submitting a phone number to the API, initiating the leakage.

**Instructions**: Use [[commands/curl-submit-phone]] to send a POST request with the phone number to the authentication endpoint:

```bash
curl -X POST https://target.com/api/auth/otp -H "Content-Type: application/json" -d '{"phone": "+1234567890"}'
```

**Expected Output**: JSON response containing the leaked OTP code alongside success indicators.

**Success Indicators**:
- HTTP 200 response received
- OTP code visible in the response body

### Step 2: Inspect API Response
procedure: [[procedures/Inspect-API-Response-for-Leaked-OTP]]

**Objective**: Analyze the API response to extract the leaked OTP code.

**Instructions**: Review the output from the previous curl command or use browser dev tools to inspect the network response for the OTP field.

**Expected Output**: Identification of the OTP value (e.g., a 6-digit code) in the JSON response.

**Success Indicators**:
- OTP code extracted without needing SMS delivery
- No errors in response parsing

### Step 3: Complete Authentication
procedure: [[procedures/Complete-Authentication-with-Leaked-OTP]]

**Objective**: Use the leaked OTP to authenticate or sign up, achieving account takeover or unauthorized access.

**Instructions**: Submit the phone number and extracted OTP using [[commands/curl-complete-auth]]:

```bash
curl -X POST https://target.com/api/auth/verify -H "Content-Type: application/json" -d '{"phone": "+1234567890", "otp": "123456"}'
```

Replace "123456" with the actual leaked OTP.

**Expected Output**: Successful authentication response with session token or user details.

**Success Indicators**:
- Authentication succeeds
- Access to user account or new sign-up confirmed
- Ability to perform actions like creating junk accounts

## Attack Chain Summary

### Key Achievements

1. Bypassed SMS OTP delivery by leaking codes in API responses
2. Enabled account takeover for any known phone number
3. Allowed mass creation of junk accounts with arbitrary numbers, undermining security controls

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
