---
tags:
  - xss
  - http-injection
  - injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 44c84eca-9039-4910-b18d-44841e30dd8d
created_at: '2025-12-14T03:15:41.424Z'
updated_at: '2025-12-14T03:15:41.424Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Inject-XSS-Payload-in-HTTP-Method

## Summary

This procedure involves crafting and sending an HTTP request with a malformed method containing an XSS payload to exploit unescaped reflection in server error messages on Gratipay.com.

## Description

The target is the HTTP method handling in the server, where invalid methods are directly included in error responses without HTML escaping. This allows injection of HTML/JS payloads like an <img> tag with an onerror handler. The attack requires a proxy to send arbitrary methods, as browsers enforce standard methods (GET/POST/etc.) in forms and XHR. Successful injection leads to self-XSS execution only in the proxy's browser context, limiting impact.

## Requirements

1. Access to a proxy tool like Burp Suite for custom HTTP methods
2. Network connectivity to gratipay.com
3. Basic knowledge of HTTP requests and XSS payloads

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all user-controlled inputs, including HTTP methods, before inclusion in responses
- Escape HTML entities in error messages (e.g., use &lt; for <)
- Monitor for anomalous HTTP methods in server logs
- Enforce strict HTTP method whitelisting at the web server level (e.g., Cowboy/Erlang configuration)

## Objectives

1. Deliver an XSS payload via HTTP method to trigger reflection
2. Confirm payload execution in a controlled environment
3. Assess vulnerability scope (self-XSS only)

## Instructions

### Step 1: Configure Proxy and Craft Request

**Context**: Set up Burp Suite to intercept and modify outgoing requests, allowing custom HTTP methods.

No specific command; use Burp Suite's Repeater tab to manually set the method to the payload: `<img src="3" onerror="alert(3)"/>` and send a request to `https://gratipay.com/` with a simple GET-like body if needed.

> In Burp Repeater, change the request line to: `<img src="3" onerror="alert(3)"/> https://gratipay.com/ HTTP/1.1` and forward. Expected: 400 response with reflected payload.

### Step 2: Send Request and Intercept

**Context**: Transmit the request through the proxy to the target server.

Use Burp Suite's proxy to route a browser request or directly from Repeater.

> Browser must be configured to use Burp as proxy (e.g., Firefox manual proxy: 127.0.0.1:8080). Attempt a navigation to gratipay.com while intercepting to modify method.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[http-injection]]
