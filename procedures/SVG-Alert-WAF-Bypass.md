---
type: procedure
description: >-
  Bypass Web Application Firewalls (WAFs) using an SVG file containing
  obfuscated JavaScript to execute XSS payloads.
tactics:
  - '[[tactics/Defense Evasion|TA0005]]'
  - '[[tactics/Execution|TA0002]]'
techniques:
  - '[[techniques/Obfuscated Files or Information|T1027]]'
  - '[[techniques/JavaScript|T1059.007]]'
sub_techniques: []
tags:
  - waf-bypass
  - xss
  - incapsula
  - svg-payload
commands: []
tools: []
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# SVG-Alert-WAF-Bypass

## Summary

This procedure demonstrates how to bypass WAF protections, such as those in Incapsula, by embedding an obfuscated JavaScript payload within an SVG file. The SVG uses an onload event to execute a global eval of an alert function, allowing XSS execution without direct script tags that WAFs typically block.

## Description

SVG files support embedded scripting, making them a vector for delivering JavaScript payloads in scenarios where direct <script> tags or inline JS are filtered by WAFs. This technique obfuscates the payload using jQuery's globalEval to execute code in the global context, evading signature-based detection. It is particularly effective against Incapsula WAF configurations that do not inspect SVG content deeply. The attack targets web applications vulnerable to file uploads, image inclusions, or reflected/stored XSS where SVG rendering is allowed. Successful execution pops an alert box, but can be adapted for more malicious payloads like data exfiltration or session hijacking.

## Requirements

1. Access to a web application protected by a WAF (e.g., Incapsula) that allows SVG file uploads or inclusions via <img> tags.
2. Knowledge of a reflection point or storage mechanism for the SVG (e.g., user profile images, file upload endpoints).
3. Basic HTML/JavaScript understanding to adapt the payload.
4. A way to deliver the SVG to the victim (e.g., social engineering or direct upload).

## Defense

- Configure WAF rules to inspect and block SVG files containing script attributes like onload or references to eval functions.
- Implement Content Security Policy (CSP) to restrict inline scripts and eval execution.
- Sanitize file uploads to reject SVGs or strip scripting capabilities.
- Monitor for anomalous JavaScript execution in browser logs or via client-side monitoring tools.
- Regularly update WAF signatures to cover SVG-based obfuscation techniques.

## Objectives

1. Evade WAF detection to deliver and execute JavaScript payloads.
2. Achieve XSS execution in environments that block standard script injections.
3. Demonstrate proof-of-concept alert or adapt for further exploitation like credential theft.

## Instructions

### Step 1: Create the SVG Payload

**Context**: Construct the malicious SVG file using the provided code snippet. This embeds the JavaScript payload that will execute upon loading.

**Code** ([[codes/SVG-XSS-Payload-with-GlobalEval]]):

```html
<svg onload=$.globalEval("alert()");>
```

> Save this as an .svg file (e.g., payload.svg). The onload attribute triggers the jQuery globalEval to run the alert in the global scope, bypassing local restrictions. Test locally in a browser to ensure it pops an alert when opened.

### Step 2: Deliver the Payload

**Context**: Inject or upload the SVG to the target application where it will be rendered by the victim's browser.

> For reflected XSS, append the SVG content to a parameter (e.g., ?img=<svg...>) if the app echoes it in an <img> tag. For stored XSS or file upload, submit the file via the upload endpoint. Ensure the WAF does not strip the onload attribute—test with a benign SVG first.

### Step 3: Verify Execution

**Context**: Confirm the bypass by observing the payload execution on the target.

> Load the page or resource containing the SVG in a victim's browser session. Success is indicated by the alert dialog appearing, confirming JS execution past the WAF.
