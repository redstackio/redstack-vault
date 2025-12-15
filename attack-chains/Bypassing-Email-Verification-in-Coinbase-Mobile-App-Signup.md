---
id: b4fb4005-3d1b-4a37-b123-f92c9af149d2
name: Bypassing Email Verification in Coinbase Mobile App Signup
type: attack_chain
description: >-
  Attack chain exploiting a navigation flaw in Coinbase's Android and iOS apps
  to bypass email verification during account creation, enabling unverified
  account access.
verified: false
submitted: true
step_count: 4
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:41.715Z'
procedures:
  - '[[procedures/Bypass-Email-Verification-via-Back-Navigation]]'
techniques:
  - '[[Valid Accounts]]'
tactics:
  - '[[Initial Access]]'
tags:
  - auth-bypass
  - mobile-security
  - email-verification
  - coinbase
platforms:
  - Android
  - iOS
  - Mobile
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Bypassing Email Verification in Coinbase Mobile App Signup

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Start Signup] --> B[Trigger Verification Prompt]
    B --> C[Back to Login]
    C --> D[Login Without Verification]
    D --> E[Access Granted]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual mobile app interaction)

### Target Environment

- Coinbase Android or iOS mobile app
- No specific services or ports required
- Device with app installed

### Initial Access Requirements

- No prior credentials needed
- Direct access to the app on a mobile device
- Internet connectivity for app communication

## Detailed Attack Procedures

### Step 1: Initiate Signup
procedure: [[procedures/Bypass-Email-Verification-via-Back-Navigation]]

**Objective**: Begin the account creation process to set up unverified credentials.

**Instructions**: Open the Coinbase mobile app and navigate to the signup screen. Enter a new email address and password to start registration.

**Expected Output**: App proceeds to the email verification prompt screen.

**Success Indicators**:
- Signup form accepted
- Email sent (check inbox if testing ethically)

### Step 2: Encounter Verification Prompt
procedure: [[procedures/Bypass-Email-Verification-via-Back-Navigation]]

**Objective**: Reach the point where email confirmation is required, setting up the bypass opportunity.

**Instructions**: The app displays a screen stating that a confirmation email has been sent and must be opened to continue. Do not proceed to open the email.

**Expected Output**: Verification prompt screen visible.

**Success Indicators**:
- Prompt for email validation appears
- No further progress without action

### Step 3: Navigate Back to Login
procedure: [[procedures/Bypass-Email-Verification-via-Back-Navigation]]

**Objective**: Exploit the app's navigation flow to return to login without completing verification.

**Instructions**: Press the device's back button to exit the verification screen and return to the login interface.

**Expected Output**: Login screen loads without error.

**Success Indicators**:
- Back navigation succeeds
- Login form is accessible

### Step 4: Complete Login and Access
procedure: [[procedures/Bypass-Email-Verification-via-Back-Navigation]]

**Objective**: Gain access to the account features without email confirmation.

**Instructions**: Enter the email and password used in signup on the login screen and submit.

**Expected Output**: Successful login with full account access; no verification prompt reappears.

**Success Indicators**:
- Login succeeds
- Account dashboard or features load
- Ability to create multiple such accounts

## Attack Chain Summary

### Key Achievements

1. Created unverified account bypassing email ownership check
2. Gained direct access to app features without confirmation
3. Enabled potential for multiple spoofed account abuse

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
