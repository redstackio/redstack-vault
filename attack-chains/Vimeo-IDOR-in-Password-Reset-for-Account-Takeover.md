---
tags:
  - idor
  - account-takeover
  - password-reset
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-IDOR-in-Password-Reset]]'
  - '[[procedures/Exploit-IDOR-to-Initiate-Unauthorized-Reset]]'
  - '[[procedures/Complete-Password-Reset-and-Takeover-Account]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:25:29.960Z'
description: >-
  Multi-stage exploitation of an Insecure Direct Object Reference (IDOR)
  vulnerability in Vimeo's password reset functionality, enabling unauthorized
  password resets and full account takeover for any user.
skill_level: intermediate
impact_level: high
id: 38782f78-5334-431e-8e93-f1f885c12c92
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Manipulation]]'
---
# Vimeo IDOR in Password Reset for Account Takeover

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR in Vimeo's password reset feature to achieve unauthorized account takeover.

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
    A[Identify IDOR Vulnerability] --> B[Initiate Unauthorized Reset]
    B --> C[Complete Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or proxy like Burp Suite for request manipulation

### Target Environment

- Web platform (Vimeo.com)
- Access to password reset endpoint
- No special services/ports required beyond standard HTTPS (443)

### Initial Access Requirements

- No prior credentials needed
- Public network access to Vimeo.com
- Ability to intercept and modify HTTP requests

## Detailed Attack Procedures

### Step 1: Identify IDOR in Password Reset
procedure: [[procedures/Identify-IDOR-in-Password-Reset]]

**Objective**: Detect the IDOR vulnerability by testing the password reset endpoint for improper authorization checks on user identifiers.

**Instructions**: Start by navigating to Vimeo's password reset page and initiating a reset for your own account. Intercept the request using a proxy tool. Examine the parameters, such as user ID or token, and attempt to replace them with another user's identifier (e.g., obtained from public profiles or enumeration). Submit the modified request and observe if a reset process is initiated for the target without authentication.

**Expected Output**: Successful initiation of reset for the unauthorized account, confirming the IDOR.

**Success Indicators**:
- Reset link or token generated for target user
- No ownership verification error

### Step 2: Exploit IDOR to Initiate Unauthorized Reset
procedure: [[procedures/Exploit-IDOR-to-Initiate-Unauthorized-Reset]]

**Objective**: Leverage the identified IDOR to request a password reset for a target account by manipulating the direct object reference.

**Instructions**: Using the intercepted request from Step 1, modify the user identifier parameter (e.g., change `user_id=your_id` to `user_id=target_id`). Resubmit the request to the password reset endpoint. Monitor the response for the reset token or link associated with the target account.

**Expected Output**: Response containing a valid reset link or token for the target user's account.

**Success Indicators**:
- Receipt of reset mechanism without target user interaction
- No access denied errors

### Step 3: Complete Password Reset and Takeover Account
procedure: [[procedures/Complete-Password-Reset-and-Takeover-Account]]

**Objective**: Use the obtained reset token to change the target's password and gain full control of the account.

**Instructions**: Access the reset link or use the token in a new request to set a new password. Submit the password change form with your chosen credentials. Once completed, log in to the target account using the new password to verify control.

**Expected Output**: Successful password update and login as the target user.

**Success Indicators**:
- Ability to log in with new credentials
- Full access to account features and data

## Attack Chain Summary

### Key Achievements

1. Identified and confirmed IDOR in password reset without authentication
2. Initiated unauthorized reset for any target account
3. Achieved complete account takeover, enabling data access or further abuse

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Manipulation]] Account Manipulation

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
