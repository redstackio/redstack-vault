---
tags:
  - web-cache-deception
  - web
type: procedure
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-cache-test]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: f9f96722-2c7f-4085-bc80-3dd605f85f70
created_at: '2025-12-13T09:00:34.270Z'
updated_at: '2025-12-13T09:00:34.270Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable Endpoint for Cache Deception

## Summary

This procedure identifies web endpoints vulnerable to cache deception by testing how the server handles caching of dynamic content disguised as static files, potentially leading to security issues like XSS.

## Description

Web cache deception occurs when an attacker tricks a caching mechanism into storing dynamic pages as static resources by appending file extensions. This is tested on platforms like Algolia by sending manipulated requests and checking cache headers. The goal is to find endpoints where improper caching allows malicious content to be stored and served.

## Requirements
1. Access to the target web application over HTTP/HTTPS
2. Tool for sending HTTP requests (e.g., Curl)
3. Knowledge of the application's URL structure

## Defense

Defensive measures and detection strategies:
- Implement strict Cache-Control headers to prevent caching of dynamic content
- Monitor for unusual URL patterns with fake extensions in access logs

## Objectives
1. Confirm if the endpoint caches manipulated requests
2. Identify potential for injecting malicious payloads
3. Document caching behavior for further exploitation

## Instructions

### Step 1: Test Caching Behavior

**Context**: Send requests with appended fake extensions to dynamic URLs and inspect headers.

**Command** ([[commands/curl-cache-test]]):
```bash
curl -I "https://target.algolia.com/dynamic-page/fake.css"
```

> This checks if the response is cacheable; look for headers like 'Cache-Control: public' or 'Age' indicating a cache hit.

### Step 2: Verify Cache Persistence

**Context**: Send follow-up requests to confirm if the content is served from cache.

**Command** ([[commands/curl-cache-test]]):
```bash
curl -I "https://target.algolia.com/dynamic-page/fake.css"
```

> Repeat the request and check for increasing 'Age' header to confirm caching.

## MITRE ATT&CK Mapping

### Tactics
- [[Initial Access]]

### Techniques
- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used
- [[commands/curl-cache-test]]

## Tools Used
- [[tools/Curl]]

## Tags
- web-cache-deception
- web
