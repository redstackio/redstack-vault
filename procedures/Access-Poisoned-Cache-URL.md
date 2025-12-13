---
tags:
  - cache-poisoning
  - xss
  - discourse
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/get-request-with-cache-deception]]'
platforms:
  - Web
  - AWS
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 45d1888a-9260-492d-bdf2-7362c38816db
created_at: '2025-12-13T09:00:34.558Z'
updated_at: '2025-12-13T09:00:34.558Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Access Poisoned Cache URL

## Summary

This procedure involves navigating to the poisoned cache URL to trigger the cached response containing the injected XSS payload in a Discourse instance.

## Description

After poisoning the cache, accessing the specified URL serves the malicious response, which includes unsanitized data from the X-Forwarded-Host header injected into font URLs, leading to XSS execution.

## Requirements

1. Poisoned cache URL from previous step
2. Web browser

## Defense

Defensive measures and detection strategies:

- Monitor for anomalous cache hits or unexpected parameters
- Use cache keys that include security-relevant headers

## Objectives

1. Retrieve the poisoned cached page
2. Prepare for XSS trigger
3. Validate cache poisoning success

## Instructions

### Step 1: Navigate to Cached URL

**Context**: Open the URL displayed by the poisoning script to load the cached response.

**Command** ([[commands/get-request-with-cache-deception]]):
```bash
GET /?xx HTTP/1.1
```

> This simulates the request to the poisoned endpoint, appending an arbitrary parameter for cache deception. Expected output: HTTP response with injected XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/get-request-with-cache-deception]]

## Tools Used



## Tags

- [[cache-poisoning]]
- [[xss]]
