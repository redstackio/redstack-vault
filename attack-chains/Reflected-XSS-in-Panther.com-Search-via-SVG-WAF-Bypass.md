---
tags:
  - xss
  - reflected-xss
  - waf-bypass
  - javascript-execution
  - session-theft
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Test-Reflected-XSS-with-HTML-Injection]]'
  - '[[procedures/Bypass-WAF-for-JavaScript-Execution-in-XSS]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:50.050Z'
description: >-
  A multi-stage attack exploiting a reflected XSS vulnerability in the search
  functionality of panther.com by first confirming HTML injection and then
  bypassing the WAF with an SVG payload to execute JavaScript, enabling session
  theft.
skill_level: intermediate
impact_level: high
id: 0f9f3d39-040e-46d7-bc9a-3f26d8e96b2e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Reflected XSS in Panther.com Search via SVG WAF Bypass

Multi-stage attack chain demonstrating exploitation of a reflected XSS vulnerability in the search endpoint of panther.com, starting from a redirection from runpanther.io. The attack confirms HTML injection first, then bypasses the Web Application Firewall (WAF) using a crafted SVG payload to achieve JavaScript execution, potentially allowing theft of user sessions or other client-side attacks.

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
    A[Initial Access: Navigate and Test HTML Injection] --> B[Execution: Bypass WAF with SVG for JS Alert]
    B --> C[Impact: Potential Session Theft]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox with developer tools)
- Optional: [[tools/Burp-Suite]] for payload crafting and interception

### Target Environment

- Web platform
- Accessible via public internet
- Services: Web search endpoint with WAF protection
- No specific ports required beyond standard HTTPS (443)

### Initial Access Requirements

- No credentials needed
- Direct network access to panther.com
- No prior access; starts from public-facing site

## Detailed Attack Procedures

### Step 1: Confirm HTML Injection in Search
procedure: [[procedures/Test-Reflected-XSS-with-HTML-Injection]]

**Objective**: Verify that the search parameter reflects unsanitized user input, allowing HTML tags to render in the browser.

**Instructions**: Navigate to the search endpoint on panther.com (accessible via redirection from runpanther.io if needed) and append a payload with HTML tags to the search parameter. Use a browser to visit the URL directly.

For example, use [[commands/curl-html-injection-test]] to simulate or verify via command line:

```bash
curl -s "https://panther.com/search/Users%3Ch1%3EHello,%20I%20am%3C/h1%3E%3Cfont%20color=red%3E%20Ibrahimatix0x01%3C/font%3E" | grep -i "h1"
```

Then, open the URL in a browser to observe rendering.

**Expected Output**: The page renders HTML elements like a heading "Hello, I am" and red-colored text, confirming reflection without sanitization.

**Success Indicators**:
- HTML tags are executed and visible in the browser DOM
- No errors or blocking from basic input

### Step 2: Bypass WAF and Execute JavaScript
procedure: [[procedures/Bypass-WAF-for-JavaScript-Execution-in-XSS]]

**Objective**: Craft a payload that evades the WAF to inject and execute JavaScript, demonstrating full XSS control.

**Instructions**: Build on the confirmed vulnerability by using an SVG-based payload in the search parameter. Visit the URL with the crafted payload in a browser to trigger the execution.

Simulate with [[commands/curl-svg-xss-test]] if needed for verification:

```bash
curl -s "https://panther.com/search/test%3Csvg+on+onload%3D%28alert%29%28document.domain%29%3E" | grep -i "svg"
```

In the browser, load the full URL and check for the alert popup.

**Expected Output**: A JavaScript alert box pops up displaying the document.domain (e.g., panther.com), confirming successful XSS execution.

**Success Indicators**:
- Alert executes without WAF block
- JavaScript runs in the context of the page, allowing potential further actions like session cookie theft

## Attack Chain Summary

### Key Achievements

1. Confirmed reflected HTML injection in the search parameter, exposing lack of input sanitization.
2. Bypassed WAF protections using an SVG onload payload to achieve arbitrary JavaScript execution.
3. Demonstrated high-impact potential for client-side attacks, such as stealing authenticated user sessions.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
