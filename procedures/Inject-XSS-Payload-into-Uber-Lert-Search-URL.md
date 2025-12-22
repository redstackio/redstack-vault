---
id: proc-inject-xss-uber-lert
tags:
  - xss
  - reflected-xss
  - injection
  - web
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:34.143Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Inject XSS Payload into Uber Lert Search URL

## Summary

This procedure exploits a reflected cross-site scripting (XSS) vulnerability in the search functionality of lert.uber.com by injecting a malicious payload into the URL path, leading to arbitrary JavaScript execution in the context of the victim's browser session.

## Description

The search field on lert.uber.com lacks proper input validation for URL parameters in the path `/s/search/`, allowing attackers to inject HTML and JavaScript that reflects back into the page. By crafting a URL that breaks out of the expected string context (e.g., closing a quote and adding a script tag), the payload executes when the victim loads the page. This can result in session token theft, defacement, or further exploitation. The vulnerability was identified through manual testing of the search feature by appending payloads to the URL.

## Requirements

1. Internet access to reach lert.uber.com
2. A method to deliver the malicious URL to the victim (e.g., phishing email or link sharing)
3. Basic knowledge of HTML/JavaScript for payload crafting

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization for all URL parameters, especially in search fields
- Use Content Security Policy (CSP) headers to restrict script execution
- Encode output properly on the server-side to prevent HTML injection
- Monitor for anomalous JavaScript execution or unexpected alerts in browser logs
- Employ Web Application Firewalls (WAF) to detect common XSS payloads

## Objectives

1. Achieve arbitrary JavaScript execution in the victim's browser
2. Demonstrate potential for data exfiltration or session hijacking
3. Highlight the need for URL parameter validation in web applications

## Instructions

### Step 1: Craft the Malicious URL

**Context**: Identify the vulnerable search endpoint and construct a payload that escapes the URL context to inject executable JavaScript.

Use a payload like `" onload=alert('XSS')` or more advanced ones to break out of attributes. Append it to the base URL:

Full example URL:

`https://lert.uber.com/s/search/All/Home"><script>alert(document.cookie)</script>`

This closes the expected quote in the URL path and injects a script tag that alerts the victim's cookies.

> The payload reflects directly into the HTML without encoding, executing on page load.

### Step 2: Deliver and Test the Payload

**Context**: Send the URL to a test victim (or controlled environment) and verify execution.

Share the URL via a link. Upon clicking, the browser loads the page, reflects the payload in the search field, and executes the script.

> Expected behavior: JavaScript runs, e.g., an alert box appears with sensitive data like cookies. No server interaction beyond the initial GET request.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[web-injection]]
