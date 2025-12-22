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
  - '[[commands/get-malformed-http-version-2]]'
platforms:
  - Web
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1c6d8333-e8b4-4f6d-af38-2518a4cb9546
created_at: '2025-12-13T09:00:34.366Z'
updated_at: '2025-12-13T09:00:34.366Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Verify Cached Poisoned Response

## Summary

This procedure verifies web cache poisoning by sending a follow-up request to the same path and checking if the cached 400 error is served instead of the expected response.

## Description

After poisoning the cache, a normal or slightly varied request to the same path should return the cached error, confirming the vulnerability. In the context of the U.S. Department of Defense website, this step showed that a request expecting a 404 returned the poisoned 400, validating the DoS potential.

## Requirements

1. Prior cache poisoning on the target path
2. Network access to the target
3. Tool to send HTTP requests

## Defense

Defensive measures and detection strategies:

- Use cache keys that include request validation factors
- Regularly purge or invalidate caches for error-prone paths
- Log and alert on repeated error responses from cache

## Objectives

1. Confirm cache poisoning success
2. Validate DoS impact
3. Prepare for escalation to real pages

## Instructions

### Step 1: Send Verification Request

**Context**: Send a similar request to check the cache.

**Command** ([[commands/get-malformed-http-version-2]]):
```bash
GET /yeettest?yeettest=1 HTTP/1.123456
```

> This command tests if the cache serves the poisoned 400 response.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques



## Commands Used

- [[commands/get-malformed-http-version-2]]

## Tools Used



## Tags

- [[web-cache-poisoning]]
- [[dos]]
