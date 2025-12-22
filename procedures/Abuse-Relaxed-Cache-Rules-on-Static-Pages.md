---
id: p-relaxed-cache-rules
tags:
  - cache-poisoning
  - relaxed-caching
  - static-pages
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-check-cache-headers]]'
verified: false
platforms:
  - Web
  - CDN
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:55.696Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Abuse Relaxed Cache Rules on Static Pages

## Summary

This procedure confirms and abuses relaxed caching on /Award/ and /List/ endpoints, where pages are treated as static without strict Vary rules, allowing poisoning with dynamic malicious content.

## Description

Glassdoor's CDN caches these paths for ~10 minutes assuming static nature, ignoring variations in queries or cookies. This enables injecting XSS via mismatched requests. Targets include CDNs with loose policies.

## Requirements

1. Access to cached endpoints
2. Ability to inspect HTTP headers
3. Multiple request capability to test caching

## Defense

Defensive measures and detection strategies:

- Add Vary: * or specific headers to cache keys
- Set shorter TTL for potentially dynamic pages
- Monitor cache hit rates for anomalies

## Objectives

1. Validate static caching assumption
2. Confirm lack of strict rules
3. Enable poisoning preparation

## Instructions

### Step 1: Inspect Cache Headers

**Context**: Request the page to check caching directives.

**Command** ([[commands/curl-check-cache-headers]]):
```bash
curl -I "https://glassdoor.com/Award/some-award" -v
```

> Look for Cache-Control: public, max-age=600 without Vary.

### Step 2: Test Cache Persistence

**Context**: Send multiple requests to verify caching without variation enforcement.

**Command** ([[commands/curl-check-cache-headers]]):
```bash
curl -I "https://glassdoor.com/Award/some-award?test=1" -v
```

> Success if same cache serves varied request.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-check-cache-headers]]

## Tools Used


## Tags

- cache-abuse
