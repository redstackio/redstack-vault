---
tags:
  - setup
  - steam
  - forums
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
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:29:56.675Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: c369af37-b089-43e3-a417-f12a2d1a95e9
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Prepare-Steam-Forum-for-IDOR-Testing

## Summary

This procedure sets up a controlled environment in Steam Community group forums to test the IDOR vulnerability, including configuring permissions and creating test discussions with deleted comments.

## Description

In the Steam Community platform, group admins can create forums with custom permissions. This procedure involves logging in as an admin, setting member-only view access without deleted comment visibility, and non-member denial. A discussion is then created with comments, some of which are deleted, to simulate real-world conditions for IDOR exploitation. This preparation is essential to verify the vulnerability's impact on data access controls.

## Requirements

1. Admin access to a Steam group with forum creation privileges
2. Valid Steam account for setup
3. Web browser for navigation and configuration

## Defense

Defensive measures and detection strategies:

- Enforce strict permission checks on all forum endpoints
- Log access attempts to restricted discussions and monitor for anomalies
- Use rate limiting on comment fetching APIs to prevent abuse

## Objectives

1. Establish a testable forum with restricted access
2. Create discussions containing sensitive (deleted) comments
3. Validate permission boundaries before exploitation

## Instructions

### Step 1: Configure Forum Permissions

**Context**: Access the group management panel to set permissions that allow members to view active discussions but hide deleted comments, while blocking non-members entirely.

Log in to Steam as a group admin and navigate to the group's forum settings. Set 'can_view' to 1 for members, 0 for non-members, and ensure deleted comments are not retrievable via standard views.

### Step 2: Create and Populate Discussion

**Context**: Generate a test discussion to hold comments for the IDOR test.

In the forum, create a new discussion topic. Add multiple comments as different users, then delete 2-3 of them using admin or moderate privileges.

**Expected Output**: Discussion visible to members with some comments hidden/deleted.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- setup
- steam
- forums
