---
type: procedure
description: >-
  Bypass Cloudflare WAF protections to inject HTML and execute XSS payloads on
  vulnerable web inputs.
verified: true
submitted: false
created_at: '2023-04-06T03:56:43.369532+00:00'
updated_at: '2023-04-10T20:21:30.892823+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/JavaScript|T1059.007 - JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/5th June 2019]]'
  - '[[tags/Cloudflare XSS Bypasses by @Bohdan Korzhynskyi]]'
  - '[[tags/Common WAF Bypass]]'
  - '[[tags/Cross Site Scripting]]'
  - xss
  - waf-bypass
  - html-injection
  - cloudflare
commands:
  - '[[commands/curl-inject-xss-payload]]'
tools: []
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Cloudflare-XSS-Bypass-via-Common-WAF-and-HTML-Injection

## Summary

This procedure demonstrates how to bypass Cloudflare's Web Application Firewall (WAF) using common evasion techniques combined with HTML injection to achieve Cross-Site Scripting (XSS). By crafting an obfuscated payload that evades WAF rules, an attacker can inject malicious JavaScript into a vulnerable input field on a protected website, leading to execution in victims' browsers for data theft or session hijacking.

## Description

This procedure targets websites protected by Cloudflare where input fields (e.g., search boxes, comment forms) are vulnerable to HTML injection but guarded by WAF rules against direct XSS. The attacker identifies a bypass technique, such as using alternative encodings or syntax tricks (e.g., onerror attributes in img tags with pipe operators), that slips past the WAF. The payload is then injected, and when rendered unsanitized, it executes JavaScript to alert, steal cookies, or perform other actions on behalf of the victim. This is particularly effective against reflected or stored XSS scenarios. Technically, it exploits insufficient input validation and WAF misconfigurations. From a business perspective, successful attacks can lead to data breaches, account takeovers, and compliance violations like GDPR or PCI-DSS.

## Requirements

1. Access to a vulnerable website protected by Cloudflare with an injectable input field (e.g., via public-facing form).
2. Knowledge of common WAF bypass techniques, such as encoding payloads or using HTML5 attributes.
3. A web browser for manual testing or tools like curl for automated injection.
4. Basic understanding of HTML injection and JavaScript execution contexts.

## Defense

Defensive measures and detection strategies:

- Implement a robust WAF configuration that includes signature-based and behavioral detection for XSS payloads, regularly updating rules for known bypasses.
- Enforce strict input sanitization and output encoding (e.g., using libraries like DOMPurify) to prevent HTML injection.
- Deploy Content Security Policy (CSP) headers to restrict inline script execution and external resource loading.
- Monitor for anomalous JavaScript execution via client-side telemetry or server logs showing unusual payload submissions.

## Objectives

1. Successfully bypass Cloudflare WAF rules to inject an HTML payload into a vulnerable field.
2. Execute malicious JavaScript in a victim's browser to steal session cookies or credentials.
3. Demonstrate potential for further actions like phishing or defacement on behalf of the victim.

## Instructions

### Step 1: Identify Vulnerable Input Field

**Context**: Locate an input field on the target site that accepts user input and reflects it without proper sanitization, such as a search parameter or comment box. Test for basic HTML injection by submitting tags like <b>test</b> and checking if they render as bold text.

Use browser developer tools or a proxy to inspect the reflected input. No specific command needed here; perform manual testing.

**Expected Output**: Input reflected as raw HTML (e.g., bold text appears) without escaping.

### Step 2: Craft and Test WAF Bypass Payload

**Context**: Develop an XSS payload that evades Cloudflare's WAF by using obfuscation techniques like alternative attribute syntax or event handlers. The payload should trigger JavaScript execution upon rendering.

Reference the bypass payload in [[codes/xss-bypass-payload-img-onerror]]. Substitute into your test submission.

**Expected Output**: Payload accepted without WAF block (HTTP 200 response, no captcha or error).

### Step 3: Inject Payload Using curl

**Context**: Submit the crafted payload to the vulnerable endpoint to simulate injection. This verifies execution in a controlled manner before targeting victims.

**Command** ([[commands/curl-inject-xss-payload]]):
```bash
curl -X POST -d "data=$_PAYLOAD" $_TARGET_URL
```

> This command sends the obfuscated XSS payload to the form endpoint. Replace $_PAYLOAD with the encoded string from the code snippet and $_TARGET_URL with the vulnerable form's action URL (e.g., https://target.com/search). Monitor the response for successful injection without WAF triggering.

**Expected Output**: Server response containing the injected HTML (e.g., 200 OK with reflected payload in body). If testing in a browser, load the page and check for alert() popup or console errors indicating execution.

### Step 4: Verify Execution and Exfiltration

**Context**: Confirm the payload executes by observing JavaScript behavior, such as an alert box or cookie theft via a beacon to an attacker-controlled server.

Load the page with the injected payload in a browser. For exfiltration, modify the payload to send document.cookie to your server.

**Expected Output**: JavaScript executes (e.g., alert fires) or network request to attacker server with stolen data.

**Success Indicators**:
- No WAF block or captcha challenge during submission.
- Payload renders and executes without errors in the browser console.
