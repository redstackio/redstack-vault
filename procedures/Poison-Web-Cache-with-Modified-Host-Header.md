---
tags:
  - web-cache-poisoning
  - host-header-injection
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/grep]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
commands:
  - '[[commands/curl-poison-host-header-loop]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: a96f3079-ef08-4faa-9b67-39157b6c7658
created_at: '2025-12-13T09:00:34.739Z'
updated_at: '2025-12-13T09:00:34.739Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
---
# Poison Web Cache with Modified Host Header

## Summary

This procedure poisons a web cache by repeatedly sending HTTP requests with a manipulated Host header that includes an arbitrary closed port, causing the cache to store and serve responses with invalid links that lead to resource failures.

## Description

The attack targets caching mechanisms that reflect the Host header without validation, such as on https://themes.shopify.com. By injecting a closed port like :1337, dynamic content like canonical links becomes poisoned, affecting all users who hit the cached response. This is typically used in web cache poisoning scenarios to achieve Denial of Service.

## Requirements

1. Access to send HTTP requests to the target site
2. Tools: curl and grep installed
3. Knowledge of a closed port (e.g., 1337) on the target

## Defense

Defensive measures and detection strategies:

- Validate and sanitize Host headers in caching logic
- Monitor for anomalous Host headers in logs
- Implement cache key normalization to exclude ports

## Objectives

1. Poison the cache with invalid Host data
2. Ensure poisoned responses are cached and served
3. Lay groundwork for DoS impact

## Instructions

### Step 1: Send Poisoned Requests

**Context**: Repeatedly send GET requests with the modified Host header to force cache poisoning and check for success using grep.

**Command** ([[commands/curl-poison-host-header-loop]]):
```bash
while true; do curl -ik "https://themes.shopify.com:443/?g4mm4=hitthecache" -H "Host: themes.shopify.com:1337"|grep ":1337"; sleep 0;echo 1; done
```

> This loop sends requests ignoring cert errors, sets the Host to include :1337, greps for confirmation, and continues indefinitely until poisoning is observed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Network Denial of Service]]

### Sub-Techniques



## Commands Used

- [[commands/curl-poison-host-header-loop]]

## Tools Used

- [[tools/curl]]
- [[tools/grep]]

## Tags

- web-cache-poisoning
- host-header-injection
