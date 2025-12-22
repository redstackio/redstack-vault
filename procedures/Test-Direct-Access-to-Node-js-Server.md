---
tags:
  - testing
  - direct-access
  - node-js
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-get-root-direct]]'
  - '[[commands/curl-get-admin-direct]]'
  - '[[commands/curl-get-forbidden-direct]]'
platforms:
  - Web
  - Node.js
techniques: []
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 27204b0b-8143-4dda-b5ad-f0c8327300a1
created_at: '2025-12-13T09:01:17.112Z'
updated_at: '2025-12-13T09:01:17.112Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
---
# Test Direct Access to Node.js Server

## Summary

This procedure tests direct HTTP access to the Node.js server's endpoints to verify baseline responses without proxy interference.

## Description

By sending GET requests directly to port 8081, this confirms the server's normal behavior: returning 'INDEX' for /, 'ADMIN' for /admin, and 'FORBIDDEN' for /forbidden. This step is crucial for contrasting with proxy-mediated access.

## Requirements

1. Node.js server running on localhost:8081
2. curl installed
3. Local network access

## Defense

Defensive measures and detection strategies:

- Monitor HTTP traffic for unusual endpoint access
- Implement rate limiting on sensitive endpoints

## Objectives

1. Verify server responses
2. Establish baseline for direct access
3. Prepare for proxy comparison

## Instructions

### Step 1: Test Root Endpoint

**Context**: Send GET to root.

**Command** ([[commands/curl-get-root-direct]]):
```bash
curl http://localhost:8081
```

> Expects 'INDEX' response.

### Step 2: Test Admin Endpoint

**Context**: Send GET to /admin.

**Command** ([[commands/curl-get-admin-direct]]):
```bash
curl http://localhost:8081/admin
```

> Expects 'ADMIN' response.

### Step 3: Test Forbidden Endpoint

**Context**: Send GET to /forbidden.

**Command** ([[commands/curl-get-forbidden-direct]]):
```bash
curl http://localhost:8081/forbidden
```

> Expects 'FORBIDDEN' response.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques



### Sub-Techniques



## Commands Used

- [[commands/curl-get-root-direct]]
- [[commands/curl-get-admin-direct]]
- [[commands/curl-get-forbidden-direct]]

## Tools Used

- [[tools/curl]]

## Tags

- [[testing]]
- [[direct-access]]
- [[node-js]]
