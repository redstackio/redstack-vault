---
id: proc-uuid-6
tags:
  - verification
  - impact
type: procedure
tools:
  - '[[tools/Safari-Browser]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:27:49.658Z'
skill_level: basic
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Verify-Account-Modification-on-CS-Money

## Summary

This procedure checks the victim's account to confirm the CSRF succeeded, observing changes like email update.

## Description

Post-exploitation, navigate to the personal info page to inspect modifications, validating the site's lack of protections across endpoints.

## Requirements

1. Original authenticated tab
2. Successful form submission

## Defense

Defensive measures and detection strategies:

- Email notifications on changes
- Audit logs for POST requests without tokens

## Objectives

1. Confirm unauthorized action
2. Assess impact scope
3. Identify further exploitable endpoints

## Instructions

### Step 1: Return to Authenticated Session

**Context**: Switch back to the login tab.

No command; navigate to original tab.

> Expected: Session still active.

### Step 2: Check Personal Info

**Context**: Inspect updated fields.

Navigate to https://new.cs.money/th/csgo/personal-info.

> Expected: Email shows nnez+attacker@wearehackerone.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Safari-Browser]]

## Tags

- verification
- impact
