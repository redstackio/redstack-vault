---
id: proc-verify-avatar-001
name: Verify-Avatar-Change
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.479Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Gather Victim Host Information]]'
sub_techniques: []
tags:
  - verification
  - privacy-violation
  - rocket-chat
commands: []
platforms:
  - Web
tools: []
skill_level: basic
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---

# Verify-Avatar-Change

## Summary

This procedure confirms the success of the avatar upload exploit by refreshing the client-side view in Rocket.Chat, ensuring the unauthorized change is visible and persisted.

## Description

After invoking ufsImportURL, the change may not immediately appear due to caching. This step involves clearing caches and reloading to validate the privacy violation. Target: Rocket.Chat web client. Prerequisites: Completed upload step and access to the targeted user's profile. Outcomes: Visual confirmation of the new avatar, demonstrating the access control bypass.

## Requirements

1. Access to the Rocket.Chat web interface
2. Browser with developer tools for cache management
3. Knowledge of the targeted user's profile

## Defense

Defensive measures and detection strategies:

- Implement client-side validation for avatar changes
- Monitor for rapid profile modifications
- Use cache headers to prevent unauthorized reloads

## Objectives

1. Validate exploit success through UI observation
2. Assess impact on user privacy
3. Document evidence for reporting

## Instructions

### Step 1: Clear Browser Cache

**Context**: Remove cached assets to force a fresh load of user data.

Use browser dev tools: Network tab > Disable cache, or hard refresh (Ctrl+Shift+R).

> Cache cleared, preventing stale avatar display.

### Step 2: Reload User Profile

**Context**: Navigate to the targeted user's profile to check for the new avatar.

No command; refresh the page or search for the user and view their avatar.

> The uploaded image appears as the user's avatar, confirming the exploit.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- verification
- privacy-violation
- rocket-chat
