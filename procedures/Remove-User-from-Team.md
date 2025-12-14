---
id: proc-remove-user-team
tags:
  - team-removal
  - access-revocation
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Access Removal]]'
updated_at: '2025-12-14T17:28:20.649Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Access Removal]]'
---
# Remove-User-from-Team

## Summary

This procedure removes a user account from a HackerOne team to test the revocation of access and notifications.

## Description

Using team admin privileges, remove the test account (@lccunha) from the 'Test' team through the management interface. This should ideally sever all associations, but in the vulnerable system, it fails to do so completely for notifications.

## Requirements

1. Admin access to the target team
2. User account targeted for removal
3. Web interface access

## Defense

Defensive measures and detection strategies:

- Log all team membership changes
- Audit removal events for completeness

## Objectives

1. Revoke user access to team
2. Clear associations and subscriptions
3. Simulate departure scenario

## Instructions

### Step 1: Access Team Management

**Context**: Navigate to team settings to initiate removal.

Log in as admin and go to the 'Test' team page, then members section.

> Team dashboard loads with member list.

### Step 2: Execute Removal

**Context**: Select and remove the user.

Choose @lccunha from the list and confirm removal.

> Confirmation message appears, user disappears from list.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Account Access Removal]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[team-removal]]
- [[access-revocation]]
