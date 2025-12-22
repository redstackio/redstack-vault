---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - 2fa-bypass
  - brute-force
  - account-takeover
  - otp
  - android
type: attack_chain
tools:
  - '[[tools/Nox-App-Player]]'
  - '[[tools/Grab-Android-App]]'
  - '[[tools/Charles-Web-Proxy]]'
  - '[[tools/Custom-C-Sharp-Bruteforcer]]'
tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Android
  - Web API
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Login-to-Grab-App-with-Google-Auth]]'
  - '[[procedures/Trigger-SMS-OTP-for-Profile-Edit]]'
  - '[[procedures/Extract-Session-Header-via-Web-Proxy]]'
  - '[[procedures/Brute-Force-OTP-with-Custom-Tool]]'
  - '[[procedures/Verify-Profile-Change-and-Account-Takeover]]'
step_count: 5
techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.925Z'
description: >-
  Multi-stage attack exploiting lack of rate limiting on 4-digit SMS OTP for
  profile editing in the Grab Android app, enabling brute-force to bypass 2FA
  and achieve account takeover.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
---
# 2FA Brute-Force Bypass Leading to Account Takeover in Grab Android App

Multi-stage attack chain demonstrating a complete workflow to bypass SMS-based 2FA in the Grab Android app by brute-forcing the 4-digit OTP on the profile editing endpoint due to absent rate limiting and code expiration. This allows attackers to change the victim's email or phone number after obtaining a valid session token, resulting in full account takeover.

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
    A[Login with Google Auth] --> B[Trigger SMS OTP]
    B --> C[Extract Session Token]
    C --> D[Brute-Force OTP]
    D --> E[Verify Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#e67e22
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Nox-App-Player]]
- [[tools/Grab-Android-App]]
- [[tools/Charles-Web-Proxy]]
- [[tools/Custom-C-Sharp-Bruteforcer]]

### Target Environment

- Android platform (emulated via Nox)
- Web API at https://p.grabtaxi.com
- SMS service for 2FA delivery

### Initial Access Requirements

- Valid phone number for Google authentication
- Network access to Grab API endpoints
- No prior account access needed beyond initial login

## Detailed Attack Procedures

### Step 1: Login to Grab App
procedure: [[procedures/Login-to-Grab-App-with-Google-Auth]]

**Objective**: Establish an authenticated session in the Grab app using Google login to initiate the vulnerable profile edit flow.

**Instructions**: Install and launch the Grab app in the emulator, then use Google authentication with a valid phone number.

**Expected Output**: Successful login with a session established.

**Success Indicators**:
- App dashboard accessible
- Session token generated

### Step 2: Trigger SMS OTP
procedure: [[procedures/Trigger-SMS-OTP-for-Profile-Edit]]

**Objective**: Initiate the profile edit process to send a 4-digit SMS OTP to the registered phone.

**Instructions**: Navigate to profile settings, attempt to edit name or phone, and save to trigger OTP request.

**Expected Output**: SMS containing 4-digit code received.

**Success Indicators**:
- OTP SMS delivered
- API request for confirmation pending

### Step 3: Extract Session Header
procedure: [[procedures/Extract-Session-Header-via-Web-Proxy]]

**Objective**: Intercept app traffic to capture the x-mts-ssid session header for subsequent authenticated requests.

**Instructions**: Configure proxy on emulator and monitor requests during profile edit attempt using [[commands/charles-intercept-traffic]] equivalent in Charles.

**Expected Output**: x-mts-ssid header value extracted.

**Success Indicators**:
- Session ID captured
- Traffic visible in proxy logs

### Step 4: Brute-Force OTP
procedure: [[procedures/Brute-Force-OTP-with-Custom-Tool]]

**Objective**: Use a custom tool to try all 9000 possible 4-digit codes until the correct one yields a 204 response.

**Instructions**: Input the session ID into the C# tool and execute brute-force against the profile edit endpoint using [[commands/put-profile-edit-otp]] pattern.

**Expected Output**: Correct code found with 204 response.

**Success Indicators**:
- 204 No Content on successful code
- Profile edit confirmed

### Step 5: Verify Takeover
procedure: [[procedures/Verify-Profile-Change-and-Account-Takeover]]

**Objective**: Confirm the profile change (e.g., phone update) by logging out and back in.

**Instructions**: After successful brute-force, logout from app and relogin to victim's updated details.

**Expected Output**: Access with new email/phone.

**Success Indicators**:
- Updated profile visible
- Full account control achieved

## Attack Chain Summary

### Key Achievements

1. Bypassed 2FA via brute-force of short OTP
2. Achieved account takeover by altering contact details
3. Demonstrated horizontal escalation potential with session compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Brute Force]] Brute Force
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
