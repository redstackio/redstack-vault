---
id: ac-shopify-2fa-bypass-google
name: Shopify 2FA Bypass via Google Apps Login Misconfiguration
type: attack_chain
description: >-
  A misconfiguration in Shopify's authentication system allows bypassing 2FA by
  enabling Google Apps login, which silently disables local 2FA while keeping
  email/password login active.
verified: false
submitted: true
step_count: 4
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:48.087Z'
procedures:
  - '[[procedures/Setup-Shopify-2FA]]'
  - '[[procedures/Enable-Google-Apps-Login]]'
  - '[[procedures/Login-with-Google-to-Disable-2FA]]'
  - '[[procedures/Bypass-2FA-with-Password-Login]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
tactics:
  - '[[Initial Access]]'
tags:
  - auth-bypass
  - 2fa-bypass
  - shopify
  - misconfiguration
platforms:
  - Web
tools: []
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
---

# Shopify 2FA Bypass via Google Apps Login Misconfiguration

Multi-stage attack chain demonstrating a complete attack workflow exploiting a Shopify authentication misconfiguration.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup 2FA] --> B[Enable Google Apps]
    B --> C[Login with Google]
    C --> D[Bypass with Password]
    D --> E[Admin Access Gained]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome)
- Valid Shopify account credentials
- Access to Google account linked for testing

### Target Environment

- Shopify admin panel (Web platform)
- Enabled admin settings access
- No additional services/ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Valid email/password for Shopify store admin
- Owner or admin privileges to modify account settings
- Network access to Shopify domains (shopify.com, myshopify.com)

## Detailed Attack Procedures

### Step 1: Setup Two Factor Authentication
procedure: [[procedures/Setup-Shopify-2FA]]

**Objective**: Establish baseline 2FA protection using Google Authenticator to demonstrate the subsequent bypass.

**Instructions**: Navigate to the Shopify admin settings and configure 2FA with an authenticator app. This assumes email/password login is already in use.

- Go to `https://[store-name].myshopify.com/admin/settings/account`.
- Under the "Two-step authentication" section, select "Set up two-step authentication".
- Scan the QR code with Google Authenticator and enter the generated code to enable.

**Expected Output**: 2FA is active; future logins require a code from the app.

**Success Indicators**:
- 2FA setup confirmation message displayed.
- 2FA tab visible in account settings.
- Login attempts now prompt for 2FA code.

### Step 2: Enable Google Apps Login
procedure: [[procedures/Enable-Google-Apps-Login]]

**Objective**: Activate the Google Apps login service in Shopify settings, preparing for the misconfiguration trigger.

**Instructions**: From the admin account settings, enable the Google login option without disabling traditional methods.

- Access `https://[store-name].myshopify.com/admin/settings/account`.
- Scroll to "Login services" and select "Google Apps".
- Follow prompts to link the Google account (requires Google Workspace or similar setup).
- Save changes; no immediate changes to login flow are notified.

**Expected Output**: Google Apps option enabled in login services.

**Success Indicators**:
- Google login button appears on the login page.
- No errors in settings save.
- Traditional login options remain available.

### Step 3: Login with Google to Disable 2FA
procedure: [[procedures/Login-with-Google-to-Disable-2FA]]

**Objective**: Trigger the silent disablement of local 2FA by authenticating via Google.

**Instructions**: Use the Google login endpoint to authenticate, which internally disables Shopify's 2FA without user notification.

- Navigate to `https://[store-name].myshopify.com/admin/auth/login?google_apps=1`.
- Click "Sign in with Google" and authenticate using the linked Google account.
- Upon successful login, check account settings; the 2FA tab should now be absent.

**Expected Output**: Successful admin panel access via Google; 2FA settings disappear.

**Success Indicators**:
- No 2FA prompt during Google login.
- 2FA option missing from `/admin/settings/account`.
- Account remains logged in without further auth.

### Step 4: Bypass 2FA with Password Login
procedure: [[procedures/Bypass-2FA-with-Password-Login]]

**Objective**: Exploit the disabled 2FA to gain admin access using only email and password.

**Instructions**: Attempt login with traditional credentials post-Google activation to confirm bypass.

- Go to `https://[store-name].myshopify.com/admin/auth/login`.
- Enter the store owner's email and password.
- Submit without entering any 2FA code.

**Expected Output**: Direct access to the admin panel without 2FA prompt.

**Success Indicators**:
- Login succeeds using only credentials.
- Full admin privileges granted.
- No request for authenticator code.

## Attack Chain Summary

### Key Achievements

1. Successfully enabled and verified initial 2FA protection.
2. Activated Google Apps without disrupting legacy login.
3. Silently disabled 2FA via Google authentication.
4. Gained unauthorized admin access using password alone, bypassing security.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Modify Authentication Process]] Modify Authentication Process

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
