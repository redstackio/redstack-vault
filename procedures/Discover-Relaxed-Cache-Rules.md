---
tags:
  - cache
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 43fb606d-de63-46e7-8ebc-b372edd52902
created_at: '2025-12-13T09:00:34.635Z'
updated_at: '2025-12-13T09:00:34.635Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover Relaxed Cache Rules

## Summary

This procedure discovers relaxed cache rules on /Award/ and /List/ endpoints where the cache assumes all pages are static.

## Description

Involves analyzing caching behavior to identify endpoints treated as static, enabling potential poisoning. Target environment includes CDNs with misconfigured rules. Expected outcome is confirmation of static caching.

## Requirements

1. Access to target endpoints.
2. Ability to inspect HTTP headers.
3. Understanding of cache mechanisms.

## Defense

Defensive measures and detection strategies:

- Implement strict cache keys including dynamic parameters.
- Monitor cache hit ratios for anomalies.

## Objectives

1. Identify static caching assumptions.
2. Prepare for poisoning exploitation.
3. Document cache behavior.

## Instructions

### Step 1: Inspect Cache Headers

**Context**: Send requests to /Award/ and /List/ and examine responses.

> Look for Cache-Control: public, max-age indicating static caching.

### Step 2: Test Cache Hits

**Context**: Repeat requests to confirm caching.

> Send identical requests and check for cache hits.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[cache]]
- [[web]]
