---
tags:
  - cache-poisoning
  - cors
  - wordpress
type: procedure
tools:
  - '[[tools/Browser-JavaScript-Console]]'
  - '[[tools/Fetch-API]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/fetch-wp-json-poison]]'
platforms:
  - Web
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 01a7c7b7-2a8f-48c7-8660-6b55448a510c
created_at: '2025-12-14T17:32:48.598Z'
updated_at: '2025-12-14T17:32:48.598Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Poison-WP-JSON-Cache-with-Arbitrary-Origin

## Summary

This procedure poisons the edge cache of WordPress.com's WP-JSON API by sending cross-origin requests with a custom Origin header, causing the API to echo it into the Access-Control-Allow-Origin response header. The cache stores this without keying on Origin, allowing the poison to affect unrelated requests.

## Description

The WP-JSON API on WordPress.com supports broad CORS by reflecting the request's Origin header in the ACAO response. However, edge caches (e.g., those with X-Cache headers) do not include Origin in their cache keys, enabling poisoning. From a different HTTPS site, execute fetch requests to /wp-json/ with a unique query parameter. Repeating 5-10 times ensures propagation across cache layers. This sets up DoS for subsequent cross-origin API consumers, such as subdomain integrations or headless CMS setups, by serving mismatched ACAO headers.

## Requirements

1. Browser with developer console access on a non-target HTTPS site
2. Target WordPress.com site with WP-JSON API (e.g., https://target.wordpress.com/wp-json/)
3. No authentication; public endpoint access

## Defense

Defensive measures and detection strategies:

- Key caches on Origin header to prevent poisoning
- Validate and whitelist allowed Origins in ACAO responses instead of echoing
- Monitor for unusual Origin headers in logs and cache hits with mismatched ACAO

## Objectives

1. Embed custom Origin in cached ACAO header
2. Propagate poison across edge cache backends
3. Prepare for DoS on legitimate cross-origin requests

## Instructions

### Step 1: Open Testing Site and Console

**Context**: Access a site different from the target to simulate a cross-origin request with a custom Origin.

**Command** ([[commands/fetch-wp-json-poison]]):
```javascript
fetch('https://target.wordpress.com/wp-json/?dontreallypoison1').then(res => res.json()).then(json => console.log(json));
```

> This sends a GET request to the WP-JSON endpoint. The browser automatically sets the Origin header to the testing site's domain. Check the Network tab for the response ACAO matching this Origin and X-Cache: MISS on first run.

### Step 2: Repeat to Ensure Caching

**Context**: Execute multiple times to fill caches across distributed backends.

**Command** ([[commands/fetch-wp-json-poison]]):
```javascript
fetch('https://target.wordpress.com/wp-json/?dontreallypoison1').then(res => res.json()).then(json => console.log(json));
```

> Run 5-10 times. On subsequent runs, expect X-Cache: HIT, confirming the poisoned response is cached with the custom ACAO.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/fetch-wp-json-poison]]

## Tools Used

- [[tools/Browser-JavaScript-Console]]
- [[tools/Fetch-API]]

## Tags

- cache-poisoning
- cors
- wordpress
