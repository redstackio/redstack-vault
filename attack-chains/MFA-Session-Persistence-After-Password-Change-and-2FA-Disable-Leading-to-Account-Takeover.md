---
tags:
  - mfa-bypass
  - session-fixation
  - account-takeover
  - 2fa
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
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Initiate-Pending-MFA-Login]]'
  - '[[procedures/Change-Password-and-Disable-2FA]]'
  - '[[procedures/Verify-and-Exploit-Persistent-Session]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[Reversible Encryption]]'
updated_at: '2025-12-14T17:24:47.660Z'
description: >-
  Exploits a flaw in Moneybird's MFA implementation where pending login sessions
  persist after password changes and 2FA disablement, enabling unauthorized
  access.
skill_level: intermediate
impact_level: high
id: 32a789ae-8e7c-4da5-9ebb-4d366723ec54
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Reversible Encryption]]'
---
# MFA Session Persistence After Password Change and 2FA Disable Leading to Account Takeover

Multi-stage attack chain demonstrating exploitation of improper session management in Moneybird's MFA system, allowing an attacker to maintain access via a pending session even after security changes.

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
    A[Initiate Pending MFA Login] --> B[Change Password and Disable 2FA]
    B --> C[Verify and Exploit Persistent Session]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox with developer tools)

### Target Environment

- Moneybird web application
- Active user account with MFA enabled
- Network access to Moneybird's login portal

### Initial Access Requirements

- Valid credentials for the target account to initiate login
- Ability to access account settings (assumes partial control or social engineering to trigger changes)
- Pending MFA session token or identifier

## Detailed Attack Procedures

### Step 1: Initiate Pending MFA Login
procedure: [[procedures/Initiate-Pending-MFA-Login]]

**Objective**: Start the authentication process to create a pending MFA session that can later be exploited.

**Instructions**: Open a web browser and navigate to the Moneybird login page. Enter valid credentials to trigger the MFA prompt, but do not complete the verification yet. Note the session identifier from browser developer tools (e.g., check network requests for session cookies or tokens).

**Expected Output**: A pending MFA challenge screen, with an active session in the backend.

**Success Indicators**:
- MFA prompt appears without full access granted
- Session cookie or token is visible in browser dev tools

### Step 2: Change Password and Disable 2FA
procedure: [[procedures/Change-Password-and-Disable-2FA]]

**Objective**: Modify account security settings to invalidate expected sessions, but due to the vulnerability, the pending session remains active.

**Instructions**: While logged in with an existing session (or via another browser tab), navigate to account settings in Moneybird. Update the password to a new value and disable two-step verification. Confirm the changes and log out if necessary.

**Expected Output**: Confirmation message that password is updated and 2FA is disabled.

**Success Indicators**:
- Password change successful
- 2FA toggle shows as disabled in settings

### Step 3: Verify and Exploit Persistent Session
procedure: [[procedures/Verify-and-Exploit-Persistent-Session]]

**Objective**: Return to the pending MFA session and complete login to gain unauthorized access despite the changes.

**Instructions**: Switch back to the browser tab with the pending MFA login. Attempt to complete the MFA step (e.g., enter a code if still prompted, or simply proceed). The session should grant full access without re-authentication.

**Expected Output**: Successful login to the Moneybird dashboard with full account privileges.

**Success Indicators**:
- Access granted without new password or 2FA
- Account actions (e.g., view invoices) are available

## Attack Chain Summary

### Key Achievements

1. Created a pending MFA session before security changes
2. Bypassed password and 2FA updates via session persistence
3. Achieved account takeover with unauthorized access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Reversible Encryption]] Multi-Factor Authentication Instrument

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Persistence]] Persistence

---
*Last updated: 2024-01-01T00:00:00Z*
