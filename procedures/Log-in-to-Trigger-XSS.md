---
tags:
  - login-trigger
  - js-execution
  - dom-xss
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
techniques:
  - '[[JavaScript]]'
sub_techniques: []
id: 25778dfa-39f3-4acc-8414-3cb99bd704e4
created_at: '2025-12-13T23:55:20.677Z'
updated_at: '2025-12-13T23:55:20.677Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Log-in-to-Trigger-XSS

## Summary

This procedure completes the authentication process in the Semmle application, triggering the vulnerable redirect and executing the injected JavaScript payload in the browser's DOM.

## Description

After visiting the malicious URL, the login flow processes the redirect parameter without sanitization, interpreting the javascript: URI as a navigation target. This executes the payload (e.g., prompt(document.domain)) in the authenticated context, allowing attackers to steal data or perform actions on behalf of the victim.

## Requirements

1. Valid user credentials for Semmle (email-based login)
2. Tainted redirect parameter from prior step
3. Browser session with the malicious URL loaded

## Defense

Defensive measures and detection strategies:

- Sanitize redirect URIs to remove or block javascript: schemes
- Implement Content Security Policy (CSP) to prevent inline script execution
- Audit login redirects for anomalous behavior and alert on JS prompts

## Objectives

1. Authenticate the user session
2. Process and execute the redirect payload
3. Achieve arbitrary JS execution for impact

## Instructions

### Step 1: Initiate Login

**Context**: Start the login by entering email on the tainted page.

Enter the victim's email address in the login form.

> Form submits; may redirect to email verification. Expected output: Email sent or OTP prompt.

### Step 2: Complete Authentication

**Context**: Finish login to trigger redirect processing.

Follow email link or enter code to authenticate.

> Upon success, application redirects via the parameter, executing `prompt(document.domain)//`. Expected output: Browser alert shows domain (e.g., "lgtm-com.pentesting.semmle.net"), confirming XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication-bypass]]
- [[payload-execution]]
