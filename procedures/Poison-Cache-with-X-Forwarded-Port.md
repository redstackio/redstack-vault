---
tags:
  - cache-poisoning
  - dos
  - x-forwarded-port
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-poison-x-forwarded-port]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: eb7b850e-f3b1-4032-b26a-321d2ff52f8f
created_at: '2025-12-14T17:26:56.759Z'
updated_at: '2025-12-14T17:26:56.759Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
---
# Poison-Cache-with-X-Forwarded-Port

## Summary

This procedure poisons a web cache by sending a request with an invalid X-Forwarded-Port header value, causing the cache to store a response that redirects to an unreachable port, leading to denial of service for subsequent users.

## Description

In environments using reverse proxies and caching like Varnish on Acquia Cloud with Drupal, the X-Forwarded-Port header is included in the cache key without validation. By setting it to an invalid value like '123', attackers create unique cache entries with poisoned redirects. This affects endpoints like index.php, blocking access until cache expiration (potentially hours). The attack is remote, unauthenticated, and exploits misconfigured header handling in the caching layer.

## Requirements

1. Network access to the target web application (e.g., https://www.hackerone.com)
2. Tool capable of sending custom HTTP headers (e.g., curl)
3. Knowledge of target endpoints (e.g., /index.php?dontpoisoneveryone=1)

## Defense

Defensive measures and detection strategies:

- Strip or validate X-Forwarded-* headers in the caching layer (e.g., Varnish VCL rules to ignore them in cache keys)
- Implement cache key normalization to exclude forwarded headers
- Monitor for unusual header values in access logs and cache hit rates
- Use short cache TTLs for dynamic content

## Objectives

1. Create a poisoned cache entry to disrupt service
2. Demonstrate impact on redirects and page loads
3. Validate vulnerability for reporting

## Instructions

### Step 1: Prepare and Send Poisoned Request

**Context**: Craft a GET request to the target endpoint with the invalid X-Forwarded-Port header to influence the cache key.

**Command** ([[commands/curl-poison-x-forwarded-port]]):
```bash
curl -H 'X-Forwarded-Port: 123' https://www.hackerone.com/index.php?dontpoisoneveryone=1
```

> This command sends a request that the server processes, generating a redirect response to port 123, which gets cached under the poisoned key. Expected output is a successful HTTP response (e.g., 302 redirect), but the cache now serves failures to others.

### Step 2: Verify Poisoning

**Context**: Immediately test a follow-up request without the header to hit the cache.

**Command** ([[commands/curl-poison-x-forwarded-port]] with no header):
```bash
curl https://www.hackerone.com/index.php?dontpoisoneveryone=1
```

> Expect a connection error or failed redirect, confirming the poison.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/curl-poison-x-forwarded-port]]

## Tools Used

- [[tools/curl]]

## Tags

- [[cache-poisoning]]
- [[dos]]
- [[web]]
