---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - xss
  - dom-xss
  - javascript-injection
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Exploit-DOM-based-XSS-with-URL-Fragment-Injection]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:27.081Z'
description: >-
  A single-stage attack exploiting a DOM-based XSS vulnerability in the LeaseWeb
  checkout success page by injecting malicious JavaScript via an unsanitized URL
  fragment, leading to arbitrary code execution in the victim's browser.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# DOM-based XSS in LeaseWeb Checkout Success Page via Malicious URL Fragment

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Malicious URL] --> B[JavaScript Execution]
    B --> C[Data Theft or Session Hijacking]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Web platform
- Access to LeaseWeb checkout success page (e.g., /checkout-success/{id})
- No authentication required

### Initial Access Requirements

- Ability to craft and share URLs (e.g., via phishing or direct navigation)
- Victim must navigate to the malicious URL

## Detailed Attack Procedures

### Step 1: Trigger XSS via Malicious URL
procedure: [[procedures/Exploit-DOM-based-XSS-with-URL-Fragment-Injection]]

**Objective**: Inject and execute arbitrary JavaScript in the victim's browser by exploiting the unsanitized URL fragment on the checkout success page.

**Instructions**: Construct a malicious URL targeting the LeaseWeb checkout success endpoint, such as https://www.leaseweb.com/checkout-success/16893#"><img src=x onerror=alert(document.domain)>. Open this URL in a web browser to trigger the DOM-based XSS. The fragment breaks out of an HTML attribute context (e.g., href or id) and injects an img tag with an onerror handler that executes JavaScript.

**Expected Output**: A JavaScript alert dialog displaying the document domain (e.g., www.leaseweb.com) or, if modified, the document cookies.

**Success Indicators**:
- Alert box pops up with document domain or cookies
- Browser console shows JavaScript execution errors or logs if customized

## Attack Chain Summary

### Key Achievements

1. Successful injection of malicious JavaScript via URL fragment
2. Arbitrary code execution without authentication
3. Potential for session hijacking or client-side data theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T12:00:00Z*
