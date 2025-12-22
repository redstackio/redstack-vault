---
id: 2e10b2ee-43b7-46b7-882e-4697c8860eb5
name: Phabricator Account Takeover via Email Injection and Request Replay
type: attack_chain
description: >-
  Multi-stage attack exploiting weak session validation in Phabricator to inject
  an attacker's email into a victim's account, enabling password reset and full
  takeover.
verified: false
submitted: true
step_count: 6
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.850Z'
procedures:
  - '[[procedures/Create-Phabricator-Account]]'
  - '[[procedures/Access-Phabricator-Email-Settings]]'
  - '[[procedures/Intercept-Phabricator-Email-Addition-Request]]'
  - '[[procedures/Modify-and-Replay-Email-Addition-Request]]'
  - '[[procedures/Perform-Phabricator-Password-Reset]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Use Alternate Authentication Material]]'
  - '[[Exploit Public-Facing Application]]'
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
tags:
  - account-takeover
  - session-replay
  - email-injection
  - phabricator
  - broken-authentication
platforms:
  - Web
tools:
  - '[[tools/Lightning-Browser]]'
  - '[[tools/SandroProxy]]'
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Use Alternate Authentication Material]]'
  - '[[Exploit Public-Facing Application]]'
---

# Phabricator Account Takeover via Email Injection and Request Replay

Multi-stage attack chain demonstrating a complete attack workflow exploiting weak session token validation in Phabricator's email settings to add an attacker's email to a victim's account, leading to password reset and full control.

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
    A[Create Account] --> B[Access Email Settings]
    B --> C[Intercept Request]
    C --> D[Modify and Replay]
    D --> E[Add Attacker Email]
    E --> F[Password Reset and Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#9b59b6
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Lightning-Browser]]
- [[tools/SandroProxy]]

### Target Environment

- Phabricator web application (e.g., https://admin.phacility.com)
- Required services/ports: HTTPS (443)
- Network access requirements: Direct access to the Phabricator instance, ability to intercept mobile traffic

### Initial Access Requirements

- No prior credentials needed for initial setup, but victim must have an active session
- Network position: Attacker must be able to proxy victim's traffic (e.g., via man-in-the-middle on shared network or compromised device)
- Prior access needed: Ability to capture victim's session cookies and CSRF tokens

## Detailed Attack Procedures

### Step 1: Create Phabricator Account

procedure: [[procedures/Create-Phabricator-Account]]

**Objective**: Establish a baseline account to understand the platform and prepare for targeting a victim.

**Instructions**: Register a new user account on the Phabricator platform using the web interface.

**Expected Output**: Successful account creation with login credentials.

**Success Indicators**:
- Account dashboard accessible after login
- Username confirmed in settings

### Step 2: Access Email Settings

procedure: [[procedures/Access-Phabricator-Email-Settings]]

**Objective**: Navigate to the victim's email settings page to initiate the addition process.

**Instructions**: Use a mobile browser to access the email settings URL: `https://admin.phacility.com/settings/user/(username)/page/email/` where `(username)` is the victim's username. Log in with victim's credentials if needed.

**Expected Output**: Email settings page loads, showing current emails.

**Success Indicators**:
- Page title indicates email settings
- Form for adding new email is visible

### Step 3: Attempt to Add Email and Intercept Request

procedure: [[procedures/Intercept-Phabricator-Email-Addition-Request]]

**Objective**: Trigger the email addition POST request and capture it for modification.

**Instructions**: Submit the form to add a new email (use a placeholder like test@example.com), configuring the proxy to intercept the traffic.

**Expected Output**: Captured POST request to `/settings/user/(username)/page/email/` with session cookies and CSRF token.

**Success Indicators**:
- Request intercepted showing headers like `X-Phabricator-Csrf` and `Cookie`
- Body parameters include `email`, `csrf`, etc.

### Step 4: Modify and Replay Request

procedure: [[procedures/Modify-and-Replay-Email-Addition-Request]]

**Objective**: Alter the email parameter to the attacker's email and resend the request using the victim's session.

**Instructions**: Edit the `email` parameter in the POST body to the attacker's email (e.g., `asuuu17@gmail.com`), keep CSRF token and cookies intact, then replay the request.

**Expected Output**: Server accepts the request and adds the email without additional verification.

**Success Indicators**:
- HTTP 200 response or redirect to settings page
- Attacker's email now listed in victim's account settings

### Step 5: Perform Password Reset

procedure: [[procedures/Perform-Phabricator-Password-Reset]]

**Objective**: Use the injected email to reset the victim's password and gain control.

**Instructions**: Initiate a password reset flow using the added email address through the Phabricator login page.

**Expected Output**: Reset link sent to attacker's email, allowing new password set.

**Success Indicators**:
- Password reset email received
- Successful login with new credentials

### Step 6: Verify Account Takeover

**Objective**: Confirm full control over the victim's account.

**Instructions**: Log in with the new password and access sensitive features or data.

**Expected Output**: Full access to victim's dashboard, projects, and settings.

**Success Indicators**:
- Ability to modify account details
- Access to victim's repositories or admin functions if applicable

## Attack Chain Summary

### Key Achievements

1. Successful injection of attacker's email into victim's account via request replay
2. Bypass of email ownership verification using replayed session tokens
3. Complete account takeover through password reset

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Use Alternate Authentication Material]] Use Alternate Authentication Material
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Persistence]] Persistence

---

*Last updated: 2023-10-01T00:00:00Z*
