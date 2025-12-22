---
tags:
  - caching
  - cloudflare
  - deception
type: procedure
tools:
  - '[[tools/CloudFlare-Proxy]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/curl-get-u-x-css]]'
  - '[[commands/curl-get-u-my-preferences-css]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-14T17:33:24.442Z'
sub_techniques: []
id: 1ee83367-4df7-43d5-bea4-dc31e7833d53
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
---
# Trigger CloudFlare Caching of Dynamic Content via CSS Extension

## Summary

This procedure appends .css to dynamic Discourse routes to force CloudFlare to cache user-specific content as static files, enabling regional cache poisoning for later retrieval.

## Description

CloudFlare caches URLs ending in .css regardless of content type. By requesting /u/x.css or /u/my/preferences.css while authenticated, the response (including CSRF token and username) is cached for the entire CloudFlare region. Repeat requests confirm HIT status.

## Requirements

1. Target behind CloudFlare proxy
2. Attacker authenticated for testing
3. Same-region access for cache population

## Defense

Defensive measures and detection strategies:

- Exclude .css extensions from user routes or add cache-bypass rules in CloudFlare
- Enable cache purging for dynamic content
- Log and alert on cache hits for user paths

## Objectives

1. Populate cache with victim data
2. Verify caching behavior
3. Prepare for taint via victim

## Instructions

### Step 1: Initial Cache Population

**Context**: Issue first request to store dynamic content.

**Command** ([[commands/curl-get-u-x-css]]):
```bash
curl -H "Host: try.discourse.org" "https://try.discourse.org/u/x.css"
```

> Populates cache with 404 page containing token.

### Step 2: Verify Cache Hit

**Context**: Repeat to confirm caching.

**Command** ([[commands/curl-get-u-my-preferences-css]]):
```bash
curl "https://try.discourse.org/u/my/preferences.css"
```

> Second request shows CF-Cache-Status: HIT with user data.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Disable or Modify Tools]]

### Sub-Techniques


## Commands Used

- [[commands/curl-get-u-x-css]]
- [[commands/curl-get-u-my-preferences-css]]

## Tools Used

- [[tools/CloudFlare-Proxy]]

## Tags

- [[caching]]
- [[cloudflare]]
- [[deception]]
