---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: IDOR in Email Editing Leading to Account Takeover on Atavist
tags:
  - idor
  - account-takeover
  - web
  - email-hijack
  - password-reset
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
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Login-and-Intercept-Email-Change-Request]]'
  - '[[procedures/Exploit-IDOR-to-Modify-Victim-Email]]'
  - '[[procedures/Reset-Password-for-Account-Takeover]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:24.343Z'
description: >-
  Exploits an Insecure Direct Object Reference (IDOR) vulnerability in the
  Atavist platform's email editing functionality to change any user's email
  address, enabling password reset and full account takeover.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# IDOR in Email Editing Leading to Account Takeover on Atavist

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR vulnerability in the Atavist platform to achieve account takeover.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Login and Intercept] --> B[Execution: Exploit IDOR to Change Email]
    B --> C[Persistence: Password Reset and Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform: Atavist CMS (https://magazine.atavist.com)
- Required services/ports: HTTPS (443)
- Network access requirements: Internet access to the target domain

### Initial Access Requirements

- Valid credentials for any authenticated Atavist account
- Network position: External attacker with account access
- Prior access needed: None beyond basic login

## Detailed Attack Procedures

### Step 1: Login and Intercept Email Change Request
procedure: [[procedures/Login-and-Intercept-Email-Change-Request]]

**Objective**: Gain authenticated access and capture the legitimate email change request to understand the vulnerable endpoint.

**Instructions**: First, login to the Atavist platform using valid credentials. Then, navigate to the account settings page and prepare to intercept the email update request using a proxy tool like [[tools/Burp-Suite]]. Attempt to change your own email to generate the baseline POST request.

**Expected Output**: Intercepted POST request to https://magazine.atavist.com/cms/reader/account containing the 'id' parameter and new email data.

**Success Indicators**:
- Successful login and access to account settings
- Proxy captures the email update request with sequential user ID

### Step 2: Exploit IDOR to Modify Victim Email
procedure: [[procedures/Exploit-IDOR-to-Modify-Victim-Email]]

**Objective**: Alter the 'id' parameter in the intercepted request to target a victim's account and update their email to one controlled by the attacker.

**Instructions**: In the proxy tool, modify the 'id' value in the request body to the victim's user ID (predictable sequential integer). Forward the modified request to the server, changing the victim's email without authorization checks.

**Expected Output**: Server response indicating successful email update (e.g., 200 OK), with the victim's email now set to the attacker's address.

**Success Indicators**:
- Modified request forwards without errors
- Victim's email is updated, verifiable via subsequent login attempts or admin checks

### Step 3: Reset Password for Account Takeover
procedure: [[procedures/Reset-Password-for-Account-Takeover]]

**Objective**: Use the forgot password feature with the newly controlled email to reset the victim's password and gain full access to their account.

**Instructions**: Navigate to the forgot password page and submit a reset request using the victim's newly set email. Follow the reset link sent to the attacker's email to set a new password and login to the victim's account.

**Expected Output**: Password reset email received, new password set, and successful login to the victim's account.

**Success Indicators**:
- Reset email arrives in attacker's inbox
- Full access to victim's account settings and content

## Attack Chain Summary

### Key Achievements

1. Bypassed authorization to arbitrarily change user emails via IDOR
2. Hijacked password reset flow for seamless account takeover
3. Achieved full control of target accounts without user interaction or additional credentials

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Defense Evasion]] Defense Evasion

---

*Last updated: 2023-10-01T12:00:00Z*
