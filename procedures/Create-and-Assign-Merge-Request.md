---
id: proc-gitlab-create-mr-001
tags:
  - gitlab
  - merge-request
  - assignment
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:11.100Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-and-Assign-Merge-Request

## Summary

This procedure creates a Merge Request in GitLab from a feature branch and assigns it to the target Developer user, linking access for later API testing.

## Description

From an admin account, use the GitLab UI to create an MR targeting the 'test' branch to 'master', and explicitly assign the Developer user. This assignment is key to the vulnerability as it persists API access post-demotion. Expected outcome: MR with assignee set.

## Requirements

1. Admin access to project
2. Existing 'test' branch with changes
3. MR creation permissions

## Defense

Defensive measures and detection strategies:

- Review MR assignments in audit logs
- Automate assignee permission checks on role changes

## Objectives

1. Link MR to target user for access persistence
2. Simulate real workflow for vulnerability reproduction
3. Obtain MR ID for API queries

## Instructions

### Step 1: Initiate Merge Request

**Context**: Start MR creation in project overview.

Click 'Merge Requests' > 'New Merge Request', select source 'test' and target 'master'.

> MR draft prepared.

### Step 2: Assign to Developer User

**Context**: Set assignee to establish access link.

In MR creation form, search and select the Developer user as assignee, then submit.

> MR created with ID (e.g., 1) and assignee confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- mr-creation
