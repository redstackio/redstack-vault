---
tags:
  - improper-authorization
  - account-takeover
  - parameter-tampering
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Manipulate-Fanclub-Subscription-Parameters]]'
  - '[[procedures/Set-Email-on-Target-Account]]'
  - '[[procedures/Initiate-Password-Reset-for-Takeover]]'
step_count: 3
techniques:
  - '[[Account Manipulation]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:24.457Z'
description: >-
  Multi-stage attack exploiting improper authorization in Chaturbate's fanclub
  subscription to manipulate account parameters, set an email, and achieve
  account takeover via password reset.
skill_level: intermediate
impact_level: high
id: 58d66741-6ecc-47cc-9528-5cf46399cc93
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
  - '[[Valid Accounts]]'
---
# Account Takeover via Fanclub Subscription Parameter Manipulation

Multi-stage attack chain demonstrating a complete attack workflow exploiting improper authorization in Chaturbate's fanclub subscription process to target another user's account, set an email address, and perform a password reset for full takeover. This requires a valid payment method for the subscription purchase and only affects accounts without an existing email.

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
    A[Parameter Manipulation] --> B[Email Setting via Subscription]
    B --> C[Password Reset Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[Burp Suite]] (for intercepting and modifying HTTP requests)
- Valid payment method (credit card or similar for subscription purchase)

### Target Environment

- Chaturbate web platform
- Fanclub subscription service
- Billing integration
- No specific ports; standard HTTPS (443)

### Initial Access Requirements

- Attacker must have a registered Chaturbate account
- Knowledge of target user's username
- Attacker's email address (to set on target)
- Network access to Chaturbate website

## Detailed Attack Procedures

### Step 1: Parameter Manipulation
procedure: [[procedures/Manipulate-Fanclub-Subscription-Parameters]]

**Objective**: Alter subscription request parameters to target another user's account instead of the attacker's own, bypassing authorization checks.

**Instructions**: Use a proxy tool like Burp Suite to intercept the fanclub subscription request. Modify the 'username' or 'target_user' parameter to the victim's username while keeping the attacker's session cookies intact. Proceed with the subscription flow.

**Expected Output**: The request is sent with tampered parameters, and the server processes it without rejecting the unauthorized target change.

**Success Indicators**:
- No authorization error in response
- Subscription proceeds to payment stage for the target account

### Step 2: Email Setting via Subscription
procedure: [[procedures/Set-Email-on-Target-Account]]

**Objective**: During the subscription purchase, set the attacker's email on the target account if it lacks one, enabling subsequent reset.

**Instructions**: Complete the payment in the intercepted request, ensuring an 'email' parameter is included with the attacker's email. The server updates the target account's profile with this email upon successful purchase.

**Expected Output**: Subscription confirmation, and the target account now has the attacker's email associated (verifiable later via reset attempt).

**Success Indicators**:
- Payment succeeds without errors
- Target account email is updated (test by attempting reset)

### Step 3: Password Reset Takeover
procedure: [[procedures/Initiate-Password-Reset-for-Takeover]]

**Objective**: Use the newly set email to request a password reset and gain control of the target account.

**Instructions**: Navigate to Chaturbate's password reset page, enter the target username, and provide the attacker's email. Receive the reset link via email and use it to set a new password.

**Expected Output**: Reset email received, link clicked, new password set, and login successful with new credentials.

**Success Indicators**:
- Reset email arrives in attacker's inbox
- Account login works with new password
- Full access to target account features

## Attack Chain Summary

### Key Achievements

1. Bypassed authorization to manipulate another user's subscription
2. Set unauthorized email on target account via billing flow
3. Achieved complete account takeover through password reset

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Manipulation]] Account Manipulation
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
