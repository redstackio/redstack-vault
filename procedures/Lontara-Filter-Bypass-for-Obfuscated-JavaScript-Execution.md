---
type: procedure
description: >-
  Bypasses web application filters using Lontara obfuscation to execute
  malicious JavaScript code in cross-site scripting attacks.
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.940749+00:00'
updated_at: '2023-04-10T20:21:44.618387+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/Bypass using Lontara]]'
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/Filter Bypass and exotic payloads]]'
  - xss
  - filter-bypass
  - obfuscation
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Lontara-Filter-Bypass-for-Obfuscated-JavaScript-Execution

## Summary

This procedure demonstrates the Lontara technique for bypassing web application filters by obfuscating JavaScript code using Unicode characters from non-Latin scripts. The obfuscated payload evades detection by content filters or Web Application Firewalls (WAFs) and executes arbitrary JavaScript on the target browser, enabling cross-site scripting (XSS) attacks to steal session cookies, perform unauthorized actions, or exfiltrate data.

## Description

Lontara obfuscation leverages unusual Unicode characters (e.g., from the Philippine scripts block) to rename variables and construct strings that mimic standard JavaScript but appear benign to regex-based filters. These characters are valid in JS identifiers but often not sanitized in input validation. Once injected into a vulnerable input field (e.g., reflected XSS in a search parameter), the browser parses and executes the code, typically invoking functions like eval() to run hidden payloads. This is effective against applications that strip common XSS patterns like <script>alert(1)</script> but miss Unicode variants. The target environment is client-side web applications with insufficient input sanitization, such as legacy forums or unpatched CMS. Expected outcomes include successful code execution without filter triggers, confirmed by browser alerts or network requests.

## Requirements

1. Access to a web application vulnerable to reflected or stored XSS (e.g., unsanitized user input reflected in HTML).
2. Knowledge of the application's filter rules to craft the obfuscation.
3. A browser or proxy tool like Burp Suite to test and inject the payload.
4. Basic JavaScript understanding to verify execution.

## Defense

- Implement strict Content Security Policy (CSP) to block inline scripts and restrict eval() usage.
- Use advanced WAF rules that normalize Unicode and detect obfuscated patterns (e.g., via libraries like js-beautify).
- Sanitize inputs with HTML entity encoding and validate against allowlists for script content.
- Enable browser security features like XSS Auditor and monitor for unusual Unicode in logs.

## Objectives

1. Bypass input filters to deliver executable JavaScript without detection.
2. Execute obfuscated code in the victim's browser context.
3. Achieve XSS effects such as session hijacking or data theft.

## Instructions

### Step 1: Identify Vulnerable Input and Prepare Obfuscated Payload

**Context**: Locate a reflected XSS vector, such as a search box or URL parameter that echoes user input without sanitization. Use the Lontara-obfuscated code to construct a payload that evades filters by using Unicode variables to build and execute a function like eval('alert("XSS")').

**Code** ([[codes/Lontara-Obfuscated-JavaScript-Payload]]):

```javascript
ᨆ='',ᨊ=!ᨆ+ᨆ,ᨎ=!ᨊ+ᨆ,ᨂ=ᨆ+{},ᨇ=ᨊ[ᨆ++],ᨋ=ᨊ[ᨏ=ᨆ],ᨃ=++ᨏ+ᨆ,ᨅ=ᨂ[ᨏ+ᨃ],ᨊ[ᨅ+=ᨂ[ᨆ]+(ᨊ.ᨎ+ᨂ)[ᨆ]+ᨎ[ᨃ]+ᨇ+ᨋ+ᨊ[ᨏ]+ᨅ+ᨇ+ᨂ[ᨆ]+ᨋ][ᨅ](ᨎ[ᨆ]+ᨎ[ᨏ]+ᨊ[ᨃ]+ᨋ+ᨇ+"(ᨆ)")()
```

> This step prepares the payload for injection. The code initializes obfuscated variables and concatenates strings to form an eval() call executing an empty or custom alert. Test in a local JS environment (e.g., browser console) to confirm it runs without errors, producing a popup or console log indicating success.

### Step 2: Inject Payload into Vulnerable Endpoint

**Context**: Deliver the obfuscated code via the identified XSS vector. Wrap it in a script tag if needed, but rely on the obfuscation to bypass any <script> stripping. Use a proxy to intercept and modify requests.

**Instructions**: Navigate to the vulnerable page (e.g., /search?q=<payload>). Replace the query parameter with the obfuscated code: <script>[[codes/Lontara-Obfuscated-JavaScript-Payload]]</script>. Submit the form or load the URL. If using a proxy, ensure no normalization occurs.

> Why: This injects the payload into the DOM where the browser will parse it as JS. Decision point: If the filter blocks Unicode, try alternative scripts or combine with HTML encoding.

### Step 3: Verify Execution and Impact

**Context**: Confirm the code executes in the target context by observing effects like an alert popup or network exfiltration.

**Instructions**: Load the injected page in a browser. Monitor the developer console for errors and the network tab for any callbacks (e.g., to attacker-controlled server). If successful, extend the payload to document.cookie or fetch() for data theft.

> Expected: No filter blocks, JS executes silently or with visible indicator (e.g., alert). If fails, iterate on obfuscation variables.
