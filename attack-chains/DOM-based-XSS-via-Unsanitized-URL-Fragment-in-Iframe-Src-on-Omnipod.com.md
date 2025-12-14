---
tags:
  - dom-xss
  - xss
  - javascript
  - web
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/DOM-based-XSS-on-Birthdate-Confirmation-Page]]'
  - '[[procedures/DOM-based-XSS-on-Thanks-Freedom-Page]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:44.309Z'
description: >-
  Exploits DOM-based XSS vulnerabilities on two pages of www.omnipod.com by
  injecting JavaScript payloads into URL fragments, leading to arbitrary code
  execution in the page context.
skill_level: basic
impact_level: high
id: cc451348-1b5d-4437-9142-afef5c2cf1f4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# DOM-based XSS via Unsanitized URL Fragment in Iframe Src on Omnipod.com

Multi-stage attack chain demonstrating exploitation of DOM-based XSS on specific pages of www.omnipod.com, where client-side JavaScript unsafely appends the full query string and fragment to an iframe src attribute without sanitization. This allows breakout from the attribute quotes and injection of event handlers like onload to execute arbitrary JavaScript, potentially enabling site defacement, keystroke logging, phishing, or session hijacking.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minute |
| Skill Level | Basic |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Vulnerable Page 1] --> B[Inject and Execute Payload]
    B --> C[Access Vulnerable Page 2]
    C --> D[Inject and Execute Payload]
    D --> E[Arbitrary JS Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#e74c3c
    style D fill:#f39c12
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Web platform
- JavaScript-enabled browser
- Public access to www.omnipod.com

### Initial Access Requirements

- No credentials required
- Direct network access to the internet
- No prior access needed

## Detailed Attack Procedures

### Step 1: Exploit DOM-based XSS on Birthdate Confirmation Page
procedure: [[procedures/DOM-based-XSS-on-Birthdate-Confirmation-Page]]

**Objective**: Inject a payload into the URL fragment to break out of the iframe src attribute and execute JavaScript via an onload handler.

**Instructions**: Craft the URL with the payload in the fragment and navigate to it in a web browser. The payload #'onload='alert(document.domain) will be appended unsafely, causing the alert to fire upon iframe load.

**Expected Output**: An alert box displaying "www.omnipod.com", confirming execution in the page context.

**Success Indicators**:
- Alert box appears with the domain name
- No errors in browser console related to script execution

### Step 2: Exploit DOM-based XSS on Thanks Freedom Page
procedure: [[procedures/DOM-based-XSS-on-Thanks-Freedom-Page]]

**Objective**: Repeat the injection on the second vulnerable page to demonstrate the vulnerability's scope and execute arbitrary JavaScript.

**Instructions**: Navigate to the crafted URL for the second page. The same payload mechanism applies, appending the fragment to the iframe src without sanitization.

**Expected Output**: An alert box displaying "www.omnipod.com", verifying cross-page exploitation.

**Success Indicators**:
- Alert box appears with the domain name
- Script executes without interference from page-specific logic

## Attack Chain Summary

### Key Achievements

1. Successful injection and execution of JavaScript on the birthdate-confirmation page via URL fragment manipulation.
2. Replication of the exploit on the thanks-freedom page, highlighting multiple entry points.
3. Demonstration of potential for broader attacks like data theft or session hijacking in the site's context.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
