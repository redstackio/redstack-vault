---
tags:
  - auth-bypass
  - jwt
  - account-takeover
  - password-reset
  - remitly
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/OWASP-ZAP]]'
  - '[[tools/Burp-JSON-Web-Token-Extension]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Initiate-Password-Reset-and-Capture-Tokens]]'
  - '[[procedures/Force-CAPTCHA-to-Extract-State-Token]]'
  - '[[procedures/Enter-Attacker-OTP-and-Swap-Tokens]]'
  - '[[procedures/Send-Modified-Reset-Request]]'
  - '[[procedures/Access-Taken-Over-Account]]'
step_count: 5
techniques:
  - '[[Valid Accounts]]'
  - '[[Use Alternate Authentication Material]]'
updated_at: '2025-12-14T17:33:42.072Z'
description: >-
  A multi-stage attack exploiting improper validation in Remitly's password
  reset endpoint to swap session tokens and JWTs, enabling unauthorized password
  reset and full account takeover without victim interaction.
id: af2c3df8-5388-4553-b51e-7131b6bba43e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Use Alternate Authentication Material]]'
---
---

# 0-Click Account Takeover via Password Reset Token Swapping in Remitly

Multi-stage attack chain demonstrating a complete attack workflow exploiting Remitly's password reset mechanism.

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
    A[Initiate Reset] --> B[Capture Tokens]
    B --> C[Swap and Modify]
    C --> D[Reset Password]
    D --> E[Account Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/OWASP-ZAP]]
- [[tools/Burp-JSON-Web-Token-Extension]]

### Target Environment

- Web application (Remitly website)
- No specific ports or services required beyond standard HTTPS (443)
- Attacker needs access to their own Remitly account and knowledge of victim's email

### Initial Access Requirements

- Valid attacker Remitly account with email/phone access for OTP
- Victim's email address
- Network access to Remitly's website
- No prior victim credentials needed

## Detailed Attack Procedures

### Step 1: Initiate Password Reset
procedure: [[procedures/Initiate-Password-Reset-and-Capture-Tokens]]

**Objective**: Start the password reset process for both victim and attacker accounts to generate necessary session data and tokens.

**Instructions**: Navigate to the Remitly 'Forgot Password' page and enter the victim's email to initiate reset. Repeat for the attacker's email. Use a proxy like [[tools/Burp-Suite]] to intercept the POST requests to /orchestrator/v1/password_reset/start.

**Expected Output**: HTTP responses containing session parameters (e.g., AMP_d0cf3ed24c with deviceId, userId, sessionId) and JWT tokens tied to the user's email.

**Success Indicators**:
- Intercepted requests show leaked tokens for both accounts
- No authentication errors during initiation

### Step 2: Force CAPTCHA for Token Extraction
procedure: [[procedures/Force-CAPTCHA-to-Extract-State-Token]]

**Objective**: Trigger an alternative flow in the MFA endpoint to reliably extract the victim's state_token and JWT without rate limiting issues.

**Instructions**: For the victim account, submit a POST to /orchestrator/v1/mfa/start with the victim's email. Modify the request to remove most of the CAPTCHA token value, forcing the CAPTCHA display. Solve the CAPTCHA and resubmit to obtain the response with state_token.

**Expected Output**: Response including state_token and JWT for the victim.

**Success Indicators**:
- CAPTCHA successfully forced and solved
- state_token and JWT extracted from the response

### Step 3: Enter Attacker OTP
procedure: [[procedures/Enter-Attacker-OTP-and-Swap-Tokens]]

**Objective**: Use the attacker's OTP to prepare for the token swap while preserving victim's session data.

**Instructions**: Receive and note the OTP sent to the attacker's email or phone during their password reset initiation. Save the victim's AMP_d0cf3ed24c and JWT from earlier captures.

**Expected Output**: Valid OTP for attacker; victim's tokens ready for swapping.

**Success Indicators**:
- OTP received and verified
- Victim's tokens isolated and unmodified

### Step 4: Modify and Send Reset Request
procedure: [[procedures/Send-Modified-Reset-Request]]

**Objective**: Swap the victim's tokens into the attacker's request and submit to reset the victim's password using the attacker's OTP.

**Instructions**: In the intercepted attacker's POST request to /orchestrator/v1/password_reset/start, replace AMP_d0cf3ed24c and JWT with the victim's values. Include the attacker's OTP in the payload. Forward the modified request.

**Expected Output**: Successful response indicating password reset completion for the victim.

**Success Indicators**:
- No validation errors; request accepted
- Password reset confirmed in response

### Step 5: Access Victim Account
procedure: [[procedures/Access-Taken-Over-Account]]

**Objective**: Log in to the victim's account using the newly set password to achieve full control.

**Instructions**: Use the victim's email and the new password (set during the reset, e.g., a password chosen by the attacker if the flow allows) to log in to Remitly.

**Expected Output**: Successful login and access to account dashboard, sensitive data, and transfer functions.

**Success Indicators**:
- Login successful without MFA prompts
- Access to funds, personal info, and transfer capabilities

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication checks in password reset by swapping unvalidated session tokens and JWTs
2. Achieved 0-click takeover without victim interaction or additional credentials
3. Gained full control over victim account, enabling data exfiltration and potential financial theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Use Alternate Authentication Material]] Use Alternate Authentication Material

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
