---
id: proc-uuid-005
tags:
  - cache-poisoning
  - xss-payload
  - dot-segments
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:55.826Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Endpoint Denial of Service]]'
---
# Construct-Payload-with-Dot-Segments-to-Poison-Cache

## Summary

This procedure builds and delivers a payload using dot segments to exploit parser confusion, poisoning the cache with XSS from /Job/ and survey pages under /List/ and /Award/, converting reflected XSS to stored for ~10 minutes.

## Description

By appending `/../` to static paths pointing to XSS-vulnerable dynamic pages, the frontend caches the malicious response under the static path, serving it to all users until TTL expires, enabling DoS via repeated poisoning.

## Requirements

1. Prior identification of XSS and parser issues
2. Knowledge of cache TTL
3. Payload encoding for evasion

## Defense

Defensive measures and detection strategies:

- Normalize URLs consistently and validate cache keys
- Block or sanitize dot segments in paths
- Implement rate limiting on cache-influencing requests

## Objectives

1. Craft hybrid URL for mismatch exploitation
2. Inject and cache XSS payload
3. Achieve stored XSS execution for victims

## Instructions

### Step 1: Build Payload URL

**Context**: Combine dot segments with XSS endpoint.

Construct: `https://target.com/Award/../Job/?param=<script>alert(document.cookie)</script>` with cookie XSS.

Send via curl:

```bash
curl -v -b "jobcookie=<img src=x onerror=alert(1)>" "https://target.com/Award/../Job/?param=<img src=x onerror=alert(1)>"
```

> Frontend caches under /Award/, backend executes /Job/ XSS.

### Step 2: Validate Poisoning

**Context**: Confirm cache serves payload.

Request /Award/ from another IP; check for XSS execution or source.

**Expected Output**: Cached response includes executable script.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Impact]] Impact

### Techniques

- [[JavaScript]] JavaScript
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- None specific

## Tags

- payload-construction
- stored-xss-conversion
