---
tags:
  - web-cache-deception
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-cache-behavior]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6b7d9d58-93a4-4ff3-bcf2-d8dfa69b1ca0
created_at: '2025-12-13T09:00:34.001Z'
updated_at: '2025-12-13T09:00:34.001Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Cacheable Endpoints in TikTok Ads

## Summary

This procedure involves scanning and testing endpoints in the TikTok Ads platform to identify those that are cacheable due to misconfigurations, setting the stage for web cache deception attacks that could lead to information leakage.

## Description

Web cache deception exploits how caches handle requests by treating dynamic pages as static resources. In TikTok Ads, this can occur if caching rules are not strictly enforced, allowing authenticated content to be cached. The procedure requires access to the public-facing TikTok Ads service and focuses on observing HTTP headers to detect caching behavior.

## Requirements

1. Access to the internet and TikTok Ads URLs
2. Basic HTTP client like curl
3. Optional: Authenticated session cookies for testing differences

## Defense

Defensive measures and detection strategies:

- Implement strict Cache-Control headers (no-cache, no-store) on sensitive endpoints
- Monitor for anomalous URL patterns with static extensions on dynamic pages

## Objectives

1. Identify endpoints vulnerable to caching
2. Confirm differences in cached vs. non-cached responses
3. Prepare for cache poisoning

## Instructions

### Step 1: Test Endpoint Caching

**Context**: Send requests to various TikTok Ads endpoints and inspect headers for caching indicators.

**Command** ([[commands/curl-test-cache-behavior]]):

```bash
curl -I https://ads.tiktok.com/example-endpoint -H 'User-Agent: Mozilla/5.0'
```

> This command retrieves headers; look for Cache-Control or X-Cache to determine if the response is cached.

### Step 2: Compare Authenticated Responses

**Context**: Repeat the test with authenticated cookies to see if sensitive data is cached.

**Command** ([[commands/curl-test-cache-behavior]]):

```bash
curl -I https://ads.tiktok.com/sensitive-endpoint -H 'Cookie: authenticated-session-cookie'
```

> Compare outputs to identify potential leakage points.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-test-cache-behavior]]

## Tools Used



## Tags

- web-cache-deception
- reconnaissance
