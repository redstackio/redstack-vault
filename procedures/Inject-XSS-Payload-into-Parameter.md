---
tags:
  - xss-injection
  - payload
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/inject-xss-payload-img-onerror]]'
  - '[[commands/inject-xss-payload-domain]]'
  - '[[commands/modified-post-request-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:19.871Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e0a8e68b-e0c2-4deb-998a-3a4e42740ff1
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Parameter

## Summary

This procedure modifies the intercepted POST request by injecting a URL-encoded XSS payload into the redacted parameter, bypassing the '=' filter to enable JavaScript execution upon reflection.

## Description

The parameter reflects < and > without filtering but blocks '=', which is bypassed via %3d. Payloads like <img src=x onerror=alert(document.cookie)> target non-HttpOnly cookies. In Burp, edit the request body directly. This leads to arbitrary JS, cookie theft, redirects, and iframe-based phishing in the DoD app context.

## Requirements

1. Intercepted POST request in Burp Suite
2. Knowledge of parameter name (redacted as ██████████)
3. URL encoding tools or manual (%3d for =)

## Defense

Defensive measures and detection strategies:

- Sanitize inputs with htmlspecialchars() in PHP
- Set HttpOnly and Secure flags on cookies
- Implement Content Security Policy (CSP) to block inline JS

## Objectives

1. Insert executable JS payload
2. Ensure encoding bypasses filters
3. Prepare request for triggering without errors

## Instructions

### Step 1: Locate Vulnerable Parameter

**Context**: Identify the target in the request body.

**Command** (Burp Edit):

In Burp, find ██████████=test in the body.

> Parameter highlighted. Expected output: Original value visible for replacement.

### Step 2: Inject Payload

**Context**: Replace with XSS using [[commands/inject-xss-payload-img-onerror]] or alternative [[commands/inject-xss-payload-domain]].

**Command** ([[commands/modified-post-request-xss]]):
```http
POST /██████_█████████ HTTP/1.1
Host: ████
...
21__Click=0&activeFlag=Y&%25%25Surrogate_██████=1&██████████=<img src%3dx onerror%3dalert(document.cookie)>
```

> Edit body in Burp Inspector. Expected output: Payload encoded, request syntax valid.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/inject-xss-payload-img-onerror]]
- [[commands/inject-xss-payload-domain]]
- [[commands/modified-post-request-xss]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xss-injection
- payload
