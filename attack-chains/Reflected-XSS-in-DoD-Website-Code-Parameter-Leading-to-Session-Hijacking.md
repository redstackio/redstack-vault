---
tags:
  - xss
  - reflected-xss
  - javascript-injection
  - session-hijacking
  - dod
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Reflected-XSS-in-Code-Parameter]]'
step_count: 1
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:34.095Z'
description: >-
  A single-stage attack exploiting a reflected XSS vulnerability in the 'code'
  parameter of a U.S. Department of Defense website to execute arbitrary
  JavaScript in the victim's browser, enabling data theft and session hijacking.
skill_level: intermediate
impact_level: high
id: f47f6b27-439a-4336-bbb6-048df67462b7
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reflected XSS in DoD Website Code Parameter Leading to Session Hijacking

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Payload Delivery via URL] --> B[JavaScript Execution in Browser]
    B --> C[Data Theft and Hijacking]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for testing (e.g., Chrome Developer Tools)

### Target Environment

- Web platform
- Vulnerable endpoint: https://www.████████.mil/?code= (and related SSO paths like /webapp/wcs/stores/servlet/ProcessUserSSO)
- Tech stack: JavaScript, Dojo Toolkit, WebSphere

### Initial Access Requirements

- Ability to craft and deliver a malicious URL (e.g., via phishing email or direct link)
- Victim must be authenticated or visit the site (for session token theft)
- No prior credentials needed for initial injection, but impacts authenticated sessions

## Detailed Attack Procedures

### Step 1: Deliver Malicious Payload
procedure: [[procedures/Exploit-Reflected-XSS-in-Code-Parameter]]

**Objective**: Inject and execute arbitrary JavaScript by manipulating the 'code' parameter to break out of string context, leading to prompt execution or data exfiltration in the victim's browser.

**Instructions**: Construct a URL with the payload that closes the JavaScript string using a single quote ('), terminates the statement with a semicolon (;), and injects a JavaScript function like prompt('XSS') to verify execution. For testing, visit the URL directly in a browser; for real attacks, deliver via phishing.

Example payload URL:

```url
https://www.████████.mil/?code=%27;prompt(%27XSS%27);//
```

The payload %27 decodes to ', %27XSS%27 to 'XSS', and // comments out the rest. This exploits direct insertion into JS without escaping.

**Expected Output**: A JavaScript alert or prompt box appears in the browser displaying 'XSS', confirming injection. In a real attack, replace prompt with code to steal document.cookie or send data to attacker-controlled server.

**Success Indicators**:
- Alert/prompt triggers on page load
- Browser console shows executed JS (check via Developer Tools)
- For exfiltration, network requests to attacker server with stolen cookies/session tokens

## Attack Chain Summary

### Key Achievements

1. Successful breakout from JavaScript string context in 'code' parameter
2. Arbitrary JS execution leading to potential theft of sensitive DoD session data
3. Exploitation across multiple injection points in SSO and logon processes

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---

*Last updated: 2024-10-01T00:00:00Z*
