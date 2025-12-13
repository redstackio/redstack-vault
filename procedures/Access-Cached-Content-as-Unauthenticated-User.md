---
tags:
  - information-disclosure
  - unauthenticated-access
type: procedure
tools:
  - '[[tools/Web-Browser]]'
  - '[[tools/Incognito-Mode]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/view-source-cached-url]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: d4b664f8-cd42-459f-9c1b-c006421bf8c3
created_at: '2025-12-13T09:00:34.393Z'
updated_at: '2025-12-13T09:00:34.393Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access Cached Content as Unauthenticated User

## Summary

This procedure involves accessing the poisoned cache as an unauthenticated user to retrieve disclosed sensitive information from the page source.

## Description

After poisoning, any user can access the cached URL in incognito mode to view the original user's data without authentication, exploiting the caching flaw.

## Requirements

1. Knowledge of the crafted URL
2. Web browser with incognito mode
3. Network access to the target

## Defense

Defensive measures and detection strategies:

- Regularly purge caches and implement authentication checks for all resources
- Detect repeated access to non-static URLs

## Objectives

1. Retrieve sensitive user data
2. Confirm successful disclosure
3. Validate attack impact

## Instructions

### Step 1: Access in Incognito Mode

**Context**: Simulate unauthenticated access to serve the cached content.

**Command** ([[commands/view-source-cached-url]]):
```bash
view-source:https://www.lyst.com/LAVFKS53DG.css
```

> This reveals the page source with user information like email and member ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/view-source-cached-url]]

## Tools Used

- [[tools/Web-Browser]]
- [[tools/Incognito-Mode]]

## Tags

- information-disclosure
- unauthenticated-access
