---
tags:
  - stored-xss
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-http-smuggling]]'
  - '[[commands/burp-request-manipulation]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 15af3786-3677-47eb-b3cb-29a25eede8fc
created_at: '2025-12-11T06:10:28.688Z'
updated_at: '2025-12-11T06:10:28.688Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Inject Stored XSS Payload via Cached Response

## Summary

This procedure injects a stored XSS payload into a poisoned cache, causing arbitrary script execution when users access the affected page.

## Description

Stored XSS stores malicious scripts in the server's response, which are executed in the user's browser. In this attack, it's achieved via cache poisoning on PayPal's sign-in page, interfering with page integrity.

## Requirements

1. Poisoned cache from prior steps
2. XSS payload crafting knowledge
3. Request manipulation tool

## Defense

- Implement Content Security Policy (CSP)
- Sanitize and validate cached content

## Objectives

1. Embed XSS in cached response
2. Achieve script execution on access
3. Disrupt sign-in functionality

## Instructions

### Step 1: Inject XSS Payload

**Context**: Modify the cached response to include XSS.

Execute [[commands/burp-request-manipulation]] to inject:

```bash
POST /signin HTTP/1.1\r\nHost: paypal.com\r\nContent-Length: 0\r\n\r\nHTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<script>alert('XSS')</script>
```

> This stores the payload in the cache.

### Step 2: Test Execution

**Context**: Verify the XSS triggers.

Load the page in a browser and observe script execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

## Commands Used

- [[commands/burp-request-manipulation]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[stored-xss]]
- [[web]]
