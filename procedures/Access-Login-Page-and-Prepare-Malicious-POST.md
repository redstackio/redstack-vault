---
id: proc-access-login-prepare-post
tags:
  - xss
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/prepare-xss-post-data]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:35.297Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access Login Page and Prepare Malicious POST

## Summary

This procedure involves navigating to the vulnerable login page of the wallet application and preparing a POST request with an XSS payload in the email parameter to test for reflection in error responses.

## Description

In the context of exploiting reflected XSS, start by accessing https://wallet.romit.io/login. Use browser tools to inspect the form and capture the CSRF token. Modify the email field to include a payload like an HTML anchor with an onmouseover event that alerts document cookies. This sets up the injection without immediate execution, relying on reflection in the server's error page.

## Requirements

1. Web browser with developer tools enabled
2. Access to the public login endpoint (no credentials needed)
3. Optional: Proxy tool like Burp Suite for request modification

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict inline scripts
- Monitor for anomalous form submissions with script-like content in logs
- Use web application firewall (WAF) rules to block common XSS payloads

## Objectives

1. Gain access to the login form and understand its structure
2. Craft a non-disruptive payload for initial testing
3. Prepare for submission to observe reflection

## Instructions

### Step 1: Navigate to Login Page

**Context**: Load the target page to inspect the form elements and capture any dynamic tokens like CSRF.

**Command** ([[commands/prepare-xss-post-data]]):
```bash
# No direct command; use browser to navigate to https://wallet.romit.io/login and inspect form
```

> Open the page, right-click the email field, and inspect to note the POST endpoint and parameters. Capture the _csrf value from hidden inputs.

### Step 2: Modify Email Parameter

**Context**: Prepare the payload in the email[] field for injection.

**Command** ([[commands/prepare-xss-post-data]]):
```bash
# Prepare payload: email[]=<a onmouseover=alert(document.cookie)>xxs link</a>
```

> Set password to a dummy value like 'g00dPa$ $w0rD' and include the CSRF token. This payload triggers on mouseover without immediate alert.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/prepare-xss-post-data]]

## Tools Used

- None

## Tags

- [[xss]]
- [[web]]
- [[recon]]
