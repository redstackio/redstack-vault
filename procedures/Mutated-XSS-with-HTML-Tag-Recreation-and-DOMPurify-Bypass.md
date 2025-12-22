---
type: procedure
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/JavaScript|T1059.007 - JavaScript]]'
  - '[[techniques/Impair Defenses|T1562 - Impair Defenses]]'
sub_techniques: []
tags:
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/Mutated XSS]]'
commands:
  - '[[commands/get-element-innerHTML]]'
tools: []
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Mutated-XSS-with-HTML-Tag-Recreation-and-DOMPurify-Bypass

## Summary

This procedure demonstrates a mutated XSS attack that recreates HTML tags using JavaScript to evade sanitization and bypasses DOMPurify by exploiting parsing quirks in noscript and title attributes, allowing arbitrary JavaScript execution in the victim's browser.

## Description

Mutated XSS involves injecting payloads that appear benign to filters but execute malicious code due to browser parsing behaviors. In this technique, HTML tags are recreated dynamically via JavaScript's innerHTML property to insert unsanitized content. Combined with a DOMPurify bypass payload using nested noscript and title attributes, the attack tricks the sanitizer into allowing an img tag with an onerror handler. This is particularly effective against sites like Google Search that use DOMPurify for input cleaning. Successful execution grants access to session cookies, DOM manipulation, or actions like phishing on behalf of the victim. The target is web applications with insufficient output encoding or flawed sanitization libraries.

## Requirements

1. Access to a web application vulnerable to reflected or stored XSS, such as an input field processed by DOMPurify.
2. Ability to inject arbitrary strings into user-controlled inputs (e.g., search fields or profile data).
3. Browser developer tools or a proxy like Burp Suite for inspecting and modifying requests.
4. Knowledge of JavaScript DOM manipulation and HTML parsing quirks.

## Defense

- Implement strict input validation and output encoding using libraries like DOMPurify with the latest updates.
- Deploy Content Security Policy (CSP) to block inline scripts and restrict script sources.
- Regularly audit and patch web applications, focusing on third-party sanitization libraries.
- Monitor for anomalous JavaScript execution via client-side logging or server-side anomaly detection.

## Objectives

1. Recreate HTML tags to insert unsanitized content and evade basic filters.
2. Bypass DOMPurify using mutated payloads to execute JavaScript.
3. Steal sensitive data like cookies or perform unauthorized actions in the victim's session.
4. Demonstrate full control over the DOM for further exploitation.

## Instructions

1. Identify the vulnerable input field and the target element for tag recreation.

   **Context**: When HTML tags fail to render due to sanitization or quirks, recreate them programmatically to force execution.

   Use [[commands/get-element-innerHTML]] to access and modify the innerHTML of the target element:

   ```javascript
element.innerHTML
   ```

   > This retrieves the current innerHTML. To recreate, create a new div element, set its innerHTML to the desired malicious HTML (e.g., a script tag), and append it to the parent.

   Example full recreation script:

   ```javascript
var originalElement = document.getElementById('vulnerable-div');
var newElement = document.createElement('div');
newElement.innerHTML = '<script>alert("XSS")</script>';
originalElement.appendChild(newElement);
   ```

   Expected output: The browser renders the injected HTML, executing any scripts.

2. Inject the mutated payload into the vulnerable input field.

   **Context**: Submit the payload to bypass DOMPurify by closing the noscript tag prematurely and injecting an executable img element.

   Use the payload from [[codes/Mutated-XSS-Payload-for-DOMPurify-Bypass]]:

   ```javascript
   <noscript><p title="</noscript><img src=x onerror=alert(1)>">
   ```

   > Inject this string into a field like a search 'data' parameter. The parser breaks out of noscript via the title attribute, allowing the img tag to execute onerror. Replace alert(1) with actual payload like document.cookie exfiltration.

   Expected output: JavaScript alert fires, or custom payload executes (e.g., network request to attacker server).

   Decision point: If the payload is stripped, test variations by adjusting nesting or attributes; otherwise, proceed to verify execution via dev tools.
