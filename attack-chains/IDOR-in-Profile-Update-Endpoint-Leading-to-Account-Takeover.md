---
tags:
  - idor
  - account-takeover
  - authorization-bypass
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-and-Verify-Test-Accounts]]'
  - '[[procedures/Capture-Profile-Update-Request-with-Burp-Suite]]'
  - '[[procedures/Extract-Victim-User-ID]]'
  - '[[procedures/Exploit-IDOR-by-Modifying-Request]]'
  - '[[procedures/Perform-Password-Reset-for-Account-Takeover]]'
step_count: 5
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:12.361Z'
description: >-
  Multi-stage attack exploiting Insecure Direct Object Reference (IDOR) in the
  profile update endpoint to perform unauthorized profile modifications,
  enabling password reset and full account takeover without victim interaction.
skill_level: intermediate
impact_level: high
id: b91e1993-8f82-430c-ac7b-a62c65a663d0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# IDOR in Profile Update Endpoint Leading to Account Takeover

Multi-stage attack chain demonstrating a complete workflow for exploiting an Insecure Direct Object Reference (IDOR) vulnerability in the profile update endpoint on mtnmobad.mtnbusiness.com.ng, allowing unauthorized updates to user profiles and subsequent account takeover via password reset redirection.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create and Verify Accounts] --> B[Capture Attacker Profile Request]
    B --> C[Extract Victim User ID]
    C --> D[Modify Request to Exploit IDOR]
    D --> E[Password Reset and Account Takeover]

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

- Web platform (mtnmobad.mtnbusiness.com.ng)
- Required services/ports: HTTPS on port 443
- Network access requirements: Direct internet access to the target site

### Initial Access Requirements

- No prior credentials needed beyond creating test accounts
- Network position: External attacker
- Prior access needed: None, but ability to register accounts

## Detailed Attack Procedures

### Step 1: Create and Verify Accounts

procedure: [[procedures/Create-and-Verify-Test-Accounts]]

**Objective**: Establish attacker and victim accounts to obtain necessary identifiers and test the environment.

**Instructions**: Register two separate accounts on the target site using different email addresses. Confirm email verification for both by checking the respective inboxes and clicking the verification links.

**Expected Output**: Two verified accounts ready for login, with access to profile update functionality.

**Success Indicators**:
- Email verification emails received and accounts activated
- Ability to log in to both accounts

### Step 2: Capture Profile Update Request

procedure: [[procedures/Capture-Profile-Update-Request-with-Burp-Suite]]

**Objective**: Intercept the legitimate profile update request from the attacker's account to understand the request structure.

**Instructions**: Log in to the attacker account using a browser configured with Burp Suite proxy. Navigate to the profile update section, make a minor change (e.g., update address), and intercept the POST request in Burp Suite's Proxy tab. Forward the request to the Repeater tab for later modification.

**Expected Output**: Captured HTTP request in Repeater showing the profile update endpoint, including the attacker's numeric user ID in the path (e.g., /update/ID).

**Success Indicators**:
- Request successfully intercepted and visible in Repeater
- Profile update completes successfully for attacker account

### Step 3: Extract Victim User ID

procedure: [[procedures/Extract-Victim-User-ID]]

**Objective**: Identify the numeric user ID associated with the victim account for use in the IDOR exploitation.

**Instructions**: In a separate browser session, log in to the victim account. Navigate to the profile update section and trigger a profile update action. Use Burp Suite to intercept the request and note the numeric ID in the endpoint path without forwarding or modifying it.

**Expected Output**: Victim's numeric user ID extracted from the request path (e.g., /update/12345).

**Success Indicators**:
- Victim ID positively identified and noted
- No changes made to victim profile

### Step 4: Exploit IDOR by Modifying Request

procedure: [[procedures/Exploit-IDOR-by-Modifying-Request]]

**Objective**: Perform unauthorized update to the victim's profile by altering the captured request to reference the victim ID and redirect password reset to the attacker's email.

**Instructions**: In Burp Suite Repeater, take the captured attacker request. Replace the user ID in the path with the victim's ID from Step 3. Modify the 'username' parameter (which maps to email) to the attacker's email address, while keeping the 'email' field as the victim's original. Send the modified request.

**Expected Output**: HTTP 200 or success response indicating the profile update was applied to the victim's account.

**Success Indicators**:
- Response confirms successful update
- Victim's profile now associates password reset with attacker's email

### Step 5: Password Reset and Account Takeover

procedure: [[procedures/Perform-Password-Reset-for-Account-Takeover]]

**Objective**: Leverage the modified profile to reset the victim's password and gain full control of the account.

**Instructions**: On the login page, initiate a password reset using the victim's username/email. Receive the reset link in the attacker's email inbox. Click the link to set a new password, then log in to the victim's account with the new credentials.

**Expected Output**: Successful login to the victim's account using the new password.

**Success Indicators**:
- Password reset email received by attacker
- Full access to victim's account dashboard and features

## Attack Chain Summary

### Key Achievements

1. Unauthorized profile modification via IDOR exploitation
2. Redirection of password reset to attacker's email
3. Complete account takeover without victim interaction

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Account Discovery]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
