---
id: proc-uuid-1
name: Create-Test-Accounts-and-Invite-Users
tags:
  - account-creation
  - setup
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:29:36.547Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Create-Test-Accounts-and-Invite-Users

## Summary

This procedure sets up multiple test accounts on developers.mtn.com and establishes team invitations to simulate legitimate team structures for subsequent IDOR testing.

## Description

In the context of exploiting an IDOR in the team management system, initial setup involves creating three distinct accounts (A, B, C) with fictional 4-digit user_ids and team_ids. Account A invites B to its team, and Account B invites C to its team. This creates a chain of relationships that allows interception of a removal action. The target environment is the web-based developers.mtn.com platform, requiring only basic registration access. Expected outcomes include confirmed team memberships, enabling the capture of parameterized removal requests.

## Requirements

1. Access to developers.mtn.com registration page
2. Valid email addresses for account verification
3. Browser for manual interactions

## Defense

Defensive measures and detection strategies:

- Rate-limit account creations to prevent abuse
- Monitor for rapid multi-account registrations from similar IPs
- Require CAPTCHA on signup to deter automation

## Objectives

1. Establish authenticated test users with team affiliations
2. Prepare for legitimate request interception
3. Ensure IDs are in the vulnerable 4-digit format

## Instructions

### Step 1: Register Test Accounts

**Context**: Create three accounts to represent different users and teams.

Navigate to developers.mtn.com and register Account A (user_id=1111, team_id=0001), Account B (user_id=1112, team_id=0002), and Account C (user_id=1113, team_id=0003). Verify each via email.

> Note: IDs are assigned by the system; use these fictional values for illustration based on observed patterns.

### Step 2: Perform Invitations

**Context**: Build team relationships to enable removal actions.

Log in to Account A and use the invite feature to add B to Team A. Log out, log in to Account B, and invite C to Team B. Confirm additions in the team dashboard.

> Expected: Success messages or updated team rosters.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[External Remote Services]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-creation
- setup
