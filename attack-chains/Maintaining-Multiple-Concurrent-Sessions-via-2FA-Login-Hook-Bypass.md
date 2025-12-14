---
tags:
  - 2fa
  - authentication-bypass
  - session-management
  - persistence
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
procedures:
  - '[[procedures/Bypass-2FA-Login-Hooks-for-Multiple-Sessions]]'
step_count: 2
techniques:
  - '[[Valid Accounts]]'
description: >-
  Exploits a flaw in the 2FA authentication flow that skips standard logon
  hooks, preventing logout of existing sessions and enabling multiple active
  sessions for persistent access.
skill_level: low
impact_level: medium
id: 5ba4cabe-68a9-47f2-bc86-a6364367bc8b
created_at: '2025-12-14T17:24:45.543Z'
updated_at: '2025-12-14T17:24:45.543Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Maintaining Multiple Concurrent Sessions via 2FA Login Hook Bypass

Multi-stage attack chain demonstrating how to exploit a 2FA login process that bypasses session logout hooks, allowing an attacker with valid credentials to maintain multiple active sessions simultaneously. This can facilitate persistent unauthorized access or session hijacking in broader attack scenarios, as discovered during the rollout of new 2FA options in the Legal Robot platform.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Low |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Establish Initial Session] --> B[Perform 2FA Login]
    B --> C[Verify Multiple Active Sessions]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Web application with 2FA enabled (e.g., Legal Robot platform)
- Valid user credentials with 2FA configured
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Valid username and password for the target account
- Access to 2FA authentication method (e.g., TOTP code or app)
- Network access to the login endpoint

## Detailed Attack Procedures

### Step 1: Establish Initial Session
procedure: [[procedures/Bypass-2FA-Login-Hooks-for-Multiple-Sessions]]

**Objective**: Create an active session using standard login to serve as the baseline for testing the bypass.

**Instructions**: Open a web browser and navigate to the login page of the target application. Enter valid credentials without using 2FA (if possible) or use a non-2FA flow to establish the first session. Log in successfully and verify access to the dashboard or protected area to confirm the session is active.

**Expected Output**: Successful login with an active session token (visible in browser developer tools under Network or Application tabs).

**Success Indicators**:
- User is logged in and can access account features
- Session cookie or token is present and valid

### Step 2: Perform 2FA Login and Verify Multiple Sessions
procedure: [[procedures/Bypass-2FA-Login-Hooks-for-Multiple-Sessions]]

**Objective**: Execute a 2FA login in a new browser session to bypass logout hooks, confirming both sessions remain active.

**Instructions**: Open a new incognito/private browser window or use a different browser. Navigate to the login page and enter the same valid credentials, but this time proceed through the 2FA flow (e.g., enter TOTP code). Complete the login. Then, return to the first browser session and refresh the page or perform an action to verify it remains authenticated. Check both sessions for active status.

**Expected Output**: Both browser sessions show the user as logged in, with no automatic logout of the initial session.

**Success Indicators**:
- Initial session remains active post-2FA login
- No session termination or redirect to login page in either session
- Multiple session tokens coexist without conflict

## Attack Chain Summary

### Key Achievements

1. Successfully bypassed session logout hooks during 2FA authentication
2. Maintained multiple concurrent active sessions with valid credentials
3. Demonstrated potential for persistent access without detection in session management

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Persistence]]

---
*Last updated: 2023-10-01*
