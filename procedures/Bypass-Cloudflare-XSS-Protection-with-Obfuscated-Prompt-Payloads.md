---
id: 8c691c95-8c33-462f-bbd6-21b19f8fd238
name: Bypass-Cloudflare-XSS-Protection-with-Obfuscated-Prompt-Payloads
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:43.393499+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Impair Defenses: Disable or Modify Tools|T1562.001 - Impair
    Defenses: Disable or Modify Tools]]
  - >-
    [[techniques/Command and Scripting Interpreter: JavaScript|T1059.007 -
    Command and Scripting Interpreter: JavaScript]]
sub_techniques: []
tags:
  - '[[tags/3rd June 2019]]'
  - >-
    [[tags/Cloudflare XSS Bypasses by [@Bohdan
    Korzhynskyi](https://twitter.com/bohdansec)]]
  - '[[tags/Common WAF Bypass]]'
  - '[[tags/Cross Site Scripting]]'
  - xss
  - waf-bypass
  - cloudflare
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Bypass-Cloudflare-XSS-Protection-with-Obfuscated-Prompt-Payloads

## Summary

This procedure demonstrates how to bypass Cloudflare's Web Application Firewall (WAF) protections against Cross-Site Scripting (XSS) attacks by using obfuscated HTML payloads that trigger a JavaScript prompt displaying the document domain. These payloads evade detection by encoding characters and leveraging alternative attributes like onload in SVG tags or srcdoc in iframes, allowing execution of malicious JavaScript in vulnerable input fields or reflected/stored XSS contexts.

## Description

Cloudflare's WAF often blocks standard XSS payloads like <script>alert(document.domain)</script> by signature matching. This technique uses URL encoding and entity references (e.g., %26# for &) to obfuscate the prompt function call, combined with non-standard HTML elements like SVG and iframe to execute code without triggering filters. It is particularly effective against reflected XSS in search parameters, form inputs, or error messages on websites protected by Cloudflare. The goal is to confirm XSS execution by prompting the domain, which can lead to session hijacking, data theft, or further exploitation. This applies to web applications where user input is reflected without proper sanitization, and the WAF rules are not tuned to detect these specific obfuscations.

## Requirements

1. Identification of a vulnerable input point (e.g., search box, URL parameter) on a Cloudflare-protected site that reflects user input without escaping.
2. Basic knowledge of the target's domain and potential XSS vectors, often discovered via reconnaissance tools like Burp Suite or manual testing.
3. A testing environment or proxy (e.g., browser developer tools) to inject and observe payloads without causing harm.
4. No special privileges required, but ethical testing permission is mandatory.

## Defense

- Implement Content Security Policy (CSP) headers to restrict script execution and inline code.
- Use strict input validation and output encoding (e.g., HTML entity encoding) on all user inputs.
- Tune WAF rules in Cloudflare to detect obfuscated payloads, including entity decoding and SVG/iframe anomalies.
- Enable browser-based protections like XSS Auditor (deprecated in modern browsers) or extensions like NoScript.
- Regularly audit reflected inputs and monitor for unusual JavaScript prompts or domain disclosures.

## Objectives

1. Evade Cloudflare WAF detection to inject and execute JavaScript code.
2. Trigger a prompt revealing the document domain to confirm successful XSS exploitation.
3. Demonstrate potential for further attacks like cookie theft or keylogging in a real scenario.

## Instructions

### Step 1: Identify Vulnerable Input Vector

**Context**: Locate a point where user input is reflected back in the HTML response, such as a search parameter (?q=) or form field. Test with a benign payload like <script>alert(1)</script> to confirm basic XSS, then proceed if blocked.

Use browser developer tools or a proxy to inspect the page source and identify reflection points. No specific command is needed here; manual inspection suffices.

**Expected Output**: Confirmation that input appears unescaped in the DOM, e.g., via searching the response for the injected string.

### Step 2: Inject Obfuscated SVG Payload

**Context**: Use the first obfuscated payload to bypass filters by encoding the prompt call within an SVG onload attribute. This executes JavaScript upon element loading, prompting the domain without direct <script> tags.

Inject the payload into the vulnerable field:

Reference the code snippet: [[codes/Cloudflare-XSS-Bypass-SVG-Prompt-Payload]]

> This payload uses %26#x000000028; for '(' and similar encodings to hide the prompt function from signature-based detection. Submit the form or navigate to the URL with the payload.

**Expected Output**: A JavaScript prompt dialog appears displaying the current document's domain (e.g., "example.com"), confirming execution.

### Step 3: Test Alternative Iframe Payload

**Context**: If the SVG payload is blocked, try the iframe-based variant which loads a scripted document via srcdoc, executing the prompt within an isolated context to further evade filters.

Inject the second or third payload variants:

Reference the code snippet: [[codes/Cloudflare-XSS-Bypass-SVG-Prompt-Payload]] (use the additional lines for variations).

> The iframe srcdoc attribute allows embedding HTML with a script tag, using template literals and backticks for obfuscation. This can bypass rules targeting direct onload attributes.

**Expected Output**: Prompt dialog with the domain, or execution of the inner script without errors in the console.

### Step 4: Verify and Escalate

**Context**: Confirm success by checking browser console for errors or network logs for anomalies. If successful, escalate by replacing prompt with more malicious code like fetching external scripts.

Monitor the page for the prompt and inspect cookies or localStorage for potential data access.

**Expected Output**: No WAF blocks (e.g., 403 errors), successful prompt, and console logs showing JS execution.
