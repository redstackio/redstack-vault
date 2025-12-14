---
id: ac-17512-account-takeover-brute-force-reset
tags:
  - brute-force
  - account-takeover
  - password-reset
  - authentication-bypass
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Enumerate-Valid-User-Emails]]'
  - '[[procedures/Request-Password-Reset-Link]]'
  - '[[procedures/Configure-Burp-Suite-for-Token-Brute-Force]]'
  - '[[procedures/Brute-Force-Reset-Token]]'
  - '[[procedures/Reset-Password-with-Valid-Token]]'
  - '[[procedures/Login-with-New-Password]]'
step_count: 6
techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:06.464Z'
description: >-
  Multi-stage attack exploiting lack of brute force protection on password reset
  tokens to achieve full account takeover on HackerOne platform.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
---
# Account Takeover via Brute Force on Password Reset Tokens

Multi-stage attack chain demonstrating a complete workflow for exploiting the absence of brute force protection on password reset tokens in HackerOne's authentication system, leading to full account takeover for any registered user, including high-privilege accounts like co-founders.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Enumerate User Emails] --> B[Request Reset Link]
    B --> C[Configure Brute Force Tool]
    C --> D[Brute Force Token]
    D --> E[Reset Password]
    E --> F[Login and Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform (HackerOne-like authentication system)
- Required services/ports: HTTPS on port 443
- Network access requirements: Direct internet access to target domain

### Initial Access Requirements

- No prior credentials needed
- Knowledge of a valid email domain (e.g., from user enumeration)
- Network position: External attacker

## Detailed Attack Procedures

### Step 1: Enumerate Valid User Emails
procedure: [[procedures/Enumerate-Valid-User-Emails]]

**Objective**: Identify a valid registered email address to target for password reset.

**Instructions**: Leverage prior user enumeration techniques to discover emails such as michiel@hackerone.com or jobert@hackerone.com. This step assumes access to an enumeration method, like querying public profiles or directories.

**Expected Output**: A list of valid email addresses associated with the target platform.

**Success Indicators**:
- Confirmed valid email (e.g., via response from enumeration tool or prior vuln)
- Email format matches target domain

### Step 2: Request Password Reset Link
procedure: [[procedures/Request-Password-Reset-Link]]

**Objective**: Generate a password reset URL containing a token for the target email.

**Instructions**: Submit a password reset request using the enumerated email. This will email a reset link, but intercept or access the URL format like https://hackerone.com/users/password/edit?reset_password_token=MUm2xQ_TEtf2RaG1H3DK.

**Expected Output**: Reset URL with a partial or full token visible in the request/response.

**Success Indicators**:
- Reset request accepted (200 OK response)
- Token parameter observed in URL

### Step 3: Configure Burp Suite for Token Brute Force
procedure: [[procedures/Configure-Burp-Suite-for-Token-Brute-Force]]

**Objective**: Set up interception and modification capabilities to brute force the reset token parameter.

**Instructions**: Launch [[tools/Burp-Suite]] and configure the Proxy to intercept requests to https://hackerone.com/users/password/edit?reset_password_token=. Enable Intruder for payload variations on the token parameter.

**Expected Output**: Burp Suite ready with a captured base request for brute forcing.

**Success Indicators**:
- Requests to token endpoint intercepted
- Intruder configured with token position marked for payloads

### Step 4: Brute Force the Reset Token
procedure: [[procedures/Brute-Force-Reset-Token]]

**Objective**: Guess valid tokens by sending variations and distinguishing responses.

**Instructions**: Use Burp Intruder to send requests with guessed tokens. Valid tokens return 200 status and 4378-character response; invalid ones return 302 status and 1525 characters.

**Expected Output**: Identification of a valid token based on response differences.

**Success Indicators**:
- Response with 200 status and longer length (4378 chars)
- Valid token extracted for use

### Step 5: Reset Password with Valid Token
procedure: [[procedures/Reset-Password-with-Valid-Token]]

**Objective**: Access the password edit page and set a new password using the valid token.

**Instructions**: Navigate to the edit page with the valid token URL and submit a new password.

**Expected Output**: Password successfully updated for the target account.

**Success Indicators**:
- Password change confirmation
- No errors on submission

### Step 6: Login with New Password
procedure: [[procedures/Login-with-New-Password]]

**Objective**: Gain full unauthorized access to the compromised account.

**Instructions**: Use the target email and newly set password to log in to the platform.

**Expected Output**: Successful login and access to account dashboard.

**Success Indicators**:
- Access to privileged features (e.g., admin panels if high-priv account)
- Session established

## Attack Chain Summary

### Key Achievements

1. Enumeration of target emails without authentication
2. Brute forcing of reset tokens due to distinguishable responses
3. Complete takeover of any account, including co-founder privileges

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Brute Force]] Brute Force
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Defense Evasion]] Defense Evasion

---
*Last updated: 2023-10-01T00:00:00Z*
