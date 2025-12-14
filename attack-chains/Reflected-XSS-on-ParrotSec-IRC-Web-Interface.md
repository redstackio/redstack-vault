---
tags:
  - xss
  - reflected-xss
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Exploit-Reflected-XSS-on-Web-Input]]'
step_count: 1
techniques:
  - '[[JavaScript]]'
description: >-
  A reflected Cross-site Scripting attack exploiting unsanitized user input on
  the ParrotSec IRC web interface, enabling arbitrary JavaScript execution in
  victims' browsers.
skill_level: intermediate
impact_level: medium
id: dfd42c72-27b1-4d01-b0eb-363dffba0833
created_at: '2025-12-14T03:46:31.627Z'
updated_at: '2025-12-14T03:46:31.627Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reflected XSS on ParrotSec IRC Web Interface

## Overview

This attack chain demonstrates a reflected Cross-site Scripting (XSS) vulnerability identified on http://irc.parrotsec.org. User-supplied input is reflected back in the web response without proper sanitization or encoding, allowing attackers to inject and execute malicious JavaScript in the browsers of unsuspecting users. The vulnerability was reported via HackerOne (Report #238842) and triaged as medium severity. Potential impacts include session hijacking, phishing, or data theft, though no specific exploitation details were provided in the report. The attack relies on tricking victims into visiting a crafted URL containing the payload.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Malicious Link] --> B[JavaScript Execution]
    B --> C[Data Exfiltration or Session Hijack]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- Web browser (e.g., Chrome with Developer Tools)

### Target Environment

- Web platform
- Accessible HTTP service on port 80
- No specific services or ports beyond standard web access

### Initial Access Requirements

- No credentials required
- Public network access to http://irc.parrotsec.org
- Victim interaction (e.g., clicking a malicious link)

## Detailed Attack Procedures

### Step 1: Exploit Reflected XSS
procedure: [[procedures/Exploit-Reflected-XSS-on-Web-Input]]

**Objective**: Inject and execute malicious JavaScript via reflected user input to compromise the victim's browser session.

**Instructions**: Identify a vulnerable input field (e.g., search or chat input on the IRC web interface). Craft a payload such as `<script>alert('XSS')</script>` and append it to the URL parameter (e.g., http://irc.parrotsec.org/search?q=<script>alert('XSS')</script>). Use a proxy like Burp Suite to intercept and modify requests if needed. Submit the request and observe if the script executes in the response.

**Expected Output**: A JavaScript alert box or console log confirming execution, indicating successful payload reflection without sanitization.

**Success Indicators**:
- Malicious script executes in the browser
- No encoding or filtering applied to the input
- Victim's session cookies or data can be accessed via further payload refinement

## Attack Chain Summary

### Key Achievements

1. Successful injection of JavaScript payload via reflected input
2. Demonstration of arbitrary code execution in user browsers
3. Potential for session hijacking or phishing attacks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01*
