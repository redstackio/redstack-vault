---
type: procedure
description: >-
  Injects malicious JavaScript code into web pages via HTML and JS contexts to
  execute arbitrary scripts, bypassing basic sanitization.
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - cross-site-scripting
  - html-context
  - js-context
  - injection
commands:
  - '[[commands/curl-inject-xss-payload]]'
tools: []
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Execute-XSS-in-HTML-and-JS-Context

## Summary

This procedure demonstrates how to perform a Cross-Site Scripting (XSS) attack in HTML and JavaScript contexts by injecting a malicious payload that bypasses quote-based sanitization. The payload executes JavaScript to display an alert or perform actions like stealing cookies, targeting vulnerable web applications with insufficient input validation.

## Description

Cross-site scripting (XSS) allows attackers to inject malicious scripts into web pages viewed by other users. In HTML context, this involves injecting elements like script tags; in JS context, it means injecting code executed by the JavaScript interpreter. This procedure focuses on a reflected or stored XSS variant using a payload that avoids quotes to evade filters. It can lead to session hijacking, data theft, or unauthorized actions. The attack requires a vulnerable input field (e.g., search box, comment form) that reflects user input without proper encoding. Target environments include web apps on any platform without CSP or output escaping. Success results in script execution in the victim's browser, enabling collection of sensitive data like cookies.

## Requirements

1. Access to a vulnerable web application with unsanitized input fields (e.g., reflected in HTML/JS).
2. Knowledge of the input mechanism (URL parameter, POST form, etc.).
3. Tools for sending requests (browser or curl) and intercepting responses if needed.
4. Attacker-controlled domain or endpoint for data exfiltration if extending beyond alert.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML entity encoding for user input).
- Deploy Content Security Policy (CSP) to block inline scripts and restrict script sources.
- Use Web Application Firewalls (WAFs) to detect and block common XSS patterns.
- Regularly scan for vulnerabilities using tools like OWASP ZAP or Burp Suite and apply patches.
- Enable browser security features like XSS Auditor (deprecated) or modern alternatives like Trusted Types.

## Objectives

1. Identify and exploit a vulnerable input point in HTML or JS context.
2. Inject and execute malicious JavaScript to confirm control (e.g., alert popup).
3. Steal sensitive information like session cookies or perform actions on behalf of the victim.

## Instructions

### Step 1: Identify Vulnerable Input Field

**Context**: Locate an input field or parameter that reflects user input directly into HTML or JS without sanitization, such as a search query or URL parameter.

Inspect the application using browser developer tools to find reflection points. Test basic payloads like `<script>alert(1)</script>` to confirm vulnerability, but expect quote filters.

### Step 2: Craft XSS Payload

**Context**: Use the specialized payload to bypass quote/double-quote sanitization, ensuring it executes in both HTML and JS contexts.

Reference the payload code [[codes/XSS-Payload-Without-Quotes-Bypass]] and substitute any variables if needed for exfiltration.

### Step 3: Inject Payload via HTTP Request

**Context**: Send the crafted payload to the vulnerable endpoint to trigger execution when the page loads or input is processed.

**Command** ([[commands/curl-inject-xss-payload]]):
```bash
curl -X POST -d "search=$_PAYLOAD" $_TARGET_URL
```

> This command submits the payload via a POST request to a form endpoint. Replace $_PAYLOAD with the encoded XSS code and $_TARGET_URL with the vulnerable URL (e.g., http://target.com/search). For GET, use `curl "$_TARGET_URL?search=$_PAYLOAD"`. Expected output: HTTP response containing the reflected payload, confirming injection. Visit the resulting page in a browser to see execution (e.g., alert popup).

### Step 4: Verify Execution and Exfiltrate Data

**Context**: Confirm the script runs in the victim's context and extend to steal data if successful.

Load the page with the injected payload in a browser. If alert(1) appears, the XSS is confirmed. Modify the payload to send document.cookie to an attacker-controlled server via XMLHttpRequest for data theft.

**Expected Output**: JavaScript alert or network request to attacker endpoint with stolen data.

**Success Indicators**:
- Alert box or console log appears on page load.
- No syntax errors in page source; payload reflected intact.
- Stolen data (e.g., cookies) received on attacker side.
