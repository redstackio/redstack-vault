---
id: proc-uuid-poison-cache
tags:
  - cache-poisoning
  - web-exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:38.468Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Poison-Cache-by-Requesting-Vulnerable-Endpoint

## Summary

This procedure sends a crafted GET request to a cacheable JavaScript endpoint with a malicious 'hav' cookie, causing the server to cache the response containing the reflected XSS payload, affecting all subsequent users.

## Description

The endpoint `https://www.abritel.fr/annonces/location-vacances/france_midi-pyrenees_46_stcere_dt0.php.js` reflects the 'hav' cookie in a .js file that is cached server-side. Without sanitization, the injected payload persists in cache, turning reflected XSS into stored XSS via poisoning. Targets PHP apps with caching layers.

## Requirements

1. Malicious 'hav' cookie set from prior procedure
2. Ability to send GET requests to the target URL
3. Caching enabled on the server (common in web apps)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all user inputs in cacheable responses
- Use cache keys that include sensitive parameters or disable caching for dynamic content
- Log and alert on cache updates with anomalous content

## Objectives

1. Trigger server to generate and cache poisoned .js response
2. Ensure payload reflection in cached content
3. Persist the exploit for victim access

## Instructions

### Step 1: Prepare the Request

**Context**: Include the poisoned 'hav' cookie in the request headers to the vulnerable URL.

Target URL: `https://www.abritel.fr/annonces/location-vacances/france_midi-pyrenees_46_stcere_dt0.php.js`

Header: `Cookie: hav=xss"</sc"ript><sv"g/onloa"d=aler"t(window.INITIAL_STATE.system.cookie)>`

### Step 2: Send the Request and Verify

**Context**: Issue the GET request and check the response for reflected payload.

Send the request; response should include `var hav="xss"</sc"ript>...>` forming executable XSS.

> Repeat the request without the cookie to confirm cache poisoning: same malicious response served.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- N/A

## Commands Used

- N/A

## Tools Used

- N/A

## Tags

- [[cache-poisoning]]
- [[xss]]
- [[web-cache]]
