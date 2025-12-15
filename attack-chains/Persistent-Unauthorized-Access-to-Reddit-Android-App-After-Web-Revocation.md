---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: Persistent Unauthorized Access to Reddit Android App After Web Revocation
type: attack_chain
description: >-
  Demonstrates how revoking Reddit Android app access via web does not terminate
  the mobile session, allowing automatic token refresh and persistent access
  after 20-24 hours.
verified: false
submitted: true
step_count: 5
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:42.693Z'
procedures:
  - '[[procedures/Establish-Reddit-Sessions-and-Revoke-Access]]'
  - '[[procedures/Observe-App-Error-and-Token-Refresh]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Steal Application Access Token]]'
tactics:
  - '[[Persistence]]'
tags:
  - session-persistence
  - mobile-security
  - token-refresh
  - authorization-bypass
platforms:
  - Android
  - Web
tools: []
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Steal Application Access Token]]'
---

# Persistent Unauthorized Access to Reddit Android App After Web Revocation

Multi-stage attack chain demonstrating a complete attack workflow exploiting insufficient session expiration in Reddit's Android app.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~24 hours |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Establish Sessions] --> B[Revoke App Access]
    B --> C[Observe Initial Failure]
    C --> D[Wait for Refresh]
    D --> E[Regain Persistent Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual testing)

### Target Environment

- Reddit Android app (version 2022.24.1 or later)
- Web browser access to reddit.com
- Active Reddit account

### Initial Access Requirements

- Valid Reddit credentials
- Physical or remote access to Android device
- No prior revocation or password change

## Detailed Attack Procedures

### Step 1: Establish Sessions
procedure: [[procedures/Establish-Reddit-Sessions-and-Revoke-Access]]

**Objective**: Log in to the Reddit account on both Android app and web to create active sessions.

**Instructions**: Manually enter credentials in the Reddit Android app and on reddit.com or old.reddit.com to authenticate and establish sessions. No automated tools are required; this is a standard login process.

**Expected Output**: Successful login on both platforms, with access to account features like posts and chats.

**Success Indicators**:
- App shows user profile and feed
- Web dashboard displays logged-in state

### Step 2: Access Account Activity Page
procedure: [[procedures/Establish-Reddit-Sessions-and-Revoke-Access]]

**Objective**: Navigate to the web interface to prepare for revocation.

**Instructions**: In the web browser, go to https://www.reddit.com/account-activity to view authorized apps.

**Expected Output**: Page loads showing sections like 'Apps you have authorized'.

**Success Indicators**:
- Account activity page accessible
- List of authorized apps visible, including 'Reddit on Android'

### Step 3: Revoke App Access
procedure: [[procedures/Establish-Reddit-Sessions-and-Revoke-Access]]

**Objective**: Explicitly revoke authorization for the Android app via web.

**Instructions**: In the 'Apps you have authorized' section, select 'Reddit on Android' and confirm the revocation action.

**Expected Output**: Confirmation message that access has been revoked.

**Success Indicators**:
- Revocation successful on web
- No immediate errors on web session

### Step 4: Observe Initial App Failure
procedure: [[procedures/Observe-App-Error-and-Token-Refresh]]

**Objective**: Verify that the app initially loses access post-revocation.

**Instructions**: Reopen the Reddit Android app and attempt to interact with features like viewing posts or profile.

**Expected Output**: App displays error messages such as 'Let's try that again' or 'uh oh something went wrong but we're not sure what', blocking access to user data.

**Success Indicators**:
- App errors prevent normal use
- No access to account information

### Step 5: Wait and Observe Token Refresh
procedure: [[procedures/Observe-App-Error-and-Token-Refresh]]

**Objective**: Demonstrate automatic session restoration after delay.

**Instructions**: Close and wait approximately 20-24 hours, then reopen the app. Optionally, trigger events like receiving a chat invite or post notification to accelerate refresh.

**Expected Output**: App refreshes access tokens using the stored keychain session, restoring full access without re-authentication.

**Success Indicators**:
- Full account access regained
- No prompt for login or password

## Attack Chain Summary

### Key Achievements

1. Successful revocation via web does not invalidate mobile session
2. Initial app failure confirms revocation impact
3. Automatic token reminting after 20-24 hours enables persistence
4. Bypasses need for password change or device logout

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Steal Application Access Token]] Steal Application Access Token

### MITRE ATT&CK Tactics

- [[Persistence]] Persistence

---
*Last updated: 2023-10-01T12:00:00Z*
