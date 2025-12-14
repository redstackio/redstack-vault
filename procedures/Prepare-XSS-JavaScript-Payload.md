---
id: proc-prepare-xss-payload-751870
tags:
  - xss
  - javascript
  - payload-crafting
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/alert-document-cookie]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:37.981Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Prepare-XSS-JavaScript-Payload

## Summary

This procedure involves crafting a simple JavaScript payload to exploit reflected XSS vulnerabilities, specifically designed to alert and expose the victim's browser cookies as a proof-of-concept for session theft.

## Description

In the context of the pubg.com vulnerability, the payload targets the lack of input sanitization in the 'p' GET parameter. The procedure creates a script that executes in the victim's browser upon reflection, accessing sensitive data like cookies. Prerequisites include basic JavaScript knowledge and a test environment to validate the payload without causing harm. Expected outcomes include successful alert display in a controlled test, confirming exploitability.

## Requirements

1. Access to a JavaScript console or text editor for payload creation
2. Understanding of URL encoding for injection
3. Target endpoint with reflected XSS (e.g., pubg.com 'p' parameter)

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to restrict inline script execution
- Sanitize and escape user inputs on server-side using libraries like DOMPurify
- Monitor for anomalous JavaScript execution via web application firewall (WAF) rules targeting common XSS payloads

## Objectives

1. Create a functional XSS payload for cookie exfiltration
2. Validate payload in a safe environment
3. Prepare for injection into vulnerable parameters

## Instructions

### Step 1: Define the Payload Script

**Context**: Start with a basic script to access and display cookies, suitable for proof-of-concept.

**Command** ([[commands/alert-document-cookie]]):
```javascript
alert(document.cookie);
```

> This command uses the browser's document.cookie API to retrieve all cookies and displays them in an alert dialog. Expected output is a popup showing cookie key-value pairs, such as '_icl_current_language=en'.

### Step 2: Test Payload in Console

**Context**: Validate the payload executes without syntax errors in a browser console.

Paste and run the script in the developer tools console on a test page.

> Successful execution shows the alert without console errors, confirming readiness for encoding and injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/alert-document-cookie]]

## Tools Used


## Tags

- [[xss]]
- [[JavaScript]]
