---
id: proc-verify-removal
tags:
  - verification
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
updated_at: '2025-12-14T17:28:20.643Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify-User-Removal-from-Team

## Summary

This procedure confirms that a user has been successfully removed from a team by checking the member list from an active member's perspective.

## Description

Log in to a current team member account (e.g., @brdoors2) and inspect the 'Test' team members to ensure @lccunha is no longer listed, validating the removal while contrasting with notification persistence.

## Requirements

1. Active team member account
2. Web access to team page
3. Knowledge of removed user

## Defense

Defensive measures and detection strategies:

- Real-time member list updates
- Audit logs for verification discrepancies

## Objectives

1. Confirm access revocation
2. Isolate notification flaw
3. Validate test setup

## Instructions

### Step 1: Log In to Active Account

**Context**: Access the team from a privileged view.

Enter credentials for @brdoors2 and navigate to 'Test' team.

> Dashboard shows current members.

### Step 2: Check Member List

**Context**: Scan for removed user.

Review the members section; @lccunha should be absent.

> List confirms no presence of removed account.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[access-check]]
