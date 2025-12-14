---
tags:
  - dos
  - cors
  - wordpress
type: procedure
tools:
  - '[[tools/Browser-JavaScript-Console]]'
  - '[[tools/Fetch-API]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/fetch-wp-json-poison]]'
platforms:
  - Web
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: e2f8bd13-1281-40fb-928a-2c8f84b2dbb6
created_at: '2025-12-14T17:32:48.594Z'
updated_at: '2025-12-14T17:32:48.594Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Verify-DoS-via-Poisoned-CORS-Response

## Summary

This procedure verifies the DoS impact by sending a cross-origin request from a new origin to the poisoned WP-JSON endpoint, observing browser-enforced CORS failure due to mismatched Access-Control-Allow-Origin headers from the cache.

## Description

After cache poisoning, legitimate requests from origins other than the poisoning one receive a cached response with an ACAO header tied to the attacker's Origin. Browsers reject this mismatch, blocking API data access. This affects CORS-dependent consumers like subdomain apps or headless sites. Use a second testing site to trigger the failure, confirming the vulnerability's scope.

## Requirements

1. Poisoned cache from prior procedure
2. Access to a second HTTPS site different from poisoning and target sites
3. Browser console for request execution

## Defense

Defensive measures and detection strategies:

- Implement cache invalidation on ACAO changes
- Use strict Origin validation or static ACAO values
- Log and alert on CORS errors or cache hits with varying Origins

## Objectives

1. Trigger cached poisoned response
2. Observe browser CORS policy enforcement
3. Confirm DoS for unrelated cross-origin requests

## Instructions

### Step 1: Switch to New Testing Site

**Context**: Use a site with a different Origin to simulate a legitimate consumer hitting the poison.

**Command** ([[commands/fetch-wp-json-poison]]):
```javascript
fetch('https://target.wordpress.com/wp-json/?dontreallypoison1').then(res => res.json()).then(json => console.log(json));
```

> The request hits the cache (X-Cache: HIT). The ACAO will match the poisoning Origin, not the current site's.

### Step 2: Observe Failure

**Context**: Check console and network for CORS block.

**Command** ([[commands/fetch-wp-json-poison]]):
```javascript
fetch('https://target.wordpress.com/wp-json/?dontreallypoison1').then(res => res.json()).then(json => console.log(json));
```

> Expect a CORS error: "Access-Control-Allow-Origin does not match the requesting origin". No JSON is processed, denying API access.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/fetch-wp-json-poison]]

## Tools Used

- [[tools/Browser-JavaScript-Console]]
- [[tools/Fetch-API]]

## Tags

- dos
- cors
- wordpress
