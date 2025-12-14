---
tags:
  - authentication-bypass
  - 2fa
  - account-takeover
  - email-verification
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
commands: []
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Register-Account-with-Victims-Email]]'
  - '[[procedures/Login-to-Unverified-Account]]'
  - '[[procedures/Enable-2FA-Without-Verification]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
description: >-
  An attacker registers an account using the victim's email, logs in without
  email verification, and enables 2FA to lock out the victim and take over the
  account.
skill_level: intermediate
impact_level: high
id: 661b90f3-4392-409a-9ee3-0d2b3c8c68a3
created_at: '2025-12-14T17:24:48.460Z'
updated_at: '2025-12-14T17:24:48.460Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
---
# Account Takeover via Unverified Email 2FA Enablement

## Overview

This attack chain exploits a vulnerability in the account registration and authentication system where email verification is not enforced before allowing login and 2FA setup. The attacker uses the victim's email to register, logs in without verifying the email, and enables 2FA on their own device, effectively denying the victim access to their account even after a password reset. This leads to account denial of service or full takeover, as the victim cannot provide the 2FA codes.

## Attack Flow Visualization

```mermaid
graph LR
    A[Register with Victim's Email] --> B[Login Without Verification]
    B --> C[Enable 2FA on Attacker's Device]
    C --> D[Account Takeover / DoS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Web application with account registration, login, and 2FA features (e.g., Moneybird platform)
- No specific ports or services required beyond standard HTTPS access

### Initial Access Requirements

- Knowledge of victim's email address
- No prior credentials needed
- Internet access to the target web application

## Detailed Attack Procedures

### Step 1: Register with Victim's Email
procedure: [[procedures/Register-Account-with-Victims-Email]]

**Objective**: Create an unverified account using the victim's email to initiate the takeover process.

**Instructions**: Navigate to the target's registration page and enter the victim's email address along with a chosen username and password. Submit the form without completing any email verification steps.

**Expected Output**: Account registration success message; verification email sent to victim's inbox (ignored by attacker).

**Success Indicators**:
- Registration completes without requiring email verification
- Attacker receives confirmation of account creation

### Step 2: Login to Unverified Account
procedure: [[procedures/Login-to-Unverified-Account]]

**Objective**: Gain access to the account despite the unverified email status.

**Instructions**: Go to the login page, enter the username and password created in Step 1. Attempt login without verifying the email.

**Expected Output**: Successful login to the account dashboard or home page.

**Success Indicators**:
- Login succeeds without email verification prompt
- Access to account settings is granted

### Step 3: Enable 2FA Without Verification
procedure: [[procedures/Enable-2FA-Without-Verification]]

**Objective**: Bind 2FA to the attacker's device, locking out the victim.

**Instructions**: From the account settings, navigate to the 2FA enablement section. Scan the QR code or enter the setup key with the attacker's authenticator app to receive verification codes on their device. Complete the 2FA setup process.

**Expected Output**: 2FA enabled confirmation; future logins require codes sent to attacker's device.

**Success Indicators**:
- 2FA setup completes without email verification check
- Victim's password reset attempts fail due to missing 2FA codes

## Attack Chain Summary

### Key Achievements

1. Bypassed email verification during registration and login
2. Enabled 2FA exclusively on attacker's device
3. Achieved account denial of service or takeover for the victim

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Modify Authentication Process]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Persistence]]

---
*Last updated: 2023-10-01*
