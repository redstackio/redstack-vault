---
tags:
  - account-takeover
  - email-verification-bypass
  - broken-access-control
  - vimeo
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
  - '[[procedures/Access-Victims-Logged-In-Session]]'
  - '[[procedures/Add-Unverified-Email-to-Account]]'
  - '[[procedures/Password-Reset-Using-Attackers-Email]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:32:58.039Z'
description: >-
  Multi-stage attack exploiting Vimeo's account settings to add an unverified
  email, enabling password reset and full account takeover with temporary
  physical access to a logged-in device.
skill_level: intermediate
impact_level: high
id: c981a7e8-a00c-42ea-808a-608eff7a8111
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Manipulation]]'
---
# Vimeo Account Takeover via Unverified Email Addition

Multi-stage attack chain demonstrating a complete attack workflow exploiting a Broken Access Control vulnerability in Vimeo's account settings. An attacker with temporary physical access to a victim's device can add their own email to the account without verification, then use it to reset the password and gain full control.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Physical Access to Device] --> B[Add Unverified Email]
    B --> C[Password Reset]
    C --> D[Full Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (relies on web browser access)

### Target Environment

- Web platform (Vimeo web application)
- Victim must be logged in on a shared or compromised device (e.g., cyber cafe, airport kiosk)
- No specific services/ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Temporary physical access to the victim's device
- Victim's Vimeo session must be active (no additional credentials needed for initial steps)
- Attacker's own email address under control

## Detailed Attack Procedures

### Step 1: Access Victim's Logged-In Session
procedure: [[procedures/Access-Victims-Logged-In-Session]]

**Objective**: Gain temporary control of the victim's authenticated Vimeo session on a shared device.

**Instructions**: Physically approach the device where the victim is logged into Vimeo. No commands or tools are needed; simply use the open browser tab or window to access the account settings.

**Expected Output**: Direct access to the victim's Vimeo dashboard without login prompts.

**Success Indicators**:
- Victim's account page loads with personalized content visible
- Account settings menu is accessible

### Step 2: Add Unverified Email to Account
procedure: [[procedures/Add-Unverified-Email-to-Account]]

**Objective**: Append the attacker's controlled email to the victim's account without triggering verification or password confirmation.

**Instructions**: Navigate to the account settings page in the browser. Locate the 'Add a New Email' feature and enter the attacker's email address. Submit the form; no verification code or password re-entry is required due to the vulnerability.

**Expected Output**: Confirmation that the email has been added to the account profile.

**Success Indicators**:
- New email appears in the account's email list
- No error messages or verification prompts appear

### Step 3: Password Reset Using Attacker's Email
procedure: [[procedures/Password-Reset-Using-Attackers-Email]]

**Objective**: Use the newly added email to initiate a password reset and assume control of the account.

**Instructions**: Log out of the victim's session if needed, then go to Vimeo's password reset page. Enter the victim's username or original email to trigger the reset. The reset link will be sent to the attacker's added email, allowing them to set a new password.

**Expected Output**: Access to the password reset link in the attacker's email inbox, followed by successful login with the new password.

**Success Indicators**:
- Reset email received and link clicked
- Full access to account features, videos, and settings

## Attack Chain Summary

### Key Achievements

1. Bypassed email verification to add attacker-controlled email
2. Exploited lack of password confirmation for account modification
3. Achieved full account takeover in under 2 minutes via password reset

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Account Manipulation]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
