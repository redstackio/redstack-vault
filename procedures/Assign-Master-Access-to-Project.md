---
id: 123e4567-e89b-12d3-a456-426614174002
name: Assign-Master-Access-to-Project
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.507Z'
tactics:
  - '[[Persistence]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - gitlab
  - access-control
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Assign-Master-Access-to-Project

## Summary

This procedure grants the malicious user Master access to a GitLab project, ensuring their username appears in role dropdowns within protected branches settings.

## Description

To maximize exposure, the injected user must have a role like Master, which includes them in permission dropdowns. This step involves inviting or adding the user via project settings. The vulnerability relies on the username rendering without escaping in access_dropdown.js (line 461), allowing XSS when the dropdown is viewed by other Master users.

## Requirements

1. Maintainer or Owner access to the target project
2. The malicious user already created
3. GitLab web interface access

## Defense

Defensive measures and detection strategies:

- Audit project member additions for suspicious users
- Limit Master role assignments
- Enable logging for role changes

## Objectives

1. Elevate the malicious user's privileges in the project
2. Include them in UI elements like dropdowns
3. Prepare for payload rendering

## Instructions

### Step 1: Navigate to Project Members

**Context**: Access the members management section.

Go to Project > Members.

### Step 2: Add the Malicious User

**Context**: Invite or add the user and assign Master role.

Search for the malicious username, select it, choose 'Master' from the role dropdown, and add.

> Ensure the role is set to Master to match the vulnerable context.

### Step 3: Confirm Access

**Context**: Verify the assignment.

Refresh the members list to see the user with Master permissions.

**Expected Output**: User listed under project members with Master role.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[access-control]]
