---
tags:
  - xss
  - reflected-xss
  - waf-bypass
  - event-handler
  - javascript
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/Access-XSS-Test-URL]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:08.350Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 2c53254a-847b-4108-8b25-db0ca8bc8953
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-Using-onfocus-and-Autofocus

## Summary

This procedure exploits a reflected XSS vulnerability in a web application's URL parameter by injecting a payload that uses onfocus event handlers combined with autofocus and tabindex attributes. It bypasses WAF filters that block HTML tags, allowing arbitrary JavaScript execution in the victim's browser upon page load and focus gain. Primary use case is testing public-facing web apps for XSS risks, potentially leading to session theft or phishing.

## Description

In the context of a U.S. Department of Defense web application, the vulnerable parameter (e.g., a search query) reflects user input without proper sanitization. The WAF removes obvious HTML tags but fails to detect attribute breakouts and event handlers. The payload closes an existing quoted attribute with ", inserts a benign <br> tag (often allowed), and adds onfocus=javascript_code with autofocus to trigger immediately. Tabindex ensures focusability. When the victim loads the page (e.g., via a phishing link), the script executes, as seen with confirm(1337). Outcomes include cookie theft via document.cookie or navigation to attacker-controlled sites.

Prerequisites: Public access to the target URL; knowledge of the reflected parameter location.

## Requirements

1. Web browser for payload delivery and testing
2. URL encoding tool or browser dev tools to craft the payload
3. Access to the target DoD web application endpoint

## Defense

Defensive measures and detection strategies:

- Implement comprehensive input validation and output encoding (e.g., HTML entity encoding for attributes)
- Configure WAF rules to block event handlers like onfocus, onload, and suspicious attributes like autofocus
- Use Content Security Policy (CSP) to restrict inline JavaScript execution
- Monitor for anomalous JavaScript alerts or network requests from user agents

## Objectives

1. Execute arbitrary JavaScript in the victim's browser context
2. Bypass WAF protections relying on tag filtering
3. Demonstrate impact such as session hijacking or data exfiltration

## Instructions

### Step 1: Identify the Vulnerable Parameter

**Context**: Locate the reflected parameter in the target URL, such as a search or query string (e.g., ?q= or ?search=). Test basic payloads like <script>alert(1)</script> to confirm reflection and WAF behavior.

**Command** ([[commands/Access-XSS-Test-URL]]):
```bash
curl -X GET "https://target.gov/search?q=test" -v
```

> This command fetches the base page to verify parameter reflection in the response. Look for the input echoed back in HTML attributes or text.

### Step 2: Craft and URL-Encode the Payload

**Context**: Build the payload to breakout from attribute context: close quote ("), add o<br>onfocus=confirm(1337) autofocus tabindex=1. The <br> acts as a non-malicious tag often permitted by WAF. URL-encode to %22%20o%3Cbr%3Eonfocus=confirm(1337)%20autofocus%20tabindex=1.

No specific command; use browser URL bar or online encoder.

### Step 3: Inject and Test the Payload

**Context**: Append the encoded payload to the parameter and load the URL in a browser. The autofocus attribute forces focus on the element, triggering onfocus.

**Command** ([[commands/Access-XSS-Test-URL]]):
```bash
curl -X GET "https://█████/██████=████%22%20o%3Cbr%3Eonfocus=confirm(1337)%20autofocus%20tabindex=1%20xss" -v
```

> Replace redacted parts with actual values. In a browser, visit the URL; expect a confirm dialog. Use curl for server-side verification of reflection, but execution requires browser.

**Expected Output**: JavaScript alert/confirm pops up; page source shows injected attributes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/Access-XSS-Test-URL]]

## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[waf-bypass]]
