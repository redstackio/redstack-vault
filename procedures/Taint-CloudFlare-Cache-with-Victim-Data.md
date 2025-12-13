---
tags:
  - web-cache-deception
  - cache-tainting
type: procedure
tools:
  - '[[tools/CloudFlare]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/request-non-existent-user-page-css]]'
  - '[[commands/request-page-to-trigger-caching]]'
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 838ad56b-c27a-4131-9d23-98b4c03ff12d
created_at: '2025-12-13T09:00:34.498Z'
updated_at: '2025-12-13T09:00:34.498Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Taint CloudFlare Cache with Victim Data

## Summary

This procedure tricks a signed-in victim into loading Discourse URLs with .css extensions via img tags, tainting the CloudFlare cache with their CSRF token and username for later extraction.

## Description

The attack leverages the lack of no-cache headers on certain Discourse routes, allowing CloudFlare to cache sensitive data when URLs are appended with cacheable extensions like .css. This is used in Web Cache Deception attacks to expose user-specific information.

## Requirements

1. Victim signed into Discourse behind CloudFlare
2. Malicious web page controlled by attacker
3. Same CloudFlare region as victim

## Defense

Defensive measures and detection strategies:

- Add Cache-Control: no-store headers to sensitive routes
- Monitor for unusual .css requests to user routes

## Objectives

1. Taint cache with victim's sensitive data
2. Prepare for data extraction
3. Enable subsequent account takeover steps

## Instructions

### Step 1: Load Malicious Img Tags

**Context**: Victim visits malicious page that loads img src with /u/$rand.css to trigger caching.

**Command** ([[commands/request-non-existent-user-page-css]]):
```bash
GET /u/x.css HTTP/1.1
Host: try.discourse.org
```

> Requests a non-existent user page with .css to expose CSRF in 404 response.

### Step 2: Trigger Caching

**Context**: Request the page multiple times to ensure CloudFlare caches it.

**Command** ([[commands/request-page-to-trigger-caching]]):
```bash
GET /u/x.css HTTP/1.1
```

> Demonstrates caching with CF-Cache-Status: HIT and exposed data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques



## Commands Used

- [[commands/request-non-existent-user-page-css]]
- [[commands/request-page-to-trigger-caching]]

## Tools Used

- [[tools/CloudFlare]]

## Tags

- web-cache-deception
- cache-tainting
