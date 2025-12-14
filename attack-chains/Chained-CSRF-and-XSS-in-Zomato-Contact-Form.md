---
id: ac-uuid-001
name: Chained CSRF and XSS in Zomato Contact Form
tags:
  - csrf
  - xss
  - web-vulnerability
  - session-hijacking
type: attack_chain
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Test-Contact-Form-for-CSRF-and-XSS-Vulnerabilities]]'
  - '[[procedures/Create-and-Execute-CSRF-PoC-to-Trigger-XSS]]'
  - '[[procedures/Observe-XSS-Execution]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:03.344Z'
description: >-
  A multi-stage attack exploiting CSRF to inject XSS payloads into Zomato's
  contact form, leading to JavaScript execution and potential session hijacking.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Chained CSRF and XSS in Zomato Contact Form

Multi-stage attack chain demonstrating a complete attack workflow exploiting CSRF to deliver XSS payloads via Zomato's contact form at https://www.zomato.com/contact.

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
    A[Initial Testing] --> B[CSRF PoC Creation]
    B --> C[XSS Execution and Observation]
    C --> D[Potential Session Hijacking]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite-Professional]]

### Target Environment

- Web platform
- Access to https://www.zomato.com/contact
- Latest Firefox browser for testing

### Initial Access Requirements

- No credentials required; works on public contact form
- Victim must be authenticated to Zomato for full impact
- Attacker needs to host a malicious HTML page

## Detailed Attack Procedures

### Step 1: Initial Testing
procedure: [[procedures/Test-Contact-Form-for-CSRF-and-XSS-Vulnerabilities]]

**Objective**: Verify the absence of CSRF protection and input sanitization in the contact form.

**Instructions**: Submit test payloads to the form at https://www.zomato.com/contact using POST with parameters like name, email, phone, message, and csrf_token. Test both logged-in and anonymous sessions in Firefox.

**Expected Output**: Successful form submissions without errors, indicating lack of validation.

**Success Indicators**:
- Form accepts submissions from external sources
- No CSRF token enforcement observed

### Step 2: CSRF PoC Creation
procedure: [[procedures/Create-and-Execute-CSRF-PoC-to-Trigger-XSS]]

**Objective**: Craft and host a malicious page that auto-submits the form with XSS payloads.

**Instructions**: Use Burp Suite to generate an HTML page with a hidden form targeting https://www.zomato.com/contact. Include XSS in name ('<script>alert(1)</script>') and email ('"<script>alert(document.cookie)</script>'), along with csrf_token 'fa53b2d4ea3ae0113d903ed5b0200fcb' and other fields. Host and load the page in the victim's browser.

**Expected Output**: Auto-submission injects the payload into Zomato's form.

**Success Indicators**:
- Form data submitted cross-origin
- Payloads reflected without sanitization

### Step 3: XSS Execution
procedure: [[procedures/Observe-XSS-Execution]]

**Objective**: Confirm JavaScript execution from the injected XSS, demonstrating data exfiltration.

**Instructions**: After CSRF submission, observe the contact form page for alert popups showing document.cookie.

**Expected Output**: Browser alert displaying victim's cookies.

**Success Indicators**:
- JavaScript alert triggers
- Cookies exposed, enabling session hijacking

## Attack Chain Summary

### Key Achievements

1. Bypassed CSRF protection to force form submissions
2. Injected and executed XSS payloads client-side
3. Demonstrated potential for cookie theft and account compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
