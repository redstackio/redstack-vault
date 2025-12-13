---
tags:
  - social-engineering
  - web-cache-deception
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: fbfb78ba-b634-4d62-8541-55312e8066e2
created_at: '2025-12-13T09:00:34.329Z'
updated_at: '2025-12-13T09:00:34.329Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Lure Victim to Modified URL

## Summary

This procedure involves luring an authenticated victim to visit a modified URL that appends a static extension, triggering the web cache to store authenticated content publicly.

## Description

By appending '/min.js' to the dynamic URL, the server treats it as the base page but the CDN caches it as a static file. This exploits the misconfiguration, allowing authenticated content to be cached without proper headers. The attacker uses social engineering to get the victim to click the link.

## Requirements

1. Authenticated victim session
2. Ability to send lure (e.g., email, message)
3. Web browser for victim

## Defense

Defensive measures and detection strategies:

- Set no-cache headers on dynamic pages
- Validate URL patterns to prevent extension appending

## Objectives

1. Trigger caching of authenticated content
2. Populate public cache with private data
3. Enable unauthorized access

## Instructions

### Step 1: Prepare Modified URL

**Context**: Create the deceptive URL.

Modified URL: https://chaturbate.com/my_collection/min.js

> Share this URL via lure method.

### Step 2: Lure Victim

**Context**: Convince victim to visit the URL while logged in.

Use social engineering to send the link, ensuring victim accesses it in [[tools/Web-Browser]].

> Victim loads the page, caching occurs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Web-Browser]]

## Tags

- social-engineering
- web-cache-deception
