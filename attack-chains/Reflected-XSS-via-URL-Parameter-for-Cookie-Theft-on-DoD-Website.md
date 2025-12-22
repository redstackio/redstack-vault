---
id: ac-reflected-xss-dod-url-param
tags:
  - xss
  - reflected-xss
  - javascript-injection
  - cookie-theft
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
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inject-and-Execute-Reflected-XSS-Payload]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:37.515Z'
description: >-
  A multi-step attack exploiting a reflected XSS vulnerability in a URL
  parameter on a U.S. Department of Defense website to execute JavaScript and
  steal victim cookies.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reflected XSS via URL Parameter for Cookie Theft on DoD Website

Multi-stage attack chain demonstrating a complete reflected XSS exploitation workflow on a U.S. Department of Defense website.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Malicious URL] --> B[Payload Execution and Cookie Theft]
    B --> C[Session Hijacking Potential]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Web platform
- Publicly accessible DoD website with vulnerable URL parameter
- No specific services/ports beyond standard HTTP/HTTPS (80/443)

### Initial Access Requirements

- No credentials required
- Victim must click or navigate to the crafted URL (e.g., via phishing)
- Network access to the target website

## Detailed Attack Procedures

### Step 1: Craft and Navigate to Malicious URL
procedure: [[procedures/Inject-and-Execute-Reflected-XSS-Payload]]

**Objective**: Inject a URL-encoded JavaScript payload into the vulnerable parameter to trigger reflected XSS upon page load.

**Instructions**: Construct the malicious URL by appending the encoded payload to the target endpoint. For example, use the base URL https://██████████/██████= and encode the payload '</script><script>alert(document.domain)</script>' as %3C/script%3E%3Cscript%3Ealert(document.domain)%3C/script%3E. Then, open a web browser and navigate to the full URL: https://██████████/██████=%3C/script%3E%3Cscript%3Ealert(document.domain)%3C/script%3E.

**Expected Output**: The page loads with the injected script reflected in the HTML, executing the JavaScript immediately.

**Success Indicators**:
- Browser alert box displays the document domain
- Page source shows unsanitized reflection of the payload

### Step 2: Observe Payload Execution and Exfiltrate Data
procedure: [[procedures/Inject-and-Execute-Reflected-XSS-Payload]]

**Objective**: Confirm execution and extend the payload to steal sensitive data like cookies for session hijacking.

**Instructions**: After navigation, inspect the browser console or network tab for execution. Replace the alert with a data exfiltration payload, such as document.cookie, sent to an attacker-controlled server (e.g., via XMLHttpRequest). Navigate to the updated URL with the new payload to capture cookies.

**Expected Output**: JavaScript executes, potentially sending cookies to the attacker's endpoint; verify receipt on the server.

**Success Indicators**:
- Cookies transmitted to attacker server
- No sanitization errors in response
- Potential for further JS actions like keylogging

## Attack Chain Summary

### Key Achievements

1. Successful injection and reflection of malicious JavaScript via URL parameter
2. Execution of arbitrary code in victim's browser context
3. Capability to steal session cookies leading to account takeover

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
