---
id: proc-uuid-001
tags:
  - race-condition
  - web
  - setup
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:18.792Z'
skill_level: intermediate
impact_level: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare-Invitation-for-Race-Condition-Test

## Summary

This procedure sets up a test invitation in a web-based team management system, such as HackerOne, to prepare for exploiting a race condition in the acceptance process.

## Description

In the context of testing for race conditions in invitation handling, this step involves creating or selecting an existing invitation for a test team. The invitation generates a unique token stored in a SQL database, which is later vulnerable to concurrent consumption. This is typically done via the platform's UI, requiring basic user access to a team admin or owner role. Expected outcome is an active invitation ready for multiple acceptance attempts, highlighting the lack of immediate token invalidation.

## Requirements

1. Access to a web platform with team invitation features (e.g., HackerOne)
2. Valid user account with permission to create invitations (e.g., team admin)
3. Web browser for navigation

## Defense

Defensive measures and detection strategies:

- Implement row-level locking on token tables during lookups and deletions
- Use atomic operations for token consumption to prevent races
- Monitor for unusual spikes in invitation acceptances from the same token

## Objectives

1. Generate a valid invitation token for testing
2. Ensure the token is in an active state in the database
3. Prepare for concurrent exploitation without alerting the system

## Instructions

### Step 1: Navigate to Team Management

**Context**: Access the section where invitations can be created to set up the test environment.

**Instructions**: Log in to the platform using [[tools/Web-Browser]] and go to the team dashboard for a test team (e.g., 'test22').

> No specific command; perform via UI: Click 'Manage Team' > 'Invitations' > 'Create New Invitation'.

### Step 2: Create the Invitation

**Context**: Generate the token that will be targeted in the race condition.

**Instructions**: Enter details for the invitation (e.g., invitee email if required, but use a generic one for testing) and submit to create the token.

> UI Action: Fill form and click 'Send Invitation' or 'Generate Link'. Copy the invitation URL containing the token.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- race-condition
- web
- setup
