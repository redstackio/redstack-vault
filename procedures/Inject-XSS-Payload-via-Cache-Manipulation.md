---
tags:
  - xss
  - web-cache-deception
type: procedure
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-xss-inject]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 59c99125-ada2-4730-a12e-a6b764b80cc0
created_at: '2025-12-13T09:00:34.267Z'
updated_at: '2025-12-13T09:00:34.267Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload via Cache Manipulation

## Summary

This procedure injects a reflected XSS payload into a web page by exploiting cache deception, forcing the cache to store the malicious content for later retrieval.

## Description

By crafting a URL with an XSS payload in a parameter and a fake static extension, the attacker deceives the cache into storing the response. This was applicable to Algolia's platform where improper cache handling allowed script injection, leading to potential client-side exploits.

## Requirements
1. Identified vulnerable endpoint from prior reconnaissance
2. HTTP request tool like Curl
3. Valid XSS payload (e.g., <script>alert('XSS')</script>)

## Defense

Defensive measures and detection strategies:
- Sanitize user inputs to prevent XSS reflection
- Use anti-caching headers on dynamic endpoints
- Log and alert on suspicious query parameters

## Objectives
1. Store malicious XSS in the cache
2. Ensure the payload is reflected in the cached response
3. Prepare for victim execution

## Instructions

### Step 1: Craft and Send Injection Request

**Context**: Append XSS payload to URL parameter and fake extension to trigger caching.

**Command** ([[commands/curl-xss-inject]]):
```bash
curl "https://target.algolia.com/search?query=<script>alert('XSS')</script>/fake.js"
```

> This sends the request, injecting the payload and deceiving the cache.

### Step 2: Confirm Injection

**Context**: Retrieve the response to verify payload presence.

**Command** ([[commands/curl-xss-inject]]):
```bash
curl "https://target.algolia.com/search?query=<script>alert('XSS')</script>/fake.js"
```

> Check if the output includes the unsanitized script tag.

## MITRE ATT&CK Mapping

### Tactics
- [[Execution]]

### Techniques
- [[JavaScript]]

### Sub-Techniques

## Commands Used
- [[commands/curl-xss-inject]]

## Tools Used
- [[tools/Curl]]

## Tags
- xss
- web-cache-deception
