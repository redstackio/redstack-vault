---
tags:
  - information-disclosure
  - web-cache-deception
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/browser-access-url]]'
platforms:
  - Web
techniques:
  - '[[Data from Cloud Storage]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 10cae67c-e11b-43be-b5de-b159e768eeb1
created_at: '2025-12-13T09:00:34.323Z'
updated_at: '2025-12-13T09:00:34.323Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Cloud Storage]]'
---
# Access Cached Content Unauthenticated

## Summary

This procedure allows an attacker to retrieve cached authenticated content without credentials by accessing the publicly stored static file.

## Description

After the victim has triggered caching, the attacker visits the modified URL in an unauthenticated session, retrieving the exposed data. This demonstrates the impact of web cache deception, leading to disclosure of tokens and personal information.

## Requirements

1. Knowledge of the cached URL
2. Web browser in incognito mode or alternative
3. No authentication needed

## Defense

Defensive measures and detection strategies:

- Configure CDN to not cache based on extensions alone
- Implement cache poisoning prevention

## Objectives

1. Retrieve exposed data
2. Confirm vulnerability exploitation
3. Access tokens and personal info

## Instructions

### Step 1: Access Cached URL

**Context**: Open the URL in an unauthenticated browser session.

Use [[tools/Web-Browser]] in incognito mode to visit https://chaturbate.com/my_collection/min.js.

Execute [[commands/browser-access-url]]:

```bash
curl https://chaturbate.com/my_collection/min.js
```

> The response includes the victim's authenticated content.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Cloud Storage]]

### Sub-Techniques



## Commands Used

- [[commands/browser-access-url]]

## Tools Used

- [[tools/Web-Browser]]

## Tags

- information-disclosure
- web-cache-deception
