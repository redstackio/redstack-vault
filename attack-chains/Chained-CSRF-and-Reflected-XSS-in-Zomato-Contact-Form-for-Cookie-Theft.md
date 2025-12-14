---
id: ac-zomato-csrf-xss-chain
tags:
  - csrf
  - xss
  - web
  - cookie-theft
  - session-hijacking
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Test-Zomato-Contact-Form-for-CSRF-and-XSS]]'
  - '[[procedures/Exploit-CSRF-to-Trigger-XSS-in-Zomato-Contact-Form]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:26.786Z'
description: >-
  A multi-stage attack exploiting CSRF in Zomato's contact form to inject and
  trigger reflected XSS payloads, leading to cookie theft and potential session
  hijacking.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Chained CSRF and Reflected XSS in Zomato Contact Form for Cookie Theft

Multi-stage attack chain demonstrating exploitation of CSRF in Zomato's contact form to deliver reflected XSS payloads, resulting in arbitrary JavaScript execution and cookie exfiltration.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Testing] --> B[PoC Generation and Execution]
    B --> C[Cookie Theft via XSS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform
- Access to https://www.zomato.com/contact
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- No credentials required (works for authenticated and unauthenticated users)
- Victim must visit attacker's controlled page hosting the CSRF PoC
- Browser like Firefox for PoC execution

## Detailed Attack Procedures

### Step 1: Initial Testing
procedure: [[procedures/Test-Zomato-Contact-Form-for-CSRF-and-XSS]]

**Objective**: Identify lack of CSRF protection and reflected XSS in the contact form fields.

**Instructions**: Use Burp Suite to intercept and test form submissions at https://www.zomato.com/contact, both with and without login. Submit payloads like `<script>alert(1)</script>` in 'name' and email fields to check for reflection without sanitization.

**Expected Output**: Form submits successfully without CSRF token validation; XSS payload reflects in response, executing JavaScript.

**Success Indicators**:
- Form submission succeeds cross-origin without errors
- Alert box pops up from reflected XSS payload

### Step 2: PoC Generation and Execution
procedure: [[procedures/Exploit-CSRF-to-Trigger-XSS-in-Zomato-Contact-Form]]

**Objective**: Craft and execute a CSRF PoC to force form submission with XSS payload, stealing victim cookies.

**Instructions**: In Burp Suite, generate an HTML PoC form that auto-submits to https://www.zomato.com/contact with hidden fields: 'name' set to `<script>alert(1)</script>`, 'email' to `vibhuti123i"><script>alert(document.cookie)</script>`, and include a valid csrf_token if obtained. Host the PoC on a local server or save as HTML file, then open in victim's browser (e.g., Firefox) to trigger submission and XSS execution.

**Expected Output**: Form submits automatically; XSS alert displays victim's cookies.

**Success Indicators**:
- PoC loads and submits without user interaction
- JavaScript alert shows document.cookie contents

## Attack Chain Summary

### Key Achievements

1. Confirmed CSRF vulnerability allowing unauthorized submissions
2. Exploited reflected XSS in form fields for JavaScript execution
3. Demonstrated potential for session hijacking via cookie theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
