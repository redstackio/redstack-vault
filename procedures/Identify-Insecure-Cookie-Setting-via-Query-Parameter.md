---
tags:
  - cookie-setting
  - insecure-cookie
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/set-yelpmainpaastacanary-cookie]]'
platforms:
  - Web
techniques:
  - '[[Steal Web Session Cookie]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: faac35a7-7110-4727-aa05-c43f2e1da392
created_at: '2025-12-13T23:56:20.377Z'
updated_at: '2025-12-13T23:56:20.377Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Identify Insecure Cookie Setting via Query Parameter

## Summary

This procedure discovers the ability to set arbitrary cookies via URL query parameters on Yelp domains.

## Description

Appending ?canary=[value] to any *.yelp.com request sets the yelpmainpaastacanary cookie, enabling smuggling of other cookies.

## Requirements

1. Web browser or HTTP client
2. Access to Yelp.com

## Defense

Defensive measures and detection strategies:

- Validate and sanitize query parameters for cookie setting
- Use strict cookie parsing

## Objectives

1. Set test cookie
2. Confirm persistence
3. Identify exploitation potential

## Instructions

### Step 1: Send Request with Canary Parameter

**Context**: Append ?canary= to URL.

Execute [[commands/set-yelpmainpaastacanary-cookie]]:

```bash
https://www.yelp.com/?canary=asdf
```

> Expected: Set-Cookie header in response.

### Step 2: Verify Cookie Set

**Context**: Check browser cookies.

Reload page and inspect cookies for yelpmainpaastacanary=asdf.

> Expected: Cookie present and persistent.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques



## Commands Used

- [[commands/set-yelpmainpaastacanary-cookie]]

## Tools Used



## Tags

- cookie-setting
- insecure-cookie
