---
tags:
  - xss
  - dom-xss
  - javascript-injection
  - cookie-theft
  - account-takeover
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
procedures:
  - '[[procedures/Bypass-ReturnUrl-Validation-with-Tab-Characters]]'
  - '[[procedures/Trigger-DOM-XSS-Payload-on-Sign-In]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
description: >-
  A multi-stage attack exploiting a DOM-based reflected XSS vulnerability in the
  ReturnUrl parameter of the Starbucks sign-in page, using tab character
  bypasses to inject and execute JavaScript for cookie theft and account
  takeover.
skill_level: intermediate
impact_level: high
id: a4db2c49-bf62-4536-93b0-8acb9a5feb22
created_at: '2025-12-13T23:52:21.126Z'
updated_at: '2025-12-13T23:52:21.126Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# DOM XSS via ReturnUrl Parameter Bypass on Starbucks Sign-In Page

Multi-stage attack chain demonstrating a complete attack workflow exploiting inadequate validation in the ReturnUrl parameter to inject JavaScript via tab character bypasses, leading to arbitrary code execution in the victim's browser upon sign-in.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Visit Malicious URL] --> B[Sign In]
    B --> C[Execute JavaScript]
    C --> D[Steal Cookies]

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
- Access to https://app.starbucks.com/account/signin
- No specific services/ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Victim must be tricked into visiting the malicious URL (e.g., via phishing)
- No prior credentials needed for initial visit
- Network access to the internet

## Detailed Attack Procedures

### Step 1: Initial Access
procedure: [[procedures/Bypass-ReturnUrl-Validation-with-Tab-Characters]]

**Objective**: Craft and visit a malicious URL that bypasses validation in the ReturnUrl parameter using tab characters to inject a JavaScript payload.

**Instructions**: Construct the URL by encoding the JavaScript payload with tab characters (%09) to evade filters. Open the URL in a browser to load the sign-in page with the injected payload.

The malicious URL is: https://app.starbucks.com/account/signin?ReturnUrl=%09Jav%09ascript:alert(document.domain)

Here, %09 inserts tab characters that split and bypass validation on 'javascript:alert(document.domain)'.

**Expected Output**: The sign-in page loads without errors, with the payload embedded in the DOM but not yet executed.

**Success Indicators**:
- Page loads successfully
- No validation errors in browser console
- Payload visible in DOM source (inspect element on ReturnUrl handling)

### Step 2: Execution
procedure: [[procedures/Trigger-DOM-XSS-Payload-on-Sign-In]]

**Objective**: Complete the sign-in process to trigger the DOM processing of the ReturnUrl, executing the injected JavaScript and stealing cookies.

**Instructions**: Enter valid credentials on the sign-in form and submit. The application processes the ReturnUrl, injecting the payload into the DOM and executing it.

Upon submission, the JavaScript alert pops with the document domain, confirming execution. In a real attack, replace alert with code to exfiltrate cookies (e.g., via fetch to attacker server).

**Expected Output**: JavaScript executes, showing an alert or sending data to attacker-controlled endpoint.

**Success Indicators**:
- Alert box appears with domain (proof of execution)
- Cookies accessible via document.cookie in console
- Potential session hijacking if cookies are stolen

## Attack Chain Summary

### Key Achievements

1. Bypassed input validation using control characters like tabs (%09)
2. Injected and executed arbitrary JavaScript in the victim's context
3. Enabled theft of session cookies for unauthorized account access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01*
