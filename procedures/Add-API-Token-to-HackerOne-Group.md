---
id: proc-uuid-2
tags:
  - api-token
  - group-membership
  - hackerone
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:39.662Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Add-API-Token-to-HackerOne-Group

## Summary

This procedure adds an existing API token as a team member to a HackerOne group, configuring the vulnerability trigger condition without immediate impact.

## Description

API tokens in HackerOne represent programmatic access and can be assigned to groups for permissions. Adding one to a group sets up the loop when the group is renamed, as the serialization process iterates improperly over token memberships. This step requires access to the API tokens page and the group ID from the previous step.

## Requirements

1. Existing API token in the program
2. Group ID from creation step
3. Authenticated session with token management permissions

## Defense

Defensive measures and detection strategies:

- Audit API token assignments to groups for anomalies
- Restrict token group memberships to prevent misuse in updates

## Objectives

1. Associate the API token with the target group
2. Verify the membership to ensure the setup is correct
3. Avoid triggering any pre-validation checks

## Instructions

### Step 1: Navigate to API Tokens

**Context**: Locate and select the API token to modify its group assignments.

Use the web UI at https://hackerone.com/[PROGRAM]/api.

> Select the token, click 'Manage groups', and assign it to the created group (e.g., ID 95004).

### Step 2: Verify Membership

**Context**: Confirm the token is now a member of the group via API.

Access https://hackerone.com/[PROGRAM]/team_members/[TEAM_MEMBER_ID].json.

> Expected: JSON showing the group under attributes.groups.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- api-token
- group-membership
