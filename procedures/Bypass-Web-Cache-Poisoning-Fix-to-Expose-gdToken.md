---
id: p-bypass-cache-poisoning-gdtoken
tags:
  - web-cache-poisoning
  - csrf-exposure
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/cache-poisoning-token-exposure]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:56:03.754Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Web-Cache-Poisoning-Fix-to-Expose-gdToken

## Summary

This procedure exploits a web cache poisoning vulnerability by appending .js to URLs, bypassing a prior fix and causing the cache to store responses containing sensitive Anti-CSRF tokens (gdToken) that are then served across different pages to unauthorized users.

## Description

In the Glassdoor application, a previous attempt to fix web cache poisoning failed because the cache system treated URLs with .js extensions as static files, leading to improper caching of dynamic responses. By crafting requests to endpoints like /job-listing/011.js?jl=1007452474740, attackers can force a 200 OK response that includes the gdToken, which gets cached and exposed to other users. This enables CSRF attacks or further exploitation. The target environment is a web app behind Cloudflare, where cache controls were insufficient.

## Requirements

1. Access to a proxy tool like Burp Suite for request crafting.
2. Network connectivity to the target domain (e.g., glassdoor.com).
3. Knowledge of job listing IDs or similar parameters to construct valid URLs.

## Defense

Defensive measures and detection strategies:

- Implement Cloudflare Web Cache Armor to validate cache keys.
- Add explicit Cache-Control: no-store headers to sensitive responses.
- Monitor for anomalous requests with unusual file extensions on dynamic paths.

## Objectives

1. Cache a response containing the gdToken using poisoned URLs.
2. Expose the token to unauthorized users via shared cache.
3. Enable downstream attacks like CSRF bypass.

## Instructions

### Step 1: Craft Poisoned URL Request

**Context**: Identify a dynamic endpoint and append .js to trick the cache into treating it as a static asset, forcing inclusion of session-specific data like gdToken.

**Command** ([[commands/cache-poisoning-token-exposure]]):
```bash
curl -X GET "https://www.glassdoor.com/job-listing/011.js?jl=1007452474740" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -v
```

> This sends a GET request to the manipulated URL, resulting in a 200 OK response. The gdToken appears in the response body. Check verbose output (-v) for cache headers confirming storage.

### Step 2: Verify Cache Poisoning

**Context**: Access the URL from a different browser or IP to confirm the poisoned cache serves the sensitive token.

**Command** ([[commands/cache-poisoning-token-exposure]]):
```bash
curl -X GET "https://www.glassdoor.com/job-listing/011.js?jl=1007452474740" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -v
```

> Expected output includes the gdToken in the body, identical to the initial request, indicating successful poisoning.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/cache-poisoning-token-exposure]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- web-cache-poisoning
- csrf-exposure
