---
id: proc-xss-cookie-corruption
tags:
  - xss
  - cookie
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
updated_at: '2025-12-14T03:47:18.627Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Corrode-Cookie-Value-for-XSS-Injection

## Summary

This procedure exploits insufficient output encoding in cookie value handling on airbnb.com to inject and execute an XSS payload, resulting in arbitrary JavaScript execution limited to Internet Explorer 11 due to Content Security Policy (CSP) restrictions.

## Description

The attack targets the cookie processing mechanism on airbnb.com, where user-controlled cookie values are not properly sanitized or encoded before being reflected in the HTML or JavaScript context. By corrupting a cookie like the 'flash' cookie with a malicious payload (e.g., `<script>alert(document.cookie)</script>`), an attacker can trigger XSS when the page loads and the cookie is read. Exploitation requires direct manipulation on the same domain, as cross-domain cookie setting is blocked by browser policies. Impact is confined to IE11, where CSP enforcement is weaker, allowing potential data exfiltration or session hijacking if chained with other vulnerabilities. Prerequisites include a valid session and browser access.

## Requirements

1. Active session on airbnb.com (authenticated user)
2. Internet Explorer 11 for payload execution (other browsers block due to CSP)
3. Browser developer tools enabled for cookie editing
4. Knowledge of the target cookie name (e.g., 'flash')

## Defense

Defensive measures and detection strategies:

- Implement strict output encoding for all cookie values (e.g., HTML entity encoding)
- Enforce robust CSP policies to block inline scripts across all browsers
- Validate and sanitize cookie inputs server-side before processing
- Monitor for anomalous cookie values or unexpected JavaScript execution in logs

## Objectives

1. Inject and execute arbitrary JavaScript via cookie corruption
2. Demonstrate browser-specific impact (IE11 only)
3. Highlight need for cross-domain exploitation chaining

## Instructions

### Step 1: Identify and Access Target Cookie

**Context**: Locate the vulnerable cookie using browser tools to prepare for manipulation.

Open airbnb.com in Internet Explorer 11, press F12 to open developer tools, navigate to the Application or Storage tab, and expand Cookies > airbnb.com. Identify the 'flash' or similar cookie that is reflected without encoding.

**Expected Output**: List of cookies displayed, with target cookie value visible.

### Step 2: Inject XSS Payload

**Context**: Modify the cookie value to include an executable script payload.

Double-click the cookie value in dev tools and replace it with a payload such as `<script>alert('XSS via Cookie')</script>`. Ensure the payload is URL-decoded if necessary for proper injection.

**Expected Output**: Cookie value updated successfully.

### Step 3: Trigger Execution

**Context**: Refresh the page to process the corrupted cookie and execute the payload.

Close dev tools and refresh the page (F5). The application will read the cookie and reflect the payload, triggering XSS in IE11.

**Expected Output**: JavaScript alert or console log confirming execution; no errors in other browsers due to CSP.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- cookie
- web
- injection
