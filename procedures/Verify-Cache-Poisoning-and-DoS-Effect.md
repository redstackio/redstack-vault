---
id: proc-uuid-004
tags:
  - verification
  - dos
  - cache-check
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/Legitimate-GET-Request-to-CDN-File]]'
verified: false
platforms:
  - Web
  - CDN
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:26:56.676Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Verify-Cache-Poisoning-and-DoS-Effect

## Summary

This procedure tests the success of cache poisoning by requesting the original legitimate URL (with cache buster) and confirming it now serves the cached 404, validating the DoS impact on static asset access.

## Description

Post-poisoning, access the normalized URL in the browser or via Burp. The CDN serves the cached 404 instead of the file, disrupting JavaScript and other assets. Applies to Shopify domains; outcome confirms vulnerability exploitation without needing further tools beyond browser/Burp.

## Requirements

1. Successful cache poisoning from prior procedure
2. Browser or Burp Suite for request
3. Cache buster parameter to match test context

## Defense

Defensive measures and detection strategies:

- Shorten cache TTL for error responses
- Implement cache key inclusion of full path without normalization
- Alert on increased 404 rates for static assets

## Objectives

1. Confirm legitimate requests hit poisoned cache
2. Observe DoS effect on file access
3. Validate attack across affected services

## Instructions

### Step 1: Request Original URL

**Context**: Access the legitimate path with cache buster to check for poisoned response.

**Command** ([[commands/Legitimate-GET-Request-to-CDN-File]]):
```http
GET /static/javascripts/vendor/bugsnag.v7.4.0.min.js?cachebuster=123 HTTP/1.1
Host: cdn.shopify.com
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
```

> In browser, visit https://cdn.shopify.com/static/javascripts/vendor/bugsnag.v7.4.0.min.js?cachebuster=123. Or send via Burp. Expected output: Cached 404 error page, not the JS file.

### Step 2: Confirm Impact

**Context**: Verify broader DoS potential by noting affected services.

> Check multiple files or domains (e.g., shopify-assets.shopifycdn.com). Success if 404 persists until cache clears.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/Legitimate-GET-Request-to-CDN-File]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- verification
- dos
- cache-check
