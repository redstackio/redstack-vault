---
tags:
  - xss
  - reflected-xss
  - javascript-injection
  - web-exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/curl-fetch-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:26.548Z'
sub_techniques: []
id: c36905b4-ca15-47f6-a72c-a74a5b53b066
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Inject-JavaScript-Payload-for-Reflected-XSS

## Summary

This procedure exploits a reflected Cross-Site Scripting (XSS) vulnerability by injecting a malicious JavaScript payload into a URL query parameter of a web application, causing the payload to be reflected and executed in the victim's browser without authentication. It demonstrates how failure to encode output allows arbitrary code execution, potentially leading to session hijacking or data theft in sensitive environments like DoD applications.

## Description

In this attack scenario, a web application (e.g., a U.S. Department of Defense portal) processes user-supplied input from URL parameters, such as a redirect URL, without proper output encoding. An attacker crafts a malicious link embedding a URL-encoded script tag (e.g., `<script>alert(origin)</script>`). When a victim clicks the link, the application echoes the payload back into the HTML response, executing the JavaScript in the browser's context. This unauthenticated attack requires no privileges and can be delivered via phishing. Expected outcomes include popup alerts for proof-of-concept or more malicious actions like stealing cookies via `document.cookie`. Prerequisites include knowledge of the vulnerable endpoint and a way to lure victims to the URL.

## Requirements

1. Access to a web browser or command-line tool like curl for testing
2. Knowledge of the vulnerable URL structure, including the injectable parameter (e.g., a redirect param)
3. No authentication; target must be publicly accessible
4. Basic understanding of URL encoding to evade basic filters

## Defense

Defensive measures and detection strategies:

- Implement strict output encoding (e.g., HTML entity encoding) for all user inputs reflected in responses
- Use Content Security Policy (CSP) headers to block inline script execution
- Validate and sanitize URL parameters, whitelisting allowed schemes and rejecting JavaScript URIs
- Monitor web server logs for suspicious query parameters containing encoded script tags
- Deploy Web Application Firewall (WAF) rules to detect common XSS payloads like `<script>` or `alert()`

## Objectives

1. Execute arbitrary JavaScript in the victim's browser to confirm vulnerability
2. Demonstrate potential for stealing session data or sensitive information
3. Highlight risks in unauthenticated web endpoints for high-impact environments

## Instructions

### Step 1: Identify Vulnerable Parameter

**Context**: Analyze the target URL to find injectable query parameters, such as those handling redirects or user input that gets reflected in the page.

No specific command; manually inspect the application or use browser dev tools to test parameters.

### Step 2: Craft and Encode Payload

**Context**: Create a simple JavaScript payload and URL-encode it to bypass basic parsing. Use `alert(origin)` to verify execution without harm.

The payload is `<script>alert(origin)</script>`, encoded as `%3C/script%3E%3Cscript%3Ealert(origin)%3C/script%3E`.

### Step 3: Deliver Payload via URL

**Context**: Append the encoded payload to the vulnerable parameter and load the URL in a browser or fetch via curl to observe reflection.

**Command** ([[commands/curl-fetch-payload]]):
```bash
curl -v "https://███/████=https://████████████/%3C/script%3E%3Cscript%3Ealert(origin)%3C/script%3E&██████" --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

> This command fetches the page with a browser-like User-Agent. Look for the unescaped `<script>` in the HTML response. In a real attack, send the URL to a victim via email or link; upon loading, the alert will fire, confirming execution.

### Step 4: Verify Execution

**Context**: In a browser, load the full URL and check for the alert dialog. For advanced payloads, replace `alert` with code to exfiltrate data (e.g., send cookies to an attacker-controlled server).

Expected output: Alert box displaying the page origin, or network request if exfiltrating data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-payload]]

## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[javascript-injection]]
