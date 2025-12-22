---
tags:
  - account-takeover
  - authentication-bypass
  - 2fa-bypass
  - replay-attack
  - basecamp
type: attack_chain
tools:
  - '[[tools/HTTP-Proxy-Interceptor]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Login-to-Victim-Account-with-Old-Password]]'
  - '[[procedures/Enable-2FA-and-Logout]]'
  - '[[procedures/Capture-Successful-2FA-Backup-Code-Response]]'
  - '[[procedures/Disable-2FA-in-Account]]'
  - '[[procedures/Replay-Captured-Response-After-Password-Change]]'
step_count: 6
techniques:
  - '[[Valid Accounts]]'
  - '[[Forge Web Credentials]]'
updated_at: '2025-12-14T17:31:30.630Z'
description: >-
  Multi-stage attack exploiting improper authentication in Basecamp's login
  process by capturing and replaying a 2FA backup code response to bypass a
  password change and achieve account takeover.
skill_level: intermediate
impact_level: high
id: b285d3b3-c891-4f5a-af40-7d7f733fb66c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Forge Web Credentials]]'
---
# Basecamp Account Takeover via Replayed 2FA Backup Code Response After Password Change

Multi-stage attack chain demonstrating a complete attack workflow exploiting an improper authentication vulnerability in Basecamp's login process. The attacker, with initial access via the old password, sets up 2FA, captures a successful login response using a backup code, disables 2FA, and then replays the captured response after the victim changes their password to bypass authentication and take over the account.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Login with Old Password] --> B[Enable 2FA and Logout]
    B --> C[Login with Backup Code and Capture Response]
    C --> D[Disable 2FA]
    D --> E[Victim Changes Password]
    E --> F[Replay Captured Response for Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#9b59b6
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/HTTP-Proxy-Interceptor]]

### Target Environment

- Web application (Basecamp login at sign-in page, likely POST to /sessions)
- Required services/ports: HTTPS (443)
- Network access requirements: Direct internet access to Basecamp domain

### Initial Access Requirements

- Knowledge of victim's old password
- Ability to access the victim's account initially
- Prior access needed: Yes, initial login with old credentials

## Detailed Attack Procedures

### Step 1: Login to Victim's Account with Old Password
procedure: [[procedures/Login-to-Victim-Account-with-Old-Password]]

**Objective**: Gain initial access to the victim's Basecamp account using the known old password.

**Instructions**: Navigate to the Basecamp sign-in page and submit the victim's email and old password via the login form. No proxy is needed at this stage.

**Expected Output**: Successful login redirect to the account dashboard.

**Success Indicators**:
- Dashboard loads without errors
- Account settings are accessible

### Step 2: Enable 2FA and Logout
procedure: [[procedures/Enable-2FA-and-Logout]]

**Objective**: Set up two-factor authentication in the account to prepare for response capture, then log out to simulate a fresh login.

**Instructions**: From the account dashboard, navigate to account settings, enable two-factor authentication (2FA), generate and note a backup code, then log out of the session.

**Expected Output**: 2FA enabled confirmation, followed by logout redirect to sign-in page.

**Success Indicators**:
- 2FA setup complete with backup codes displayed
- Logout successful, no active session

### Step 3: Capture Successful 2FA Backup Code Response
procedure: [[procedures/Capture-Successful-2FA-Backup-Code-Response]]

**Objective**: Log back in using the old password and backup code while intercepting the successful 2FA validation response for later replay.

**Instructions**: Configure an HTTP proxy (e.g., Burp Suite) to intercept traffic. Submit login with email and old password, then enter the backup code when prompted. Save the full HTTP response from the 2FA validation endpoint.

**Expected Output**: Successful login to dashboard, with captured response containing session tokens or cookies.

**Success Indicators**:
- Proxy captures the 200 OK response from 2FA step
- Response includes authentication artifacts (e.g., session ID)

### Step 4: Disable 2FA in Account
procedure: [[procedures/Disable-2FA-in-Account]]

**Objective**: Remove 2FA to allow the victim to change password without 2FA interference, while retaining the captured response.

**Instructions**: From the dashboard, navigate to account settings and disable two-factor authentication. Log out after confirmation.

**Expected Output**: 2FA disabled confirmation, account returns to password-only auth.

**Success Indicators**:
- No 2FA prompt on next login attempt
- Settings reflect 2FA as off

### Step 5: Victim Changes Password

**Objective**: Simulate the victim updating their password, which should invalidate old sessions but does not in this vulnerability.

**Instructions**: This step is victim-initiated. The victim logs in with the old password and updates to a new one in account settings. Attacker waits for this to occur.

**Expected Output**: Victim receives password change confirmation.

**Success Indicators**:
- Victim no longer able to login with old password alone
- Attacker's prior sessions (if any) invalidated

### Step 6: Replay Captured Response After Password Change
procedure: [[procedures/Replay-Captured-Response-After-Password-Change]]

**Objective**: Use the old password in a login attempt and replace the failed response with the captured 2FA response to bypass the new password requirement.

**Instructions**: Attempt login with email and old password via proxy. When the server responds with failure due to password change, intercept and replace the response body/headers with the saved 2FA success response from Step 3. Forward the modified response to the client.

**Expected Output**: Successful access to the account dashboard despite the password change.

**Success Indicators**:
- Login succeeds without knowing new password
- Full account control achieved (account takeover)

## Attack Chain Summary

### Key Achievements

1. Initial access and 2FA manipulation without alerting the victim
2. Capture of reusable authentication response
3. Bypass of password change via response replay, leading to persistent access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Forge Web Credentials]] Forge Web Credentials

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
