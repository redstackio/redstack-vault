---
tags:
  - visibility
  - hidden-users
  - yelp
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
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:30:35.259Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 3d11bcf3-9401-4641-9888-5071f116e8cc
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Verify-Invisible-Users-from-Owner-Perspective

## Summary

This procedure confirms the impact of the privilege escalation by checking that newly invited users are not visible in the account owner's user management interface, allowing hidden unauthorized access.

## Description

Due to a failure in visibility enforcement, users added via the exploited invite feature do not appear in the owner's team list or management page. This procedure involves switching to the owner account and inspecting the user roster, highlighting the persistence risk. It targets the web-based user management section of Yelp Business accounts and requires owner credentials post-invite.

## Requirements

1. Owner account credentials
2. Knowledge of the invited user emails for cross-verification
3. Active browser session or incognito mode to avoid cookie conflicts

## Defense

Defensive measures and detection strategies:

- Synchronize user lists across all roles with real-time updates
- Audit logs for discrepancies between invite actions and visible users
- Require owner approval for all user additions

## Objectives

1. Log in as the account owner and access user management
2. Confirm absence of invited users in the list
3. Validate the hidden access risk

## Instructions

### Step 1: Log In as Owner

**Context**: Switch to the owner account to inspect from an administrative viewpoint.

No command required; log out of the non-owner session, then log in at https://biz.yelp.com/login using owner credentials.

> Dashboard should load with full admin features, including user management.

### Step 2: Inspect User Management

**Context**: Check the team or users page for visibility of unauthorized additions.

No command required; navigate to 'User Management' or 'Team Members', list all users, and search for the invited emails.

> Expected output: List shows only pre-existing users; invited ones are missing, confirming invisibility.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Steal Web Session Cookie]] Steganography (adapted for hidden account visibility)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[invisibility]]
- [[user-management]]
