---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - 2fa-bypass
  - brute-force
  - auth-bypass
  - otp-bruteforce
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Enter-Credentials-to-Reach-2FA-Prompt]]'
  - '[[procedures/Intercept-2FA-Submission-Request]]'
  - '[[procedures/Brute-Force-mfaToken-with-Burp-Intruder]]'
  - '[[procedures/Identify-Correct-OTP-and-Complete-Login]]'
step_count: 4
techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:48.218Z'
description: >-
  A multi-stage attack exploiting a lack of rate limiting in SingleStore's 2FA
  system to brute-force the OTP using Burp Suite, enabling full account
  takeover.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# 2FA Bypass via Brute-Force OTP in SingleStore Portal

Multi-stage attack chain demonstrating a complete 2FA bypass workflow in SingleStore's authentication system by exploiting the absence of effective rate limiting on OTP submissions when requests are intercepted.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5-10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Enter Credentials] --> B[Intercept 2FA Request]
    B --> C[Brute-Force OTP]
    C --> D[Complete Login]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform
- Access to https://portal.singlestore.com/
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Victim's email and password
- Network access to the SingleStore portal
- Burp Suite configured as proxy for browser traffic

## Detailed Attack Procedures

### Step 1: Enter Credentials to Reach 2FA Prompt
procedure: [[procedures/Enter-Credentials-to-Reach-2FA-Prompt]]

**Objective**: Authenticate with email and password to trigger the 2FA challenge.

**Instructions**: Navigate to the login page and submit the victim's credentials to advance to the OTP input screen.

**Expected Output**: 2FA prompt appears, session active.

**Success Indicators**:
- Login page accepts credentials without error
- Redirect to 2FA verification page

### Step 2: Intercept 2FA Submission Request
procedure: [[procedures/Intercept-2FA-Submission-Request]]

**Objective**: Capture the OTP submission POST request using an incorrect code to prepare for modification.

**Instructions**: Enter a fake OTP (e.g., 000000) and intercept the request in Burp Suite Proxy without forwarding it.

**Expected Output**: Intercepted POST request with mfaToken parameter visible in Burp.

**Success Indicators**:
- Request held in intercept mode
- Session remains active without reset

### Step 3: Brute-Force mfaToken with Burp Intruder
procedure: [[procedures/Brute-Force-mfaToken-with-Burp-Intruder]]

**Objective**: Systematically test a range of 6-digit OTPs by modifying the mfaToken payload.

**Instructions**: Send the intercepted request to Intruder, mark mfaToken as payload position, configure Numbers payload (e.g., 000000 to 999999 or narrower range like 160000-170000), and launch the attack with Intercept enabled.

**Expected Output**: Series of responses with varying HTTP status codes.

**Success Indicators**:
- Multiple requests processed without session reset
- Status code changes observed (200/303 for fails, 302 for success)

### Step 4: Identify Correct OTP and Complete Login
procedure: [[procedures/Identify-Correct-OTP-and-Complete-Login]]

**Objective**: Detect the successful OTP from response indicators and finalize access.

**Instructions**: Monitor Intruder results for 302 redirects indicating the correct code, then refresh the browser's 2FA page to submit it manually or forward the successful request to complete login.

**Expected Output**: Successful redirection to the SingleStore dashboard.

**Success Indicators**:
- 302 status on correct OTP attempt
- Full unauthorized access to account

## Attack Chain Summary

### Key Achievements

1. Bypassed 2FA without triggering lockouts or rate limits
2. Achieved account takeover using only email/password
3. Demonstrated vulnerability in both static OTP and TOTP modes

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Brute Force]] Brute Force
- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T12:00:00Z*
