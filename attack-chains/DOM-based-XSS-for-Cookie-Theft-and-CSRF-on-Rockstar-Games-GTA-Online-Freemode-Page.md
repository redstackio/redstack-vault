---
id: ac-dom-xss-rockstar-gta
tags:
  - xss
  - dom-xss
  - cookie-theft
  - csrf
  - phishing
  - web
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
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-and-Test-DOM-XSS-Vulnerability]]'
  - '[[procedures/Exploit-DOM-XSS-for-Cookie-Theft]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:02.560Z'
description: >-
  A multi-stage attack exploiting a DOM-based XSS vulnerability on the Rockstar
  Games GTA Online freemode features page to steal cookies, enable CSRF attacks,
  and facilitate phishing.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# DOM-based XSS for Cookie Theft and CSRF on Rockstar Games GTA Online Freemode Page

Multi-stage attack chain demonstrating exploitation of a DOM-based XSS vulnerability on www.rockstargames.com/GTAOnline/features/freemode, allowing attackers to inject malicious JavaScript via URL parameters reflected in the DOM, leading to session hijacking via cookie theft, CSRF token bypass, and phishing lures.

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
    A[Identify Vulnerable Endpoint] --> B[Inject Malicious Payload]
    B --> C[Exfiltrate Cookies and Enable CSRF/Phishing]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser with developer tools (e.g., Chrome DevTools)
- Optional: Proxy tool like Burp Suite for parameter manipulation

### Target Environment

- Web platform
- Accessible public-facing webpage: www.rockstargames.com/GTAOnline/features/freemode
- No specific ports or services required beyond standard HTTPS (443)

### Initial Access Requirements

- No credentials needed; public webpage
- Direct network access to the internet
- No prior access; exploitable via crafted URL

## Detailed Attack Procedures

### Step 1: Identify Vulnerable Endpoint
procedure: [[procedures/Identify-and-Test-DOM-XSS-Vulnerability]]

**Objective**: Locate the DOM-based XSS entry point by testing URL parameters for unsanitized reflection in client-side JavaScript.

**Instructions**: Navigate to the target page and inspect the source code using browser developer tools to identify parameters (e.g., 'q' or 'search') that are processed via document.write, innerHTML, or location.hash without sanitization. Test with a benign payload like '<script>alert(1)</script>' appended to the parameter.

**Expected Output**: Alert box pops up, confirming DOM manipulation.

**Success Indicators**:
- JavaScript alert triggers on payload injection
- No server-side filtering observed

### Step 2: Exploit for Cookie Theft
procedure: [[procedures/Exploit-DOM-XSS-for-Cookie-Theft]]

**Objective**: Inject a payload to exfiltrate session cookies and enable follow-on attacks like CSRF or phishing.

**Instructions**: Craft a malicious URL with a payload that sends document.cookie to an attacker-controlled server, e.g., via an img src or XMLHttpRequest. Deliver the URL via phishing email or social engineering to trick users into visiting it.

**Expected Output**: Cookies transmitted to attacker's endpoint, visible in server logs.

**Success Indicators**:
- Cookies received on exfiltration endpoint
- Ability to use stolen cookies for session hijacking
- CSRF attacks possible with stolen session data

## Attack Chain Summary

### Key Achievements

1. Successful identification of DOM-based XSS sink on the freemode page
2. Cookie exfiltration enabling account takeover
3. Facilitation of CSRF and phishing using stolen session data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
