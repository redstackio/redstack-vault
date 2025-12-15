---
tags:
  - brute-force
  - 2fa-bypass
  - account-takeover
  - email-verification
  - evernote
type: attack_chain
tools:
  - '[[tools/burp-suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/request-email-confirmation-code-during-2fa-setup]]'
  - '[[procedures/brute-force-6-digit-verification-code-using-burp-intruder]]'
  - '[[procedures/identify-correct-verification-code-from-response-length]]'
  - '[[procedures/configure-2fa-with-attackers-phone-number]]'
step_count: 4
techniques:
  - '[[Brute Force]]'
description: >-
  Multi-stage attack exploiting lack of rate limiting on 6-digit email
  verification codes during Evernote 2FA setup, enabling brute-force to hijack
  2FA configuration and lock out the victim.
skill_level: intermediate
impact_level: high
id: fcc64c44-a520-4142-a4b0-edaa64542efb
created_at: '2025-12-14T17:24:47.717Z'
updated_at: '2025-12-14T17:24:47.717Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Evernote 2FA Setup Email Verification Brute-Force Leading to Account Lockout

Multi-stage attack chain demonstrating a complete attack workflow exploiting the absence of rate limiting on email verification codes during Evernote's 2FA setup process. An attacker creates an account with the victim's email, brute-forces the 6-digit code sent to that email, verifies it, and configures 2FA with their own phone number, resulting in permanent lockout of the victim from their account.

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
    A[Request Confirmation Code] --> B[Brute-Force Code] --> C[Identify Correct Code] --> D[Complete 2FA Setup]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/burp-suite]]

### Target Environment

- Web application (Evernote signup/2FA setup endpoint)
- Required services/ports: HTTPS (443) for web access, email service for code delivery
- Network access requirements: Direct internet access to Evernote

### Initial Access Requirements

- No prior credentials needed; attacker uses victim's email to initiate signup
- Network position: External attacker
- Prior access needed: None, but control over a proxy like Burp Suite

## Detailed Attack Procedures

### Step 1: Request Confirmation Code
procedure: [[procedures/request-email-confirmation-code-during-2fa-setup]]

**Objective**: Initiate the 2FA setup process to trigger sending of a 6-digit verification code to the victim's email.

**Instructions**: Navigate to Evernote's account creation page, enter the victim's email (e.g., victim@gmail.com), and proceed to the 2FA setup where the verification code is requested. Intercept the initial verification request using Burp Suite proxy.

**Expected Output**: A 6-digit code is emailed to the victim; the intercepted request shows the confirmationCode parameter ready for submission.

**Success Indicators**:
- Email received by victim (or attacker if they have email access)
- Intercepted request in Burp Suite with confirmationCode field

### Step 2: Brute-Force the Confirmation Code
procedure: [[procedures/brute-force-6-digit-verification-code-using-burp-intruder]]

**Objective**: Automate testing of all possible 6-digit codes (000000-999999) against the verification endpoint without rate limits.

**Instructions**: In Burp Suite, send the intercepted request to Intruder. Configure positions to mark the confirmationCode parameter for fuzzing. Set the payload type to Numbers, range 000000 to 999999, step 1. Start the attack to send 1,000,000 requests.

**Expected Output**: A series of HTTP responses from the verification endpoint, with varying lengths.

**Success Indicators**:
- Intruder completes without blocks or delays
- Multiple responses generated for analysis

### Step 3: Identify the Correct Code
procedure: [[procedures/identify-correct-verification-code-from-response-length]]

**Objective**: Distinguish the successful verification response from failures based on response size differences.

**Instructions**: Review the Intruder results table in Burp Suite, sorting by response length. The correct code will produce a shorter response (approximately 373 bytes) compared to invalid attempts (longer, error-containing responses).

**Expected Output**: Identification of the exact 6-digit code that triggered the short response.

**Success Indicators**:
- One response with ~373 bytes length
- Confirmation via re-submitting the code manually if needed

### Step 4: Complete 2FA Setup
procedure: [[procedures/configure-2fa-with-attackers-phone-number]]

**Objective**: Use the verified code to link the attacker's phone number to the account, locking out the victim.

**Instructions**: Submit the correct code to verify email ownership, then proceed to enter and confirm the attacker's phone number for 2FA. Complete the setup to enable OTP delivery to the attacker's device.

**Expected Output**: 2FA successfully configured; account now requires OTPs sent to attacker's phone.

**Success Indicators**:
- 2FA setup confirmation message
- Victim unable to access or reset the account without attacker's OTP

## Attack Chain Summary

### Key Achievements

1. Bypassed email verification without legitimate access to the victim's inbox
2. Brute-forced low-entropy 6-digit code due to no rate limiting
3. Achieved pre-account takeover by hijacking 2FA setup
4. Permanently denied victim access to their Evernote account

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Brute Force]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Credential Access]]

---
*Last updated: 2023-10-01*
