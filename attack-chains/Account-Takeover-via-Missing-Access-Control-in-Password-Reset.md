---
tags:
  - account-takeover
  - password-reset
  - authentication-bypass
  - access-control
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Initiate-Password-Reset]]'
  - '[[procedures/Compromise-Reset-Link]]'
  - '[[procedures/Reset-Password-and-Auto-Login]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
description: >-
  Multi-stage attack exploiting a missing access control in the password reset
  process, allowing automatic login after reset without additional
  authentication, leading to full account takeover if the reset link is
  compromised.
skill_level: intermediate
impact_level: high
id: 7f13299d-24c8-4153-80b4-1644d8dafa1d
created_at: '2025-12-14T17:28:58.789Z'
updated_at: '2025-12-14T17:28:58.789Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Account Takeover via Missing Access Control in Password Reset

Multi-stage attack chain demonstrating a complete attack workflow exploiting improper authentication in the password reset feature of a web application.

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
    A[Initiate Reset] --> B[Compromise Link]
    B --> C[Reset and Login]
    C --> D[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox)
- Access to email or mechanism to intercept reset links

### Target Environment

- Web application with password reset feature
- No specific ports required beyond standard HTTPS (443)
- Network access to the application's frontend

### Initial Access Requirements

- Knowledge of target user's email address
- Ability to compromise reset link (e.g., via referrer leakage)
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Initiate Password Reset
procedure: [[procedures/Initiate-Password-Reset]]

**Objective**: Trigger the password reset process to generate a reset link for the target account.

**Instructions**: Navigate to the application's login or forgot password page and enter the target user's email address to request a reset. The application sends a reset link via email or similar mechanism.

**Expected Output**: Receipt of a password reset email containing a unique reset link.

**Success Indicators**:
- Reset email received
- Reset link extracted from email

### Step 2: Compromise Reset Link
procedure: [[procedures/Compromise-Reset-Link]]

**Objective**: Obtain the reset link without legitimate access, exploiting leakage such as referrer tokens.

**Instructions**: Monitor for the reset link exposure, for example, through browser referrer headers, shared logs, or other leakage vectors in the application's implementation.

**Expected Output**: Valid reset link in possession of the attacker.

**Success Indicators**:
- Link obtained without authentication
- Link verified as active (e.g., by attempting to access it)

### Step 3: Reset Password and Auto-Login
procedure: [[procedures/Reset-Password-and-Auto-Login]]

**Objective**: Use the compromised link to change the password and gain automatic session access to the account.

**Instructions**: Open the reset link in a browser, enter a new password, submit the form, and observe automatic login due to the missing access controls.

**Expected Output**: Successful password change and logged-in session with full account access.

**Success Indicators**:
- Password updated
- Active session established without further authentication
- Access to account dashboard or sensitive data

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication via flawed reset process
2. Achieved full account takeover
3. Demonstrated impact of violating OWASP password reset guidelines

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
