---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: Inject-CRLF-for-Response-Splitting
tags:
  - crlf-injection
  - response-splitting
  - web
type: procedure
tools: []
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
updated_at: '2025-12-14T03:16:30.757Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-CRLF-for-Response-Splitting

## Summary

This procedure exploits CRLF injection vulnerabilities to split HTTP responses, allowing attackers to inject arbitrary headers or content, which can lead to XSS, cache poisoning, or other attacks on web applications like the DoD site.

## Description

CRLF injection occurs when user inputs containing carriage return (CR) and line feed (LF) characters are not sanitized, enabling manipulation of HTTP response structures. In the attack scenario, inputs in URL parameters or forms are used to inject new headers, potentially chaining with XSS for script execution. Prerequisites include a vulnerable endpoint that echoes inputs into responses. Expected outcomes include altered responses that browsers interpret as additional content or scripts, amplifying impact like session manipulation.

## Requirements

1. Proxy tool to intercept and modify requests
2. Knowledge of HTTP protocol and response structure
3. Target endpoint that processes and reflects unsanitized inputs
4. Testing environment to validate splitting without production impact

## Defense

Defensive measures and detection strategies:

- Sanitize all inputs to remove or encode CR (%0D) and LF (%0A) characters
- Validate HTTP response lengths and structures server-side
- Use web application firewalls (WAF) to block suspicious CRLF patterns in requests

## Objectives

1. Split HTTP responses to inject malicious headers or content
2. Chain with XSS for JavaScript execution
3. Enable broader attacks like content spoofing or hijacking

## Instructions

### Step 1: Test for CRLF Vulnerability

**Context**: Probe the target for acceptance of CRLF sequences in inputs.

Submit a test payload like `test%0d%0aX-Test: Injected` in a URL parameter and inspect the response headers for the injected line.

### Step 2: Craft Splitting Payload

**Context**: Build a payload to terminate the original response and inject new content, such as a script.

Example URL:

```url
http://dod-site.com/param=inject%0d%0aHTTP/1.1 200 OK%0d%0aContent-Type: text/html%0d%0a%0d%0a<script>alert('Split!');</script>
```

> This attempts to end the legitimate response and start a new one with embedded script.

### Step 3: Deliver and Observe

**Context**: Send the payload via a crafted request and monitor for successful splitting.

Use a proxy to send the request; check browser rendering for injected content execution.

> Expected output: Response shows split headers, and script executes if chained with XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[crlf-injection]]
- [[response-splitting]]
- [[web]]
