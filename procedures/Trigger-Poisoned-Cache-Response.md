---
tags:
  - cache-poisoning
  - dos
  - cache-hit
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Network Denial of Service]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: b13ee76c-0262-40b5-8d8b-ad527707f42b
created_at: '2025-12-14T17:26:56.748Z'
updated_at: '2025-12-14T17:26:56.748Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Trigger-Poisoned-Cache-Response

## Summary

This procedure triggers the retrieval of a poisoned cache entry to observe the denial of service effect, confirming how legitimate users are impacted by the cache poisoning.

## Description

After poisoning the cache, normal requests to the same URL will hit the cached response, which includes a redirect to an invalid port (e.g., 123). This causes connection failures in browsers or clients, simulating DoS for all users until the cache clears. No special tools are needed beyond a standard browser or HTTP client, making it easy to verify the attack's persistence.

## Requirements

1. Prior cache poisoning (e.g., via X-Forwarded-Port)
2. Access to a browser or HTTP client
3. Same network as the initial poison request

## Defense

Defensive measures and detection strategies:

- Enable cache bypassing for suspicious requests
- Log and alert on high failure rates from cached redirects
- Regularly purge caches on anomaly detection
- Validate redirect ports server-side

## Objectives

1. Confirm DoS impact on unauthenticated users
2. Measure persistence of the poison
3. Document evidence for vulnerability reports

## Instructions

### Step 1: Access Target in Browser

**Context**: Simulate a legitimate user by loading the URL without custom headers, triggering a cache hit.

**Command** (Browser or curl):
```bash
# Or simply open in browser: https://www.hackerone.com/index.php?dontpoisoneveryone=1
curl https://www.hackerone.com/index.php?dontpoisoneveryone=1
```

> The browser will attempt to connect to the invalid port, resulting in a 'connection refused' or timeout error. Curl may show a similar failure.

### Step 2: Validate Site-Wide Impact

**Context**: Test other redirects or pages to check if the poison affects broader site functionality.

**Command** (Test redirect):
```bash
curl -L https://www.hackerone.com
```

> Expect failures in chained redirects due to shared cache behavior.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[cache-poisoning]]
- [[dos]]
