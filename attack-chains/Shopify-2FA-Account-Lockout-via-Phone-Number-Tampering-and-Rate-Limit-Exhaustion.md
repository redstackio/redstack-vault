---
tags:
  - dos
  - 2fa
  - parameter-tampering
  - rate-limit-exhaustion
  - shopify
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2024-10-05T12:00:00Z'
procedures:
  - '[[procedures/Prepare-Shopify-Account-for-2FA-Interception]]'
  - '[[procedures/Tamper-2FA-Phone-Number-Parameter]]'
  - '[[procedures/Exhaust-2FA-OTP-Rate-Limits-via-Resend-Spam]]'
  - '[[procedures/Verify-Victim-Account-Lockout]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:30:27.380Z'
description: >-
  A denial-of-service attack exploiting Shopify's SMS-based 2FA by tampering
  with the phone number parameter during setup and spamming resend codes to
  exhaust rate limits, locking out victims for 24 hours.
skill_level: intermediate
impact_level: high
id: 91010eb6-e402-427c-af8b-7619c514dff2
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
---
# Shopify 2FA Account Lockout via Phone Number Tampering and Rate Limit Exhaustion

Multi-stage attack chain demonstrating a complete denial-of-service workflow against Shopify accounts using SMS-based 2FA.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Attacker Prepares Account] --> B[Intercept and Tamper Phone Number]
    B --> C[Trigger 2FA and Spam Resend]
    C --> D[Victim Lockout DoS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Shopify web platform
- SMS service for 2FA
- No specific ports; web-based over HTTPS

### Initial Access Requirements

- Attacker needs a valid Shopify account (free trial possible)
- Victim's phone number (public or guessed)
- Network access to Shopify.com
- Burp Suite configured as proxy for request interception

## Detailed Attack Procedures

### Step 1: Prepare Attacker Account for 2FA Interception
procedure: [[procedures/Prepare-Shopify-Account-for-2FA-Interception]]

**Objective**: Create a controlled environment to intercept the 2FA setup request.

**Instructions**: Register a new Shopify account and navigate to the 2FA activation page to prepare for request capture. No commands are executed; this is UI-based navigation.

**Expected Output**: Access to the 2FA setup form with phone number input field.

**Success Indicators**:
- New account created successfully
- 2FA setup page loaded

### Step 2: Tamper with 2FA Phone Number Parameter
procedure: [[procedures/Tamper-2FA-Phone-Number-Parameter]]

**Objective**: Modify the intercepted request to associate the victim's phone number with the attacker's 2FA setup.

**Instructions**: Enter a dummy phone number in the form, intercept the POST request using Burp Suite, replace the phone number parameter with the victim's, and forward the request. The endpoint is typically a POST to the 2FA setup path (e.g., /account/two_factor).

**Expected Output**: Server accepts the tampered request without validation, associating the victim's number.

**Success Indicators**:
- Request forwarded successfully
- No server-side rejection of the modified phone number

### Step 3: Exhaust 2FA OTP Rate Limits via Resend Spam
procedure: [[procedures/Exhaust-2FA-OTP-Rate-Limits-via-Resend-Spam]]

**Objective**: Trigger 2FA verification and spam the resend button to burn through rate limits on OTP delivery to the victim's phone.

**Instructions**: Log out and attempt to log back in to trigger 2FA, then repeatedly click 'Resend Code' (approximately 20-50 times) until the server stops responding or reflects rate limit errors. This exhausts the 24-hour quota for OTP sends to the phone number.

**Expected Output**: Server halts OTP delivery; error messages indicate rate limiting.

**Success Indicators**:
- Multiple resend attempts succeed initially
- Subsequent attempts fail with throttling
- No new OTPs delivered to the phone

### Step 4: Verify Victim Account Lockout
procedure: [[procedures/Verify-Victim-Account-Lockout]]

**Objective**: Confirm the DoS impact on the victim by simulating or observing their login attempt.

**Instructions**: Have the victim (or simulate) attempt login: enter credentials, reach 2FA page, request code, and observe failure to receive OTP or resend. Old OTPs may appear, but new ones are blocked for 24 hours.

**Expected Output**: Victim redirected to 2FA but unable to proceed without recovery codes.

**Success Indicators**:
- Victim cannot receive OTP
- Resend blocked due to rate limits
- Account inaccessible for 24 hours

## Attack Chain Summary

### Key Achievements

1. Bypassed phone number ownership verification in 2FA setup
2. Exhausted SMS OTP rate limits without direct access to victim's account
3. Achieved 24-hour lockout for any targeted Shopify user relying on SMS 2FA

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Network Denial of Service]] Network Denial of Service

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---

*Last updated: 2024-10-05T12:00:00Z*
