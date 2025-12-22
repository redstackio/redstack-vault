---
tags:
  - xss
  - reflected-xss
  - javascript
  - web
  - defense
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
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Reflected-XSS-via-Malicious-HTML-Form]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:44.320Z'
description: >-
  A multi-step exploitation of a reflected XSS vulnerability in the search
  functionality of a U.S. Department of Defense web portal, enabling arbitrary
  JavaScript execution for potential session hijacking.
skill_level: intermediate
impact_level: high
id: 0a016686-eede-4262-aa83-947af60f273b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reflected XSS in DoD Web Portal Search Leading to JavaScript Execution

Multi-stage attack chain demonstrating a complete reflected XSS exploitation workflow in a U.S. Department of Defense web portal's search functionality.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious HTML PoC] --> B[Load HTML in Victim Browser]
    B --> C[Observe JavaScript Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Web platform
- Access to the target URL: https://█████████/web/guest/search
- No specific services or ports beyond standard HTTPS (443)

### Initial Access Requirements

- Victim must be authenticated or visiting the portal
- Attacker needs to deliver the malicious HTML (e.g., via phishing or direct access)
- Network access to the target domain

## Detailed Attack Procedures

### Step 1: Create Malicious HTML PoC
procedure: [[procedures/Exploit-Reflected-XSS-via-Malicious-HTML-Form]]

**Objective**: Craft an HTML file that auto-submits a POST request with a malicious 'query' parameter to trigger the reflected XSS.

**Instructions**: Create an HTML file named `exploit.html` with the following content, which includes a form that auto-submits on load to the vulnerable endpoint:

```html
<!DOCTYPE html>
<html>
<head>
    <title>XSS PoC</title>
</head>
<body onload="document.forms[0].submit()">
    <form action="https://█████████/web/guest/search" method="post">
        <input type="hidden" name="query" value="';alert('XSS');var x={y:'">
    </form>
</body>
</html>
```

Save the file locally.

**Expected Output**: A valid HTML file ready for loading in a browser.

**Success Indicators**:
- HTML file created without syntax errors
- Form action points to the correct vulnerable endpoint

### Step 2: Load HTML in Victim Browser
procedure: [[procedures/Exploit-Reflected-XSS-via-Malicious-HTML-Form]]

**Objective**: Trigger the automatic form submission by opening the HTML file, sending the POST request to the search endpoint.

**Instructions**: Open `exploit.html` in a web browser. The onload event will automatically submit the form with the payload `';alert('XSS');var x={y:'` in the 'query' parameter.

**Expected Output**: The browser sends a POST request to `/web/guest/search` and receives a response reflecting the unsanitized input.

**Success Indicators**:
- Form submits automatically upon page load
- Network request visible in browser developer tools (F12 > Network tab) showing the POST with malicious query

### Step 3: Observe JavaScript Execution
procedure: [[procedures/Exploit-Reflected-XSS-via-Malicious-HTML-Form]]

**Objective**: Confirm the reflected payload executes arbitrary JavaScript in the browser context, demonstrating the vulnerability.

**Instructions**: Monitor the browser for the alert dialog. The server's response will reflect the 'query' value without sanitization, allowing the JavaScript `alert('XSS')` to run, followed by an incomplete object definition to close the tag properly.

**Expected Output**: An alert box pops up displaying 'XSS' in the context of the DoD portal.

**Success Indicators**:
- JavaScript alert executes
- No errors in console; payload reflected in response HTML
- Potential for further payloads to hijack sessions or perform unauthorized actions

## Attack Chain Summary

### Key Achievements

1. Identified and exploited unsanitized 'query' parameter in POST requests to `/web/guest/search`
2. Demonstrated arbitrary JavaScript execution via reflected XSS
3. Highlighted risks of session hijacking and unauthorized actions in a high-security environment

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
