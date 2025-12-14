---
id: proc-002-remove-user
tags:
  - access-control
  - removal
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-05T00:00:00Z'
techniques:
  - '[[Account Access Removal]]'
updated_at: '2025-12-14T17:28:28.263Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Access Removal]]'
---
# Remove-User-from-Program

## Summary

This procedure removes a user from a HackerOne program, exploiting the flaw where subscriber relationships to reports are not cleared, leaving residual access to notifications.

## Description

Program admins or users can remove membership via the HackerOne UI. However, the backend (Ruby on Rails) fails to delete the User from the Report model's subscribers list in the TeamMember::Destroy interactor, introduced on July 17, 2017. This persists unauthorized notification eligibility.

## Requirements

1. Admin access or self-removal capability in the program
2. Active membership in the target program
3. HackerOne session active

## Defense

Defensive measures and detection strategies:

- Audit subscriber lists on user removal
- Implement cascading deletes for relationships
- Monitor for orphaned subscriptions

## Objectives

1. Revoke program access
2. Preserve subscriber link for leak demonstration
3. Simulate insider departure

## Instructions

### Step 1: Access Program Management

**Context**: Navigate to membership controls.

Log in as admin or user, go to program settings > Members.

### Step 2: Initiate Removal

**Context**: Execute removal without unsubscribing reports.

Select the user and click 'Remove' or 'Leave Program'. Confirm action; no report unsubscribe occurs due to the flaw.

### Step 3: Verify Partial Removal

**Context**: Check that program access is revoked but notifications persist.

Attempt to access program dashboard (should fail) and check subscription status (remains active).

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Account Access Removal]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- access-control
- removal
