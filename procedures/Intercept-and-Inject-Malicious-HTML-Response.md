---
id: uuid-proc-3
name: Intercept-and-Inject-Malicious-HTML-Response
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.548Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Adversary-in-the-Middle]]'
sub_techniques: []
tags:
  - xss
  - mitm
  - html-injection
commands: []
platforms:
  - Windows
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---

# Intercept-and-Inject-Malicious-HTML-Response

## Summary

This procedure uses a MITM proxy to intercept the error response from the invalid URI and injects malicious HTML payload, exploiting the lack of sanitization in the Nextcloud client's alert box to enable local file execution.

## Description

Burp Suite intercepts the HTTP request/response for the invalid server URI. The response body is modified to include HTML tags that, when rendered, execute local files via file:// links. This leverages the client's elevated permissions (akin to Internet Explorer's local zone) to bypass confirmations, targeting Windows systems for arbitrary code execution like launching calc.exe.

## Requirements

1. Burp Suite running and configured as the system's proxy
2. Invalid URI request triggered from the client
3. Knowledge of target local file paths (e.g., C:/WINDOWS/system32/calc.exe)

## Defense

Defensive measures and detection strategies:

- Detect proxy interception via certificate pinning or HSTS enforcement
- Log and alert on anomalous HTTP responses in client traffic

## Objectives

1. Successfully modify the error response with XSS payload
2. Ensure HTML is unsanitized and executable in the alert context
3. Prepare for automatic local file invocation

## Instructions

### Step 1: Intercept the Request

**Context**: Capture the outgoing HTTP request to the invalid URI using Burp.

Configure browser/system proxy to 127.0.0.1:8080 (Burp default) and submit the URI.

> Request appears in Burp's Proxy tab for interception.

### Step 2: Modify Response Body

**Context**: Inject HTML payload into the 403 response body.

In Burp Repeater or Interceptor, edit the response to include: <html><body><A HREF="file:///C:/WINDOWS/system32/calc.exe">CALC.EXE</A></body></html>

> Forward the modified response to the client.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xss
- mitm
- html-injection
