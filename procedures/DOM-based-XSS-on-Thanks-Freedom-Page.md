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
updated_at: '2025-12-13T23:52:44.302Z'
skill_level: basic
impact_level: high
detection_risk: low
sub_techniques: []
id: 01c2292b-2f94-48d5-ba91-9768da59ede2
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# DOM-based-XSS-on-Thanks-Freedom-Page

## Summary

This procedure exploits a DOM-based XSS vulnerability on the www.omnipod.com/pif/thanks-freedom page by injecting a JavaScript payload into the URL fragment. Similar to the birthdate-confirmation page, the client-side script unsafely appends the query string and fragment to an iframe src attribute, enabling attribute breakout and arbitrary JavaScript execution.

## Description

The root cause is identical: unsanitized use of window.location.toString().split('?')[1] (including fragment) appended to iframe src via document.write. The payload in the fragment, such as #'onload='alert(document.domain), escapes the quotes and injects an onload handler. No sid parameter is present or needed on this page. Successful exploitation confirms JavaScript execution in the page context, with risks including defacement, keystroke logging, phishing, or session hijacking.

## Requirements

1. Web browser with JavaScript enabled
2. Internet access to www.omnipod.com
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Validate and escape all URL components before DOM insertion, avoiding direct concatenation.
- Use structured DOM manipulation instead of document.write.
- Deploy CSP headers to block unsafe inline scripts and eval.
- Log and alert on unexpected script injections detected by client-side monitoring or server-side proxies.

## Objectives

1. Trigger JavaScript execution via injected onload handler.
2. Validate the alert displays the correct domain.
3. Illustrate the vulnerability's persistence across multiple site pages.

## Instructions

### Step 1: Craft and Navigate to Vulnerable URL

**Context**: Build the URL incorporating the fragment payload to exploit the unsanitized iframe construction.

No command required; perform manually in browser.

Navigate to:

```url
https://www.omnipod.com/pif/thanks-freedom?#'onload='alert(document.domain)
```

> The fragment is appended directly, causing quote breakout and onload injection upon iframe rendering.

### Step 2: Observe Script Execution

**Context**: Confirm the exploit by observing the alert and optionally inspecting the rendered iframe.

Use browser developer tools to watch for execution.

> Expected: Alert box shows "www.omnipod.com". Inspect the iframe src in the Elements tab to verify the injected attribute.

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
