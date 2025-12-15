---
tags:
  - idor
  - account-takeover
  - oauth-bypass
  - email-verification
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-IDOR-in-WakaTime-Email-Confirmation]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:29.025Z'
description: >-
  Multi-stage attack exploiting Insecure Direct Object Reference (IDOR) in
  WakaTime's email verification API to send confirmation emails to arbitrary
  addresses, enabling account takeover and OAuth bypass for linking multiple
  GitHub accounts.
skill_level: intermediate
impact_level: high
id: ef107f1d-672b-48d3-9eda-dc1ee561c5a0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# IDOR in WakaTime Email Verification Leading to Account Takeover

Multi-stage attack chain demonstrating a complete attack workflow exploiting IDOR in WakaTime's email verification process to takeover arbitrary accounts and bypass OAuth restrictions.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Authenticated Account via GitHub OAuth] --> B[Request Confirmation to Original Email]
    B --> C[Modify Request for Arbitrary Email IDOR]
    C --> D[Click Verification Link on Arbitrary Email]
    D --> E[Verify Account Takeover and Multi-Account Linking]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser with developer tools (e.g., Firefox or Chrome)
- Access to a GitHub account for OAuth login

### Target Environment

- WakaTime web application (https://wakatime.com)
- Required services: GitHub OAuth integration
- Network access: Internet connectivity to wakatime.com and github.com

### Initial Access Requirements

- Valid GitHub credentials for initial account creation
- No prior access to WakaTime needed; starts with public OAuth flow

## Detailed Attack Procedures

### Step 1: Create Original Account Using GitHub Third-Party Login
procedure: [[procedures/Exploit-IDOR-in-WakaTime-Email-Confirmation]]

**Objective**: Establish an authenticated session on WakaTime linked to the original GitHub account and email.

**Instructions**: Navigate to https://wakatime.com and initiate login via GitHub OAuth. Authorize the application to create a new WakaTime account associated with your GitHub profile and original email.

**Expected Output**: Successful login, redirect to WakaTime dashboard with session cookies established.

**Success Indicators**:
- Authenticated session active (check for session cookies in browser dev tools)
- Account dashboard accessible

### Step 2: Send Verification Email to Original Email Address
procedure: [[procedures/Exploit-IDOR-in-WakaTime-Email-Confirmation]]

**Objective**: Trigger the initial email verification flow to understand the normal response.

**Instructions**: From the account settings page (https://wakatime.com/settings/account), use browser dev tools to intercept the POST request or directly send via a tool like curl. Execute [[commands/wakatime-confirm-email]] with the original email:

```bash
curl -X POST https://wakatime.com/api/v1/users/current/confirm_email \
  -H "Content-Type: application/json" \
  -H "X-CSRFToken: YOUR_CSRF_TOKEN" \
  -H "Cookie: YOUR_SESSION_COOKIES" \
  -d '{"email":"original@example.com"}'
```

**Expected Output**: 201 Created response; verification email received at original email with a link like https://wakatime.com/confirm_email/{token}/{original_email}.

**Success Indicators**:
- 201 status code
- Email received with confirmation link

### Step 3: Modify and Send Verification Email to Arbitrary Different Email Address
procedure: [[procedures/Exploit-IDOR-in-WakaTime-Email-Confirmation]]

**Objective**: Exploit IDOR by altering the email parameter to target an arbitrary address without validation.

**Instructions**: Using the same authenticated session, modify the POST body to use an arbitrary email (e.g., victim@example.com). Intercept and edit the request in browser dev tools or use curl with [[commands/wakatime-confirm-email-idor]]:

```bash
curl -X POST https://wakatime.com/api/v1/users/current/confirm_email \
  -H "Content-Type: application/json" \
  -H "X-CSRFToken: YOUR_CSRF_TOKEN" \
  -H "Cookie: YOUR_SESSION_COOKIES" \
  -d '{"email":"arbitrary@victim.com"}'
```

**Expected Output**: 201 Created response; verification email sent to the arbitrary email with a new link like https://wakatime.com/confirm_email/{new_token}/{arbitrary_email}.

**Success Indicators**:
- 201 status code despite email mismatch
- Confirmation email arrives at arbitrary address

### Step 4: Click the Verification Link from the Arbitrary Email
procedure: [[procedures/Exploit-IDOR-in-WakaTime-Email-Confirmation]]

**Objective**: Complete the verification on the arbitrary email to link it to the original account, achieving takeover.

**Instructions**: Access the email at the arbitrary address and click the confirmation link (https://wakatime.com/confirm_email/{token}/{arbitrary_email}). This verifies the email without ownership checks, associating it with the original WakaTime account ID.

**Expected Output**: Redirect to WakaTime dashboard; account now linked to both emails and original GitHub.

**Success Indicators**:
- Successful verification message
- Dashboard access granted via the arbitrary email link

### Step 5: Verify that Both Original and Arbitrary Email Links Grant Access to the Same Account
procedure: [[procedures/Exploit-IDOR-in-WakaTime-Email-Confirmation]]

**Objective**: Confirm account takeover by demonstrating shared access and potential for multi-GitHub linking.

**Instructions**: Log in using both the original and arbitrary email confirmation links. Attempt to link a second GitHub account via OAuth from the settings page. Check account details to verify the same WakaTime user ID (e.g., e4dd48de-57aa-4ec8-ab41-53e9b4e33dfe) is used across.

**Expected Output**: Both links provide access to the identical account; second GitHub account links successfully, bypassing normal restrictions.

**Success Indicators**:
- Shared account ID across emails
- Multiple GitHub integrations active without conflicts

## Attack Chain Summary

### Key Achievements

1. Bypassed email ownership validation in API endpoint
2. Achieved takeover of arbitrary accounts via unverified links
3. Enabled unauthorized linking of multiple OAuth providers to a single account

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
