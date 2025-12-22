---
id: fee2febf-967e-4f5d-a47b-81a5b8080c51
name: Identify-XSS-Using-Polyglot-Payload
type: procedure
verified: true
submitted: true
created_at: '2020-09-07T06:38:29.093745+00:00'
updated_at: '2023-05-26T01:11:04.704917+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - owasp
  - owasp top 10
  - polyglot
  - web applications
  - xss
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Identify-XSS-Using-Polyglot-Payload

## Summary

This procedure uses a polyglot XSS payload to quickly identify cross-site scripting (XSS) vulnerabilities in web applications. By injecting a single versatile payload into user input fields, such as search boxes, it tests for execution across multiple injection contexts like HTML attributes, JavaScript, styles, and SVG elements, saving time compared to testing individual payloads.

## Description

Cross-site scripting (XSS) vulnerabilities allow attackers to inject malicious scripts into web pages viewed by other users, potentially leading to session hijacking, data theft, or defacement. Identifying XSS manually requires testing numerous payloads tailored to specific contexts (e.g., reflected in HTML, JavaScript, or event handlers), which is time-consuming. A polyglot payload combines obfuscated variations to bypass common filters and trigger execution in diverse contexts simultaneously. This technique is particularly useful during penetration testing of web applications with user-controlled inputs like search fields, forms, or URL parameters. The procedure assumes access to a browser or intercepting proxy and focuses on reflected XSS detection via an alert box. Successful execution confirms the vulnerability, after which further exploitation can be explored.

## Requirements

1. Access to a web application with user input fields (e.g., search box, login form, or comment section).
2. A modern web browser (e.g., Chrome, Firefox) or an intercepting proxy like Burp Suite for manual injection.
3. No special privileges required, but developer tools enabled in the browser for inspection.
4. Basic knowledge of web application structure and HTTP requests.

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict script execution and inline JavaScript.
- Sanitize and encode all user inputs using libraries like OWASP ESAPI or DOMPurify.
- Use Web Application Firewalls (WAFs) to detect and block common XSS patterns, including polyglots.
- Enable browser security features like XSS Auditor (deprecated in modern browsers) or strict output encoding.
- Monitor application logs for suspicious input patterns and alert on JavaScript execution attempts.

## Objectives

1. Rapidly detect XSS vulnerabilities without testing multiple payloads.
2. Confirm execution by observing a JavaScript alert box.
3. Identify the injection point for further payload refinement or exploitation.
4. Verify the vulnerability's context (e.g., reflected, stored) for reporting.

## Instructions

### Step 1: Identify User Input Fields

**Context**: Locate potential injection points in the web application where user input is reflected back without proper sanitization. Common locations include search bars, form fields, URL parameters, or error messages. Use browser developer tools or a proxy to inspect how input is processed and echoed.

Inspect the page source or use a tool like Burp Suite to map the application. Look for fields that accept arbitrary text and display it dynamically.

### Step 2: Inject the Polyglot Payload

**Context**: Insert the polyglot payload into the identified input field to test for XSS execution across multiple contexts. This payload is designed to trigger a JavaScript alert() if the input is not sanitized, working in scenarios like HTML tags, event handlers, script blocks, and SVG onload attributes.

Navigate to the input field (e.g., search box) and enter the following polyglot payload, then submit the form or click the associated button (e.g., "Search").

Reference the payload: [[codes/XSS-Polyglot-Payload]]

```html
*jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert() )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert()//>\x3e*
```

If using a proxy like Burp Suite, intercept the request, modify the parameter (e.g., ?q=payload), and forward it.

### Step 3: Observe Execution and Verify

**Context**: After submission, monitor the response for signs of payload execution. A successful XSS will trigger a browser alert box displaying "alert()" or similar, confirming the vulnerability. If no alert appears, inspect the page source to check if the payload was reflected intact or altered by filters.

Reload the page if necessary and use browser console (F12) to check for JavaScript errors or executed code. If the payload is partially sanitized, note the context (e.g., escaped quotes) for targeted follow-up tests.

## Expected Output

Upon successful injection, the browser displays a pop-up alert box with the message from alert(). The page source may show the obfuscated payload reflected without escaping, such as in a <script> tag or event attribute. No alert indicates potential sanitization; further testing with context-specific payloads is needed.

## Success Indicators

- JavaScript alert() dialog appears immediately after submission.
- Page source inspection reveals unescaped payload elements (e.g., <svg/onload=alert()>).
- No HTTP errors or redirects that prevent reflection.
