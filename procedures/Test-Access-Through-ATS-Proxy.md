---
tags:
  - testing
  - proxy-access
  - ats
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-get-root-proxy]]'
  - '[[commands/curl-get-admin-proxy]]'
  - '[[commands/curl-get-forbidden-proxy]]'
platforms:
  - Web
  - Node.js
techniques: []
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 04016cc2-d0ea-4dcb-b33e-37f6257a84d5
created_at: '2025-12-13T09:01:17.109Z'
updated_at: '2025-12-13T09:01:17.109Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
---
# Test Access Through ATS Proxy

## Summary

This procedure tests HTTP access through the ATS proxy to observe access controls and rerouting behavior.

## Description

Requests to port 8080 go through ATS, where /admin is rerouted to /forbidden, returning 'FORBIDDEN'. This establishes the proxy's control mechanism that the smuggling attack will bypass.

## Requirements

1. ATS proxy running on localhost:8080
2. curl installed
3. Local network access

## Defense

Defensive measures and detection strategies:

- Log proxy requests for anomalies
- Enforce strict access controls in proxy configuration

## Objectives

1. Verify proxy responses
2. Confirm rerouting for restricted paths
3. Set baseline for smuggling exploit

## Instructions

### Step 1: Test Root Endpoint via Proxy

**Context**: Send GET to root through proxy.

**Command** ([[commands/curl-get-root-proxy]]):
```bash
curl http://localhost:8080
```

> Expects 'INDEX' response.

### Step 2: Test Admin Endpoint via Proxy

**Context**: Send GET to /admin through proxy.

**Command** ([[commands/curl-get-admin-proxy]]):
```bash
curl http://localhost:8080/admin
```

> Expects 'FORBIDDEN' due to rerouting.

### Step 3: Test Forbidden Endpoint via Proxy

**Context**: Send GET to /forbidden through proxy.

**Command** ([[commands/curl-get-forbidden-proxy]]):
```bash
curl http://localhost:8080/forbidden
```

> Expects 'FORBIDDEN' response.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques



### Sub-Techniques



## Commands Used

- [[commands/curl-get-root-proxy]]
- [[commands/curl-get-admin-proxy]]
- [[commands/curl-get-forbidden-proxy]]

## Tools Used

- [[tools/curl]]

## Tags

- [[testing]]
- [[proxy-access]]
- [[ats]]
