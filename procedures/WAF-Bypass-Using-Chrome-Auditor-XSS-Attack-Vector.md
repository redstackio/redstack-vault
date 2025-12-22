---
id: 6f1c0fcf-cf44-4821-9280-d00f2c0a27c7
name: WAF-Bypass-Using-Chrome-Auditor-XSS-Attack-Vector
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:43.457340+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - '[[sub-techniques/JavaScript|T1059.007 - JavaScript]]'
tags:
  - '[[tags/Chrome Auditor - 9th August 2018]]'
  - '[[tags/Common WAF Bypass]]'
  - '[[tags/Cross Site Scripting]]'
  - xss
  - waf-bypass
commands:
  - '[[commands/curl-inject-xss-payload]]'
platforms:
  - Web
tools: []
validated: true
---

# WAF-Bypass-Using-Chrome-Auditor-XSS-Attack-Vector

## Summary

This procedure demonstrates how to bypass Web Application Firewall (WAF) protections by injecting a specially crafted Cross-Site Scripting (XSS) payload known as the Chrome Auditor XSS Attack Vector. The payload exploits weaknesses in signature-based WAF detection to execute arbitrary JavaScript in a victim's browser, enabling actions like stealing session cookies or performing unauthorized operations.

## Description

Web Application Firewalls (WAFs) often rely on signature-based detection to block common XSS payloads, but obfuscated or cleverly encoded variants like the Chrome Auditor vector can evade these rules. This technique targets web applications vulnerable to reflected or stored XSS, where user input is not properly sanitized. The attacker identifies an injection point (e.g., a search field or URL parameter), injects the payload, and tricks a victim into interacting with the tainted page. Upon execution, the JavaScript runs in the victim's browser context, allowing access to sensitive data like cookies, local storage, or DOM manipulation. This is particularly effective against WAFs like ModSecurity or Cloudflare when the payload avoids common blacklisted patterns. The target environment is typically a modern web application running on HTTP/HTTPS with client-side rendering.

## Requirements

1. Network access to the target web application (e.g., via browser or proxy).
2. Identification of a reflected or stored XSS injection point (e.g., through manual testing or tools like Burp Suite).
3. Knowledge of the application's input fields or URL parameters that accept user input without sanitization.
4. A listening server or method to capture exfiltrated data (e.g., for cookie theft).

## Defense

Defensive measures and detection strategies:

- Implement a WAF with behavior-based anomaly detection alongside signatures, monitoring for unusual JavaScript execution patterns.
- Enforce Content Security Policy (CSP) headers to restrict inline script execution and external resource loading.
- Sanitize and encode all user inputs server-side using libraries like OWASP ESAPI, and validate on the client-side.
- Perform regular vulnerability scans with tools like OWASP ZAP or Nessus, and conduct penetration testing focused on XSS.
- Enable browser security features like XSS Auditor (deprecated in Chrome) or modern alternatives, and log client-side errors for review.

## Objectives

1. Evade WAF signature detection to inject an XSS payload.
2. Execute JavaScript in the victim's browser context.
3. Collect sensitive information such as session tokens or perform actions on the victim's behalf.

## Instructions

### Step 1: Identify XSS Injection Point

**Context**: Locate a vulnerable input field or parameter in the web application where user-supplied data is reflected back without proper escaping. This could be a search box, URL query parameter, or form field. Test basic payloads like `<script>alert(1)</script>` to confirm vulnerability, noting if the WAF blocks it.

Use manual testing in a browser or intercept with a proxy to probe endpoints.

### Step 2: Prepare the Chrome Auditor XSS Payload

**Context**: Use the obfuscated payload to bypass WAF filters. This payload closes an existing script tag, injects an SVG element with an embedded script, and uses URL encoding to evade detection.

Reference the payload code: [[codes/Chrome-Auditor-XSS-WAF-Bypass-Payload]]

The payload is: `</script><svg><script>alert(1)-%26apos;%3B`

Customize if needed (e.g., replace `alert(1)` with exfiltration code like `document.cookie` sent to an attacker server).

**Expected Output**: A ready-to-inject string that, when successful, executes without triggering WAF blocks.

### Step 3: Inject the Payload via HTTP Request

**Context**: Deliver the payload to the vulnerable endpoint. For reflected XSS, append it to a URL parameter; for forms, submit via POST. Use tools like curl for automated testing or a browser for manual injection.

**Command** ([[commands/curl-inject-xss-payload]]):
```bash
curl -X POST -d "search=$_PAYLOAD" http://target.com/vulnerable-endpoint
```

> This command sends the XSS payload in a POST request to a search endpoint. Replace `$_PAYLOAD` with the encoded Chrome Auditor vector. If the WAF bypass succeeds, the response will contain the injected script, which executes when rendered in a browser.

**Expected Output**: HTTP response (200 OK) with the reflected payload in the HTML body, without WAF error pages (e.g., 403 Forbidden). In a browser, this triggers the alert or exfiltration.

### Step 4: Verify Execution and Exfiltrate Data

**Context**: Load the tainted page in a victim's browser context (e.g., via phishing link) and confirm execution. Monitor for data theft, such as incoming requests to your server with stolen cookies.

Visit the URL with the injected payload in a browser, or simulate with a tool like Selenium for automation.

**Expected Output**: JavaScript execution (e.g., alert popup) or network request to attacker server containing sensitive data like `document.cookie`.

**Success Indicators**:
- No WAF block (response code 200, no error messages).
- Script executes in browser (alert fires or data is exfiltrated).
- Captured data confirms access to victim session.
