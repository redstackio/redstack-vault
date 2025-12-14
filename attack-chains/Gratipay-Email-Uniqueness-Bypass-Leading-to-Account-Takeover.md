---
id: ac-gratipay-email-bypass-ato
tags:
  - business-logic
  - email-bypass
  - account-takeover
  - gratipay
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Review-Gratipay-Source-Code-for-Email-Logic]]'
  - '[[procedures/Login-to-Gratipay-Attacker-Account]]'
  - '[[procedures/Exploit-Email-Addition-with-Encoded-Space]]'
  - '[[procedures/Verify-Email-and-Set-as-Primary]]'
  - '[[procedures/Perform-Password-Reset-for-Takeover]]'
step_count: 5
techniques:
  - '[[Valid Accounts]]'
  - '[[Device Registration]]'
updated_at: '2025-12-14T17:32:57.829Z'
description: >-
  A multi-stage business logic attack exploiting a flaw in Gratipay's email
  addition feature to bypass uniqueness checks using URL-encoded spaces,
  enabling addition of a victim's primary email to the attacker's account and
  subsequent takeover via password reset.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Device Registration]]'
---
# Gratipay Email Uniqueness Bypass Leading to Account Takeover

Multi-stage attack chain demonstrating a business logic flaw in Gratipay's email management, allowing an attacker to add a victim's primary email to their own account by appending a URL-encoded space (%20) to evade uniqueness checks, leading to potential receipt of sensitive emails and account takeover if email access is available.

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
    A[Source Code Review] --> B[Attacker Login]
    B --> C[Manipulated Email Addition]
    C --> D[Email Verification]
    D --> E[Password Reset Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Firefox or Chrome with developer tools)
- Access to GitHub for source code review

### Target Environment

- Gratipay web application (Python-based)
- No specific ports or services required beyond standard HTTPS (443)
- Attacker must have a registered Gratipay account

### Initial Access Requirements

- Attacker's own Gratipay credentials
- Victim's email address (publicly known or enumerated)
- Optional: Temporary access to victim's email inbox for verification

## Detailed Attack Procedures

### Step 1: Source Code Review
procedure: [[procedures/Review-Gratipay-Source-Code-for-Email-Logic]]

**Objective**: Identify the business logic flaw in email uniqueness checking to plan the bypass.

**Instructions**: Access the Gratipay GitHub repository and examine the email.py file in the models/participant directory, focusing on lines 123 (uniqueness check) and 131 (email sending). Note the lack of whitespace trimming or URL-decoding handling.

**Expected Output**: Confirmation of the flaw where %20 appended emails pass the check but normalize during verification.

**Success Indicators**:
- Flaw identified in email uniqueness logic
- Understanding of bypass using URL-encoded space

### Step 2: Attacker Login
procedure: [[procedures/Login-to-Gratipay-Attacker-Account]]

**Objective**: Authenticate as the attacker to access the email addition feature.

**Instructions**: Navigate to the Gratipay login page and enter the attacker's credentials to gain access to the account dashboard.

**Expected Output**: Successful login with access to account settings, including the add-email action.

**Success Indicators**:
- Dashboard accessible
- Add-email form or action available

### Step 3: Manipulated Email Addition
procedure: [[procedures/Exploit-Email-Addition-with-Encoded-Space]]

**Objective**: Bypass the email uniqueness check to add the victim's email to the attacker's account.

**Instructions**: In the add-email form or action, submit the victim's email address appended with %20 (e.g., victim@example.com%20). This evades the database check at line 123.

**Expected Output**: Email addition succeeds without error, triggering a verification email to the actual address (ignoring the space).

**Success Indicators**:
- No uniqueness error returned
- Verification email sent to victim's inbox

### Step 4: Email Verification
procedure: [[procedures/Verify-Email-and-Set-as-Primary]]

**Objective**: Verify the added email and set it as primary to enable sensitive notifications.

**Instructions**: If the attacker has access to the victim's email, open the verification link from the sent email and confirm it. Then, in the account settings, set this email as primary (line 314 update occurs without re-check).

**Expected Output**: Email verified and set as primary on attacker's account; potential receipt of payment-related emails.

**Success Indicators**:
- Verification successful
- Email listed as primary in account settings

### Step 5: Account Takeover
procedure: [[procedures/Perform-Password-Reset-for-Takeover]]

**Objective**: Use the controlled email to reset the victim's password and gain full account access.

**Instructions**: Initiate the forgot password flow using the victim's email address. Access the reset link from the victim's inbox (now controllable by attacker) and set a new password.

**Expected Output**: Successful password reset, granting login access to the victim's account.

**Success Indicators**:
- Password reset email received and acted upon
- Full control of victim's Gratipay account

## Attack Chain Summary

### Key Achievements

1. Bypassed email uniqueness via URL-encoded whitespace
2. Added and verified victim's primary email to attacker's account
3. Achieved account takeover through password reset

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Device Registration]] Account Manipulation

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Persistence]] Persistence

---
*Last updated: 2023-10-01T00:00:00Z*
