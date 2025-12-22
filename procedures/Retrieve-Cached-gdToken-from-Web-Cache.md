---
tags:
  - web-cache-deception
  - exfiltration
type: procedure
tools:
  - '[[tools/Web-Cache-Deception-Concept]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-fetch-cached-response]]'
platforms:
  - Web
techniques:
  - '[[Steal Web Session Cookie]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: db117710-edb6-4315-bb14-927de883af02
created_at: '2025-12-13T09:00:34.601Z'
updated_at: '2025-12-13T09:00:34.601Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Retrieve Cached gdToken from Web Cache

## Summary

This procedure retrieves the cached response containing the victim's gdToken from the web cache after deception has been triggered.

## Description

Once cached, the attacker can access the static-like URL to fetch the stored data without authentication, extracting the gdToken for further exploitation in Glassdoor attacks.

## Requirements

1. Knowledge of the deceptive URL
2. Access to the web cache (publicly accessible)
3. Prior successful caching by victim

## Defense

Defensive measures and detection strategies:

- Disable caching for sensitive endpoints
- Log and alert on cache retrieval attempts

## Objectives

1. Fetch cached response
2. Extract gdToken value
3. Enable CSRF attacks

## Instructions

### Step 1: Access Cached URL

**Context**: Directly request the cached deceptive URL.

**Command** ([[commands/curl-fetch-cached-response]]):
```bash
curl "https://www.glassdoor.com/dynamic-endpoint.css"
```

> This returns the cached content with gdToken.

### Step 2: Parse for Token

**Context**: Extract the gdToken from the response.

**Command** ([[commands/curl-fetch-cached-response]]):
```bash
curl "https://www.glassdoor.com/dynamic-endpoint.css" | grep "gdToken"
```

> Filters the response for the token.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques



## Commands Used

- [[commands/curl-fetch-cached-response]]

## Tools Used

- [[tools/Web-Cache-Deception-Concept]]

## Tags

- web-cache-deception
- exfiltration
