---
tags:
  - gitlab
  - issue-move
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T05:32:13.161Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 5bc70e3e-f622-4d92-a673-5acea255c612
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Move-Issue-to-Private-Project-for-Escalation

## Summary

This procedure exploits the 'Move to' feature in GitLab issues to migrate an issue with an attached design from a Reporter's project to a private project, bypassing upload permissions and achieving privilege escalation for design files.

## Description

The root cause is the lack of permission validation in the 'Move to' functionality for Design Management files during migration. By selecting the private project (where Reporter has only read access) and confirming the move, the design is uploaded without checks, escalating effective write access. This targets GitLab UI's issue workflow; prerequisites include the issue with design; outcomes: Unauthorized design in private project, demonstrating escalation.

## Requirements

1. Issue with design in Reporter project
2. Read access to the private target project
3. GitLab UI access as Reporter

## Defense

Defensive measures and detection strategies:

- Patch GitLab to version fixing this (post-13.11 or equivalent)
- Audit issue moves across projects, especially to private ones
- Enforce strict permission checks on migrations via custom hooks or policies

## Objectives

1. Initiate and complete issue migration
2. Bypass design upload restrictions
3. Verify escalation by checking design in target project

## Instructions

### Step 1: Initiate Move

**Context**: Start the migration from the issue view.

**Instructions**: Open the issue in Reporter Project, scroll to right sidebar bottom, click 'Move' to open dialog.

> Dialog shows source project and available targets.

### Step 2: Select Destination

**Context**: Choose the private project to target escalation.

**Instructions**: In dialog, search/select the private project, preview changes if needed.

> Ensure private project is selectable due to read access.

### Step 3: Confirm and Verify

**Context**: Execute move and validate bypass.

**Instructions**: Click 'Move' to confirm; after completion, navigate to private project > Issues to view the migrated issue and design.

> Design should be uploaded and visible, confirming escalation.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[issue-move]]
- [[privilege-escalation]]
