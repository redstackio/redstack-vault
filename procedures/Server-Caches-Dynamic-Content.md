---
tags:
  - web-cache-poisoning
  - server-side
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7aaf68ac-c7b5-487b-9509-0dba527f17af
created_at: '2025-12-13T09:00:34.397Z'
updated_at: '2025-12-13T09:00:34.397Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Server Caches Dynamic Content

## Summary

This procedure describes the server-side behavior where dynamic user-specific content is improperly cached as a static resource due to misleading file extensions.

## Description

The vulnerability arises from lack of proper cache validation, treating URLs ending in .css as static files while including logged-in user data like email and member ID in the cached response. This occurs automatically after a logged-in visit.

## Requirements

1. Vulnerable web server with caching enabled
2. Prior trigger from a logged-in user access
3. No direct attacker control needed

## Defense

Defensive measures and detection strategies:

- Use Vary headers and proper Cache-Control directives
- Monitor cache logs for anomalous entries

## Objectives

1. Store sensitive data in cache
2. Enable disclosure to unauthenticated users
3. Exploit caching misconfiguration

## Instructions

### Step 1: Wait for Caching

**Context**: No action required; server handles caching post-trigger.

The cache stores the response without validation, including dynamic data.

> Verify by proceeding to access step.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- web-cache-poisoning
- server-side
