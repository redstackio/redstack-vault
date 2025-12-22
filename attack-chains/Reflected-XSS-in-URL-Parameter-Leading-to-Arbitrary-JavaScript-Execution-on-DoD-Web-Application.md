---
tags:
  - xss
  - reflected-xss
  - web-vulnerability
  - dod
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
  - '[[procedures/Exploit-Reflected-XSS-in-URL-Parameter]]'
step_count: 1
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:10.475Z'
description: >-
  A single-stage attack exploiting a reflected Cross-Site Scripting
  vulnerability in a URL parameter of a U.S. Department of Defense web
  application to execute arbitrary JavaScript in the victim's browser.
skill_level: beginner
impact_level: high
id: 403fe811-42c4-4792-835d-68fb6028dfdf
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reflected XSS in URL Parameter Leading to Arbitrary JavaScript Execution on DoD Web Application

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
    B --> C[Client-Side Impact]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Web application hosted at https://████████/████
- No specific services/ports required beyond standard HTTP/HTTPS (ports 80/443)
- Publicly accessible URL

### Initial Access Requirements

- No credentials required
- Victim must access the malicious URL (e.g., via phishing or direct link)
- Attacker needs knowledge of the vulnerable URL parameter

## Detailed Attack Procedures

### Step 1: Inject and Deliver Malicious Payload
procedure: [[procedures/Exploit-Reflected-XSS-in-URL-Parameter]]

**Objective**: Inject a malicious JavaScript payload into the vulnerable URL parameter to reflect and execute arbitrary code in the victim's browser upon access.

**Instructions**: Identify the vulnerable URL parameter in the DoD web application. Craft a payload such as an <img> tag with an onerror handler to trigger JavaScript execution. URL-encode the payload to ensure proper transmission. Deliver the malicious URL to the victim, who will access it, causing the payload to reflect unsanitized and execute.

For example, append the encoded payload to the URL:

```url
https://████████/████?param=<img%20src=x%20onerror=alert(document.cookie)>
```

Replace 'param' with the actual vulnerable parameter name. The alert() function here demonstrates execution; in a real attack, replace with code to exfiltrate session cookies or perform other actions.

**Expected Output**: Upon accessing the URL, a JavaScript alert box pops up displaying the victim's session cookies, confirming execution.

**Success Indicators**:
- Alert or other JS effect triggers in the browser
- No sanitization errors; payload reflects as-is in the page source
- Potential theft of sensitive data like session tokens

## Attack Chain Summary

### Key Achievements

1. Successful injection and reflection of malicious JavaScript via URL parameter
2. Arbitrary code execution in the victim's browser context
3. Potential for session hijacking or data theft from a high-value DoD target

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
