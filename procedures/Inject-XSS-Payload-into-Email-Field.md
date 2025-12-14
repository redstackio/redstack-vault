---
id: proc-inject-xss-email-001
name: Inject-XSS-Payload-into-Email-Field
tags:
  - xss
  - payload-injection
  - javascript
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.299Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---
id: proc-inject-xss-email-001
name: Inject-XSS-Payload-into-Email-Field
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T12:00:00Z
updated_at: 2023-10-01T12:00:00Z
tactics: [[Execution]], [[Collection]]
techniques: [[JavaScript]]
sub_techniques: []
tags: xss, payload-injection, javascript
commands: []
platforms: Web
tools: []
---

# Inject-XSS-Payload-into-Email-Field

## Summary

This procedure demonstrates injecting a reflected XSS payload into the email field on IntenseDebate's account editing page to execute arbitrary JavaScript, such as alerting document cookies for session theft.

## Description

The email input field lacks proper sanitization, allowing HTML and JavaScript tags to be injected and reflected back unsanitized. By appending a payload like "><img src=x onerror=alert(document.cookie);> to the email value, the attacker triggers execution when the input is echoed in the response. This can lead to client-side attacks like cookie exfiltration or session hijacking in a real scenario.

## Requirements

1. Access to the account editing page from the prior procedure
2. Web browser with JavaScript enabled
3. Knowledge of the target's email format for payload appending

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs, especially in reflected fields, using HTML entity encoding
- Implement Content Security Policy (CSP) to restrict inline script execution
- Log and monitor for anomalous JavaScript alerts or cookie access patterns

## Objectives

1. Inject and trigger XSS payload execution
2. Demonstrate JavaScript execution in the victim's browser
3. Enable potential data exfiltration like session cookies

## Instructions

### Step 1: Prepare and Inject Payload

**Context**: Locate the email input field and append the malicious payload to exploit the reflection.

No command-line tool needed; perform manually in the browser:

In the email field, enter your existing email followed by the payload: example@email.com"><img src=x onerror=alert(document.cookie);>

Submit the form or save changes to trigger reflection.

> The payload closes the input tag, injects an image with an onerror handler, and executes alert(document.cookie) when the erroneous image loads. This pops an alert with cookie data.

**Expected Output**: JavaScript alert displays session cookies.

### Step 2: Verify Execution

**Context**: Confirm the payload worked by observing the alert and inspecting the reflected HTML.

Use browser developer tools (F12) to inspect the page source after submission. Look for the injected <img> tag in the reflected email value.

> Successful injection shows the payload in the HTML without escaping, confirming the vulnerability.

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
- [[injection]]
