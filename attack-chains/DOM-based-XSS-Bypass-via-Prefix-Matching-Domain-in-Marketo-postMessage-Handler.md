---
tags:
  - xss
  - dom-xss
  - postmessage
  - origin-bypass
  - marketo
  - javascript
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Register-Prefix-Matching-Domain-for-Origin-Bypass]]'
  - '[[procedures/Host-Malicious-POC-on-Controlled-Domain]]'
  - '[[procedures/Trigger-XSS-via-postMessage-from-Malicious-Site]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
description: >-
  A multi-stage attack exploiting a DOM-based XSS vulnerability in
  www.hackerone.com by bypassing origin validation in Marketo's forms2.min.js
  using a prefix-matched domain.
skill_level: intermediate
impact_level: high
id: ac15bb73-7df6-4673-b98f-d78e8bb50d4f
created_at: '2025-12-13T23:55:38.321Z'
updated_at: '2025-12-13T23:55:38.321Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# DOM-based XSS Bypass via Prefix-Matching Domain in Marketo postMessage Handler

Multi-stage attack chain demonstrating a complete attack workflow exploiting a flaw in origin validation for postMessage in Marketo's forms2.min.js library on www.hackerone.com.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Domain Registration] --> B[POC Hosting]
    B --> C[Exploit Trigger]
    C --> D[XSS Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Domain registrar account (e.g., for .ma domains)
- Web hosting service for POC file

### Target Environment

- Web platform with Marketo integration (e.g., www.hackerone.com)
- Browsers without strict CSP (e.g., Chrome without CSP, Firefox/Edge for phishing)
- No specific ports or services beyond HTTPS

### Initial Access Requirements

- No credentials needed
- Public network access
- Ability to register and host on custom domain

## Detailed Attack Procedures

### Step 1: Domain Registration
procedure: [[procedures/Register-Prefix-Matching-Domain-for-Origin-Bypass]]

**Objective**: Acquire a domain that prefixes the expected Marketo origin to bypass the flawed origin check in forms2.min.js.

**Instructions**: Register a .ma domain like 'app-sj17.ma' via a registrar such as a Moroccan domain provider. This domain allows the origin 'https://app-sj17.ma' to pass the check because 'https://app-sj17.marketo.com' starts with 'https://app-sj17.ma' due to the incorrect i.indexOf(origin) === 0 validation.

**Expected Output**: Ownership of the domain 'app-sj17.ma' for approximately €60.

**Success Indicators**:
- Domain registered and DNS propagated
- Origin 'https://app-sj17.ma' can be used in postMessage events

### Step 2: POC Hosting
procedure: [[procedures/Host-Malicious-POC-on-Controlled-Domain]]

**Objective**: Deploy the malicious HTML file that sends crafted postMessage data to trigger the XSS.

**Instructions**: Upload the POC HTML file (reusing the one from report #398054) to the registered domain at a path like /marketo/post2.html. Ensure the file contains JavaScript to send postMessage data targeting the Marketo origin, such as a malicious redirect payload.

**Expected Output**: POC accessible at https://app-sj17.ma/marketo/post2.html.

**Success Indicators**:
- File hosted and publicly accessible via HTTPS
- postMessage script loads without errors

### Step 3: Exploit Trigger
procedure: [[procedures/Trigger-XSS-via-postMessage-from-Malicious-Site]]

**Objective**: Visit the POC to send the postMessage, bypassing the origin check and executing arbitrary JavaScript or redirects in the context of www.hackerone.com.

**Instructions**: Open https://app-sj17.ma/marketo/post2.html in a target browser. The page will send postMessage data to the Marketo handler on www.hackerone.com, which fails the prefix-based origin validation, leading to execution of the payload (e.g., a redirect to a phishing site or JS alert).

**Expected Output**: Malicious redirect or JS execution observed in the browser console or page behavior.

**Success Indicators**:
- postMessage event processed without origin rejection
- Arbitrary JS runs in www.hackerone.com context (browsers without CSP) or phishing prompt in Firefox/Edge

## Attack Chain Summary

### Key Achievements

1. Bypassed previous fix (#398054) using prefix domain registration
2. Hosted and triggered POC to exploit postMessage handler
3. Achieved DOM-based XSS for JS execution or phishing on vulnerable browsers

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
