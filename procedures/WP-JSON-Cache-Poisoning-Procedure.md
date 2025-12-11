---
id: cc0c0c43-45c2-4e56-9d50-51ac7b161bdc
name: WP-JSON Cache Poisoning Procedure
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:15.354Z'
updated_at: '2025-12-11T06:10:15.354Z'
tactics:
  - '[[Impact]]'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
sub_techniques:
  - '[[Application or System Exploitation]]'
tags:
  - cache-poisoning
  - cors
  - dos
  - wordpress
commands:
  - '[[commands/fetch-wp-json-poison]]'
platforms:
  - Web
  - WordPress.com
tools:
  - '[[tools/Browser-JavaScript-Console]]'
  - '[[tools/fetch-API]]'
  - '[[tools/publicwww.com]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0040]]'
mitre_techniques:
  - '[[T1499]]'
  - '[[T1190]]'
---

# WP-JSON Cache Poisoning Procedure

## Summary

This procedure exploits a cache poisoning vulnerability in the WP-JSON API on WordPress.com sites by sending requests with arbitrary Origin headers, which are echoed back and cached, leading to CORS failures and denial of service for legitimate cross-origin requests.

## Description

The attack targets the WP-JSON API endpoints where the Access-Control-Allow-Origin header echoes the request's Origin without validation, and responses are cached without keying on the Origin. By poisoning the cache from one origin and testing from another, CORS checks fail, causing DoS for services relying on cross-origin access, such as headless WordPress frontends. This was discovered through testing CORS behavior on cached responses.

## Requirements

1. Access to a web browser with JavaScript console
2. Multiple HTTPS websites for different origins
3. Target WordPress.com site with exposed WP-JSON API

## Defense

Defensive measures and detection strategies:

- Implement proper cache keying on Origin headers in edge caches
- Validate and whitelist allowed Origins in CORS configurations
- Monitor for unusual cache hit rates or repeated requests with varying Origins

## Objectives

1. Poison the cache with a mismatched Origin
2. Trigger CORS failures on subsequent requests
3. Achieve denial of service for cross-origin API access

## Instructions

### Step 1: Open External HTTPS Site

**Context**: Initiate from a different origin to set up CORS triggering.

Use any external HTTPS site (e.g., https://nathandavison.com) to open the browser JavaScript console.

> Prepares the environment for cross-origin requests.

### Step 2: Execute Poisoning Fetch Requests

**Context**: Send requests to poison the cache with the current Origin.

**Command** ([[commands/fetch-wp-json-poison]]):
```javascript
fetch('https://██████████.com/wp-json/?dontreallypoison1').then(res => res.json()).then(json => console.log(json))
```

> Execute multiple times to ensure the response is cached with the echoed Origin header.

### Step 3: Switch to Another Origin and Fetch

**Context**: Test the poisoned cache from a new origin.

**Command** ([[commands/fetch-wp-json-poison]]):
```javascript
fetch('https://██████████.com/wp-json/?dontreallypoison1').then(res => res.json()).then(json => console.log(json))
```

> Attempts to access the cached response from a different origin.

### Step 4: Observe CORS Failure

**Context**: Confirm the DoS by checking for CORS errors.

In the browser console, note the error due to mismatched Access-Control-Allow-Origin header.

> Browser blocks the response, resulting in denial of service.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques

- [[Application or System Exploitation]]

## Commands Used

- [[commands/fetch-wp-json-poison]]

## Tools Used

- [[tools/Browser-JavaScript-Console]]
- [[tools/fetch-API]]

## Tags

- [[cache-poisoning]]
- [[cors]]
- [[dos]]
- [[wordpress]]
