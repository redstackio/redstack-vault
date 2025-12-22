---
tags:
  - dom-xss
  - xss
  - javascript
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:44.305Z'
skill_level: basic
impact_level: high
detection_risk: low
sub_techniques: []
id: 6d527a54-33ab-4312-b7c0-196e5953edf7
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# DOM-based-XSS-on-Birthdate-Confirmation-Page

## Summary

This procedure exploits a DOM-based XSS vulnerability on the www.omnipod.com/freedom/birthdate-confirmation page by injecting a JavaScript payload into the URL fragment. The client-side script unsafely appends the entire query string and fragment to an iframe src attribute using document.write, allowing attribute breakout and execution of arbitrary code in the page's context.

## Description

The vulnerability arises because the JavaScript code uses window.location.toString().split('?')[1] without sanitization, including the fragment identifier, and directly appends it to the iframe src inside quotes. An attacker crafts a URL like https://www.omnipod.com/freedom/birthdate-confirmation?sid=a1t2J000005vUzlQAE#'onload='alert(document.domain), where the fragment #'onload='alert(document.domain) breaks out of the quotes, injecting an onload handler that executes when the iframe loads. This enables attacks such as defacement, logging, phishing, or hijacking in the www.omnipod.com domain context. The sid parameter is irrelevant to the exploit.

## Requirements

1. Web browser with JavaScript enabled
2. Internet access to www.omnipod.com
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Sanitize and encode URL fragments before appending to HTML attributes, using methods like encodeURIComponent or DOM parsers.
- Avoid using document.write for dynamic content; prefer safer DOM APIs like createElement.
- Implement Content Security Policy (CSP) to restrict inline script execution.
- Monitor for anomalous JavaScript execution via browser dev tools or web application firewalls (WAF).

## Objectives

1. Execute arbitrary JavaScript in the context of the vulnerable page.
2. Confirm vulnerability by displaying an alert with the document domain.
3. Demonstrate potential for information disclosure or session manipulation.

## Instructions

### Step 1: Craft and Navigate to Vulnerable URL

**Context**: Construct the URL with the payload in the fragment to trigger the DOM-based XSS upon page load.

No command required; perform manually in browser.

Navigate to:

```url
https://www.omnipod.com/freedom/birthdate-confirmation?sid=a1t2J000005vUzlQAE#'onload='alert(document.domain)
```

> This appends the fragment to the iframe src, breaking out with onload='alert(document.domain)', executing the alert on iframe load.

### Step 2: Observe Script Execution

**Context**: Verify the payload execution by checking for the alert and inspecting the DOM if needed.

Open browser developer tools (F12) and monitor the console and network tabs.

> Expected: An alert pops up showing "www.omnipod.com". Check the iframe element in the DOM to see the injected onload attribute.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dom-xss]]
- [[xss]]
