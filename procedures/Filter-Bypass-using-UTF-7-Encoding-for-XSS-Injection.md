---
id: 8f158aec-b431-4cb1-b7b8-f13067d046e0
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:43.029039+00:00'
updated_at: '2023-04-10T20:21:56.208276+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/JavaScript|T1059.007 - JavaScript]]'
  - '[[techniques/Impair-Defenses|T1562 - Impair Defenses]]'
sub_techniques: []
tags:
  - '[[tags/Bypass using UTF-7]]'
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/Filter Bypass and exotic payloads]]'
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Filter-Bypass-using-UTF-7-Encoding-for-XSS-Injection

## Summary

This procedure demonstrates how to bypass input sanitization filters in web applications using UTF-7 encoding to inject a cross-site scripting (XSS) payload. By encoding a malicious JavaScript snippet in UTF-7, attackers can evade filters that block common XSS patterns, allowing execution of arbitrary code in the victim's browser to steal session cookies, credentials, or perform other malicious actions.

## Description

Cross-Site Scripting (XSS) attacks exploit insufficient input validation to inject and execute malicious scripts in the context of a trusted website. Many web applications filter out obvious XSS payloads like '<script>alert(1)</script>', but fail to handle alternative encodings such as UTF-7. UTF-7 encoding represents characters using a base64-like scheme prefixed with '+ADw-' for '<' and similar, allowing the payload to slip through. This technique targets reflected or stored XSS vulnerabilities in user input fields, search boxes, or comment sections. Successful execution can lead to session hijacking, keylogging, or phishing within the site. It is particularly effective against legacy systems or applications without comprehensive encoding normalization.

## Requirements

1. Access to a web application with a vulnerable input field that reflects user input without proper sanitization or decoding normalization.
2. Knowledge of the target's character encoding support (must allow UTF-7).
3. A browser or tool like Burp Suite to test and inject the payload.
4. Basic understanding of HTML and JavaScript for payload customization.

## Defense

- Implement strict input validation and output encoding using libraries like OWASP ESAPI or DOMPurify to normalize and sanitize all user inputs.
- Enforce Content Security Policy (CSP) headers to restrict inline script execution and restrict script sources.
- Deploy a Web Application Firewall (WAF) configured to detect encoded payloads, including UTF-7 variants, and block suspicious patterns.
- Regularly scan for XSS vulnerabilities using tools like OWASP ZAP or Burp Suite Scanner.

## Objectives

1. Bypass client-side or server-side filters designed to prevent XSS injections.
2. Execute arbitrary JavaScript in the victim's browser context.
3. Demonstrate potential for data theft or further exploitation, such as stealing authentication tokens.

## Instructions

### Step 1: Identify Vulnerable Input Field

**Context**: Locate an input field on the target website that echoes user input directly into the HTML without sanitization, such as a search box or profile update form. Test for basic XSS by injecting '<script>alert(1)</script>' and observing if it executes or is filtered.

> If the basic payload is blocked but the input is reflected, proceed to UTF-7 encoding to bypass the filter.

### Step 2: Encode the XSS Payload Using UTF-7

**Context**: Convert a standard XSS payload into UTF-7 encoding to evade pattern-based filters. The example uses an image tag with an onerror handler to trigger JavaScript execution when the invalid source fails to load.

**Code** ([[codes/UTF-7-Encoded-XSS-Alert-Payload]]):

```javascript
+ADw-img src=+ACI-1+ACI- onerror=+ACI-alert(1)+ACI- /+AD4-
```

> This encoded string decodes to '<img src="1" onerror="alert(1)" />'. The 'src' points to a non-existent resource, triggering the onerror event to execute alert(1). Submit this in the vulnerable field and observe if an alert box appears, confirming successful injection and execution.

### Step 3: Verify Execution and Escalate

**Context**: Confirm the payload executes by checking for the alert or any console errors/logs. If successful, customize the payload for real exploitation, such as replacing alert(1) with code to exfiltrate document.cookie to an attacker-controlled server.

> Monitor network traffic for any data leakage. If the site uses UTF-7, ensure the response renders the decoded HTML in the browser context.
