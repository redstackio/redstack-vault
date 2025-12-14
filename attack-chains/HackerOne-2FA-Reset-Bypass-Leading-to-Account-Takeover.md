---
tags:
  - 2fa-bypass
  - account-takeover
  - authentication-bypass
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Enable-2FA-on-HackerOne-Account]]'
  - '[[procedures/Trigger-2FA-Reset-Request]]'
  - '[[procedures/Ignore-2FA-Reset-Cancellation-Email]]'
  - '[[procedures/Access-Account-After-2FA-Disablement]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
updated_at: '2025-12-14T17:33:12.295Z'
description: >-
  Exploits a flaw in HackerOne's 2FA reset process to disable two-factor
  authentication automatically if the victim ignores the cancellation email,
  enabling login with just email and password for full account takeover.
skill_level: low
impact_level: high
id: 88279cf0-2b17-409c-9c1f-62bd59b1e379
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
---
# HackerOne 2FA Reset Bypass Leading to Account Takeover

Multi-stage attack chain demonstrating a complete attack workflow exploiting a vulnerability in HackerOne's 2FA reset mechanism.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~24 hours |
| Skill Level | Low |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup 2FA] --> B[Trigger Reset]
    B --> C[Wait for Auto-Disable]
    C --> D[Account Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (browser-based interaction)

### Target Environment

- HackerOne web platform (https://hackerone.com)
- Access to victim's email and password
- Victim's email service for monitoring (attacker does not interact)

### Initial Access Requirements

- Valid email and password for the target HackerOne account
- No prior network access beyond internet connectivity
- Ability to wait 24 hours without victim intervention

## Detailed Attack Procedures

### Step 1: Enable 2FA on Account
procedure: [[procedures/Enable-2FA-on-HackerOne-Account]]

**Objective**: Set up two-factor authentication on the target account to enable the reset exploit.

**Instructions**: Log in to the HackerOne account using the known email and password, navigate to account settings, and configure 2FA via TOTP setup. Once enabled, sign out of the account.

**Expected Output**: 2FA successfully enabled, confirmed by the setup interface; account logged out.

**Success Indicators**:
- 2FA prompt appears on next login attempt
- Account settings reflect 2FA activation

### Step 2: Trigger 2FA Reset Request
procedure: [[procedures/Trigger-2FA-Reset-Request]]

**Objective**: Initiate the 2FA reset process during login to send a cancellation email to the victim.

**Instructions**: Navigate to https://hackerone.com/login, enter the victim's email and password, but skip the TOTP input field. Select the 'Reset two-factor authentication' option and confirm by clicking OK.

**Expected Output**: An email is sent to the victim's registered email address with a link to cancel the reset request.

**Success Indicators**:
- Reset request initiated without TOTP
- Confirmation dialog appears and is acknowledged
- Victim receives the cancellation email (verifiable if attacker has email access, but not required)

### Step 3: Ignore 2FA Reset Cancellation Email
procedure: [[procedures/Ignore-2FA-Reset-Cancellation-Email]]

**Objective**: Allow the reset request to proceed by not interacting with the victim's email.

**Instructions**: Do nothing with the email sent to the victim. The email contains a prompt to cancel the reset; if ignored for 24 hours, 2FA will auto-disable.

**Expected Output**: No action taken; after 24 hours, 2FA is disabled server-side.

**Success Indicators**:
- Victim does not click the cancellation link
- No further emails or notifications from HackerOne regarding cancellation

### Step 4: Access Account After 2FA Disablement
procedure: [[procedures/Access-Account-After-2FA-Disablement]]

**Objective**: Log in to the account using only email and password once 2FA is disabled.

**Instructions**: After waiting exactly 24 hours from the reset trigger, return to https://hackerone.com/login, enter the email and password, and proceed without any 2FA prompt.

**Expected Output**: Successful login granting full access to the HackerOne account dashboard and features.

**Success Indicators**:
- No 2FA prompt during login
- Full account control achieved, including ability to view reports, change settings, etc.

## Attack Chain Summary

### Key Achievements

1. Bypassed 2FA protection using the reset mechanism's auto-disable feature
2. Achieved full account takeover with only email/password credentials
3. Demonstrated low-skill exploit requiring minimal technical intervention beyond waiting

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Modify Authentication Process]] Modify Authentication Process

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
