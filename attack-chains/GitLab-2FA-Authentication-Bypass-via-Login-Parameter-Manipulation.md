---
id: ac-gitlab-2fa-bypass-128085
tags:
  - auth-bypass
  - 2fa
  - gitlab
  - information-disclosure
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - Ruby on Rails
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Initiate-Attacker-Login-Session]]'
  - '[[procedures/Intercept-2FA-Submission-Request]]'
  - '[[procedures/Modify-Request-to-Target-User]]'
  - '[[procedures/Submit-Modified-Request-with-Target-OTP]]'
  - '[[procedures/Achieve-Unauthorized-Target-Access]]'
step_count: 5
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:30.884Z'
description: >-
  Multi-stage attack exploiting GitLab's SessionsController to bypass password
  authentication for 2FA-enabled users by manipulating the login parameter
  during OTP submission, allowing unauthorized access with only the target's
  username and OTP code.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# GitLab 2FA Authentication Bypass via Login Parameter Manipulation

Multi-stage attack chain demonstrating a complete workflow to bypass password requirements in GitLab for users with 2FA enabled. The exploit leverages a flaw in the SessionsController's find_user method, which prioritizes the 'user[login]' parameter over the session-stored OTP user ID, allowing attackers to authenticate as any 2FA-enabled user using only their username and a valid OTP code.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initiate Attacker Session] --> B[Intercept 2FA Request]
    B --> C[Modify for Target User]
    C --> D[Submit with Target OTP]
    D --> E[Gain Target Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- GitLab instance (Ruby on Rails web application)
- Access to the login page (/users/sign_in)
- Network access to the target GitLab server

### Initial Access Requirements

- Attacker's own valid GitLab credentials (username and password)
- Knowledge of target's username
- Valid 6-digit OTP code for the target user
- No prior access to target account needed

## Detailed Attack Procedures

### Step 1: Initiate Attacker Login Session
procedure: [[procedures/Initiate-Attacker-Login-Session]]

**Objective**: Establish a session with the attacker's credentials to set session[:otp_user_id] for subsequent manipulation.

**Instructions**: Navigate to the GitLab sign-in page and enter the attacker's username and password. This creates a session tied to the attacker's user ID.

**Expected Output**: Redirect to the 2FA prompt page, with session[:otp_user_id] set to attacker's ID in the backend.

**Success Indicators**:
- 2FA prompt appears for attacker
- No errors during initial login

### Step 2: Intercept 2FA Submission Request
procedure: [[procedures/Intercept-2FA-Submission-Request]]

**Objective**: Capture the POST request to /users/sign_in during 2FA token submission to analyze and prepare for modification.

**Instructions**: Configure Burp Suite to intercept traffic. Submit the attacker's 2FA token on the prompt page. The request will be a multipart form-data POST to /users/sign_in containing user[otp_attempt] but no user[login].

**Expected Output**: Intercepted request showing form fields like user[otp_attempt] with the attacker's code.

**Success Indicators**:
- Request captured successfully
- Form data includes OTP attempt

### Step 3: Modify Request to Target User
procedure: [[procedures/Modify-Request-to-Target-User]]

**Objective**: Inject the target user's login parameter to override the session user ID during verification.

**Instructions**: In Burp Suite, add a new form-data field: Content-Disposition: form-data; name="user[login]" with value set to the target's username (e.g., 'john'). Retain the existing user[otp_attempt].

**Expected Output**: Modified request now includes both user[login] and user[otp_attempt].

**Success Indicators**:
- Parameter added without breaking request format
- Request ready for OTP replacement

### Step 4: Submit Modified Request with Target OTP
procedure: [[procedures/Submit-Modified-Request-with-Target-OTP]]

**Objective**: Replace the OTP with the target's valid code to complete authentication as the target.

**Instructions**: In the intercepted request, change user[otp_attempt] value to the target's valid 6-digit OTP (e.g., from '212421' to target's code). Forward the modified POST to /users/sign_in.

**Expected Output**: Server response indicating successful authentication (e.g., redirect to dashboard as target user).

**Success Indicators**:
- No 'Invalid two-factor code' error
- Logged in as target user

### Step 5: Achieve Unauthorized Target Access
procedure: [[procedures/Achieve-Unauthorized-Target-Access]]

**Objective**: Confirm full access to the target account without the password.

**Instructions**: Upon successful response, access target account features like repositories or settings to validate control.

**Expected Output**: Full dashboard access under target's username.

**Success Indicators**:
- Account actions perform as target
- Session persists for target user

## Attack Chain Summary

### Key Achievements

1. Bypassed password requirement using only username and OTP
2. Exploited parameter precedence in SessionsController
3. Enabled information disclosure of 2FA status via error message differences

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
