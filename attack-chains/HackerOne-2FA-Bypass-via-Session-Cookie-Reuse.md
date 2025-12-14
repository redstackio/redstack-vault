---
tags:
  - 2fa-bypass
  - cookie-theft
  - session-hijacking
  - auth-bypass
type: attack_chain
tools:
  - '[[tools/Browser-Cookie-Editor]]'
  - '[[tools/Evilginx2]]'
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Enable-and-Authenticate-2FA-for-Cookie-Capture]]'
  - '[[procedures/Export-Session-Cookies-Post-2FA]]'
  - '[[procedures/Import-Cookies-to-Bypass-2FA]]'
step_count: 6
techniques:
  - '[[Valid Accounts]]'
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:24:47.967Z'
description: >-
  A multi-stage attack exploiting session cookie reuse to bypass two-factor
  authentication on the HackerOne platform, allowing unauthorized account access
  after initial cookie theft.
skill_level: intermediate
impact_level: high
id: 9e21f16b-9e95-4c01-bbaf-c5c4afbcc366
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Adversary-in-the-Middle]]'
---
# HackerOne 2FA Bypass via Session Cookie Reuse

Multi-stage attack chain demonstrating a complete workflow to bypass two-factor authentication on the HackerOne platform by reusing session cookies obtained after successful 2FA authentication. This vulnerability allows attackers to impersonate users without re-verifying the second factor, leading to unauthorized access, data breaches, and potential fraudulent activities.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Enable 2FA and Authenticate] --> B[Export Session Cookies]
    B --> C[Steal Cookies via MitM]
    C --> D[Import Cookies in New Browser]
    D --> E[Bypass 2FA and Access Account]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Browser-Cookie-Editor]]
- [[tools/Evilginx2]]

### Target Environment

- Web platform (HackerOne)
- Required services/ports: HTTPS (443)
- Network access requirements: Ability to perform MitM or direct browser access

### Initial Access Requirements

- Valid username and password for the target account
- Access to an authenticator app for 2FA code generation (for initial setup)
- Network position: Attacker must be able to intercept traffic or have physical access to the victim's browser
- Prior access needed: Compromised credentials or MitM capability

## Detailed Attack Procedures

### Step 1: Enable 2FA in Account Settings
procedure: [[procedures/Enable-and-Authenticate-2FA-for-Cookie-Capture]]

**Objective**: Activate two-factor authentication to establish a baseline for capturing post-2FA session cookies.

**Instructions**: Log in to the HackerOne account with valid credentials, navigate to account settings, and enable 2FA using an authenticator app. This sets up the environment for subsequent authentication.

**Expected Output**: 2FA enabled confirmation and setup of authenticator app.

**Success Indicators**:
- 2FA activation successful
- Authenticator app configured with secret key

### Step 2: Log Out and Log Back In Using Valid Credentials
procedure: [[procedures/Enable-and-Authenticate-2FA-for-Cookie-Capture]]

**Objective**: Initiate a fresh login session to trigger 2FA verification.

**Instructions**: Log out of the current session, then log back in using the username and password. This prompts the 2FA challenge.

**Expected Output**: Login page with 2FA code prompt.

**Success Indicators**:
- Successful credential entry
- 2FA prompt displayed

### Step 3: Enter the Required 2FA Code to Complete Login
procedure: [[procedures/Enable-and-Authenticate-2FA-for-Cookie-Capture]]

**Objective**: Complete authentication to generate valid session cookies.

**Instructions**: Generate and enter the time-based one-time password (TOTP) from the authenticator app to finalize login.

**Expected Output**: Successful login and access to the account dashboard.

**Success Indicators**:
- Session established
- Cookies set in browser (verifiable via developer tools)

### Step 4: Export Session Cookies Using a Cookie Editor Tool
procedure: [[procedures/Export-Session-Cookies-Post-2FA]]

**Objective**: Extract the authentication cookies established after 2FA for reuse.

**Instructions**: With the session active, use a browser extension like EditThisCookie to view and export all cookies associated with the HackerOne domain, including session tokens.

**Expected Output**: Exported cookie data in JSON or text format.

**Success Indicators**:
- Cookies copied successfully
- Session identifiers visible in export

### Step 5: Paste the Copied Cookies into Another Browser
procedure: [[procedures/Import-Cookies-to-Bypass-2FA]]

**Objective**: Transfer cookies to a new browser instance to replicate the authenticated session.

**Instructions**: Open a new browser or incognito window, navigate to HackerOne, and import the exported cookies using the cookie editor tool. Refresh the page to apply the session.

**Expected Output**: Authenticated session loaded without login prompt.

**Success Indicators**:
- Cookies imported without errors
- No 2FA prompt on access

### Step 6: Access the Account Without Providing the 2FA Code
procedure: [[procedures/Import-Cookies-to-Bypass-2FA]]

**Objective**: Verify bypass by accessing protected resources.

**Instructions**: Navigate to account settings or reports; the session should grant full access using the imported cookies.

**Expected Output**: Full account access, including sensitive data.

**Success Indicators**:
- Unauthorized access confirmed
- No additional authentication required

## Attack Chain Summary

### Key Achievements

1. Successful 2FA enablement and authentication to capture cookies
2. Cookie export and import across browsers, bypassing re-verification
3. Full account impersonation, enabling data exfiltration or malicious actions

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

---

*Last updated: 2023-10-01T00:00:00Z*
