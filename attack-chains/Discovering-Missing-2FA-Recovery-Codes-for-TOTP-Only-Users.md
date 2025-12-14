---
tags:
  - 2fa
  - totp
  - u2f
  - business-logic
  - authentication
  - recovery-code
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Enable-TOTP-as-Sole-2FA-Method]]'
  - '[[procedures/Check-for-2FA-Recovery-Code-Feature]]'
  - '[[procedures/Verify-Recovery-Code-Availability-in-U2F-Configuration]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:47.499Z'
description: >-
  A multi-step process to identify a business logic flaw in 2FA implementation
  where TOTP-only users lack access to recovery codes, potentially leading to
  account lockout.
skill_level: beginner
impact_level: medium
id: 4277cff3-3e96-4e6d-82ce-e2b6ff9ccdf3
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discovering Missing 2FA Recovery Codes for TOTP-Only Users

Multi-stage attack chain demonstrating the identification of a business logic error in a web application's 2FA setup, where users relying solely on TOTP are deprived of recovery code access, unlike those using U2F.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Enable TOTP 2FA] --> B[Check Recovery Access]
    B --> C[Compare with U2F]
    C --> D[Confirm Logic Flaw]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual testing via web interface)

### Target Environment

- Web application with 2FA settings page
- Access to authentication configuration UI
- Test account with admin or user privileges

### Initial Access Requirements

- Valid user credentials for the target application
- Network access to the web platform
- No prior exploits needed; legitimate account setup

## Detailed Attack Procedures

### Step 1: Enable TOTP 2FA
procedure: [[procedures/Enable-TOTP-as-Sole-2FA-Method]]

**Objective**: Configure the account to use only TOTP for 2FA, simulating a user without hardware keys.

**Instructions**: Navigate to the 2FA settings in the application and enable TOTP by scanning the QR code with an authenticator app. Ensure no other 2FA methods like U2F are activated.

**Expected Output**: TOTP is successfully enabled, and login now requires authenticator codes.

**Success Indicators**:
- Authenticator app generates valid TOTP codes for login
- No other 2FA options are selected

### Step 2: Check for 2FA Recovery Code Feature
procedure: [[procedures/Check-for-2FA-Recovery-Code-Feature]]

**Objective**: Attempt to locate and access any recovery code generation or viewing feature for the TOTP setup.

**Instructions**: In the 2FA settings page, look for buttons, links, or sections labeled 'Recovery Codes', 'Backup Codes', or similar. Try generating or viewing them if available.

**Expected Output**: Absence of recovery code option, or an error/blank section indicating unavailability.

**Success Indicators**:
- No recovery code feature visible for TOTP-only setup
- UI elements present only for other 2FA types

### Step 3: Verify Recovery Code Availability in U2F Configuration
procedure: [[procedures/Verify-Recovery-Code-Availability-in-U2F-Configuration]]

**Objective**: Compare the TOTP setup against a U2F-enabled account to confirm the inconsistency in recovery code access.

**Instructions**: Create or switch to a test account with U2F enabled (alongside or instead of TOTP). Navigate to the same 2FA settings and check for recovery code access. Note the presence of fallback options like TOTP for U2F users.

**Expected Output**: Recovery codes and fallback mechanisms are available for U2F users but missing for TOTP-only.

**Success Indicators**:
- U2F accounts show recovery code links
- Confirmed disparity highlights the business logic error

## Attack Chain Summary

### Key Achievements

1. Successfully isolated TOTP as the only 2FA method
2. Identified missing recovery code feature for TOTP users
3. Verified inconsistency by comparison with U2F, proving potential for user lockout

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
