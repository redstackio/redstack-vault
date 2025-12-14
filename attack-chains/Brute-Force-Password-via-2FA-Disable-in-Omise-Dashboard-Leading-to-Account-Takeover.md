---
id: ac-omise-2fa-bruteforce-001
tags:
  - brute-force
  - 2fa-bypass
  - account-takeover
  - credential-access
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
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Brute-Force-Password-in-2FA-Disable-Process]]'
step_count: 5
techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:47.520Z'
description: >-
  An attack chain exploiting lack of rate limiting on password confirmation
  during 2FA disable in Omise dashboard, allowing brute force to guess passwords
  and disable multi-factor authentication using an active session.
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
# Brute Force Password via 2FA Disable in Omise Dashboard Leading to Account Takeover

Multi-stage attack chain demonstrating a complete attack workflow exploiting improper authentication restrictions in Omise's dashboard.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10-30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Login to Dashboard] --> B[Access Profile and 2FA Disable]
    B --> C[Intercept Password Submission]
    C --> D[Brute Force Password Parameter]
    D --> E[Disable 2FA and Takeover Account]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#f39c12
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform (Omise dashboard at https://dashboard.omise.co)
- Active user session (e.g., forgotten login on another device)
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Valid credentials for initial login to establish session
- Attacker must have network access to the dashboard
- Prior session hijacking or physical access to a device with active session

## Detailed Attack Procedures

### Step 1: Login to the Omise Dashboard
procedure: [[procedures/Brute-Force-Password-in-2FA-Disable-Process]]

**Objective**: Establish an active session in the victim's Omise dashboard to access protected features.

**Instructions**: Navigate to the signin page and authenticate using valid credentials. This creates a session cookie that persists across requests.

**Expected Output**: Successful redirection to the dashboard homepage.

**Success Indicators**:
- Dashboard loads with user-specific data
- Session cookies are set in the browser

### Step 2: Access User Profile
procedure: [[procedures/Brute-Force-Password-in-2FA-Disable-Process]]

**Objective**: Navigate to the profile section to reach 2FA settings.

**Instructions**: From the dashboard, click on the username in the top navigation or profile menu to open user options.

**Expected Output**: Profile dropdown or menu appears with options like Two-factor authentication.

**Success Indicators**:
- Profile menu is visible
- No session expiration errors

### Step 3: Navigate to Disable 2FA
procedure: [[procedures/Brute-Force-Password-in-2FA-Disable-Process]]

**Objective**: Trigger the password confirmation prompt for disabling 2FA.

**Instructions**: In the profile menu, select Two-factor authentication and then choose the Disable 2FA option. This submits a request prompting for password confirmation.

**Expected Output**: A form appears with a field labeled 'Please confirm your identity to register a new Two-Factor Authenticator' or similar for disable.

**Success Indicators**:
- Password input field is displayed
- No additional auth barriers

### Step 4: Submit Initial Random Password
procedure: [[procedures/Brute-Force-Password-in-2FA-Disable-Process]]

**Objective**: Test the password submission to capture the baseline request for fuzzing.

**Instructions**: Enter a random password in the confirmation field and submit the form. Use browser dev tools or a proxy to observe the request.

**Expected Output**: Error response indicating invalid password, with observable response details like content length.

**Success Indicators**:
- Request is sent to the disable endpoint
- Response differences noted for valid vs. invalid (e.g., shorter error for wrong, longer for correct)

### Step 5: Capture and Fuzz the Password Parameter
procedure: [[procedures/Brute-Force-Password-in-2FA-Disable-Process]]

**Objective**: Brute force the password by fuzzing the parameter and detecting correct guesses via side-channel leaks.

**Instructions**: Intercept the HTTP POST request to the 2FA disable endpoint using [[tools/Burp-Suite]]. Identify the password parameter (e.g., 'password'). Use Burp Intruder or a script to fuzz with a wordlist of potential passwords. Monitor response content length or timing differences to identify the correct password. Once guessed, resubmit to disable 2FA.

**Expected Output**: Successful disable confirmation, with 2FA removed from the account.

**Success Indicators**:
- Response length changes on correct password (e.g., success page vs. error)
- Account settings reflect 2FA disabled
- Full access without MFA on other devices

## Attack Chain Summary

### Key Achievements

1. Exploited active session to access 2FA disable without re-auth
2. Brute forced password due to no rate limits, using response side-channels
3. Disabled MFA, enabling persistent account takeover

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Brute Force]] Brute Force
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
