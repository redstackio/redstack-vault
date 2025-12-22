---
type: procedure
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - cloudflare
  - waf-bypass
  - svg
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

# Cloudflare-XSS-Bypass-Using-SVG-OnLoad-Prompt

## Summary

This procedure demonstrates a technique to bypass Cloudflare's Web Application Firewall (WAF) protections against Cross-Site Scripting (XSS) attacks by injecting a malicious SVG element with an onload event that triggers a JavaScript prompt. This allows execution of arbitrary code in the victim's browser, potentially leading to session hijacking, data theft, or further exploitation.

## Description

Cloudflare WAF filters common XSS payloads to protect web applications, but certain encodings or alternative vectors like SVG onload events can evade detection. The SVG onload attribute executes JavaScript when the image loads, bypassing filters that block direct <script> tags or inline event handlers. This is particularly effective against reflected or stored XSS in user-controlled inputs reflected in HTML contexts. The attack requires an injection point where user input is rendered without proper sanitization, such as search fields or comment sections on Cloudflare-protected sites. Success results in immediate code execution without additional user interaction beyond loading the page.

## Requirements

1. Access to a Cloudflare-protected website with a vulnerable XSS injection point (e.g., reflected input in HTML).
2. A web browser or proxy tool like Burp Suite to craft and send the payload.
3. Basic knowledge of HTML/SVG and JavaScript execution contexts.
4. Attacker-controlled domain or direct testing environment to observe the prompt.

## Defense

Defensive measures and detection strategies:

- Regularly update Cloudflare WAF rulesets to include SVG-specific filters for onload events.
- Implement Content Security Policy (CSP) headers to restrict inline script execution and SVG sources.
- Sanitize all user inputs with HTML entity encoding and validate against allowlists for SVG attributes.
- Monitor for anomalous JavaScript execution via browser logs or WAF alerts on SVG uploads.

## Objectives

1. Evade Cloudflare WAF filtering to inject executable JavaScript.
2. Trigger a prompt or arbitrary code execution in the victim's browser.
3. Demonstrate potential for session theft or data exfiltration via the executed script.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Locate a user input field on the target site where input is reflected back in the HTML response without sanitization, such as a search parameter or form field. Use browser developer tools to inspect how the input is echoed.

Inspect the page source after submitting benign input to confirm the reflection context allows SVG tags.

### Step 2: Craft the SVG Payload

**Context**: Prepare the malicious SVG snippet that uses the onload event to execute JavaScript. This payload is self-contained and triggers on load.

**Code** ([[codes/SVG-OnLoad-Prompt-XSS-Payload]]):

```html
<svg/OnLoad="`${prompt()}`">
```

> This injects an SVG element that executes the prompt() function upon loading, displaying an alert box. The backticks enable template literal execution if needed for further chaining, but here it simply prompts the user. Expected output is a browser prompt dialog confirming execution.

### Step 3: Inject and Test the Payload

**Context**: Submit the payload through the identified injection point and observe the response. If using a proxy, intercept and modify the request to include the SVG.

Encode the payload if necessary (e.g., URL encode for GET parameters) and submit via the vulnerable form or URL. Reload or trigger the reflection to load the SVG.

### Step 4: Verify Execution

**Context**: Confirm the bypass by checking for the prompt or any console errors/logs indicating JavaScript execution.

In the browser console, look for the prompt dialog. If successful, no WAF block occurs, and code runs client-side.

Expected Output: A JavaScript prompt box appears, proving the XSS execution.
