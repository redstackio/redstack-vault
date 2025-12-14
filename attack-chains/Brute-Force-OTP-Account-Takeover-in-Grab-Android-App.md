---
id: ac-grab-otp-bruteforce-001
tags:
  - otp-bruteforce
  - account-takeover
  - mobile-security
  - authentication-bypass
  - api-abuse
type: attack_chain
tools:
  - '[[tools/Nox-App-Player]]'
  - '[[tools/Web-Debugging-Proxy]]'
  - '[[tools/Custom-CSharp-OTP-Tool]]'
  - '[[tools/Grab-Android-App]]'
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
verified: false
platforms:
  - Android
  - Mobile
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Testing-Environment-for-Grab-App]]'
  - '[[procedures/Prepare-Target-Phone-Number-for-OTP-Brute-Force]]'
  - '[[procedures/Execute-OTP-Brute-Force-Attack]]'
step_count: 3
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:30:27.434Z'
description: >-
  Multi-stage attack exploiting lack of rate limiting on OTP resend in Grab
  Android App to brute-force 4-digit OTPs, enabling account takeover using only
  phone number and country code.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute-Force OTP Account Takeover in Grab Android App

Multi-stage attack chain demonstrating account takeover via brute-forcing short OTP codes in the Grab Android App's phone-based login flow, exploiting no rate limiting on OTP resends and a small 4-digit code space.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~24-72 hours |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Environment] --> B[Prepare Target]
    B --> C[Brute-Force OTP]
    C --> D[Account Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Nox-App-Player]]
- [[tools/Web-Debugging-Proxy]]
- [[tools/Custom-CSharp-OTP-Tool]]
- [[tools/Grab-Android-App]]

### Target Environment

- Android platform
- Grab Android App (version supporting phone login with OTP)
- Access to SMS service for OTP delivery (though bypassed in attack)
- Internet connectivity for API calls

### Initial Access Requirements

- Victim's phone number with country code (e.g., UA for Ukraine, without + sign)
- No prior credentials needed; attack uses public API endpoints
- Development environment with .NET 4.0 for custom tool

## Detailed Attack Procedures

### Step 1: Setup Testing Environment
procedure: [[procedures/Setup-Testing-Environment-for-Grab-App]]

**Objective**: Establish a controlled Android environment to analyze and interact with the Grab App's API endpoints for OTP login flow.

**Instructions**: Install and configure the Android emulator with proxy interception to monitor API requests during app registration and login initiation.

**Expected Output**: Proxied view of API calls, including OTP request to https://p.grabtaxi.com/api/passenger/v2/profiles/activationsms.

**Success Indicators**:
- App launches in emulator without issues
- Proxy captures initial OTP SMS trigger
- Endpoints identified: activationsms and activate

### Step 2: Prepare Target Phone Number
procedure: [[procedures/Prepare-Target-Phone-Number-for-OTP-Brute-Force]]

**Objective**: Input the victim's phone details into the custom tool to target the specific account for brute-force attempts.

**Instructions**: Launch the custom C# tool and enter the phone number with country code to initialize API targeting.

**Expected Output**: Tool ready state, prepared to hit endpoints https://p.grabtaxi.com/api/passenger/v2/profiles/activationsms and https://p.grabtaxi.com/api/passenger/v2/profiles/activate.

**Success Indicators**:
- Phone number accepted without errors
- Tool logs confirm endpoint preparation
- No immediate rate limiting triggered

### Step 3: Execute Brute-Force Attack
procedure: [[procedures/Execute-OTP-Brute-Force-Attack]]

**Objective**: Automate repeated OTP guesses and resends to exhaust the 4-digit code space until account activation succeeds.

**Instructions**: Start the tool to cycle through fixed OTP attempts (e.g., 1056, 1057, 1058) every 30 seconds, resending new OTPs upon failure to bypass the 3-attempt limit per code.

**Expected Output**: Success response from activate endpoint with session header granting account access.

**Success Indicators**:
- Tool logs show matching OTP attempt
- API response includes authentication token or session
- Access to victim's Grab account features confirmed

## Attack Chain Summary

### Key Achievements

1. Bypassed OTP authentication using brute-force due to weak rate limiting and small code space.
2. Achieved full account takeover without passwords or additional credentials.
3. Enabled horizontal privilege escalation to access user data and services.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Brute Force]] Brute Force

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

---
*Last updated: 2023-10-01T00:00:00Z*
