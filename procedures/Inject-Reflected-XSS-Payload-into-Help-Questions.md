---
id: 123e4567-e89b-12d3-a456-426614174001
tags:
  - xss
  - reflected-xss
  - javascript-injection
  - web-exploit
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
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:41.097Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174001
name: Inject-Reflected-XSS-Payload-into-Help-Questions
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Execution]]
techniques: [[Exploit Public-Facing Application]], [[JavaScript]]
sub_techniques: []
tags: xss, reflected-xss, javascript-injection, web-exploit
commands: []
platforms: Web
tools: []
---

# Inject-Reflected-XSS-Payload-into-Help-Questions

## Summary

This procedure exploits a reflected cross-site scripting (XSS) vulnerability on the Simperium help questions page by injecting a malicious JavaScript payload into an unsanitized input field, resulting in arbitrary code execution within the victim's browser. It demonstrates how attacker-controlled input is directly reflected back without proper HTML/JS escaping, enabling client-side attacks like session theft.

## Description

The target endpoint https://simperium.com/help/questions/ fails to sanitize user input in query parameters or form fields, allowing attackers to inject HTML and JavaScript. By crafting a payload that closes open HTML tags and triggers a JavaScript event (e.g., onerror on a malformed image), the injected code executes when a victim visits the malicious URL. This can lead to stealing cookies, session tokens, or performing other client-side actions. The procedure requires no authentication and works on public-facing web applications vulnerable to reflected XSS.

## Requirements

1. Web browser with developer tools for inspection
2. Public access to https://simperium.com/help/questions/
3. Basic knowledge of HTML and JavaScript payloads

## Defense

Defensive measures and detection strategies:

- Implement input sanitization and output encoding (e.g., using libraries like DOMPurify or built-in escaping in frameworks)
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript execution or unexpected alerts in web logs
- Employ Web Application Firewalls (WAF) to block common XSS payloads

## Objectives

1. Confirm the presence of reflected XSS by executing a benign payload
2. Demonstrate potential impact through JavaScript execution
3. Highlight risks of client-side data exposure

## Instructions

### Step 1: Access the Vulnerable Endpoint

**Context**: Navigate to the help questions page to identify input fields or URL parameters that accept user input.

Open a web browser and visit https://simperium.com/help/questions/. Inspect the page source or use developer tools (F12) to locate form inputs or query parameters related to searching or submitting questions.

### Step 2: Craft and Inject the Payload

**Context**: Construct a payload that escapes the HTML context and injects executable JavaScript, then submit it to trigger reflection.

In the input field or URL parameter (e.g., ?q=), enter the payload: `'><img src=x onerror=prompt(document.domain);>`. Submit the form or load the modified URL. The payload closes any open tags (e.g., <input value="..."> becomes <input value="'><img..."), and the onerror event fires due to the invalid src, executing prompt(document.domain).

> This manual injection simulates how an attacker would craft a phishing link for victims.

### Step 3: Verify Execution

**Context**: Confirm the vulnerability by observing the execution of the injected code.

Upon submission, an alert dialog should appear displaying the current domain (simperium.com). If no alert shows, inspect the page source to check if the payload is reflected unsanitized.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[javascript-injection]]
