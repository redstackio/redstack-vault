---
tags:
  - gitlab
  - group-creation
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
techniques: []
updated_at: '2025-12-13T23:56:03.674Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 857986b9-fe06-48e5-ad9d-93fb8d8d34c7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Create Group for Custom Emojis in GitLab

## Summary

This procedure sets up a new group in GitLab to serve as a namespace for creating custom emojis, which is necessary for injecting the XSS payload via the GraphQL API.

## Description

Groups in GitLab provide isolated scopes for projects and features like custom emojis. Creating a group named 'xss_target' allows targeted emoji creation without affecting other parts of the instance. This step uses the GitLab web UI and requires user credentials with group creation permissions. It's a low-risk setup step in the context of the XSS exploit chain.

## Requirements

1. Valid GitLab user account with permissions to create groups
2. Access to the GitLab web interface
3. Enabled custom emoji feature (from prior procedure)

## Defense

Defensive measures and detection strategies:

- Limit group creation to trusted users via role-based access control
- Audit new group creations in GitLab logs
- Enforce naming conventions to detect suspicious groups like 'xss_target'

## Objectives

1. Establish a container for the malicious emoji
2. Ensure the group is accessible for project and API operations
3. Minimize visibility of the attack setup

## Instructions

### Step 1: Navigate to Groups

**Context**: Log in to GitLab and access the groups management section.

**Command** (GitLab UI):
No command; use the web interface to click 'New group' under the Groups menu.

> Enter group name 'xss_target' and visibility settings (e.g., internal). Expected output: Confirmation of group creation.

### Step 2: Verify Group Access

**Context**: Confirm the group is listed and editable.

**Command** (GitLab UI):
Browse to the new group page.

> Expected output: Group dashboard loads without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- group
