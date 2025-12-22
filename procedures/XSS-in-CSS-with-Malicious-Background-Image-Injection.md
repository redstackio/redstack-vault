---
id: f58059eb-0fec-4868-97ed-c7c5e1923a39
name: XSS-in-CSS-with-Malicious-Background-Image-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.157835+00:00'
updated_at: '2023-04-10T20:21:52.322995+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/XSS in CSS]]'
  - '[[tags/XSS in files]]'
  - xss
  - css-injection
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# XSS-in-CSS-with-Malicious-Background-Image-Injection

## Summary

This procedure demonstrates how to inject cross-site scripting (XSS) payloads into a website's CSS files by exploiting the background-image property. Attackers can craft a malicious data URL that encodes an SVG element with JavaScript, allowing execution of arbitrary code in the victim's browser when the CSS is applied, such as stealing cookies or session tokens.

## Description

XSS in CSS via malicious background image injection targets vulnerabilities where user input influences CSS properties, such as dynamic stylesheets or reflected inputs in CSS contexts. The technique uses a data URI scheme to embed an SVG image containing an onload JavaScript handler, which executes when the browser parses the background-image. This bypasses some content security policies (CSP) that may not fully restrict CSS-evaluated content. It is effective against web applications with insufficient input sanitization on CSS-related endpoints, leading to code execution in the context of the victim's session. The attack requires identifying injectable points, such as URL parameters reflected into CSS or file upload features that process stylesheets.

## Requirements

1. Access to a web application with a vulnerability allowing user input to influence CSS properties (e.g., reflected parameters in stylesheets or dynamic CSS generation).
2. Knowledge of the target's CSS structure and rendering behavior.
3. A browser or tool like Burp Suite for testing and intercepting requests.
4. Basic understanding of data URIs, SVG, and JavaScript execution in CSS contexts.

## Defense

- Implement strict input validation and sanitization for all user-supplied data that could affect CSS, rejecting or escaping data URIs and SVG content.
- Deploy a robust Content Security Policy (CSP) with 'unsafe-inline' restrictions and explicit style-src directives to block inline styles and data URLs.
- Regularly scan CSS files and dynamic content generation points for injection vulnerabilities using tools like OWASP ZAP or static analysis.
- Use HTTP-only and Secure flags on cookies to mitigate theft even if XSS occurs.

## Objectives

1. Identify and exploit a CSS injection point to insert a malicious background-image property.
2. Execute JavaScript in the victim's browser to demonstrate code execution, such as displaying an alert or exfiltrating data.
3. Verify the payload triggers without breaking the page layout or alerting the user.

## Instructions

### Step 1: Identify the CSS Injection Point

**Context**: Locate a vulnerability where user input is reflected into a CSS file or inline style without proper escaping, such as a search parameter that generates dynamic CSS rules.

Inspect the application's source code or use developer tools to find elements where user input appears in style attributes or linked CSS files. Test for injection by submitting payloads like '/*' to comment out existing CSS and observe if it alters rendering.

### Step 2: Craft the Malicious Payload

**Context**: Create a data URL that encodes an SVG with JavaScript to execute on load, targeting the background-image property.

Use the following payload structure, which closes the style tag prematurely and injects an SVG that alerts the document domain:

Embed the code from [[codes/XSS-CSS-Background-Image-SVG-Payload]] into your input field or request.

> This payload works by using a base64-encoded data URI for a JPG (to bypass simple filters), but actually contains SVG with an onload handler. When applied as background-image, the browser executes the JavaScript.

### Step 3: Inject the Payload

**Context**: Submit the crafted payload to the vulnerable endpoint to trigger the CSS injection.

If the vulnerability is in a URL parameter (e.g., ?style=), append the payload to the request. For file uploads, create a CSS file with the malicious rule and upload it. Monitor the response to ensure the payload is reflected without sanitization.

### Step 4: Verify Execution

**Context**: Load the affected page in a browser and confirm the JavaScript executes.

Navigate to the page where the CSS is applied. Look for the alert box or any side effects (e.g., network requests if modified for exfiltration). Use browser console to check for errors or successful script execution.

**Expected Output**: An alert dialog displaying the current domain (e.g., "alert(document.domain)" shows "example.com"), confirming XSS execution without visible layout breakage.
