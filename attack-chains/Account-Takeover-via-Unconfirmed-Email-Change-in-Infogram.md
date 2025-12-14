---
tags:
  - account-takeover
  - broken-access-control
  - email-change
  - session-hijacking
type: attack_chain
tools: []
tactics:
  - '[[Persistence]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Account-Settings]]'
  - '[[procedures/Change-Email-Without-Confirmation]]'
  - '[[procedures/Sign-Out-After-Modification]]'
  - '[[procedures/Verify-Takeover-via-New-Login]]'
step_count: 4
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:32:57.809Z'
description: >-
  Multi-stage attack exploiting the lack of email change confirmation in
  Infogram's account settings to achieve full account takeover.
skill_level: beginner
impact_level: high
id: 18dc204a-5d0b-484e-af9b-f3d6a08aa8c9
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Account Takeover via Unconfirmed Email Change in Infogram

Multi-stage attack chain demonstrating a complete attack workflow exploiting the absence of confirmation or notification during email address changes in Infogram's account settings, enabling an attacker with temporary session access to fully take over the victim's account.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Gain Session Access] --> B[Modify Email]
    B --> C[Sign Out]
    C --> D[Login with New Email]
    D --> E[Account Takeover Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Infogram web application
- Account with active session (e.g., via shared device or session hijacking)
- No special ports or services required beyond standard HTTPS (443)

### Initial Access Requirements

- Temporary access to a logged-in session as the victim
- Attacker's own email address for redirection
- No prior credentials needed beyond the session

## Detailed Attack Procedures

### Step 1: Access the Account Settings
procedure: [[procedures/Access-Account-Settings]]

**Objective**: Navigate to the profile settings to locate the email change functionality.

**Instructions**: While logged in as the victim, open the Infogram web application in a browser and locate the account or profile section in the user menu (typically under a settings icon or dropdown).

**Expected Output**: Profile or account settings page loads, displaying current email and edit options.

**Success Indicators**:
- Settings page accessible without errors
- Victim's current email visible

### Step 2: Change the Email Without Confirmation
procedure: [[procedures/Change-Email-Without-Confirmation]]

**Objective**: Alter the email address to the attacker's controlled email, exploiting the lack of verification.

**Instructions**: In the email field, replace the victim's email (e.g., victim@example.com) with the attacker's email (e.g., attacker@evil.com). Submit the form. The change applies immediately without any confirmation email or notification to the original address.

**Expected Output**: Success message or redirect confirming the email update; no alerts sent.

**Success Indicators**:
- Email field updates to new value
- No verification prompt or email received by victim

### Step 3: Sign Out After Modification
procedure: [[procedures/Sign-Out-After-Modification]]

**Objective**: Terminate the current session to force future logins through the new email.

**Instructions**: From the user menu, select the logout option to end the session.

**Expected Output**: User is redirected to the login page; session ends.

**Success Indicators**:
- Logout successful
- No immediate access to account post-logout without new credentials

### Step 4: Verify Takeover via New Login
procedure: [[procedures/Verify-Takeover-via-New-Login]]

**Objective**: Confirm control by logging in with the new email and ensuring the victim cannot access.

**Instructions**: Attempt login with the original victim email (should fail). Then, log in using the attacker's new email; no password reset is needed as the session change suffices.

**Expected Output**: Login with old email fails (account not found or invalid); login with new email succeeds, granting full access to the account.

**Success Indicators**:
- Victim's login denied
- Attacker gains dashboard access with victim's data

## Attack Chain Summary

### Key Achievements

1. Silent email redirection without victim notification
2. Full account control transfer to attacker
3. Loss of access for the legitimate user

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Manipulation]]

### MITRE ATT&CK Tactics

- [[Persistence]]

---
*Last updated: 2023-10-01T00:00:00Z*
