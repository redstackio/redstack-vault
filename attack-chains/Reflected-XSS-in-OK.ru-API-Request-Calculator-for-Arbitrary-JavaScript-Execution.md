---
id: ac-uuid-001
name: >-
  Reflected XSS in OK.ru API Request Calculator for Arbitrary JavaScript
  Execution
tags:
  - xss
  - reflected-xss
  - javascript-injection
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Reflected-XSS-in-API-Request-Calculator]]'
step_count: 1
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.708Z'
description: >-
  A reflected XSS vulnerability in the OK.ru API request calculator tool allows
  injection of malicious JavaScript via unsanitized application_secret_key and
  session_secret_key parameters, leading to arbitrary code execution in the
  victim's browser.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Reflected XSS in OK.ru API Request Calculator for Arbitrary JavaScript Execution

Multi-stage attack chain demonstrating a complete attack workflow exploiting a reflected XSS vulnerability in the OK.ru API request calculator tool.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Payload Injection] --> B[JavaScript Execution]
    B --> C[Data Exfiltration or Session Hijacking]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome Developer Tools for payload testing)

### Target Environment

- Web platform
- Access to public-facing OK.ru API calculator at https://apiok.ru/wiki/pages/viewpage.action?pageId=75989046
- No authentication required

### Initial Access Requirements

- Ability to craft and share malicious URLs
- Victim interaction via clicking a link
- No prior credentials or network position needed

## Detailed Attack Procedures

### Step 1: Inject Malicious Payload
procedure: [[procedures/Exploit-Reflected-XSS-in-API-Request-Calculator]]

**Objective**: Deliver a malicious URL to the victim that injects JavaScript via unsanitized input parameters, executing arbitrary code in their browser context.

**Instructions**: Construct a URL to the API calculator tool with a JavaScript payload in the application_secret_key or session_secret_key parameter. For testing, use a simple alert payload; for exploitation, replace with code to steal cookies or exfiltrate data.

Example payload URL:

```url
https://apiok.ru/wiki/pages/viewpage.action?pageId=75989046&application_secret_key=<script>alert('XSS')</script>
```

Send this URL to the victim via email, social engineering, or phishing. Upon clicking and submitting the form (or direct parameter reflection), the payload executes.

**Expected Output**: Browser alert pops up, or in a real attack, network requests for data exfiltration (e.g., sending document.cookie to attacker-controlled server).

**Success Indicators**:
- JavaScript alert or console log appears in victim's browser
- Injected script accesses browser APIs (e.g., localStorage, cookies)
- No server-side errors; payload reflects directly in response

## Attack Chain Summary

### Key Achievements

1. Successful injection of JavaScript payload via unsanitized parameters
2. Arbitrary code execution in victim's browser context
3. Potential for session hijacking or sensitive data theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
