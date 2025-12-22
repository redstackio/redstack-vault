---
tags:
  - authentication-bypass
  - account-takeover
  - shopify
  - privilege-escalation
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Create-New-Shopify-Store-and-Set-Victim-Email]]'
  - '[[procedures/Configure-Burp-Suite-for-Request-Manipulation]]'
  - '[[procedures/Perform-Email-Confirmation-Bypass-via-Avatar-Upload]]'
  - '[[procedures/Complete-Account-Takeover-and-Access-Victim-Resources]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
description: >-
  Multi-stage attack exploiting email confirmation bypass in Shopify legacy
  accounts to achieve unauthorized account takeover
skill_level: intermediate
impact_level: high
id: 5b980216-4c3d-4cde-a9da-c74300f2057e
created_at: '2025-12-11T06:10:22.802Z'
updated_at: '2025-12-11T06:10:22.802Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1078]]'
  - '[[T1190]]'
---
# Shopify Legacy Account Email Confirmation Bypass Leading to Account Takeover

Multi-stage attack chain demonstrating a complete attack workflow exploiting an email confirmation bypass vulnerability in Shopify's legacy accounts on your-store.myshopify.com. This allows attackers to verify arbitrary emails and escalate privileges to take over non-SSO accounts by manipulating email changes, avatar uploads, and confirmation flows using a proxy tool.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Store Setup] --> B[Request Manipulation]
    B --> C[Confirmation Bypass]
    C --> D[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform
- Shopify services including Shopify ID and SSO
- Network access to Shopify admin dashboard

### Initial Access Requirements

- Access to Shopify partners dashboard
- Attacker-controlled email address
- Victim's email address

## Detailed Attack Procedures

### Step 1: Initial Store Setup - [[procedures/Create-New-Shopify-Store-and-Set-Victim-Email]]

**Procedure**: [[procedures/Create-New-Shopify-Store-and-Set-Victim-Email]]

**Objective**: Set up a new store and initiate email change to the victim's address without verification.

**Expected Output**: New store created with victim's email set in account settings.

**Success Indicators**:
- Successful navigation to admin/settings/account without email verification
- Email field updated to victim's email

### Step 2: Request Manipulation Setup - [[procedures/Configure-Burp-Suite-for-Request-Manipulation]]

**Procedure**: [[procedures/Configure-Burp-Suite-for-Request-Manipulation]]

**Objective**: Intercept and modify HTTP requests to replace email addresses dynamically.

**Expected Output**: Burp Suite configured with match and replace rules for email substitution.

**Success Indicators**:
- Match and replace rule active in Burp Suite
- Requests successfully modified on refresh

### Step 3: Bypass Confirmation - [[procedures/Perform-Email-Confirmation-Bypass-via-Avatar-Upload]]

**Procedure**: [[procedures/Perform-Email-Confirmation-Bypass-via-Avatar-Upload]]

**Objective**: Manipulate avatar uploads and confirmation links to bypass email verification for the victim's email.

**Expected Output**: Confirmation link clicked with modified requests, leading to successful bypass.

**Success Indicators**:
- Avatar uploaded with modified email
- Confirmation email received and link processed with victim's email substituted

### Step 4: Final Takeover - [[procedures/Complete-Account-Takeover-and-Access-Victim-Resources]]

**Procedure**: [[procedures/Complete-Account-Takeover-and-Access-Victim-Resources]]

**Objective**: Set up Shopify ID, password, and access the victim's store and partner account.

**Expected Output**: Full access to victim's resources without restrictions.

**Success Indicators**:
- Shopify ID setup completed
- New password set and login successful to victim's account

## Attack Chain Summary

### Key Achievements

1. Bypassed email confirmation for legacy accounts
2. Achieved privilege escalation to account owner level
3. Gained unauthorized access to stores and partner accounts

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Privilege Escalation]]

*Last updated: 2023-10-01*
