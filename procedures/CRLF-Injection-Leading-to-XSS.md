---
tags:
  - crlf-injection
  - xss
  - header-manipulation
type: procedure
tools:
  - '[[tools/Chrome]]'
  - '[[tools/Firefox]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:24.288Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e89c1547-3e5a-4bd6-816c-1e22c9acd014
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# CRLF-Injection-Leading-to-XSS

## Summary

This procedure exploits a CRLF injection vulnerability in a URL query parameter to inject custom HTTP headers and response body content, disabling security headers like X-XSS-Protection and injecting an XSS payload that executes arbitrary JavaScript in the victim's browser, such as alerting the document domain for proof-of-concept or stealing session data.

## Description

In the context of the Starbucks staging site (stagecafrstore.starbucks.com), the vulnerability arises from insufficient sanitization of URL query parameters, allowing attackers to embed CRLF (%0d%0a) sequences. These are interpreted by the server as HTTP header separators, enabling the injection of headers (e.g., Location for redirects, Content-Type: text/html, X-XSS-Protection: 0) and direct insertion of HTML/script into the response body. When a victim accesses the crafted URL, the server issues a 301 redirect with the manipulated response, executing the XSS payload. This can lead to session hijacking, cookie theft, or further client-side attacks. Prerequisites include browser access to the target site; no server-side access is needed.

## Requirements

1. Web browser with developer tools (e.g., Chrome or Firefox) for payload testing and network inspection
2. Direct HTTP access to the vulnerable endpoint (http://stagecafrstore.starbucks.com/?)
3. Knowledge of URL encoding for CRLF sequences (%0d%0a)

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to strip or block CRLF characters in query parameters
- Use HTTP response splitting prevention libraries or WAF rules to detect and block anomalous header injections
- Enable and enforce Content Security Policy (CSP) and X-XSS-Protection headers to mitigate XSS even if injection occurs
- Monitor server logs for unusual 301 redirects or response sizes indicating injection attempts

## Objectives

1. Manipulate HTTP response to bypass security headers and inject malicious content
2. Execute JavaScript in the context of the target domain for data exfiltration
3. Demonstrate potential for session hijacking or phishing via stolen credentials

## Instructions

### Step 1: Identify Vulnerable Parameter

**Context**: Test the URL query parameter for CRLF injection susceptibility by appending encoded newlines and observing server response behavior.

No specific command; use browser address bar or developer console to input test payloads like ?param=test%0d%0aHeader: Value and inspect the network tab for header reflection.

> If the server echoes the injection without sanitization, proceed to payload crafting. Expected output: Response headers include the injected "Header: Value".

### Step 2: Craft Injection Payload

**Context**: Build a payload that injects multiple headers to control the redirect and disable protections, followed by an XSS script in the body.

Construct the URL manually:

```url
http://stagecafrstore.starbucks.com/?param=%0d%0aLocation:%20javascript:alert(document.domain)%0d%0aContent-Type:%20text/html%0d%0aX-XSS-Protection:%200%0d%0a%0d%0a<script>alert('XSS via CRLF')</script>
```

> This injects a Location header pointing to a javascript: URI for direct script execution, sets Content-Type to HTML, disables XSS protection, and adds a script tag. Expected output: Upon access, the browser executes the alert without blocking.

### Step 3: Trigger and Verify Execution

**Context**: Access the crafted URL in the browser to trigger the vulnerable response and confirm XSS execution.

Navigate to the payload URL in Chrome or Firefox.

> Inspect the network response to verify injected headers and body. Expected output: JavaScript alert displays the document domain, confirming domain-context execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome]]
- [[tools/Firefox]]

## Tags

- [[crlf-injection]]
- [[xss]]
- [[web]]
