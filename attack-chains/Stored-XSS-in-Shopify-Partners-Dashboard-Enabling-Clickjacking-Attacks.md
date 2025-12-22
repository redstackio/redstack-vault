---
id: ac-shopify-xss-clickjacking-271765
name: Stored XSS in Shopify Partners Dashboard Enabling Clickjacking Attacks
type: attack_chain
description: >-
  A multi-stage attack exploiting stored XSS in user profile fields reflected in
  the Shopify partners dashboard, combined with missing X-Frame-Options headers
  to enable clickjacking and arbitrary JavaScript execution.
verified: false
submitted: true
step_count: 3
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:37.571Z'
procedures:
  - '[[procedures/Inject-Stored-XSS-Payload-into-Shopify-User-Profile]]'
  - '[[procedures/Trigger-Stored-XSS-in-Partners-Dashboard]]'
  - '[[procedures/Exploit-Missing-X-Frame-Options-for-Clickjacking]]'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
tags:
  - xss
  - stored-xss
  - clickjacking
  - shopify
  - web-vulnerability
platforms:
  - Web
tools: []
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---

# Stored XSS in Shopify Partners Dashboard Enabling Clickjacking Attacks

Multi-stage attack chain demonstrating a complete attack workflow exploiting stored cross-site scripting (XSS) in Shopify's account settings, which reflects unsanitized user names in the partners dashboard, combined with the absence of X-Frame-Options headers to facilitate clickjacking.

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
    A[Inject XSS Payload into Profile] --> B[Trigger XSS in Partners Dashboard]
    B --> C[Exploit Clickjacking via Missing Headers]
    C --> D[Arbitrary JS Execution and UI Redressing]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for payload testing
- No specialized tools required; manual browser-based exploitation

### Target Environment

- Web platform
- Access to Shopify account settings at https://accounts.shopify.com/account
- Ability to create or access a Shopify Partners account at https://partners.shopify.com/

### Initial Access Requirements

- Valid Shopify user account with access to account settings
- Network access to Shopify domains
- No prior elevated privileges needed; authenticated user context sufficient

## Detailed Attack Procedures

### Step 1: Inject XSS Payload into User Profile

procedure: [[procedures/Inject-Stored-XSS-Payload-into-Shopify-User-Profile]]

**Objective**: Introduce a malicious JavaScript payload into the First Name and Last Name fields to store it for later reflection.

**Instructions**: Navigate to the account settings page and modify the profile fields with an XSS payload such as `<script>alert('XSS')</script>` or a more advanced payload like `<img src=x onerror=alert(document.cookie)>`. Save the changes to persist the payload.

**Expected Output**: Profile updates successfully without errors, storing the payload server-side.

**Success Indicators**:
- Profile fields accept and save the payload without sanitization errors
- No immediate execution, as it's stored

### Step 2: Trigger Stored XSS in Partners Dashboard

procedure: [[procedures/Trigger-Stored-XSS-in-Partners-Dashboard]]

**Objective**: Access the partners dashboard to reflect and execute the stored payload in the context of authenticated users.

**Instructions**: Create a new partner account or navigate to an existing one at https://partners.shopify.com/. Proceed to confirmation or completion pages like https://partners.shopify.com/[partnerID]/confirm or https://partners.shopify.com/[partnerID]/complete. The unsanitized user name will render the payload, triggering JavaScript execution.

**Expected Output**: Alert or payload execution in the browser, confirming XSS success.

**Success Indicators**:
- JavaScript alert or console output from the payload
- Potential session data access if payload is designed for theft

### Step 3: Exploit Missing X-Frame-Options for Clickjacking

procedure: [[procedures/Exploit-Missing-X-Frame-Options-for-Clickjacking]]

**Objective**: Leverage the lack of frame protection to embed the vulnerable pages in iframes for UI redressing attacks.

**Instructions**: Inspect the HTTP headers of the affected pages using browser dev tools or curl. Confirm absence of X-Frame-Options. Create an attacker-controlled page with an invisible iframe embedding https://partners.shopify.com/[partnerID]/confirm, overlaying deceptive elements to trick users into clicking hidden actions like form submissions or approvals.

**Expected Output**: Pages load in iframes without restrictions; users can be phished into unintended interactions.

**Success Indicators**:
- No X-Frame-Options header present in response
- Successful iframe embedding and overlay functionality

## Attack Chain Summary

### Key Achievements

1. Persistent storage of XSS payload in user profiles without sanitization
2. Reflection and execution of arbitrary JavaScript in authenticated partner sessions
3. Enablement of clickjacking to manipulate user interactions for unauthorized actions

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
