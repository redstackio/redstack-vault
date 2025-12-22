---
tags:
  - web-cache-poisoning
  - http
  - dos
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/get-malformed-http-version-1]]'
platforms:
  - Web
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e4504b24-416e-41c9-95bd-94a16b978ca0
created_at: '2025-12-13T09:00:34.370Z'
updated_at: '2025-12-13T09:00:34.370Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Send Malformed HTTP Request to Poison Cache

## Summary

This procedure involves sending a malformed HTTP request with an invalid version to trigger a 400 Bad Request response on a web server, which is then cached, poisoning the cache for that path and enabling denial of service.

## Description

The attack targets web caches that store error responses without proper validation. By using an invalid HTTP version like HTTP/1.1234567 in a GET request, the server generates a 400 error, which gets cached under the request's key. This affects subsequent legitimate requests to the same path, serving the error instead of the intended content. The procedure was demonstrated on a U.S. Department of Defense website using nginx, leading to DoS for up to 24 hours.

## Requirements

1. Network access to the target web server
2. Ability to send custom HTTP requests (e.g., via curl or similar)
3. Knowledge of cacheable paths on the target

## Defense

Defensive measures and detection strategies:

- Configure caches to exclude error responses (e.g., 4xx codes) from being stored
- Implement request validation to reject malformed HTTP versions before caching
- Monitor for anomalous HTTP requests with invalid versions or large headers

## Objectives

1. Poison the web cache with an error response
2. Disrupt access to the targeted path
3. Enable basis for DoS attacks

## Instructions

### Step 1: Craft and Send Malformed Request

**Context**: Send a GET request to a test path with an invalid HTTP version to trigger the error.

**Command** ([[commands/get-malformed-http-version-1]]):
```bash
GET /yeettest?yeettest=1 HTTP/1.1234567
```

> This command uses an arbitrary test path and invalid version to cause the server to return and cache a 400 response.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques



## Commands Used

- [[commands/get-malformed-http-version-1]]

## Tools Used



## Tags

- [[web-cache-poisoning]]
- [[dos]]
