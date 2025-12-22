---
id: 92232eff-af88-4e5c-a0f5-a8e60204e826
name: Identifying-DOM-Based-XSS
type: procedure
verified: true
submitted: true
created_at: '2020-07-28T15:23:15.697101+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/DOM XSS]]'
  - '[[tags/injection]]'
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Web Applications]]'
  - '[[tags/xss]]'
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
---

# Identifying-DOM-Based-XSS

## Summary

This procedure demonstrates how to identify DOM-based Cross-Site Scripting (XSS) vulnerabilities in web applications where user input from client-side sources, such as URL fragments (after the # symbol), is processed and executed directly in the browser's Document Object Model (DOM) without being sent to the server. It involves manipulating the URL, injecting payloads, and verifying that the input does not reach the server while still executing in the browser.

## Description

DOM-based XSS occurs when client-side JavaScript takes untrusted data from sources like the URL fragment identifier (everything after #) and uses it to update the DOM in an unsafe manner, such as via innerHTML, document.write, or eval. Unlike reflected or stored XSS, the input never reaches the server, making it harder to detect with server-side logging or WAFs. This procedure is useful during web application penetration testing to uncover client-side injection points, particularly in single-page applications (SPAs) or sites using JavaScript frameworks like React or Angular. The target environment is typically a web browser interacting with a JavaScript-heavy web app. Expected outcomes include successful payload execution confirming the vulnerability, allowing potential theft of session cookies, keystroke logging, or phishing attacks.

## Requirements

1. Access to a web browser (e.g., Chrome or Firefox) with developer tools enabled.
2. A proxy tool like [[tools/Burp-Suite]] configured to intercept browser traffic.
3. Valid access to the target web application, such as a URL with a client-side processing feature (e.g., a search or hash-based navigation page).
4. Basic knowledge of JavaScript and URL structure.

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) with strict script-src directives to prevent inline script execution.
- Use safe DOM APIs like textContent or createTextNode instead of innerHTML or document.write.
- Sanitize and validate all client-side inputs, encoding URL fragments before DOM insertion.
- Enable browser security features like XSS Auditor (deprecated in modern browsers) or rely on CSP reporting to log potential violations.
- Perform client-side code reviews and static analysis with tools like ESLint for unsafe sink usage.

## Objectives

1. Confirm that user input from the URL fragment is processed client-side without server transmission.
2. Inject and execute a JavaScript payload to demonstrate DOM manipulation.
3. Verify the vulnerability by checking for execution without server-side reflection.
4. Document the injection point for further exploitation or reporting.

## Instructions

### Step 1: Identify Potential Client-Side Input Points

**Context**: Examine the target page for features that use URL fragments (after #) to update content dynamically, such as hash-based routing, search parameters, or page states. This step ensures you're targeting a location where input might be read client-side via JavaScript (e.g., location.hash).

Navigate to the target URL in your browser and inspect the page source or use developer tools (F12) to look for JavaScript code accessing location.hash or similar properties. No specific command is needed; use manual inspection.

> Look for code patterns like document.getElementById('output').innerHTML = location.hash.substring(1); which indicate unsafe DOM sinks.

### Step 2: Modify the URL Fragment with a Test Payload

**Context**: Append a JavaScript payload to the URL fragment to test if it's executed in the DOM. A simple alert payload confirms execution without requiring advanced tools.

In the browser address bar, modify the URL by adding the payload after the # symbol, e.g., change https://target.com/page#test to https://target.com/page#<script>alert('XSS')</script>. Press Enter to load the modified URL.

> The payload should trigger an alert box in the browser if vulnerable, indicating client-side execution.

### Step 3: Intercept Traffic to Verify No Server Transmission

**Context**: Use a proxy to confirm the payload does not reach the server, distinguishing this from reflected XSS. Configure your browser to route traffic through [[tools/Burp-Suite]] Proxy.

With Burp Suite running and proxy enabled (default 127.0.0.1:8080), reload the modified URL. In Burp's Proxy > HTTP history tab, inspect the GET request for the target page.

> The request URI should show the path up to the # but not the fragment (e.g., GET /page HTTP/1.1, without the payload), confirming client-side only processing.

### Step 4: Validate Payload Execution

**Context**: Confirm the payload executed successfully in the browser while ensuring no server-side involvement, solidifying the DOM XSS identification.

Observe the browser for the alert dialog or any DOM changes (e.g., via Elements tab in dev tools). If an alert pops up, the vulnerability is confirmed.

> Success is indicated by the alert firing without any corresponding payload in Burp's intercepted requests. If no execution occurs, try variations like alert(document.domain) or URL-encode the payload (%3Cscript%3Ealert('XSS')%3C/script%3E).
