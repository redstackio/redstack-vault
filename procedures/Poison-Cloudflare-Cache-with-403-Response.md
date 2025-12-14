---
id: proc-uuid-1
tags:
  - cache-poisoning
  - dos
  - cloudflare
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-poison-cache]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:56.244Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Poison-Cloudflare-Cache-with-403-Response

## Summary

This procedure crafts an HTTP request with an invalid Authorization header to trigger a 403 Forbidden from Azure Blob Storage, which Cloudflare caches, poisoning the cache for subsequent requests to static files on downloads.exodus.com.

## Description

In scenarios where static assets like file hashes or installers are served via Cloudflare CDN backed by Azure Blob Storage, the absence of proper cache validation allows attackers to poison cache entries with error responses. By including an invalid Authorization header in a request to a public resource, Azure rejects it with 403, and Cloudflare mistakenly caches this error, denying service to legitimate users until the cache expires. This affects paths like /releases/hashes-exodus-21.2.12.txt and can extend to other cached resources.

## Requirements

1. Network access to the target subdomain (e.g., downloads.exodus.com)
2. Tool capable of sending custom HTTP headers (e.g., curl)
3. Knowledge of the target file path and cache-buster parameters if used

## Defense

Defensive measures and detection strategies:

- Configure Cloudflare to exclude error status codes (e.g., 4xx, 5xx) from caching via Page Rules or Cache Rules
- Implement origin validation to prevent caching of unauthorized responses
- Monitor for anomalous 403 responses in access logs and cache hit rates

## Objectives

1. Trigger and cache a 403 error response in Cloudflare
2. Establish a poisoned cache entry for a specific resource path
3. Achieve temporary DoS on file downloads

## Instructions

### Step 1: Craft and Send Poisoning Request

**Context**: Send a GET request to the target path with an invalid Authorization header to provoke Azure's 403 response, which gets cached by Cloudflare.

**Command** ([[commands/curl-poison-cache]]):
```bash
curl -X GET "https://downloads.exodus.com/releases/hashes-exodus-21.2.12.txt?cachebuster=hackerone" -H "Authorization: InvalidBearerToken" -v
```

> This command issues the request with a bogus Authorization header, causing Azure to return 403 Forbidden. Cloudflare caches it due to misconfiguration. Expected output includes HTTP/1.1 403 Forbidden and cache headers like CF-Cache-Status: MISS (initially, but subsequent requests hit cache).

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-poison-cache]]

## Tools Used


## Tags

- [[cache-poisoning]]
- [[dos]]
- [[cloudflare]]
