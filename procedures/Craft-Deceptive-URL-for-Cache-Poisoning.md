---
tags:
  - web-cache-deception
  - exploitation
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-test-cache-behavior]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 19fc0f22-82b2-4f48-b385-e67bba882a23
created_at: '2025-12-13T09:00:33.995Z'
updated_at: '2025-12-13T09:00:33.995Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Deceptive URL for Cache Poisoning

## Summary

This procedure details how to create a specially crafted URL that deceives the web cache into storing a dynamic, authenticated page as a static resource in TikTok Ads.

## Description

By appending a static file extension to a dynamic URL, the cache may treat it as cacheable, poisoning the cache when an authenticated user accesses it. This is based on the reported vulnerability in TikTok Ads.

## Requirements

1. Identified vulnerable endpoint from prior reconnaissance
2. Means to share the URL with an authenticated victim
3. HTTP client for testing

## Defense

Defensive measures and detection strategies:

- Validate URL patterns and reject suspicious extensions on dynamic routes
- Use content-type checks to prevent caching of non-static content

## Objectives

1. Create a cache-poisoning URL
2. Trigger caching via victim interaction
3. Set up for data exfiltration

## Instructions

### Step 1: Construct the URL

**Context**: Append a static extension to the dynamic endpoint.

Modify the URL manually, e.g., change /sensitive-page to /sensitive-page.css.

### Step 2: Test Poisoning

**Context**: Simulate victim access to poison the cache.

**Command** ([[commands/curl-test-cache-behavior]]):

```bash
curl https://ads.tiktok.com/sensitive-page.css -H 'Cookie: authenticated-session-cookie'
```

> This should force the cache to store the response.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-test-cache-behavior]]

## Tools Used



## Tags

- web-cache-deception
- exploitation
