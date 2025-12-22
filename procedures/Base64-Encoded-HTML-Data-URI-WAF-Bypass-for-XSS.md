---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: Base64-Encoded-HTML-Data-URI-WAF-Bypass-for-XSS
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - waf-bypass
  - xss
  - base64-encoding
  - incapsula
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Base64-Encoded-HTML-Data-URI-WAF-Bypass-for-XSS

## Summary

This procedure demonstrates a Web Application Firewall (WAF) bypass technique using Base64-encoded HTML content embedded in a data URI within an HTML 'object' tag. The encoded payload evades WAF inspection that targets plaintext malicious scripts, allowing execution of Cross-Site Scripting (XSS) attacks on vulnerable web applications, such as those protected by Incapsula WAF.

## Description

Web Application Firewalls (WAFs) often block direct injections of malicious HTML or JavaScript, such as <script>alert(1)</script>, by inspecting request payloads for known patterns. This technique encodes the malicious HTML using Base64 and embeds it into a data URI scheme (data:text/html;base64,... ) assigned to the 'data' attribute of an HTML 'object' tag. The WAF sees only the encoded string and harmless tag structure, passing the request through. On the client-side, the browser decodes and renders the content, executing the XSS payload. This is particularly effective against WAFs that do not perform Base64 decoding during inspection. The attack targets reflected or stored XSS vectors, such as search fields, user inputs, or comment sections, enabling attackers to steal session cookies, perform keylogging, or redirect users to phishing sites. In a real-world scenario, this could compromise user accounts on e-commerce or corporate portals protected by Incapsula.

## Requirements

1. Access to a vulnerable web application endpoint that reflects or stores user input without proper sanitization (e.g., a search parameter or form field).
2. A WAF (e.g., Incapsula) configured to block common XSS patterns but not decoding Base64 data URIs.
3. Basic knowledge of Base64 encoding and HTML structure.
4. Tools for testing, such as a browser developer console or proxy like Burp Suite to craft and send requests.
5. Target application must support rendering of HTML 'object' tags in the context of the injection point.

## Defense

- Configure WAF rules to detect and block Base64-encoded data URIs in user inputs, using regex patterns like /data\:text\/html;base64,[A-Za-z0-9+\/=]+/i.
- Implement Content Security Policy (CSP) headers to restrict inline scripts, data URIs, and object embeddings (e.g., object-src 'none').
- Perform client-side and server-side input validation, including decoding and scanning encoded content before rendering.
- Regularly update WAF signatures to handle encoding-based evasions and monitor for anomalous object tag usage in logs.
- Use Web Vulnerability Scanners (e.g., OWASP ZAP) to test for such bypasses during security assessments.

## Objectives

1. Evade WAF detection by encoding malicious HTML payloads in Base64.
2. Inject and execute XSS via the 'object' tag data URI to trigger alerts or steal data.
3. Demonstrate the limitations of plaintext-only WAF inspections in preventing client-side attacks.

## Instructions

### Step 1: Prepare the Malicious Payload

**Context**: Identify the XSS payload to execute, such as a simple alert for testing or a more advanced script for data exfiltration. Encode it in Base64 to obfuscate from WAF inspection. This step ensures the payload is ready for embedding without triggering signature-based blocks.

Encode your desired HTML/script using a Base64 encoder. For example, the string '<script>alert(1)</script>' becomes 'PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=='.

> This encoding prevents the WAF from matching plaintext keywords like 'alert' or '<script>'. Use online tools or command-line base64 for generation, but verify the output manually.

### Step 2: Construct the Object Tag Payload

**Context**: Build the HTML 'object' tag using the data URI scheme to embed the Base64-encoded content. The multiple semicolons (;;;) in the data URI add further obfuscation, exploiting lenient parsers.

Use the following structure, referencing the code snippet [[codes/Object-Tag-Base64-Encoded-XSS-Payload]]:

```html
<object data='data:text/html;;;;;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=='></object>
```

> The 'object' tag is chosen because it can render arbitrary data URIs as HTML without strict validation in many contexts. Customize the Base64 part for your payload. Test in a local HTML file first to confirm rendering.

### Step 3: Inject and Test the Payload

**Context**: Deliver the payload to the target application via a vulnerable input point, such as a reflected search parameter (e.g., ?q=<payload>) or a form submission. Intercept with a proxy if needed to ensure proper encoding in transit.

Submit the payload to the endpoint. For example, in a URL: http://target.com/search?q=<object data='data:text/html;;;;;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=='></object>. Observe the response in the browser.

> If the WAF blocks it, iterate by adjusting the URI (e.g., add more semicolons or use different MIME types). Success is confirmed if the page renders the object and executes the script without WAF intervention.

### Step 4: Verify Execution and Impact

**Context**: Confirm the bypass worked by checking for payload execution, such as a popup alert or network requests to an attacker-controlled domain. This validates the technique and assesses potential impact.

In the browser console, inspect for errors or use developer tools to monitor script execution. For advanced payloads, check server logs or exfiltrated data.

> Look for indicators like no WAF block messages and successful client-side rendering. If failed, the WAF may have updated rules—fallback to other encodings like URL or HTML entities.
