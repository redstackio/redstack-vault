---
tags:
  - mfa-bypass
  - session-management
  - authentication
  - web
type: attack_chain
tools: []
tactics:
  - '[[Persistence]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '[TIMESTAMP]'
procedures:
  - '[[procedures/Access-Account-on-Multiple-Devices]]'
  - '[[procedures/Activate-MFA-on-One-Device]]'
  - '[[procedures/Verify-Session-Persistence-on-Second-Device]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:48.472Z'
description: >-
  Demonstrates a design flaw where enabling MFA does not invalidate existing
  sessions, allowing persistent access without re-authentication.
skill_level: beginner
impact_level: medium
id: a35c960a-25e0-43ad-ad8b-f21c8d48de81
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# MFA Bypass via Uninvalidated Existing Sessions in Grammarly Account

Multi-stage attack chain demonstrating a complete attack workflow.

The vulnerability exploits a flaw in the MFA implementation on Grammarly's account management system, where activating 2FA does not terminate existing sessions. This allows an attacker with prior access to maintain control without providing the new MFA code. The chain involves logging in on multiple devices, enabling MFA on one, and confirming persistence on the other. No actual exploitation beyond demonstration occurred, and no users were impacted.

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
    A[Multi-Device Login] --> B[MFA Activation]
    B --> C[Session Persistence Check]
    C --> D[Bypass Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Web platform
- Access to https://account.grammarly.com/
- Valid account credentials

### Initial Access Requirements

- Existing account credentials
- No special network position required (public internet access)
- Prior login not needed beyond standard authentication

## Detailed Attack Procedures

### Step 1: Multi-Device Login
procedure: [[procedures/Access-Account-on-Multiple-Devices]]

**Objective**: Establish simultaneous sessions on two devices to test session handling.

**Instructions**: Log in to the target account using the same credentials on both devices via the web interface.

**Expected Output**: Active sessions on both devices, allowing navigation within the account dashboard.

**Success Indicators**:
- Successful login on device A
- Successful login on device B without logout on the first device

### Step 2: MFA Activation
procedure: [[procedures/Activate-MFA-on-One-Device]]

**Objective**: Enable 2FA on one device to trigger the security change, observing effects on other sessions.

**Instructions**: Navigate to the security settings on device A and complete the MFA setup process.

**Expected Output**: MFA successfully enabled, with a new 2FA method (e.g., authenticator app) configured.

**Success Indicators**:
- Confirmation message for MFA activation
- 2FA code prompt appears for new logins on device A

### Step 3: Session Persistence Check
procedure: [[procedures/Verify-Session-Persistence-on-Second-Device]]

**Objective**: Confirm that the existing session on the second device remains valid post-MFA activation.

**Instructions**: Reload the page or perform an action on device B to test session continuity.

**Expected Output**: Session remains active; no MFA prompt or logout occurs.

**Success Indicators**:
- Page reloads without authentication challenge
- Continued access to account features on device B

## Attack Chain Summary

### Key Achievements

1. Simultaneous multi-device access established without session conflicts.
2. MFA activated without disrupting existing sessions.
3. Demonstrated bypass of MFA enforcement for persistent unauthorized access.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Persistence]]

---
*Last updated: [TIMESTAMP]*
