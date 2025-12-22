---
id: ac-uuid-001
name: >-
  Account Takeover via Brute-Force of Password Reset Verification Code Due to
  Missing Rate Limiting
tags:
  - account-takeover
  - brute-force
  - rate-limiting-bypass
  - password-reset
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Initiate-Password-Reset-Request]]'
  - '[[procedures/Intercept-Verification-Code-Submission]]'
  - '[[procedures/Brute-Force-Verification-Code-with-Burp-Intruder]]'
  - '[[procedures/Complete-Password-Reset-for-Account-Takeover]]'
step_count: 4
techniques:
  - '[[Brute Force]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:06.525Z'
description: >-
  A multi-stage attack exploiting the absence of rate limiting on a web
  application's password reset verification process, enabling brute-force
  guessing of short verification codes to achieve full account takeover.
validated: true
mitre_tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Exploit Public-Facing Application]]'
---
# Account Takeover via Brute-Force of Password Reset Verification Code Due to Missing Rate Limiting

Multi-stage attack chain demonstrating a complete workflow for exploiting a lack of rate limiting in a web application's forgot password feature, leading to unauthorized account access in a U.S. Department of Defense system.

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
    A[Initiate Reset] --> B[Intercept Request]
    B --> C[Brute-Force Code]
    C --> D[Reset Password]
    D --> E[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web application with forgot password functionality
- Valid target email address associated with an account
- Network access to the application's URL (e.g., https://www.example.com/forgot-password)

### Initial Access Requirements

- Knowledge of victim's email address
- No prior credentials needed, but proxy setup for request interception

## Detailed Attack Procedures

### Step 1: Initiate Password Reset

procedure: [[procedures/Initiate-Password-Reset-Request]]

**Objective**: Trigger the password reset process to receive a verification code via email.

**Instructions**: Navigate to the forgot password page and submit a valid email address to start the reset flow.

**Expected Output**: An email containing a verification code is sent to the target address.

**Success Indicators**:
- Email received with verification code
- Redirect to verification page

### Step 2: Intercept Verification Code Submission

procedure: [[procedures/Intercept-Verification-Code-Submission]]

**Objective**: Capture the POST request for code verification after submitting an incorrect code, preparing for brute-force.

**Instructions**: Enter an incorrect code on the verification page while proxying traffic through Burp Suite to intercept the request.

**Expected Output**: Intercepted POST request to the verification endpoint, showing the code parameter.

**Success Indicators**:
- Request captured with code parameter visible
- Error response for invalid code

### Step 3: Brute-Force Verification Code

procedure: [[procedures/Brute-Force-Verification-Code-with-Burp-Intruder]]

**Objective**: Use the intercepted request to systematically guess the verification code.

**Instructions**: Send the captured request to Burp Intruder, mark the code parameter as a payload position, and launch an attack with a list of possible codes (e.g., 4-6 digit numbers).

**Expected Output**: Successful response (e.g., 200 OK or redirect) indicating the correct code.

**Success Indicators**:
- Valid code identified in Intruder results
- Difference in response length or status code for success

### Step 4: Complete Password Reset

procedure: [[procedures/Complete-Password-Reset-for-Account-Takeover]]

**Objective**: Use the discovered code to set a new password and gain account control.

**Instructions**: Submit the correct code to access the new password form and set a known password.

**Expected Output**: Password successfully reset; login with new credentials works.

**Success Indicators**:
- Access to account dashboard
- Ability to perform actions as the victim

## Attack Chain Summary

### Key Achievements

1. Bypassed rate limiting to guess verification code
2. Achieved full account takeover without original credentials
3. Demonstrated high-impact vulnerability in authentication flow

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Brute Force]] Brute Force
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
