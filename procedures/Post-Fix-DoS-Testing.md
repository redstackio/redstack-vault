---
id: proc-post-fix-testing-001
tags:
  - post-fix
  - slow2-php
  - cache-bypass
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/uuidgen]]'
  - '[[tools/PHP]]'
  - '[[tools/nginx]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-slow2-dos-launch]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:26:48.928Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Post-Fix-DoS-Testing

## Summary

This procedure tests DoS resilience after partial fixes by using slow2.php (4kB every 4s for 624s) and random query strings to bypass caching, confirming if long pendings and large downloads persist.

## Description

After initial fixes, create slow2.php for adjusted timing; append ?$(uuidgen) to URLs to disable CDN. Launch curls; verify logs show ~624s responses. Final full fix limits to 8s.

## Requirements

1. Updated PHP scripts ([[procedures/Create-Slow-Response-PHP-Script]] variant)
2. Proxy URLs post-embedding

## Defense

Defensive measures and detection strategies:

- Dynamic query string handling in caching
- Comprehensive timeout enforcement
- Query parameter normalization

## Objectives

1. Bypass partial mitigations like caching
2. Validate remaining vulnerabilities
3. Confirm fix effectiveness

## Instructions

### Step 1: Create slow2.php

**Context**: Adjust for post-fix (smaller chunks, shorter sleeps).

Create /var/www/html/slow2.php similar to slow.php but 4kB every 4s, 156 iterations (624s total), HTTP 500.

> Expected output: ~640kB total sent over 10min+.

### Step 2: Launch with Cache Bypass

**Context**: Use uuidgen for unique queries.

Execute [[commands/curl-slow2-dos-launch]] 3-50 times:

```bash
curl https://camo.stream.highwebmedia.com/ec276c9fdbd7f4ae273a2b7f02d0bef651aebadd/█████████?$(uuidgen) > /dev/null &
```

> Expected output: Requests pend ~624s; no caching.

### Step 3: Verify Logs Post-Test

**Context**: Check nginx for confirmation.

Use [[procedures/Verify-and-Monitor-DoS-Impact]]; expect 500, 640kB, 624s.

### Step 4: Final Fix Verification

**Context**: After full fix, retest.

Relaunch; expect ~8s timeouts, no excessive backend.

> Expected output: Quick failures, no long pendings.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/curl-slow2-dos-launch]]

## Tools Used

- [[tools/curl]]
- [[tools/uuidgen]]
- [[tools/PHP]]
- [[tools/nginx]]

## Tags

- post-fix
- cache-bypass
