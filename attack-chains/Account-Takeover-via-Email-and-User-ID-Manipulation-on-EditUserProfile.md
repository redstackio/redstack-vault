---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - account-takeover
  - auth-bypass
  - idor
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Create-Test-Accounts-and-Login]]'
  - '[[procedures/Prepare-Profile-Edit-Form]]'
  - '[[procedures/Intercept-and-Modify-Request-for-Takeover]]'
  - '[[procedures/Execute-Takeover-and-Verify-Access]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:06.619Z'
description: >-
  Multi-stage attack exploiting improper authentication checks on the
  EditUserProfile endpoint to overwrite victim account details and achieve
  account takeover.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Account Takeover via Email and User ID Manipulation on EditUserProfile

Multi-stage attack chain demonstrating account takeover by exploiting lack of authentication checks on the EditUserProfile endpoint, allowing email and user ID manipulation to overwrite victim credentials.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Account Setup] --> B[Form Preparation]
    B --> C[Request Manipulation]
    C --> D[Takeover Execution]
    D --> E[Access Verification]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web application with user registration and profile editing features
- Access to EditUserProfile endpoint (e.g., https://target.com/user/EditUserProfile)
- Intercepting proxy capability

### Initial Access Requirements

- Ability to register new accounts
- Valid credentials for attacker account
- Knowledge of victim's email (e.g., via enumeration or prior recon)
- Victim's user ID (may require brute-force or enumeration)

## Detailed Attack Procedures

### Step 1: Account Setup
procedure: [[procedures/Create-Test-Accounts-and-Login]]

**Objective**: Establish attacker and victim accounts to prepare for manipulation.

**Instructions**: Register two separate accounts on the target platform, one as the attacker and one as the victim. Log in to both to obtain session cookies if needed.

**Expected Output**: Successful registration and login for both accounts.

**Success Indicators**:
- Attacker account active
- Victim account active
- Access to EditUserProfile page

### Step 2: Form Preparation
procedure: [[procedures/Prepare-Profile-Edit-Form]]

**Objective**: Initiate the profile edit process with attacker's credentials to set up for request interception.

**Instructions**: Navigate to the EditUserProfile endpoint using the attacker's session. Enter the attacker's current password for authentication and modify the email field to the victim's email.

**Expected Output**: Form populated with changes, ready for submission.

**Success Indicators**:
- Password field authenticated
- Email field updated to victim's email
- Form submission intercepted

### Step 3: Request Manipulation
procedure: [[procedures/Intercept-and-Modify-Request-for-Takeover]]

**Objective**: Intercept the submission request and alter the user ID to target the victim's account.

**Instructions**: Use an intercepting proxy to capture the form submission. Modify the user ID parameter from the attacker's to the victim's (brute-force if unknown). Forward the request and observe the response.

**Expected Output**: 302 redirect indicating successful profile update.

**Success Indicators**:
- Request modified successfully
- Victim's account details overwritten
- No authentication errors

### Step 4: Takeover Execution and Verification
procedure: [[procedures/Execute-Takeover-and-Verify-Access]]

**Objective**: Complete the overwrite process and confirm access to the victim's account using attacker's password.

**Instructions**: Revert any temporary changes if needed and resubmit. Attempt login to the victim's email with the attacker's password.

**Expected Output**: Successful login to victim's account.

**Success Indicators**:
- Login successful with attacker's password on victim's email
- Full access to victim's profile and features
- Original attacker account preserved

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication checks to overwrite victim account details
2. Achieved unauthorized access without resetting passwords
3. Demonstrated full account takeover with minimal tools

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T12:00:00Z*
