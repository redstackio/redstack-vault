---
id: proc-verify-ui
tags:
  - ui-validation
  - access-check
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:51.668Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify-UI-Access-Restrictions

## Summary

This procedure checks that UI elements for admin actions are hidden or inaccessible after role downgrade in the Omise dashboard.

## Description

As the downgraded user, refresh or revisit https://dashboard.omise.co/v2/links to confirm enforcement of access controls at the frontend level. Admin features like create/edit links should no longer be visible. This validates UI-side restrictions while setting up for backend bypass testing. Outcome: Restricted UI view confirmed.

## Requirements

1. Downgraded user session active
2. Access to links page
3. Recent role change

## Defense

Defensive measures and detection strategies:

- Ensure UI reflects backend roles in real-time
- Use client-side checks backed by server validation
- Log access attempts to restricted UI

## Objectives

1. Confirm UI enforcement post-downgrade
2. Highlight potential backend/UI mismatch
3. Validate test setup for replay

## Instructions

### Step 1: Refresh Dashboard

**Context**: Reload the session to apply role changes.

No specific command; refresh browser or re-login as downgraded user.

> Session persists with updated role.

### Step 2: Check Links Page Access

**Context**: Attempt to view admin features.

No specific command; navigate to https://dashboard.omise.co/v2/links.

> Edit/add options hidden or return permission error.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ui-validation
- access-check
