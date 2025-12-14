---
tags:
  - auth-bypass
  - 2fa-bypass
  - cloudflare
  - apple-id
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Create-Apple-ID-with-Victim-Email]]'
  - '[[procedures/Initiate-Sign-in-with-Apple-Flow]]'
  - '[[procedures/Bypass-2FA-and-Access-Account]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
description: >-
  Multi-stage attack exploiting Cloudflare's Sign in with Apple integration to
  bypass 2FA and achieve account takeover using the victim's email for a new
  Apple ID.
skill_level: intermediate
impact_level: high
id: 373512a1-e4ae-4efa-8dcb-7a45b015526b
created_at: '2025-12-14T17:24:48.035Z'
updated_at: '2025-12-14T17:24:48.035Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Cloudflare 2FA Bypass via Sign in with Apple on Existing Accounts

Multi-stage attack chain demonstrating a complete attack workflow exploiting the lack of email verification in Cloudflare's Apple ID integration, allowing unauthorized account access.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Apple ID] --> B[Initiate Apple Sign-in]
    B --> C[Bypass 2FA and Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for account creation and login

### Target Environment

- Cloudflare web platform
- Apple ID services
- No specific ports; web-based access

### Initial Access Requirements

- Knowledge of victim's Cloudflare email address
- Access to Apple's account creation page
- No prior credentials needed for victim

## Detailed Attack Procedures

### Step 1: Create Apple ID
procedure: [[procedures/Create-Apple-ID-with-Victim-Email]]

**Objective**: Establish control over an Apple ID tied to the victim's email to enable subsequent authentication.

**Instructions**: Navigate to Apple's account creation page and register a new Apple ID using the exact email address associated with the target Cloudflare account. Ensure the email is not already linked to an existing Apple ID.

**Expected Output**: Confirmation of new Apple ID creation with access to the account.

**Success Indicators**:
- Apple ID created successfully without email verification conflicts
- Ability to log in to the new Apple ID

### Step 2: Initiate Sign-in Flow
procedure: [[procedures/Initiate-Sign-in-with-Apple-Flow]]

**Objective**: Leverage the new Apple ID to start the authentication process on Cloudflare's login page.

**Instructions**: Visit the Cloudflare login page, select the 'Sign in with Apple' option, and authenticate using the newly created Apple ID. The flow will attempt to link the Apple ID to the existing Cloudflare account based on email match.

**Expected Output**: Authentication prompt from Apple completes, redirecting back to Cloudflare.

**Success Indicators**:
- Successful linkage without additional prompts
- No email ownership verification required

### Step 3: Bypass 2FA and Gain Access
procedure: [[procedures/Bypass-2FA-and-Access-Account]]

**Objective**: Complete the login without 2FA, achieving full account takeover.

**Instructions**: Upon redirection from Apple authentication, the Cloudflare session grants access to the dashboard without requesting the 2FA code, as the integration lacks proper checks.

**Expected Output**: Full access to the Cloudflare account dashboard and features.

**Success Indicators**:
- Dashboard loads without 2FA prompt
- Ability to perform account actions (e.g., view settings, manage domains)

## Attack Chain Summary

### Key Achievements

1. Created a rogue Apple ID using victim's email
2. Bypassed Cloudflare's 2FA via unverified integration
3. Achieved unauthorized account takeover

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01*
